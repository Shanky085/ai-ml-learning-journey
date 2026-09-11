#!/usr/bin/env python3
"""
Test version of learning tracker - runs once and exits
"""

import os
import hashlib
import subprocess
import json
from datetime import datetime
from pathlib import Path

# Configuration
LEARNING_FILE = r"C:\Users\shank\Desktop\ai\LEARNING.md"
REPO_PATH = r"C:\Users\shank\ai-ml-learning-journey"
STATE_FILE = os.path.join(REPO_PATH, ".learning_sync_state.json")
LOG_DIR = os.path.join(REPO_PATH, "daily-log")

def get_file_hash(filepath):
    """Get MD5 hash of file content"""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except FileNotFoundError:
        return None

def load_state():
    """Load previous state from JSON file"""
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return {"last_hash": "", "last_synced": None}

def save_state(state):
    """Save state to JSON file"""
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def save_to_daily_log(content):
    """Save content to daily log file"""
    # Ensure log directory exists
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # Create filename based on date
    today = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(LOG_DIR, f"learning-{today}.md")
    
    # Format content
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_content = f"""# Learning Update - {timestamp}

## Summary
Automated sync from learning tracker at {timestamp}

## Content
{content}

---
*Synced automatically by learning tracker automation*
"""
    
    # If file exists, append; otherwise create new
    if os.path.exists(log_file):
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write("\n\n" + formatted_content)
    else:
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
    
    return log_file

def git_commit_and_push(message):
    """Commit changes and push to GitHub"""
    try:
        # Change to repo directory
        os.chdir(REPO_PATH)
        
        # Add all changes
        subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
        
        # Check if there are changes to commit
        status_result = subprocess.run(['git', 'status', '--porcelain'], 
                                     capture_output=True, text=True)
        if not status_result.stdout.strip():
            print("No changes to commit")
            return True
        
        # Commit
        commit_result = subprocess.run(
            ['git', 'commit', '-m', message], 
            capture_output=True, text=True
        )
        
        if commit_result.returncode != 0:
            print(f"Commit failed: {commit_result.stderr}")
            return False
        
        # Push
        push_result = subprocess.run(
            ['git', 'push', 'origin', 'main'], 
            capture_output=True, text=True
        )
        
        if push_result.returncode != 0:
            print(f"Push failed: {push_result.stderr}")
            return False
        
        print(f"Successfully committed and pushed: {message}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Git operation failed: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def main():
    """Main sync function - runs once"""
    print("Running learning tracker sync (test mode)...")
    print(f"Monitoring: {LEARNING_FILE}")
    print(f"Repo: {REPO_PATH}")
    
    # Check if learning file exists
    if not os.path.exists(LEARNING_FILE):
        print(f"ERROR: Learning file not found: {LEARNING_FILE}")
        return False
    
    # Get current hash
    current_hash = get_file_hash(LEARNING_FILE)
    if current_hash is None:
        print("ERROR: Could not read learning file")
        return False
    
    # Load state
    state = load_state()
    last_hash = state.get("last_hash", "")
    
    print(f"Last hash: {last_hash}")
    print(f"Current hash: {current_hash}")
    
    # Check if file has changed since last sync
    if current_hash == last_hash and state.get("last_synced"):
        print("No changes detected since last sync")
        return True
    
    # Read current content
    try:
        with open(LEARNING_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"Read {len(content)} characters from learning file")
    except Exception as e:
        print(f"ERROR reading learning file: {e}")
        return False
    
    # Save to daily log
    try:
        log_file = save_to_daily_log(content)
        print(f"Saved to daily log: {log_file}")
    except Exception as e:
        print(f"ERROR saving to daily log: {e}")
        return False
    
    # Prepare commit message
    commit_msg = f"Learning update: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    
    # Commit and push
    print("Attempting to commit and push...")
    if git_commit_and_push(commit_msg):
        # Update state
        state["last_hash"] = current_hash
        state["last_synced"] = datetime.now().isoformat()
        save_state(state)
        print(f"Synced successfully at {state['last_synced']}")
        return True
    else:
        print("Sync failed")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
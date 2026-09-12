# AI/ML Learning Journey

This repository automatically tracks your daily progress in AI/ML learning.

## How to Use

After you finish a lesson and update your learning notes in `C:\Users\shank\Desktop\ai\LEARNING.md`, run one of the following commands to sync your progress to GitHub:

### Option 1: Double-click (Windows File Explorer)
Double-click the file `sync_learning.bat` located in this repository or on your desktop.

### Option 2: Git Bash / Command Prompt
Navigate to this repository and run:
```
learn-sync
```
or
```
python sync_learning_test.py
```

### Option 3: Continuous Background Sync (Optional)
To automatically sync whenever you save your learning notes, run:
```
python sync_learning.py
```
This will watch your `LEARNING.md` file and sync changes in real time.

## What Happens
- Your learning notes are read and a timestamped entry is saved to `daily-log/learning-YYYY-MM-DD.md`.
- A git commit is created with the message "Learning update: YYYY-MM-DD HH:MM".
- The changes are pushed to the `main` branch of this repository.

## Files
- `sync_learning_test.py` - One-time sync script (used by `learn-sync` and `sync_learning.bat`)
- `sync_learning.py` - Continuous file watcher (optional)
- `sync_learning.bat` - Windows batch file to run the one-time sync
- `learn-sync` - Bash script for Git Bash/CMD to run the one-time sync
- `daily-log/` - Folder containing daily markdown logs of your learning progress
- `.learning_sync_state.json` - Tracks the last synced state (hidden)

## Notes
- Ensure you have Git installed and configured with your GitHub account.
- The automation uses the `gh` CLI (GitHub CLI) for authentication, which should already be set up.
- Do not edit files in the `daily-log/` folder manually; they are generated automatically.

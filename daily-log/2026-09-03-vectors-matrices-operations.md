# Day 3 — Vectors, Matrices & Operations

**Date:** September 3, 2026  
**Phase:** Phase 1 — Math Foundations  
**Lesson:** Vectors, Matrices & Operations (Lesson 2 of 22)  
**Time spent:** ~60 minutes  
**Quiz:** 5/6 (83%)

## What I Learned

- Built a **Matrix class from scratch** covering add, multiply, transpose, determinant, and inverse operations.
- Distinguished **element-wise multiplication** from **matrix multiplication**.
- Understood **broadcasting**.
- Corrected my understanding of the matrix multiplication shape rule: **(m×n) @ (n×p)**.
- Understood the **identity matrix** and matrix inverse.
- Learned that a **zero determinant means a matrix has no inverse**.
- Understood that **transpose swaps rows and columns**.
- Reviewed the **ReLU activation function**.
- Connected matrix multiplication to neural networks: `relu(W @ x + b)` computes the outputs of all neurons together.

## Practiced

- Matrix operations through dry-runs and implementation.
- Matrix × vector multiplication.
- Shape matching for matrix multiplication.
- Continued matrix/vector reasoning from Day 2.

## Quiz Result

**5/6 (83%)**

### Missed

**Matrix multiplication dimensions:** the inner dimensions must match — the number of columns in the first matrix must equal the number of rows in the second.

## Progress

**Phase 1 — Math Foundations:** 2/22 lessons (9%)  
**Overall course:** 1/523 lessons completed

## Key Takeaway

> `relu(W @ x + b)` — matrix multiplication lets a neural network compute the outputs of many neurons at once, followed by bias addition and an activation function.

## Next Lesson

**Matrix Transformations & Eigenvalues** — how matrices rotate, stretch, and compress space.

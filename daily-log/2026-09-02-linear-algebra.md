# Day 2 — Linear Algebra & LoRA

**Date:** September 2, 2026

## Learned

- **Linear independence** — why redundant features can cause problems such as multicollinearity.
- **Projection** — squishing a vector onto a direction; connected to regression, PCA, and attention.
- **Gram-Schmidt process** — building clean orthonormal bases from vectors.
- **LoRA (Low-Rank Adaptation)** — training small adapter matrices instead of updating the full model.

## Practiced

- Projection: `a = [3, 4]` onto `b = [2, 0]` → `[3, 0]` ✅
- Gram-Schmidt:
  - `v1 = [1, 1]`
  - `v2 = [3, 1]`
  - `u1 = [0.707, 0.707]`
  - `u2 = [0.707, -0.707]` ✅
- Continued matrix × vector multiplication practice.

## Struggled With

- Missed a linear independence quiz question: did not recognize that `v3 = 2*v1 + v2` makes the set dependent.
- Confused the statement **“3 vectors in 3D”** with **“3 independent vectors in 3D.”**

## Quiz

**Score:** 2/3

Missed the linear independence question.

## Next

- Lesson 02: **Vectors, Matrices & Operations**

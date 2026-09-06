# Day 5 — Calculus for ML: Derivatives & Gradients

**Date:** September 5, 2026
**Session time:** ~75 minutes
**Phase:** Phase 1 — Math Foundations
**Lesson:** Lesson 4 of 22

## Session

Completed:
- Calculus for ML — Derivatives & Gradients
- Review session covering weak spots from Lessons 1–4
- Phase 1 recap of Lessons 1–3

## Learned

- **Derivative** — slope / rate of change.
- **Partial derivatives** — differentiate one variable at a time.
- **Gradient** — vector of partial derivatives; points in the direction of steepest ascent.
- **Gradient descent** — `w = w - lr × gradient`.
- **Numerical derivative** — central-difference approximation.
- **Chain rule** — multiply derivatives along a computational chain.
- **Backpropagation** — chain rule applied backward through a model.
- **Sigmoid, MSE, and cross-entropy derivatives**.
- **Hessian** — second derivatives describing curvature.
- **Newton's method vs Adam**.
- **Taylor series** — Level 0, 1, and 2 approximations.

## Practiced / Reviewed

- Central difference: `(f(x+h) - f(x-h)) / 2h`
- Hessian size reasoning: `2M` parameters → `4 trillion` entries → impractical.
- Linear independence: identified `v2 = 2×v1` as dependent.
- Matrix multiplication dimensions: `(64,128) @ (128,1) → (64,1)`.

## Quiz

**Score:** 3/5 (60%)

Missed:
1. Why Newton's method fails at scale — the Hessian is `N×N` and becomes intractable.
2. Central-difference formula.

Both were reviewed afterward.

## Review Check

**4/4 ✅**

All weak spots from Lessons 1–4 were cleared in the review session.

## Progress

**Phase 1 — Math Foundations:** 4/22 lessons (18%)

**Overall:** 4/523 lessons completed

### Cumulative Phase 1 scores

| Lesson | Score | Note |
|---|---:|---|
| Lesson 1 — Linear Algebra Intuition | 2/3 | Vectors, dot product, embeddings |
| Lesson 2 — Vectors, Matrices & Operations | 5/6 | Matrix operations, `relu(W@x+b)` |
| Lesson 3 — Matrix Transformations & Eigenvalues | 5/5 | Transformations, eigenvectors, PCA/stability |
| Lesson 4 — Calculus for ML | 3/5 | New topic; weak spots recovered in review |

**Average:** 15/19 (79%)

## Key Takeaway

> “The derivative tells you the slope. The gradient points uphill. You subtract it to go downhill. That one line is how every neural network learns.”

## Next

**Chain Rule & Automatic Differentiation** — how PyTorch computes exact derivatives mechanically through autodiff.

# Intuition for Matrix/Vector from Scalar

|                Matrix ($X$)                 |         Scalar (x)         |
| :-----------------------------------------: | :------------------------: |
|         $X = Q \Lambda Q^{T}$ [^1]          | $x = \sqrt[]{x}\sqrt[]{x}$ |
|       $X \succ 0$ (positive definite)       |          $ x > 0$          |
| $X \succcurlyeq 0$ (positive semi-definite) |         $x \geq 0$         |
|            Jaccobian Matrix [^2]            |      first derivative      |
|             Hessian Matrix [^3]             |     second derivative      |

[^1]: Every real symmetric matrix can be decomposed into an expression using only real-valued eigenvectors and eigenvalues.  Analogy in the scalar world: Every real number can be decomposed into the square root of itself multiply the square root of itself.
[^2]: Given $\mathcal{f}: \mathbb{R}^{m}\rightarrow\mathbb{R}^{n}$ , Jaccobian Matrix $\mathcal{J}$ is definited as $\mathcal{f}_{i, j} = \frac{\partial}{\partial x_j} f(x)_i$ 
[^3]: Given $\mathcal{f}: \mathbb{R}^{n}\rightarrow\mathbb{R}$ , Hessian Matrix $\mathcal{H}$ is definited as $\mathcal{f}_{i, j} = \frac{\partial}{\partial x_i \partial x_j} f(x)$


# Computational Methods & Numerical Algorithms

A comprehensive repository containing clean implementations of key computational methods, numerical linear algebra algorithms, optimization techniques, and foundations of computer vision. Developed as part of advanced computer science coursework.

## 🚀 Implemented Methods

### 1. Optimization & Metaheuristics
* **Anual Sealing (AS) & Traveling Salesperson Problem (TSP):** A heuristic alghoritm of generating solutions for NP problem os TSP.
### 2. Signal Processing & Transforms
* **Discrete Fourier Transform (DFT):** Native mathematical approach to transforming discrete signals from the time domain to the frequency domain ($O(N^2)$ complexity).
* **Fast Fourier Transform (FFT):** An optimized, $O(N \log N)$ implementation using the Radix-2 Cooley-Tukey algorithm, significantly reducing computational overhead for signal analysis.

### 3. Numerical Linear Algebra
* **LU Factorization:** Decomposing a square matrix into lower ($L$) and upper ($Y$) triangular components ($A = LU$), used to solve linear system equations efficiently.
* **QR Factorization:** Decomposition of a matrix into an orthogonal ($Q$) and an upper triangular ($R$) matrix via Gram-Schmidt orthogonalization or Householder reflections.
* **Singular Value Decomposition (SVD) & Image Compression:** Factorization of a matrix ($A = U \Sigma V^T$) used to extract dominant features. Applied to reduce image dimensionality and achieve low-rank lossy image compression.
* **Power Method:** An iterative eigenvalue algorithm used to calculate the dominant eigenvalue and its corresponding eigenvector of a matrix.

### 4. Root-Finding Algorithms
* **Bisection Method:** A robust, error-bounded bracketing method based on the Intermediate Value Theorem to find roots of continuous functions.
* **Newton-Raphson Method:** An open iterative root-finding technique using function derivatives to achieve quadratic convergence speed.

### 5. Graph Theory & Network Analysis
* **PageRank Algorithm:** The classic link-analysis algorithm used by search engines to rank elements by importance within a network, solved as a stationary distribution of a Markov chain.

### 6. Computer Vision & Machine Learning
* **Convolution-Based OCR (Optical Character Recognition):** A localized matrix-convolution methodology utilizing custom filters and edge-detection kernels to isolate, segment, and recognize textual characters in images.

---

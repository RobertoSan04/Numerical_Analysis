# Numerical Analysis - CS 5th Semester

A comprehensive collection of numerical methods and algorithms implemented during my Numerical Analysis course. This repository serves as both a learning resource and a reference for common numerical computation techniques.

## 📚 Course Overview

This repository contains implementations of fundamental numerical methods used to solve mathematical problems computationally, including:

- Root finding algorithms
- Systems of linear equations
- Interpolation and approximation
- Numerical integration and differentiation
- Differential equation solvers
- Optimization techniques

## 🛠️ Technologies

- **Language**: Python 3.x (or specify your language)
- **Libraries**: NumPy, SciPy, Matplotlib
- **Platform**: macOS (Apple Silicon compatible)

## 📁 Repository Structure

```
numerical-analysis/
├── root_finding/          # Bisection, Fixed Point, Newton-Raphson, Secant methods
├── linear_systems/        # Gauss-Jordan, LU decomposition, Jacobi, Gauss-Seidel, Triangular systems methods
├── non linear_systems/    # Newton multivariable method
├── interpolation/         # Lagrange, Newton Divided differences, Least squares, Spline interpolation
├── differentiation/       # Forward, backward, central differences
├── integration/           # Trapezoidal, Simpson's, Boole, Romberg, Gaussian quadrature, Multiple
├── differential_eqs/      # Euler's, Runge-Kutta methods, Adams-Bashforth, Zombie outbreak model
├── optimization/          # Gradient descent, Newton's method
├── tests/                 # Unit tests and validation
└── utils/                 # Helper functions and utilities
```

## 🚀 Getting Started

### Prerequisites

```bash
# Install required packages
pip install numpy scipy matplotlib
```

### Running Examples

```bash
# Navigate to the desired method directory
cd root_finding

# Run an implementation
python bisection_method.py
```

## 📖 Implemented Methods

### Root Finding
- [ ] Bisection Method
- [ ] Fixed Point Iteration
- [ ] Newton-Raphson Method
- [ ] Secant Method

### Linear Systems
- [ ] Gauss-Jordan
- [ ] LU Decomposition
- [ ] Jacobi Method
- [ ] Gauss-Seidel Method
- [ ] Triangular systems

### Non-Linear Systems
- [ ] Newton multivariable

### Interpolation
- [ ] Lagrange Interpolation
- [ ] Newton's Divided Differences
- [ ] Least squares
- [ ] Spline

### Numerical Differentiation
- [ ] Forward Difference
- [ ] Backward Difference
- [ ] Central Difference

### Numerical Integration
- [ ] Trapezoidal Rule
- [ ] Simpson's 1/3 Rule
- [ ] Simpson's 3/8 Rule
- [ ] Boole
- [ ] Romberg Integration
- [ ] Gaussian Quadrature
- [ ] Multiple integration

### Differential Equations
- [ ] Euler's Method
- [ ] Improved Euler Method
- [ ] Runge-Kutta 4th Order
- [ ] Adams-Bashforth Method
- [ ] Zombie outbreak model

## 📊 Example Usage

```python
from root_finding.newton_raphson import newton_raphson

# Define function and its derivative
f = lambda x: x**2 - 4
df = lambda x: 2*x

# Find root
root = newton_raphson(f, df, initial_guess=1.0, tolerance=1e-6)
print(f"Root found: {root}")
```

## 🧪 Testing

Each method includes test cases to verify correctness:

```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_bisection.py
```

## 📈 Error Analysis

Most implementations include:
- Convergence criteria
- Error estimation
- Iteration count tracking
- Visualization of convergence behavior

## 📝 Notes

- All algorithms include detailed comments explaining the mathematical theory
- Complexity analysis provided where applicable
- Comparison of methods for different problem types
- Stability and accuracy considerations

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome! Feel free to:
- Report bugs or issues
- Suggest optimizations
- Share alternative implementations

## 📚 References

- **Numerical Analysis** by Richard L. Burden and J. Douglas Faires
- **Numerical Methods for Engineers** by Steven C. Chapra
- Course lecture notes and materials

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎓 Academic Integrity

This repository is shared for educational purposes. If you're taking a similar course, please use this as a learning resource rather than copying solutions directly. Always follow your institution's academic integrity policies.

---

**Course**: Numerical Analysis
**Semester**: 5th Semester - Computer Science
**Year**: 2024-2025

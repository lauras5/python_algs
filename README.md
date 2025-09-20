# python_algs 🐍⚡

A collection of Python implementations for classic algorithms, data structures, and practice problems.  
This repo is structured into topic-focused directories and includes unit tests to validate solutions.

---

## 📂 Repository Structure

- **algs/**  
  General algorithm implementations (search, recursion, numeric, etc.).

- **data_structures/**  
  Sorting algorithms, trees, and common data structure implementations.

- **machine_learning/**  
  Practice notebooks and implementations for ML concepts.

- **string_manipulation/**  
  Functions and exercises for working with strings.

- **trees/**  
  Recursive functions (like Fibonacci) and tree-related algorithms.

- **vectordbs/**  
  Vector database utilities, including cosine similarity examples.

- **schools.json**  
  Example dataset used in cosine similarity/vector DB experiments.

- **algs_tester.py**  
  Unit tests using Python’s built-in `unittest` framework.

---

## 🚀 Getting Started

### Prerequisites
- Python **3.8+** (Python 2.x is not supported — type hints are used).
- Recommended: create a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

## Running Tests
This repo uses unittests for validation.
Run all tests in `algs`
```bash
python3 -m unittest algs_tester.py
```
Expected tests include:
* fib_recursion
* two_sum
* median of two sorted arrays (binary search solution)

---

## 🎯 Goals

* Practice and refine algorithm skills.
* Maintain clean, tested, Pythonic implementations.
* Explore ML and vector DB concepts alongside core CS fundamentals.

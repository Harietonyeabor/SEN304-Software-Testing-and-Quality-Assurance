# SEN 304 – Software Testing and Quality Assurance

## Project Overview

This repository contains the practical implementation for SEN 304: Software Testing and Quality Assurance at Miva Open University.

The project demonstrates software debugging, automated unit testing, error handling, software verification, and code coverage analysis using Python.

## Part A: Debugging Implementation

This section demonstrates the identification, investigation, and correction of intentional programming errors.

Key activities include:
- Identification of syntax, logical, and runtime errors.
- Use of Visual Studio Code debugging tools, including breakpoints, watch expressions, step-by-step execution, and variable inspection.
- Implementation of appropriate corrections and exception handling.
- Verification of the corrected program using different input scenarios.

## Part B: Automated Software Testing

This section implements an E-Commerce Order and Customer Support System.

Key activities include:
- Development of application modules for order processing and customer support.
- Automated unit testing using PyTest.
- Black-box testing using Equivalence Partitioning and Boundary Value Analysis.
- White-box testing using Statement Coverage and Branch Coverage.
- Additional tests examining representative application workflows.

## Technologies and Tools

- Python
- PyTest
- pytest-cov
- Visual Studio Code
- Git and GitHub

## Project Structure

- `Part-A-Debugging/`: Contains the initial buggy implementation and corrected debugging program.
- `Part-B-Automated-Testing/`: Contains the application modules and automated test files.
- `requirements.txt`: Lists the Python testing dependencies.

## Installation and Execution

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Navigate to the automated testing directory:

```bash
cd Part-B-Automated-Testing
```

Run the automated test suite:

```bash
python -m pytest -v
```

Run statement and branch coverage analysis:

```bash
python -m pytest -v --cov=order --cov=support --cov-branch --cov-report=term-missing
```

## Testing Results

The final automated test suite contains 33 test cases, all of which passed successfully.

The final coverage results recorded:

- Statement coverage: 100%
- Branch coverage: 100%
- Executable statements covered: 44
- Measured branches covered: 26

These results demonstrate complete measured statement and branch coverage across the two application modules. They do not establish exhaustive path coverage.

## Academic Information

**Course:** SEN 304 – Software Testing and Quality Assurance

**Institution:** Miva Open University

**Assessment:** Individual Practical Laboratory Exercise
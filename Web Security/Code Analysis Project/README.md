# Code Analysis Project

This project demonstrates the difference between static and dynamic code analysis using a sample vulnerable Python application. It uses tools and techniques to identify insecure functions, hardcoded secrets, and risky behavior both at rest and during execution.

## Features

- Static code scanning using regex and simple heuristics
- Dynamic code analysis with runtime behavior logging
- Comparison report between static and dynamic findings

## Usage

### Static Analysis

```bash
python3 src/static_analyzer.py --file vulnerable_app.py
```

### Dynamic Analysis

```bash
python3 src/dynamic_analyzer.py --file vulnerable_app.py
```

## Example Output

- Hardcoded passwords
- Use of dangerous functions (`eval`, `exec`)
- Suspicious file or network operations during runtime

## Requirements

- Python 3+
- `ast`, `subprocess`, `trace` (standard libraries)

Install any needed packages:

```bash
pip install -r requirements.txt
```

> Note: Use this project only for educational purposes or testing your own code.

# Fuzzing Project

This project demonstrates automated fuzz testing to identify software bugs and vulnerabilities by sending random or malformed input to a target program.

## Features

- Simple fuzzer that generates random inputs for a test function
- Detects crashes and unexpected exceptions
- Logs fuzzing results with inputs causing errors

## Usage

```bash
python3 src/fuzzer.py
```

## Requirements

- Python 3+
- `random`, `logging` (standard libraries)
  
Install dependencies if needed:
```bash
pip install -r requirements.txt
```
> Use this fuzzer as a basic template to extend for more complex applications or protocols.

# Username Profiler

## Description
The Username Profiler is an OSINT tool that checks the presence of a given username across multiple websites and social platforms. It is designed to assist in CTF challenges involving identity tracing, social footprint discovery, or reconnaissance during investigations. The tool automates web requests to known services and reports the status of the username, without requiring API keys or credentials.

## Features
- Checks username availability across a list of popular platforms
- Displays HTTP status codes and response interpretations
- Lightweight and fast using concurrent requests
- Fully CLI-based and customizable

## Installation
Install required Python dependencies with:

```bash
pip install -r requirements/requirements.txt
```

## Usage

Run the tool with:
```bash
python src/username_profiler.py <username>
```
Example:
```bash
python src/username_profiler.py johnsmith
```

## Notes

- This tool does not log in or scrape any protected content; it only checks public profiles.
- Sites that require JavaScript to render may return false negatives.
- User-Agent spoofing is built in to reduce detection.
- Intended for CTF and legal investigation/research purposes only.

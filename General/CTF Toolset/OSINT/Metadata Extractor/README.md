# Metadata Extractor

## Description
This tool extracts embedded metadata from image and document files to assist in OSINT investigations. It supports common formats such as JPEG, PNG, PDF, and Office documents. Extracted information may include GPS coordinates, authorship, software used, timestamps, and more. The tool is intended to help identify hidden data within files that may be useful for tracing origin, authorship, or location.

## Features
- Extracts EXIF data from images (JPEG, PNG, etc.)
- Extracts metadata from PDFs and Microsoft Office documents (DOCX, PPTX, XLSX)
- Displays GPS, timestamps, software, and author fields
- Supports bulk extraction via command-line interface
- Outputs parsed metadata in a readable format

## Installation
Install dependencies with:

```bash
pip install -r requirements/requirements.txt
```

## Usage
```bash
python metadata_extractor.py --file path/to/file.jpg
```
To scan all files in a directory:
```bash
python metadata_extractor.py --dir path/to/folder
```
Supported formats: `.jpg`, `.jpeg`, `.png`, `.pdf`, `.docx`, `.pptx`, `.xlsx`

## Notes

- GPS location data is only available if present in the original file metadata.
- Output is printed to the console for readability.
- Useful for identifying traces left behind by document authors, photographers, or editors.

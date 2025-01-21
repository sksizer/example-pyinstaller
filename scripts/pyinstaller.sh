#!/bin/bash
rm -Rf dist
pyinstaller src/example_pyinstaller/main.py
dist/main/main
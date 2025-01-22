#!/bin/bash
rm -Rf dist
pyinstaller src/example_pyinstaller/main.py \
    --add-data "assets:assets" \

dist/main/main
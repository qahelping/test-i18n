# HTML Tag Checker

## Project Description

This project is designed to check HTML files to make sure that all tags such as `<p>`, `<button>`, `<h2>`, `<h>` are tagged with `i18n`. This is especially important for sites that need to be translated into multiple languages.
## Problem

Often developers forget to add `i18n` tags to HTML tags, which makes it difficult to translate a site into other languages. This script helps to find such errors and facilitates the internationalisation process (i18n).
## Task

Check that all HTML tags(the list can be modified in code by replacing the input data in the folder "forms"):
- `<p>`
- `<button>`
- `<h2>`
- `<h>`

are labelled `i18n' (the label can also be changed in the label 'tag').

## Installation

1. Clone the repository to your local computer

    ```bash
    git clone https://github.com/ArretWins/test-i18n.git
    cd test-i18n
    ```
    

2. Make sure you have Python 3.6 or higher installed.

## Usage


1. Place all the HTML files you want to check into a directory.
2. Open the file "exam.py".
3. Run the script by specifying the path to the search directory in the variable ‘search_dir’.

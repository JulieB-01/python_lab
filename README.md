# News Article Text Analyzer

## Overview

The News Article Text Analyzer is a Python program that performs basic text analysis on a news article stored in a Markdown (`.md`) file. The program prompts the user to enter a word and then provides several statistics about the document.

## Features

- Counts how many times a specific word appears in the text.
- Identifies the most frequently occurring word.
- Calculates the average word length.
- Counts the number of paragraphs.
- Counts the number of sentences.
- Accepts user input for searching a specific word.
- Ignores differences in letter casing when counting words.

## Requirements

- Python 3.8 or later
- A Markdown file named `NewsArticlePython.md` located in the same directory as the script.

## Project Structure

```
project/
│
├── NewsArticlePython.md    # Input text file
├── text_analyzer.py        # Python program
└── README.md               # Project documentation
```

## How It Works

1. The program reads the contents of `NewsArticlePython.md`.
2. The user is prompted to enter a word to search for.
3. The program analyzes the text and displays:
   - Number of occurrences of the searched word
   - Most common word
   - Average word length
   - Number of paragraphs
   - Number of sentences


## Functions

### `count_specific_word(text, search_word)`
Counts how many times a specified word appears in the text.

### `identify_most_common_word(text)`
Returns the most frequently occurring word in the text.

### `calculate_average_word_length(text)`
Calculates and returns the average length of all words in the document.

### `count_paragraphs(text)`
Counts the number of paragraphs separated by blank lines.

### `count_sentences(text)`
Counts the number of sentences using punctuation marks (`.`, `!`, and `?`) as sentence delimiters.

## Notes

- Word matching is case-insensitive.
- Words are extracted using regular expressions.
- Empty user input is not accepted.
- The program assumes that `NewsArticlePython.md` exists in the project directory.

## Technologies Used

- Python
- `re` (Regular Expressions)
- `collections.Counter`
- `pathlib.Path`


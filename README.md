# bookbot
```markdown
# Word and Letter Count in Text Analysis

This script reads the contents of the "frankenstein.txt" file, performs word counting, and calculates the frequency of each letter in the text. The report provides information about the number of words and the frequency of each character (letter) in descending order.

## How to Use

1. Make sure you have a file named "frankenstein.txt" containing the text you want to analyze. Place it in the "books" directory.
2. Run the provided Python script using a compatible interpreter (e.g., Python 3.x).

```bash
python3 main.py
```

## What the Script Does

1. **Opening the Book**: The script opens the "frankenstein.txt" file located in the "books" directory and reads its contents into a variable.

2. **Word Counting**: The `word_count` function counts the number of words in the provided text by splitting it into words using spaces and counting the resulting list's length.

3. **Letter Counting**: The `letters_count` function calculates the frequency of each letter in the text. It converts the entire text to lowercase and iterates through each character. If the character is an alphabetical letter, it updates the letter's count in the `letters` dictionary. The dictionary is then converted into a list of tuples, which is sorted in descending order based on the letter frequencies.

4. **Reporting**: The script prints a report containing the total number of words found in the text and the frequency of each letter in descending order.

## Output

The output of running the script will be a report that provides information about the number of words in the document and the frequency of each character (letter) in descending order.

## Note

This script assumes the existence of the "frankenstein.txt" file in the "books" directory. Make sure to adjust the file paths if needed.

```

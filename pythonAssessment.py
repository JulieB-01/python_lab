import re
from collections import Counter
from pathlib import Path


# file_path = Path("NewsArticlePython.md")
# text = file_path.read_text(encoding="utf-8")

text = input("")
def count_specific_word(text, search_word):
    words = re.findall(r"\b\w+\b", text.lower())

    count = 0
    for word in words:  
        if word == search_word.lower():
            count += 1
        else:
            continue

    return count


def identify_most_common_word(text):
    if text.strip() == "":
        return None
    else:
        words = re.findall(r"\b\w+\b", text.lower())

        if len(words) == 0:
            return None

        word_counts = Counter(words)
        return word_counts.most_common(1)[0][0]


def calculate_average_word_length(text):
    words = re.findall(r"\b\w+\b", text)

    if len(words) == 0:
        return 0

    total_length = 0

    for word in words:
        total_length += len(word)

    average = total_length / len(words)
    return float(average)



def count_paragraphs(text):
    if text.strip() == "":
        return 1
    else:
        paragraphs = [p for p in text.split("\n\n") if p.strip()]
        return len(paragraphs)



def count_sentences(text):
    if text.strip() == "":
        return 1
    else:
        sentences = re.split(r"[.!?]+", text)
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)




while True:  
    search_word = input("Enter the word to search for: ").strip()

    if search_word == "":
        print("Please enter a valid word.")
    else:
        break

count = count_specific_word(text, search_word)
most_common = identify_most_common_word(text)
average_length = calculate_average_word_length(text)
paragraphs = count_paragraphs(text)
sentences = count_sentences(text)

print(f"\n'{search_word}' shows up {count} times.")
print(f"The most common word is '{most_common}'.")
print(f"The average word length is {average_length:.2f}.")
print(f"There are {paragraphs} paragraphs.")
print(f"There are {sentences} sentences.")
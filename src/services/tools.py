import re
import csv
from server import mcp


@mcp.tool()
def normalize_text(text: str) -> str:
    """
    Normalize text by removing bracketed content, punctuation, extra newlines, and extra spaces.
    """
    text = re.sub(r"[\(\[\{\<].*?[\)\]\}\>]", "", text)
    text = re.sub(r"[.!?]+(?=\s|$)", "", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r"\s{2,}", " ", text)

    return text.strip()


@mcp.tool()
def split_unique_word(text: str) -> list[str]:
    """
    Split text into unique, capitalized words, ignoring punctuation except apostrophes.
    """
    lower_text = text.strip().lower()
    words_only = re.sub(r"[^'\w\s]", "", lower_text)

    uniques = []
    for word in words_only.split():
        capitalized_word = word.capitalize()

        if capitalized_word not in uniques:
            uniques.append(capitalized_word)

    return uniques


@mcp.tool()
def split_unique_sentences(text: str) -> list[str]:
    """
    Split song lyrics by line breaks, remove duplicates (ignoring case/spacing),
    and capitalize the first character of each line.
    """
    lines = text.split("\n")
    seen = set()
    unique_lines = []

    for line in lines:
        cleaned = line.strip()
        normalized = re.sub(r"\s+", " ", cleaned).lower()

        if cleaned and normalized not in seen:
            seen.add(normalized)
            capitalized = cleaned[0].upper() + cleaned[1:] if cleaned else ""
            unique_lines.append(capitalized)

    return unique_lines


@mcp.tool()
def save_csv_to_file(pairs: list[list[str]], filename: str = "anki_cards.csv") -> str:
    """
    Saves a 2D list of [original, translation] to a CSV file on disk.
    Returns the file path.
    """
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(pairs)
    return filename

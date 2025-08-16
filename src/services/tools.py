import re
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

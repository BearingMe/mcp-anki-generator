from mcp.server.fastmcp import FastMCP
from lib import read_as_str
import re

mcp = FastMCP("Lyrics")


@mcp.resource("lyrics://{name}")
def retrieve_lyrics(name: str):
    relative_path = f"./src/assets/lyrics/{name}.txt"
    lyric = read_as_str(relative_path)

    if not lyric:
        return ""

    return lyric.strip()


@mcp.resource("resource://my-resource")
def get_data() -> str:
    return "Hello, world!"


@mcp.tool()
def split_words(lyrics: str):
    """
    Cleans and processes a string of song lyrics by removing certain punctuation,
    redundant whitespace, and content within brackets. The text is then normalized
    (stripped and lowercased), and a list of unique characters is returned.

    Args:
        lyrics (str): The input song lyrics as a string.

    Returns:
        List[str]: A list of unique characters from the cleaned and lowercased lyrics.
    """
    lyrics = re.sub(r"[\(\[\{\<].*?[\)\]\}\>]", "", lyrics)
    lyrics = re.sub(r"[.!?]+(?=\s|$)", "", lyrics)
    lyrics = re.sub(r"\n", " ", lyrics)
    lyrics = re.sub(r"\s{2,}", " ", lyrics)
    lyrics = lyrics.strip().lower()

    return list(set(lyrics.split()))


if __name__ == "__main__":
    mcp.run(transport="streamable-http")

from server import mcp
from lib import read_as_str


@mcp.resource("file://src/assets/lyrics/{name}")
def retrieve_lyrics(name: str):
    """
    Retrieve and return the lyrics for the given name from the assets directory.
    Returns an empty string if the file is not found or empty.
    """
    relative_path = f"./src/assets/lyrics/{name}.txt"
    lyric = read_as_str(relative_path)

    if not lyric:
        return ""

    return lyric.strip()

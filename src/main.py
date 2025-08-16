from mcp.server.fastmcp import FastMCP
from lib import read_as_str


mcp = FastMCP("Lyrics")


@mcp.resource("lyric://{name}")
def retrieve_lyrics(name: str):
    relative_path = f"./src/assets/lyrics/{name}.txt"
    lyric = read_as_str(relative_path)

    if not lyric:
        return ""

    return lyric.strip()


@mcp.tool()
def split_lyrics(lyrics: str):
    return list(set(lyrics.split()))

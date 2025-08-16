from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Lyrics")


def run_server():
    mcp.run(transport="streamable-http")

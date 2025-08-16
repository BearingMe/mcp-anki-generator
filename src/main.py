from services import tools, resources
from server import mcp


# using the imports so ruff will stop annoying me
_ = tools
_ = resources

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

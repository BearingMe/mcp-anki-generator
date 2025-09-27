# MCP Study Project

**Disclaimer:** This project is for educational purposes only. Its primary goal is to demonstrate and understand the fundamentals of the Message Control Protocol (MCP). It is not intended for production use and has no real-world value beyond being a learning exercise.

## Overview

This project implements a simple server using the `FastMCP` framework to illustrate how different components can communicate with each other using Remote Call Procedures (RCP). The server is designed to work with song lyrics, and it exposes tools for processing and manipulating text data.

## Running the Project

### Install UV

UV is a Rust-based package manager that doesn't suck like poetry. You can install it on Linux or macOS using this command:
```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

If you use Windows, you still have time to repent your sins, or you can use the command below:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Although not recommended, you can also use pipx:
```bash
pipx install uv
```

### Starting the Server

The easiest way to get it running is as a web server:

```bash
uv run src/main.py # install and run the server
```

This will launch the `FastMCP` server with the `streamable-http` transport, making it ready to accept requests.

### Using with VSCode

After running the project, you should be able to use it with Copilot Chat.

`ctrl | cmd + shift + p`

You can use `#` to select both resources and tools. For some reason, the resources provided by this library don't work, so you must select your input manually.

Usually, the AI should be able to select the right tool on its own based on context, however, GPT-4o has been proven dumb as fuck, so you may need to point it to the right tool. The tools available are:

- `normalize_text`: Removes bracketed content, punctuation, extra newlines, and extra spaces.
- `split_unique_word`: Splits text into unique, capitalized words, ignoring punctuation except for apostrophes.
- `split_unique_sentences`: Splits song lyrics by line breaks, removes duplicates (ignoring case/spacing), and capitalizes the first character of each line.
- `save_csv_to_file`: Saves to a CSV file using the format "Original, Translation".

For better results, follow the sequence above. You may also want to translate the sentences or words in an additional step.

### Troubleshooting VSCode

Make sure you're using the latest version of VSCode. Even if your current version has support for an MCP server, it may not be fully compatible with `StreamableHTTP`, so keep an eye on it.

If you need to restart or force-start, go to `.vscode/mcp.json`. You're going to see some options above "local" in the third line. If you don't see them, then you should really upgrade your version or stop using a knockoff and install the actual VSCode (I'm looking at you, VSCodium users).

## How It Works

The core of the project is the MCP server, which orchestrates communication between a client, the server itself, and an AI layer. This communication happens over a `streamable-http` transport, allowing different parts of the system to call functions remotely as if they were local.

### Architecture Layers

The system is composed of three main conceptual layers:

1.  **Server Layer**: The main application, defined in `server.py`, which creates a `FastMCP` instance. This layer is responsible for managing and exposing "resources" and "tools" that can be accessed remotely.

2.  **Client Layer**: Any application capable of sending HTTP requests to the server's endpoint. The client initiates requests to call procedures on the server, such as retrieving lyrics or asking the AI to perform a task. I recommend using Claude Desktop or VSCode with MCP.

3.  **AI Layer**: The intelligence within the MCP framework that can understand and execute complex tasks by chaining together calls to the registered `@mcp.tool()` functions. For example, a client could ask the AI to "normalize and split the lyrics of a song," and the AI would use the `normalize_text` and `split_unique_word` tools to accomplish this.

I've been using GPT-4o since GPT-5 isn't working well with my tools. Note that not all AIs support MCP clients, so stick to the latest versions of them and you should be fine.

### Remote Call Procedures (RCP)

RCP is the mechanism that allows the layers to communicate. In this project, it's implemented through decorators:

-   **`@mcp.resource`**: This decorator exposes a function as a data resource. In `services/resources.py`, the `retrieve_lyrics` function is exposed, allowing clients to fetch song lyrics by name (e.g., `file://src/assets/lyrics/100_messagi`).

-   **`@mcp.tool()`**: This decorator registers a function as a tool that the AI layer can use. The functions in `services/tools.py` (like `normalize_text`, `split_unique_sentences`, etc.) are examples of these tools. The AI can combine these building blocks to perform tasks requested by the client.

If you want to really understand how it works, take some time to use Ollama and implement your own protocol. You'll also understand the model's limitations better.

from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def weather() -> str:
    return f"Hello, the termperature is 70 degrees!"


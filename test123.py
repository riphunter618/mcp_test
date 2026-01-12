from fastmcp import FastMCP
import requests

mcp = FastMCP("My MCP Server")


@mcp.tool
def health():
    url = "https://farmosapi.graylogic.com/health"
    data = requests.get(url).json()
    return data


@mcp.tool
def data_types():
    url = "https://farmosapi.graylogic.com/data-types"
    data = requests.get(url).json()
    return data

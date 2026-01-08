from fastmcp import FastMCP
import requests

mcp = FastMCP("My MCP Server")

@mcp.tool
def weather(city) -> str:
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()
    return data["current_condition"][0]["temp_C"], "°C"

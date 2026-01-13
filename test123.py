from typing import List, Optional
from fastmcp import FastMCP
from pydantic import BaseModel, Field
import httpx
import os

mcp = FastMCP(
    name="FarmOS Batch Fetch MCP",
    instructions="Batch satellite and weather data fetch for multiple locations"
)

# --------------------
# Schemas (CRITICAL)
# --------------------

class LocationModel(BaseModel):
    lat: float = Field(..., ge=-90, le=90, description="Latitude")
    lon: float = Field(..., ge=-180, le=180, description="Longitude")

class DateRangeModel(BaseModel):
    start_date: str = Field(..., description="YYYY-MM-DD")
    end_date: str = Field(..., description="YYYY-MM-DD")

class BatchFetchInput(BaseModel):
    locations: List[LocationModel] = Field(
        ..., description="List of locations to fetch data for"
    )
    date_range: DateRangeModel = Field(
        ..., description="Date range for the data fetch"
    )
    data_types: List[str] = Field(
        ..., description="Satellite or weather data types (e.g. sentinel2, modis)"
    )
    parallel: bool = Field(
        default=True,
        description="Execute requests in parallel"
    )

# --------------------
# MCP Tool
# --------------------

@mcp.tool(
    name="batch_fetch_multiple_locations",
    description=(
        "Fetch satellite and weather data for multiple locations in a single batch. "
        "Use this for multi-field analysis, regional comparisons, or bulk data retrieval."
    )
)
async def batch_fetch_multiple_locations(input: BatchFetchInput):
    """
    MCP wrapper around FarmOS /batch-fetch API
    """

    FARMOS_API_URL = "https://farmosapi.graylogic.com/batch-fetch"

    headers = {
        "Content-Type": "application/json",
        "X-API-Key": os.getenv("API_KEY", "")
    }

    payload = {
        "locations": [loc.model_dump() for loc in input.locations],
        "date_range": input.date_range.model_dump(),
        "data_types": input.data_types,
        "parallel": input.parallel
    }

    async with httpx.AsyncClient(timeout=300) as client:
        response = await client.post(
            FARMOS_API_URL,
            json=payload,
            headers=headers
        )

    response.raise_for_status()
    return response.json()

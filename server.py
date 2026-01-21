from fastmcp import FastMCP
from datetime import datetime
import random

# Create the MCP server
mcp = FastMCP(
    name="dummy-fastmcp-server",
    description="A minimal FastMCP server for testing FastMCP Cloud"
)

# -------------------
# Simple math tool
# -------------------
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# -------------------
# String utility
# -------------------
@mcp.tool()
def shout(text: str) -> str:
    """Convert text to uppercase with excitement."""
    return text.upper() + "!!!"

# -------------------
# Random number
# -------------------
@mcp.tool()
def roll_dice(sides: int = 6) -> int:
    """Roll a dice with the given number of sides."""
    return random.randint(1, sides)

# -------------------
# Server time
# -------------------
@mcp.tool()
def current_time() -> str:
    """Get the current UTC time."""
    return datetime.utcnow().isoformat() + "Z"

# -------------------
# Health check
# -------------------
@mcp.tool()
def health() -> dict:
    """Basic health check."""
    return {
        "status": "ok",
        "service": "fastmcp-cloud-demo"
    }

# Entry point for FastMCP Cloud
if __name__ == "__main__":
    mcp.run()

from fastmcp import FastMCP
from datetime import datetime
import random

mcp = FastMCP()

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def shout(text: str) -> str:
    """Convert text to uppercase with excitement."""
    return text.upper() + "!!!"

@mcp.tool()
def roll_dice(sides: int = 6) -> int:
    """Roll a dice with the given number of sides."""
    return random.randint(1, sides)

@mcp.tool()
def current_time() -> str:
    """Get the current UTC time."""
    return datetime.utcnow().isoformat() + "Z"

@mcp.tool()
def health() -> dict:
    """Basic health check."""
    return {"status": "ok"}

if __name__ == "__main__":
    mcp.run()


import random
from fastmcp import FastMCP

mcp = FastMCP(
    name="fastmcp_demo",
    instructions="A demo for FastMCP"
)

@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Rolls a number of dice and returns the results."""
    if not 1 <= n_dice <= 10:
        raise ValueError("n_dice must be between 1 and 10")
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns the result."""
    return a + b

if __name__ == "__main__":
    mcp.run()

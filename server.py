from fastmcp import FastMCP, Context

# Create an MCP server with a descriptive name
mcp = FastMCP(
    name="Weather Service",
    instructions="""
    This server provides weather information and greeting capabilities.
    
    Use the say_hello tool to check connectivity.
    Use the get_weather tool to fetch current weather for a given location.
    """
)
# Basic greeting tool
@mcp.tool()
def say_hello(name: str = "World") -> str:
    """A simple tool that greets a person by name"""
    return f"Hello, {name}! This is your MCP server running on Python! 🚀"
# Weather information tool
@mcp.tool()
async def get_weather(city: str, country: str = "US") -> str:
    """
    Get current weather information for a city
    
    Args:
        city: Name of the city
        country: Country code (default: US)
    """
    # This is a mock implementation - in a real app, you'd call a weather API
    import random
    conditions = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy"]
    temp = random.randint(40, 90)
    
    return f"Current weather in {city}, {country}: {random.choice(conditions)}, {temp}°F"
# Run the server when executed directly
if __name__ == "__main__":
    import os
    
    # Set default host and port
    host = os.environ.get("MCP_HOST", "0.0.0.0")
    port = int(os.environ.get("MCP_PORT", "8080"))
    
    # Determine transport from environment
    transport = os.environ.get("MCP_TRANSPORT", "sse")
    
    print(f"Starting server with transport={transport}, host={host}, port={port}")
    mcp.run(transport=transport, host=host, port=port)

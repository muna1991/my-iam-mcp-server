import boto3
from loguru import logger
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "my-iam-mcp-server",
    instructions="""
    # My IAM MCP Server
    This server provides basic IAM operations.
    Currently supports listing IAM users.
    """,
    dependencies=["boto3", "loguru"]
)

@mcp.tool()
def list_users(max_items: int = 10) -> list[str]:
    """List IAM user names (up to max_items)."""
    try:
        logger.info(f"Listing up to {max_items} IAM users...")
        iam = boto3.client("iam")
        response = iam.list_users(MaxItems=max_items)
        return [user["UserName"] for user in response.get("Users", [])]
    except Exception as e:
        logger.error(f"Error listing IAM users: {e}")
        raise

def main():
    mcp.run()

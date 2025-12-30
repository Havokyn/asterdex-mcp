"""MCP server for AsterDex market data."""

import json
import asyncio
from typing import Any
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

from .client import AsterDexClient


# Initialize server and client
server = Server("asterdex-mcp")
client = AsterDexClient()


def format_response(data: Any) -> str:
    """Format API response as JSON string."""
    return json.dumps(data, indent=2)


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="get_orderbook",
            description="Get order book depth for a trading pair. Returns bids and asks with prices and quantities.",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading pair symbol (e.g., BTCUSDT, ETHUSDT)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Depth limit: 5, 10, 20, 50, 100, 500, or 1000. Default: 100",
                        "default": 100,
                        "enum": [5, 10, 20, 50, 100, 500, 1000]
                    }
                },
                "required": ["symbol"]
            }
        ),
        Tool(
            name="get_klines",
            description="Get kline/candlestick OHLCV data for technical analysis. Returns open, high, low, close, volume for each time period.",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading pair symbol (e.g., BTCUSDT)"
                    },
                    "interval": {
                        "type": "string",
                        "description": "Kline interval",
                        "enum": ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"]
                    },
                    "start_time": {
                        "type": "integer",
                        "description": "Start time in milliseconds (optional)"
                    },
                    "end_time": {
                        "type": "integer",
                        "description": "End time in milliseconds (optional)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Number of results (max 1500). Default: 500",
                        "default": 500,
                        "maximum": 1500
                    }
                },
                "required": ["symbol", "interval"]
            }
        ),
        Tool(
            name="get_funding_rate_history",
            description="Get historical funding rate data for perpetual contracts. Shows funding rate and time for each funding period.",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading pair symbol (optional, returns all symbols if not provided)"
                    },
                    "start_time": {
                        "type": "integer",
                        "description": "Start time in milliseconds (optional)"
                    },
                    "end_time": {
                        "type": "integer",
                        "description": "End time in milliseconds (optional)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Number of results (max 1000). Default: 100",
                        "default": 100,
                        "maximum": 1000
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="get_ticker_24h",
            description="Get 24-hour price change statistics including price change, volume, high, low, and more.",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading pair symbol (optional, returns all symbols if not provided)"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="get_mark_price",
            description="Get current mark price, index price, and funding rate information. Essential for perpetual futures trading.",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading pair symbol (optional, returns all symbols if not provided)"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="get_ticker_price",
            description="Get the latest price for a trading pair. Simple price lookup.",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading pair symbol (optional, returns all symbols if not provided)"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="get_book_ticker",
            description="Get best bid and ask price with quantities from the order book. Real-time spread data.",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading pair symbol (optional, returns all symbols if not provided)"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="get_index_price_klines",
            description="Get historical index price kline/candlestick data. Shows how the index price (spot market average) changed over time.",
            inputSchema={
                "type": "object",
                "properties": {
                    "pair": {
                        "type": "string",
                        "description": "Trading pair (e.g., BTCUSDT)"
                    },
                    "interval": {
                        "type": "string",
                        "description": "Kline interval",
                        "enum": ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"]
                    },
                    "start_time": {
                        "type": "integer",
                        "description": "Start time in milliseconds (optional)"
                    },
                    "end_time": {
                        "type": "integer",
                        "description": "End time in milliseconds (optional)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Number of results (max 1500). Default: 500",
                        "default": 500,
                        "maximum": 1500
                    }
                },
                "required": ["pair", "interval"]
            }
        ),
        Tool(
            name="get_mark_price_klines",
            description="Get historical mark price kline/candlestick data. Shows how the mark price (used for liquidations) changed over time.",
            inputSchema={
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Trading pair symbol (e.g., BTCUSDT)"
                    },
                    "interval": {
                        "type": "string",
                        "description": "Kline interval",
                        "enum": ["1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"]
                    },
                    "start_time": {
                        "type": "integer",
                        "description": "Start time in milliseconds (optional)"
                    },
                    "end_time": {
                        "type": "integer",
                        "description": "End time in milliseconds (optional)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Number of results (max 1500). Default: 500",
                        "default": 500,
                        "maximum": 1500
                    }
                },
                "required": ["symbol", "interval"]
            }
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    try:
        if name == "get_orderbook":
            data = await client.get_depth(
                symbol=arguments["symbol"],
                limit=arguments.get("limit", 100)
            )

        elif name == "get_klines":
            data = await client.get_klines(
                symbol=arguments["symbol"],
                interval=arguments["interval"],
                start_time=arguments.get("start_time"),
                end_time=arguments.get("end_time"),
                limit=arguments.get("limit", 500)
            )

        elif name == "get_funding_rate_history":
            data = await client.get_funding_rate(
                symbol=arguments.get("symbol"),
                start_time=arguments.get("start_time"),
                end_time=arguments.get("end_time"),
                limit=arguments.get("limit", 100)
            )

        elif name == "get_ticker_24h":
            data = await client.get_ticker_24h(
                symbol=arguments.get("symbol")
            )

        elif name == "get_mark_price":
            data = await client.get_mark_price(
                symbol=arguments.get("symbol")
            )

        elif name == "get_ticker_price":
            data = await client.get_ticker_price(
                symbol=arguments.get("symbol")
            )

        elif name == "get_book_ticker":
            data = await client.get_book_ticker(
                symbol=arguments.get("symbol")
            )

        elif name == "get_index_price_klines":
            data = await client.get_index_price_klines(
                pair=arguments["pair"],
                interval=arguments["interval"],
                start_time=arguments.get("start_time"),
                end_time=arguments.get("end_time"),
                limit=arguments.get("limit", 500)
            )

        elif name == "get_mark_price_klines":
            data = await client.get_mark_price_klines(
                symbol=arguments["symbol"],
                interval=arguments["interval"],
                start_time=arguments.get("start_time"),
                end_time=arguments.get("end_time"),
                limit=arguments.get("limit", 500)
            )

        else:
            return [TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]

        return [TextContent(
            type="text",
            text=format_response(data)
        )]

    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error: {str(e)}"
        )]


async def main():
    """Run the MCP server."""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


def run():
    """Entry point for the server."""
    asyncio.run(main())


if __name__ == "__main__":
    run()

# AsterDex MCP Server

MCP (Model Context Protocol) server for AsterDex perpetual futures market data. Provides real-time and historical market data tools for Claude Code.

## Features

### 9 Market Data Tools:

1. **get_orderbook** - Order book depth with bids and asks
2. **get_klines** - OHLCV candlestick data for technical analysis
3. **get_funding_rate_history** - Historical funding rate data
4. **get_ticker_24h** - 24-hour price statistics
5. **get_mark_price** - Mark price and funding rate info
6. **get_ticker_price** - Latest price lookup
7. **get_book_ticker** - Best bid/ask prices
8. **get_index_price_klines** - Index price history
9. **get_mark_price_klines** - Mark price history

## Installation

### Prerequisites

- Python 3.10 or higher
- Claude Code CLI

### Install the MCP Server

```bash
cd asterdex-mcp
pip install -e .
```

### Configure Claude Code

Add the server to your Claude Code MCP settings:

```bash
claude mcp add asterdex-mcp
```

Or manually add to your MCP configuration file (`~/.claude/mcp.json`):

```json
{
  "mcpServers": {
    "asterdex": {
      "command": "python",
      "args": ["-m", "asterdex_mcp.server"]
    }
  }
}
```

## Usage

Once installed, you can use the tools directly in Claude Code conversations:

### Example Queries

**Get BTC/USDT order book:**
```
Get the orderbook for BTCUSDT with 20 levels
```

**Get ETH price data:**
```
Show me 4-hour klines for ETHUSDT from the last 7 days
```

**Analyze funding rates:**
```
Get funding rate history for BTCUSDT over the last 30 days
```

**Check current prices:**
```
What's the current mark price and funding rate for SOLUSDT?
```

**Compare index vs mark price:**
```
Show me the difference between index price and mark price klines for BTCUSDT over the last day
```

## Available Tools

### get_orderbook

Get order book depth for a trading pair.

**Parameters:**
- `symbol` (required): Trading pair (e.g., "BTCUSDT")
- `limit` (optional): Depth limit - 5, 10, 20, 50, 100, 500, or 1000. Default: 100

**Example:**
```json
{
  "symbol": "BTCUSDT",
  "limit": 50
}
```

### get_klines

Get OHLCV candlestick data.

**Parameters:**
- `symbol` (required): Trading pair (e.g., "ETHUSDT")
- `interval` (required): Time interval - "1m", "5m", "15m", "30m", "1h", "4h", "1d", etc.
- `start_time` (optional): Start time in milliseconds
- `end_time` (optional): End time in milliseconds
- `limit` (optional): Number of candles (max 1500). Default: 500

**Example:**
```json
{
  "symbol": "ETHUSDT",
  "interval": "1h",
  "limit": 100
}
```

### get_funding_rate_history

Get historical funding rate data.

**Parameters:**
- `symbol` (optional): Trading pair (returns all if not provided)
- `start_time` (optional): Start time in milliseconds
- `end_time` (optional): End time in milliseconds
- `limit` (optional): Number of records (max 1000). Default: 100

**Example:**
```json
{
  "symbol": "BTCUSDT",
  "limit": 50
}
```

### get_ticker_24h

Get 24-hour price change statistics.

**Parameters:**
- `symbol` (optional): Trading pair (returns all if not provided)

**Example:**
```json
{
  "symbol": "SOLUSDT"
}
```

### get_mark_price

Get mark price and funding rate information.

**Parameters:**
- `symbol` (optional): Trading pair (returns all if not provided)

**Example:**
```json
{
  "symbol": "BTCUSDT"
}
```

### get_ticker_price

Get latest price.

**Parameters:**
- `symbol` (optional): Trading pair (returns all if not provided)

**Example:**
```json
{
  "symbol": "ETHUSDT"
}
```

### get_book_ticker

Get best bid/ask from order book.

**Parameters:**
- `symbol` (optional): Trading pair (returns all if not provided)

**Example:**
```json
{
  "symbol": "BTCUSDT"
}
```

### get_index_price_klines

Get index price candlestick history.

**Parameters:**
- `pair` (required): Trading pair (e.g., "BTCUSDT")
- `interval` (required): Time interval
- `start_time` (optional): Start time in milliseconds
- `end_time` (optional): End time in milliseconds
- `limit` (optional): Number of candles (max 1500). Default: 500

**Example:**
```json
{
  "pair": "BTCUSDT",
  "interval": "1h",
  "limit": 200
}
```

### get_mark_price_klines

Get mark price candlestick history.

**Parameters:**
- `symbol` (required): Trading pair (e.g., "BTCUSDT")
- `interval` (required): Time interval
- `start_time` (optional): Start time in milliseconds
- `end_time` (optional): End time in milliseconds
- `limit` (optional): Number of candles (max 1500). Default: 500

**Example:**
```json
{
  "symbol": "BTCUSDT",
  "interval": "4h",
  "limit": 100
}
```

## Configuration

### Environment Variables

- `ASTERDEX_BASE_URL`: Override the API base URL (default: `https://fapi.asterdex.com`)

**Example:**
```bash
export ASTERDEX_BASE_URL=https://testnet-fapi.asterdex.com
```

## Time Format

All timestamps are in **milliseconds** since Unix epoch.

**Convert from seconds:**
```python
time_ms = time.time() * 1000
```

**Common time calculations:**
```python
import time

# Current time
now_ms = int(time.time() * 1000)

# 24 hours ago
day_ago_ms = now_ms - (24 * 60 * 60 * 1000)

# 7 days ago
week_ago_ms = now_ms - (7 * 24 * 60 * 60 * 1000)
```

## Interval Options

Valid kline intervals:
- Minutes: `1m`, `3m`, `5m`, `15m`, `30m`
- Hours: `1h`, `2h`, `4h`, `6h`, `8h`, `12h`
- Days/Weeks/Months: `1d`, `3d`, `1w`, `1M`

## Common Trading Pairs

- `BTCUSDT` - Bitcoin/USDT
- `ETHUSDT` - Ethereum/USDT
- `SOLUSDT` - Solana/USDT
- `BNBUSDT` - BNB/USDT
- `DOGEUSDT` - Dogecoin/USDT

Use the `get_ticker_price` tool without a symbol to see all available trading pairs.

## Troubleshooting

### Server not connecting

Check that the MCP server is properly installed:
```bash
claude mcp list
```

You should see `asterdex` in the list.

### Import errors

Make sure dependencies are installed:
```bash
pip install -e .
```

### API errors

The AsterDex API may have rate limits. If you encounter errors, wait a moment and try again.

## Development

### Project Structure

```
asterdex-mcp/
├── src/asterdex_mcp/
│   ├── __init__.py
│   ├── server.py       # MCP server and tools
│   ├── client.py       # AsterDex API client
│   └── tools/
│       └── __init__.py
├── pyproject.toml
└── README.md
```

### Testing

Run the server directly:
```bash
python -m asterdex_mcp.server
```

## API Documentation

For detailed API documentation, see:
- [AsterDex API Documentation](https://docs.asterdex.com/product/aster-perpetuals/api/api-documentation)
- [GitHub API Docs](https://github.com/asterdex/api-docs)

## License

MIT

## Support

For issues or questions:
- GitHub: [asterdex/api-docs](https://github.com/asterdex/api-docs)
- AsterDex Docs: [docs.asterdex.com](https://docs.asterdex.com)

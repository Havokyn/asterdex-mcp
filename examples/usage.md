# AsterDex MCP Usage Examples

This file contains example queries you can use with Claude Code once the AsterDex MCP server is installed.

## Basic Price Queries

### Get current price
```
What's the current price of BTCUSDT?
```

### Get 24h statistics
```
Show me 24-hour stats for ETHUSDT
```

### Get mark price
```
What's the mark price and funding rate for SOLUSDT?
```

## Order Book Analysis

### Simple order book
```
Get the orderbook for BTCUSDT with 20 levels
```

### Deep order book analysis
```
Get the top 100 bids and asks for ETHUSDT and calculate the total volume
```

### Best bid/ask
```
What's the best bid and ask for BTCUSDT right now?
```

## Historical Data Analysis

### Get recent candles
```
Show me the last 50 1-hour candles for BTCUSDT
```

### Specific time range
```
Get 4-hour klines for ETHUSDT from the last 7 days
```

### Multiple timeframes
```
Compare 1-hour and 4-hour klines for SOLUSDT over the last 2 days
```

## Funding Rate Analysis

### Recent funding rates
```
Get the last 20 funding rate payments for BTCUSDT
```

### Historical funding analysis
```
Show me funding rate history for ETHUSDT over the last 30 days and calculate the average
```

### Compare funding across pairs
```
Get current funding rates for BTCUSDT, ETHUSDT, and SOLUSDT and compare them
```

## Advanced Analysis

### Price vs Mark Price
```
Compare the regular price klines with mark price klines for BTCUSDT over the last day. Are there any significant differences?
```

### Index Price Tracking
```
Get index price klines for BTCUSDT and compare them with the mark price klines
```

### Funding Rate Correlation
```
Get funding rate history for BTCUSDT and compare it with price movements. When was the funding rate highest?
```

### Volume Analysis
```
Get 4-hour klines for ETHUSDT over the last week and identify the periods with highest trading volume
```

### Market Depth Analysis
```
Get the orderbook for BTCUSDT and calculate:
1. Total bid volume in the top 50 levels
2. Total ask volume in the top 50 levels
3. The spread percentage
```

## Multi-Pair Analysis

### Cross-pair comparison
```
Compare 24-hour stats for BTCUSDT, ETHUSDT, SOLUSDT, and BNBUSDT. Which had the highest percentage gain?
```

### Correlation analysis
```
Get 1-hour klines for BTCUSDT and ETHUSDT over the last 3 days. Calculate their price correlation.
```

## Time-Based Queries

### Specific date range
```
Get daily klines for BTCUSDT for the month of December 2024
```

Note: Use timestamp conversion:
- December 1, 2024 00:00 UTC = 1701388800000 ms
- December 31, 2024 23:59 UTC = 1735689599000 ms

### Last N periods
```
Get the last 100 15-minute candles for ETHUSDT
```

## Technical Analysis Setup

### Prepare data for indicators
```
Get 200 4-hour candles for BTCUSDT so I can calculate a 50-period moving average
```

### Support/Resistance identification
```
Get the last 500 1-hour candles for ETHUSDT and identify the major support and resistance levels
```

### Volatility analysis
```
Get daily klines for BTCUSDT over the last 30 days and calculate the daily volatility (high-low percentage)
```

## Market Overview

### All prices at once
```
Get current prices for all trading pairs
```

### Market snapshot
```
Get 24-hour stats for all trading pairs and rank them by volume
```

### Active markets
```
Show me the book tickers for all pairs and identify which ones have the tightest spreads
```

## Tips for Effective Queries

1. **Be specific about symbols**: Always use the full trading pair (e.g., BTCUSDT, not just BTC)

2. **Use appropriate timeframes**:
   - Scalping: 1m, 5m
   - Day trading: 15m, 1h
   - Swing trading: 4h, 1d
   - Position trading: 1d, 1w

3. **Request reasonable data amounts**:
   - Start with smaller limits and increase if needed
   - Max 1500 candles per request
   - Max 1000 funding rate records

4. **Combine tools for deeper insights**:
   - Use orderbook + recent trades for market microstructure
   - Use klines + funding rates for trend analysis
   - Use mark price + index price to detect basis

5. **Time calculations**:
   - Current time: Use "now" or "current"
   - Recent data: "last 24 hours", "last 7 days"
   - Specific dates: Provide in standard format (YYYY-MM-DD)

## Integration Examples

### With Technical Analysis
```
Get 4-hour klines for BTCUSDT over the last 30 days. Calculate:
1. 20-period SMA
2. RSI(14)
3. Bollinger Bands
```

### With Risk Management
```
For ETHUSDT, get:
1. Current orderbook depth
2. Last 24h volume
3. Current funding rate
Help me calculate appropriate position sizing for a $10,000 trade
```

### With Market Making
```
Get the orderbook and recent trades for BTCUSDT. Based on the spread and volume, what would be a good market making strategy?
```

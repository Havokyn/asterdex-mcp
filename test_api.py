"""Test script for AsterDex MCP API client."""

import asyncio
import json
from asterdex_mcp.client import AsterDexClient


async def test():
    """Test the API client with BTCUSDT."""
    client = AsterDexClient()

    try:
        print("=" * 60)
        print("Testing AsterDex MCP Server")
        print("=" * 60)

        # Test 1: Get current price
        print("\n1. Getting BTCUSDT current price...")
        price_data = await client.get_ticker_price('BTCUSDT')
        print(json.dumps(price_data, indent=2))

        # Test 2: Get 24h statistics
        print("\n2. Getting BTCUSDT 24h statistics...")
        ticker_24h = await client.get_ticker_24h('BTCUSDT')
        print(f"Symbol: {ticker_24h['symbol']}")
        print(f"Current Price: ${ticker_24h['lastPrice']}")
        print(f"24h High: ${ticker_24h['highPrice']}")
        print(f"24h Low: ${ticker_24h['lowPrice']}")
        print(f"24h Volume: {ticker_24h['volume']}")
        print(f"24h Price Change: {ticker_24h['priceChangePercent']}%")

        # Test 3: Get mark price
        print("\n3. Getting BTCUSDT mark price...")
        mark_price = await client.get_mark_price('BTCUSDT')
        print(f"Mark Price: ${mark_price['markPrice']}")
        print(f"Index Price: ${mark_price['indexPrice']}")
        print(f"Funding Rate: {float(mark_price['lastFundingRate']) * 100:.4f}%")
        print(f"Next Funding Time: {mark_price['nextFundingTime']}")

        # Test 4: Get orderbook
        print("\n4. Getting BTCUSDT orderbook (10 levels)...")
        orderbook = await client.get_depth('BTCUSDT', limit=10)
        print(f"Best Bid: ${orderbook['bids'][0][0]} (qty: {orderbook['bids'][0][1]})")
        print(f"Best Ask: ${orderbook['asks'][0][0]} (qty: {orderbook['asks'][0][1]})")
        spread = float(orderbook['asks'][0][0]) - float(orderbook['bids'][0][0])
        spread_pct = (spread / float(orderbook['bids'][0][0])) * 100
        print(f"Spread: ${spread:.2f} ({spread_pct:.4f}%)")

        print("\n" + "=" * 60)
        print("✅ All tests passed! AsterDex MCP is working correctly.")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(test())

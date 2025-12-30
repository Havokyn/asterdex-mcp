"""AsterDex API client for making HTTP requests."""

import os
from typing import Any, Optional
import httpx


class AsterDexClient:
    """Async HTTP client for AsterDex Futures API."""

    def __init__(self, base_url: Optional[str] = None):
        """Initialize the AsterDex API client.

        Args:
            base_url: Base URL for the API. Defaults to ASTERDEX_BASE_URL env var
                     or https://fapi.asterdex.com
        """
        self.base_url = base_url or os.getenv(
            "ASTERDEX_BASE_URL",
            "https://fapi.asterdex.com"
        )
        self.client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=30.0,
            follow_redirects=True
        )

    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()

    async def _request(self, endpoint: str, params: Optional[dict] = None) -> dict:
        """Make a GET request to the API.

        Args:
            endpoint: API endpoint path (e.g., /fapi/v3/depth)
            params: Query parameters

        Returns:
            JSON response as dictionary

        Raises:
            httpx.HTTPError: If the request fails
        """
        response = await self.client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    # Market Data Endpoints

    async def get_depth(
        self,
        symbol: str,
        limit: int = 100
    ) -> dict:
        """Get order book depth.

        Args:
            symbol: Trading pair symbol (e.g., BTCUSDT)
            limit: Depth limit (5, 10, 20, 50, 100, 500, 1000)

        Returns:
            Order book with bids and asks
        """
        return await self._request("/fapi/v3/depth", {
            "symbol": symbol,
            "limit": limit
        })

    async def get_klines(
        self,
        symbol: str,
        interval: str,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: int = 500
    ) -> list:
        """Get kline/candlestick data.

        Args:
            symbol: Trading pair symbol
            interval: Kline interval (1m, 5m, 15m, 30m, 1h, 4h, 1d, etc.)
            start_time: Start time in milliseconds
            end_time: End time in milliseconds
            limit: Number of results (max 1500)

        Returns:
            List of kline data
        """
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        return await self._request("/fapi/v3/klines", params)

    async def get_funding_rate(
        self,
        symbol: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: int = 100
    ) -> list:
        """Get funding rate history.

        Args:
            symbol: Trading pair symbol (optional, returns all if not provided)
            start_time: Start time in milliseconds
            end_time: End time in milliseconds
            limit: Number of results (max 1000)

        Returns:
            List of funding rate records
        """
        params = {"limit": limit}
        if symbol:
            params["symbol"] = symbol
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        return await self._request("/fapi/v3/fundingRate", params)

    async def get_ticker_24h(self, symbol: Optional[str] = None) -> dict | list:
        """Get 24-hour ticker price change statistics.

        Args:
            symbol: Trading pair symbol (optional, returns all if not provided)

        Returns:
            Ticker data (single dict if symbol provided, list if not)
        """
        params = {}
        if symbol:
            params["symbol"] = symbol

        return await self._request("/fapi/v3/ticker/24hr", params)

    async def get_ticker_price(self, symbol: Optional[str] = None) -> dict | list:
        """Get latest price for symbol(s).

        Args:
            symbol: Trading pair symbol (optional, returns all if not provided)

        Returns:
            Price data (single dict if symbol provided, list if not)
        """
        params = {}
        if symbol:
            params["symbol"] = symbol

        return await self._request("/fapi/v3/ticker/price", params)

    async def get_book_ticker(self, symbol: Optional[str] = None) -> dict | list:
        """Get best bid/ask price and quantity.

        Args:
            symbol: Trading pair symbol (optional, returns all if not provided)

        Returns:
            Book ticker data (single dict if symbol provided, list if not)
        """
        params = {}
        if symbol:
            params["symbol"] = symbol

        return await self._request("/fapi/v3/ticker/bookTicker", params)

    async def get_mark_price(self, symbol: Optional[str] = None) -> dict | list:
        """Get mark price and funding rate.

        Args:
            symbol: Trading pair symbol (optional, returns all if not provided)

        Returns:
            Mark price data including funding rate info
        """
        params = {}
        if symbol:
            params["symbol"] = symbol

        return await self._request("/fapi/v3/premiumIndex", params)

    async def get_index_price_klines(
        self,
        pair: str,
        interval: str,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: int = 500
    ) -> list:
        """Get index price kline/candlestick data.

        Args:
            pair: Trading pair (e.g., BTCUSDT)
            interval: Kline interval (1m, 5m, 15m, 30m, 1h, 4h, 1d, etc.)
            start_time: Start time in milliseconds
            end_time: End time in milliseconds
            limit: Number of results (max 1500)

        Returns:
            List of index price kline data
        """
        params = {
            "pair": pair,
            "interval": interval,
            "limit": limit
        }
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        return await self._request("/fapi/v3/indexPriceKlines", params)

    async def get_mark_price_klines(
        self,
        symbol: str,
        interval: str,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        limit: int = 500
    ) -> list:
        """Get mark price kline/candlestick data.

        Args:
            symbol: Trading pair symbol
            interval: Kline interval (1m, 5m, 15m, 30m, 1h, 4h, 1d, etc.)
            start_time: Start time in milliseconds
            end_time: End time in milliseconds
            limit: Number of results (max 1500)

        Returns:
            List of mark price kline data
        """
        params = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit
        }
        if start_time:
            params["startTime"] = start_time
        if end_time:
            params["endTime"] = end_time

        return await self._request("/fapi/v3/markPriceKlines", params)

    # Utility endpoints

    async def ping(self) -> dict:
        """Test connectivity to the API."""
        return await self._request("/fapi/v3/ping")

    async def get_server_time(self) -> dict:
        """Get server time."""
        return await self._request("/fapi/v3/time")

    async def get_exchange_info(self) -> dict:
        """Get exchange trading rules and symbol information."""
        return await self._request("/fapi/v3/exchangeInfo")

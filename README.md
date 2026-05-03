# ETH Dashboard

Ethereum analytics dashboard with real-time market data, on-chain metrics, and weighted technical analysis.

## Features

- **Live Price** — real-time ETH/USD with 24h range bar
- **Fear & Greed Index** — 7-day trend from Alternative.me
- **Staking Queue** — entry/exit queue with pressure bars and 30-day trend chart
- **Technical Indicators** — weighted scoring system with category-based analysis
- **On-chain Data** — gas fees, staking APR, supply dynamics, DeFi TVL
- **Key Price Levels** — support/resistance from 60-day range and moving averages

## Technical Analysis

Weighted scoring system (-100 to +100):

| Category | Weight | Indicators |
|---|---|---|
| Trend | 40% | MA20, MA50, MA200 (mean reversion) |
| Momentum | 30% | RSI, MACD, KDJ |
| Volatility | 15% | Bollinger Bands |
| Volume | 15% | OBV divergence, volume ratio |

Signals: Highly Recommended Buy / Recommended Buy / Hold / Recommended Sell / Highly Recommended Sell

## Data Sources

| Source | Data |
|---|---|
| CryptoCompare | Live price, 200-day history |
| Blockchair | Supply, burned ETH, staking stats |
| validatorqueue.com | Staking entry/exit queue (via GitHub Actions) |
| Alternative.me | Fear & Greed Index |
| Lido | stETH APR |
| DefiLlama | DeFi TVL |
| ultrasound.money | Gas fee stats |

## Architecture

Single-file HTML dashboard (`index.html`) — no build step, no dependencies, everything runs client-side.

Validator queue data is scraped every 15 minutes by GitHub Actions and served as same-origin JSON to avoid CORS issues.

Live: https://tenillusions.github.io/ethd/

## License

See [LICENSE](./LICENSE).

# ETH Dashboard

Ethereum analytics dashboard with real-time market data, on-chain metrics, and technical analysis.

## Features

- **Live Price** — real-time ETH/USD with 24h range bar
- **Fear & Greed Index** — 7-day trend from Alternative.me
- **Staking Queue** — entry/exit queue, active validators, pressure bars
- **Technical Indicators** — RSI, MACD, Bollinger Bands, KDJ, OBV, ATR, MA(20/50/200)
- **Verdict Engine** — aggregated buy/sell signal with composite score
- **On-chain Data** — gas fees, staking APR, supply dynamics, DeFi TVL
- **Key Price Levels** — support/resistance from 60-day high/low and moving averages

## Data Sources

| Source | Data |
|---|---|
| CryptoCompare | Live price, 200-day history |
| Blockchair | Supply, burned ETH, staking stats |
| validatorqueue.com | Staking entry/exit queue |
| Alternative.me | Fear & Greed Index |
| Lido | stETH APR |
| DefiLlama | DeFi TVL |
| ultrasound.money | Gas fee stats |

## Usage

Open `index.html` in a browser. No build step, no dependencies — everything runs client-side.

Live: https://tenillusions.github.io/ethd/

## License

See [LICENSE](./LICENSE).

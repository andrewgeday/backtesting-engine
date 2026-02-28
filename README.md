# Backtesting Engine

This repository implements a simple, transparent backtesting framework
designed to demonstrate core backtesting mechanics and risk evaluation.

## Overview
The framework:
- Generates trading signals from simple strategies
- Applies an explicit backtesting loop with transaction costs
- Avoids lookahead bias
- Evaluates performance using basic risk metrics

This project is intended for educational and demonstration purposes.
It is not a production trading system.

## Assumptions
- Long-only strategies
- Daily close-to-close returns
- Fixed transaction costs
- No leverage

## How to Run
```bash
pip install -r requirements.txt
python run_backtest.py
```

## Notes
Performance results are not intended to represent real-world trading outcomes.
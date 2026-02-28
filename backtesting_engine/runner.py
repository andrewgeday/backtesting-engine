import pandas as pd
import yaml

from backtesting_engine.strategies.moving_average import MovingAverageStrategy
from backtesting_engine.engine.backtest import run_backtest
from backtesting_engine.metrics.performance import sharpe_ratio, max_drawdown


def load_config(path="config.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def run_experiment(config_path: str = "config.yaml"):
    config = load_config(config_path)

    prices = pd.read_csv("data/sample_prices.csv", parse_dates=["date"])
    prices = prices.set_index("date")

    strategy = MovingAverageStrategy(
        short_window=config["strategy"]["short_window"],
        long_window=config["strategy"]["long_window"],
    )

    signals = strategy.generate_signals(prices)
    returns = run_backtest(
        prices,
        signals,
        transaction_cost=config["backtest"]["transaction_cost"],
    )

    print("Sharpe Ratio:", round(sharpe_ratio(returns), 2))
    print("Max Drawdown:", round(max_drawdown(returns), 2))


if __name__ == "__main__":
    run_experiment()
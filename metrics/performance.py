import numpy as np
import pandas as pd

def sharpe_ratio(returns: pd.Series, risk_free: float = 0.0) -> float:
    if returns.std() == 0:
        return 0.0
    return (returns.mean() - risk_free) / returns.std() * np.sqrt(252)

def max_drawdown(returns: pd.Series) -> float:
    cumulative = (1 + returns).cumprod()
    peak = cumulative.cummax()
    drawdown = cumulative / peak - 1
    return drawdown.min()
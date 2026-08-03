# FX forecasting — evaluation summary

| Model | MAE | RMSE | MAPE (%) | Directional accuracy (regression) | Directional accuracy (classifier) |
|---|---|---|---|---|---|
| Hybrid_CNN_LSTM_Transformer | 0.00172 | 0.00256 | 399.6 | 0.4997 | 0.4981 |
| ARIMA | 0.00143 | 0.00215 | 103.9 | 0.4875 | n/a |
| GARCH | 0.00142 | 0.00214 | 106.4 | 0.5044 | n/a |

## Key observations

- Lowest overall MAE: GARCH (0.00142).
- Highest directional accuracy: GARCH (0.5044).
- Caution: the proposed Hybrid model does not outperform GARCH on this run. On data without a strong, real cross-modal signal, extra model capacity tends to fit noise rather than add predictive power — see the README for guidance on validating the architecture against data with a known injected signal, and on real market data once available.
- Hybrid_CNN_LSTM_Transformer's directional accuracy (0.4997) is close to the 0.5 random-guess baseline — treat any directional edge from this run as inconclusive rather than a confirmed skill.
- ARIMA's directional accuracy (0.4875) is close to the 0.5 random-guess baseline — treat any directional edge from this run as inconclusive rather than a confirmed skill.
- GARCH's directional accuracy (0.5044) is close to the 0.5 random-guess baseline — treat any directional edge from this run as inconclusive rather than a confirmed skill.
# FX forecasting — evaluation summary

| Model | MAE | RMSE | MAPE (%) | Directional accuracy (regression) | Directional accuracy (classifier) |
|---|---|---|---|---|---|
| Hybrid_CNN_LSTM_Transformer | 0.00980 | 0.01658 | 1209.2 | 0.5138 | 0.4951 |
| ARIMA | 0.00887 | 0.01512 | 195.3 | 0.4925 | n/a |
| GARCH | 0.00885 | 0.01510 | 136.3 | 0.5237 | n/a |

## Key observations

- Lowest overall MAE: GARCH (0.00885).
- Highest directional accuracy: GARCH (0.5237).
- Caution: the proposed Hybrid model does not outperform GARCH on this run. On data without a strong, real cross-modal signal, extra model capacity tends to fit noise rather than add predictive power — see the README for guidance on validating the architecture against data with a known injected signal, and on real market data once available.
- Hybrid_CNN_LSTM_Transformer's directional accuracy (0.5138) is close to the 0.5 random-guess baseline — treat any directional edge from this run as inconclusive rather than a confirmed skill.
- ARIMA's directional accuracy (0.4925) is close to the 0.5 random-guess baseline — treat any directional edge from this run as inconclusive rather than a confirmed skill.
- GARCH's directional accuracy (0.5237) is close to the 0.5 random-guess baseline — treat any directional edge from this run as inconclusive rather than a confirmed skill.
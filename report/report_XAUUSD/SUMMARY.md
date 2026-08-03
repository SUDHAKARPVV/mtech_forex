# FX forecasting — evaluation summary

| Model | MAE | RMSE | MAPE (%) | Directional accuracy (regression) | Directional accuracy (classifier) |
|---|---|---|---|---|---|
| Hybrid_CNN_LSTM_Transformer | 0.00495 | 0.00784 | 211.9 | 0.5167 | 0.4979 |
| ARIMA | 0.00471 | 0.00736 | 103.1 | 0.5063 | n/a |
| GARCH | 0.00470 | 0.00735 | 107.9 | 0.5378 | n/a |

## Key observations

- Lowest overall MAE: GARCH (0.00470).
- Highest directional accuracy: GARCH (0.5378).
- Caution: the proposed Hybrid model does not outperform GARCH on this run. On data without a strong, real cross-modal signal, extra model capacity tends to fit noise rather than add predictive power — see the README for guidance on validating the architecture against data with a known injected signal, and on real market data once available.
- Hybrid_CNN_LSTM_Transformer's directional accuracy (0.5167) is close to the 0.5 random-guess baseline — treat any directional edge from this run as inconclusive rather than a confirmed skill.
- ARIMA's directional accuracy (0.5063) is close to the 0.5 random-guess baseline — treat any directional edge from this run as inconclusive rather than a confirmed skill.
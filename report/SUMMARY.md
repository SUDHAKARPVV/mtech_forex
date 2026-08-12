# FX forecasting — evaluation summary

| Model | MAE | RMSE | MAPE (%) | Directional accuracy (regression) | Directional accuracy (classifier) |
|---|---|---|---|---|---|
| Hybrid_CNN_LSTM_Transformer | 0.01519 | 0.02463 | 293.9 | 0.5898 | 0.5163 |
| ARIMA | 0.01073 | 0.01456 | 351.8 | 0.6267 | n/a |
| GARCH | 0.01067 | 0.01445 | 313.9 | 0.6133 | n/a |

## Key observations

- Lowest overall MAE: GARCH (0.01067).
- Highest directional accuracy: ARIMA (0.6267).
- Caution: the proposed Hybrid model does not outperform ARIMA, GARCH on this run. On data without a strong, real cross-modal signal, extra model capacity tends to fit noise rather than add predictive power — see the README for guidance on validating the architecture against data with a known injected signal, and on real market data once available.
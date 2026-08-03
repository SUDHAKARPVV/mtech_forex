# -*- coding: utf-8 -*-
"""Body content for the in-place update. Uses H0/H1/H2/BODY/SUB/BUL/CAP/IMG/TBL
helpers, all of which clone formatting from the user's own document."""

TOC_ITEMS = [
 "1. Introduction",
 "1.1 Broad Area of Work",
 "1.2 Background",
 "1.3 Objective",
 "1.4 Scope of Work",
 "1.5 Structure of the Dissertation",
 "2. Literature Survey",
 "2.1 Classical Econometric Foundations",
 "2.2 Deep Sequential and Hybrid Architectures",
 "2.3 Sentiment Fusion",
 "2.4 Volatility Forecasting",
 "2.5 Uncertainty Quantification and Forecast Evaluation",
 "2.6 Synthesis: Four Gaps and How They Are Addressed",
 "3. Implementation Details",
 "3.1 Methodology",
 "3.1.1 Data Layer and Acquisition Pipeline",
 "3.1.2 Multi-Modal Feature Engineering",
 "3.1.3 Dual-Tower Fusion with Cross-Attention",
 "3.1.4 Dilated Causal CNN Layer",
 "3.1.5 Causal Transformer Block",
 "3.1.6 Parallel Gated Recurrent Layer",
 "3.1.7 External Expert Fusion",
 "3.1.8 Regime-Aware Probabilistic Heads",
 "3.1.9 End-to-End Integration and Training",
 "3.2 Design Overview",
 "3.3 Tools and Platform",
 "3.4 Assumptions & Constraints",
 "4. Evaluation Methodology",
 "4.1 Chronological Splitting and Walk-Forward Protocol",
 "4.2 The Base-Rate Control",
 "4.3 Multi-Seed Stability",
 "4.4 Significance Testing",
 "4.5 Metrics and What Each One Answers",
 "4.6 Interval Calibration Protocol",
 "4.7 Leakage Controls and Reproducibility",
 "5. Results & Discussions",
 "5.1 Directional Accuracy: An Honest Negative Result",
 "5.2 Move-Magnitude Forecasting: Where the Hybrid Beats ATR% and GARCH",
 "5.3 Statistical Significance of the Magnitude Edge",
 "5.4 Calibrated Uncertainty through Adaptive Conformal Inference",
 "5.5 Feature and Architecture Studies, Including Negative Results",
 "5.6 Instrument-Specific Results",
 "5.7 Cross-Instrument Comparison",
 "6. Future Plan",
 "6.1 Where the Evidence Says Effort Should Go",
 "6.2 Immediate Extensions",
 "6.3 Exploratory Directions",
 "6.4 Directions Blocked by Data Availability",
 "6.5 Prioritisation, Effort and Risk",
 "7. Conclusion and Future Scope of Work",
 "7.1 What Was Built",
 "7.2 What Was Found",
 "7.3 Contributions",
 "7.4 Limitations and Threats to Validity",
 "7.5 Closing Remarks",
 "8. References",
]

# ============================================================ FRONT MATTER
ACK = []
_A = ACK.append
_A(FRONT("Acknowledgements"))
_A(BODY("I would like to express my sincere gratitude to my supervisor, **Priya Ranjani**, for the guidance and steady encouragement that shaped this dissertation. The direction that mattered most was the insistence on measuring carefully before claiming anything, and that discipline is what turned an ordinary forecasting exercise into a study whose negative findings are as defensible as its positive ones."))
_A(BODY("I am deeply grateful to my faculty mentor, **Dr. Sandeep Subhash Chapalkar**, for the academic guidance that gave this dissertation its shape. The advice to state the evaluation protocol before the results, and to report the studies that failed alongside those that succeeded, is the reason this report reads as a piece of research rather than a demonstration. I am thankful for the patience with which each draft was reviewed and for the consistent insistence on academic rigour."))
_A(BODY("I am equally grateful to my additional examiner, **Vallikannu Karuppiah**, whose critical questions on the directional results pressed me to look harder at how accuracy was being measured. That line of questioning led directly to the base-rate control described in Section 4.2, which reversed one of my early headline results and became central to the argument of this report. A challenge that overturns a result is a more valuable contribution than one that confirms it, and I am thankful for it."))
_A(BODY("I thank **Birla Institute of Technology and Science, Pilani** and the **Work Integrated Learning Programmes** division for the structure and academic resources that made it possible to carry out this work alongside professional commitments, and the faculty of the M.Tech programme for the foundation on which it was built."))
_A(BODY("This dissertation depends heavily on open-source software and openly available data, and that debt should be recorded explicitly. The model is implemented in **PyTorch**; sentiment scoring uses the **FinBERT** model distributed through **Hugging Face Transformers**; the econometric baselines use **statsmodels** and the **arch** package; the tabular expert uses **XGBoost**; the analysis rests on **NumPy**, **pandas**, **SciPy** and **scikit-learn**; the figures are produced with **Matplotlib**; and the live dashboard is built with **Streamlit**. Price data is obtained through the **MetaTrader 5** terminal, news coverage through the **GDELT Project**, Google News and public RSS feeds, and macroeconomic series from **Yahoo Finance** and the **U.S. Bureau of Labor Statistics**. I am grateful to the maintainers and contributors behind each of them."))
_A(BODY("Finally, I thank my family for their patience through the many evenings and weekends this work consumed, and my colleagues for their support and understanding while I balanced this dissertation with professional responsibilities. Any errors that remain in this report are entirely my own."))
_A(BODY("**Disclosure of AI assistance.**  Generative AI assistance was used during the preparation of this report for code review, for drafting and editing prose, and for producing the figures from the underlying result files. All experiments, results and numerical values reported here were generated by the author's own code and data; every figure and statistic in this document is traceable to a committed result artefact, and the author takes full responsibility for the content."))
_A(BODY("**Sudhakar Puppala**"))
_A(BODY("2024AA05488  \u00b7  M.Tech, Birla Institute of Technology and Science, Pilani"))

ABBR = []
_B = ABBR.append
_B(FRONT("Acronyms and Abbreviations"))
_B(TBL([["Abbreviation", "Expansion"],
       ["ACI", "Adaptive Conformal Inference"],
       ["ADX", "Average Directional Index"],
       ["AI", "Artificial Intelligence"],
       ["API", "Application Programming Interface"],
       ["AR(1)", "First-order Autoregressive model"],
       ["ARIMA", "Autoregressive Integrated Moving Average"],
       ["ATR", "Average True Range; ATR% denotes ATR as a percentage of price"],
       ["BatchNorm", "Batch Normalisation"],
       ["Bi-GRU", "Bidirectional Gated Recurrent Unit"],
       ["Bi-LSTM", "Bidirectional Long Short-Term Memory"],
       ["BLS", "Bureau of Labor Statistics (United States)"],
       ["CFTC", "Commodity Futures Trading Commission"],
       ["CNN", "Convolutional Neural Network"],
       ["COT", "Commitments of Traders, a CFTC positioning report"],
       ["CPI", "Consumer Price Index"],
       ["CPU", "Central Processing Unit"],
       ["CSV", "Comma-Separated Values"],
       ["DM", "Diebold–Mariano test of equal predictive accuracy"],
       ["DOM", "Depth of Market"],
       ["DXY", "United States Dollar Index"],
       ["EMA", "Exponential Moving Average"],
       ["EUR/USD", "Euro quoted against the United States Dollar"],
       ["EWMA", "Exponentially Weighted Moving Average"],
       ["FFN", "Feed-Forward Network, the position-wise sub-layer of a Transformer"],
       ["FinBERT", "Finance-tuned BERT (Bidirectional Encoder Representations from Transformers)"],
       ["FX", "Foreign Exchange"],
       ["GARCH", "Generalised Autoregressive Conditional Heteroskedasticity"],
       ["GDELT", "Global Database of Events, Language and Tone"],
       ["GELU", "Gaussian Error Linear Unit"],
       ["GPU", "Graphics Processing Unit"],
       ["GRU", "Gated Recurrent Unit"],
       ["H1", "One-hour bar interval"],
       ["HAC", "Heteroskedasticity- and Autocorrelation-Consistent variance estimator"],
       ["HAR", "Heterogeneous Autoregressive model"],
       ["HAR-RV", "Heterogeneous Autoregressive model of Realised Volatility"],
       ["ICT", "Inner Circle Trader, a retail technical-analysis methodology"],
       ["IRX", "Thirteen-week United States Treasury bill yield (ticker ^IRX)"],
       ["LayerNorm", "Layer Normalisation"],
       ["LSTM", "Long Short-Term Memory"],
       ["MACD", "Moving Average Convergence Divergence"],
       ["MCS", "Model Confidence Set (Hansen, Lunde and Nason)"],
       ["MLP", "Multi-Layer Perceptron"],
       ["MT5", "MetaTrader 5"],
       ["NLL", "Negative Log-Likelihood"],
       ["NLP", "Natural Language Processing"],
       ["OHLC", "Open, High, Low and Close prices of a bar"],
       ["ReLU", "Rectified Linear Unit"],
       ["RSI", "Relative Strength Index"],
       ["RSS", "Really Simple Syndication, a web feed format"],
       ["RV", "Realised Volatility"],
       ["SHAP", "SHapley Additive exPlanations"],
       ["TNX", "Ten-year United States Treasury note yield (ticker ^TNX)"],
       ["XAG/USD", "Silver quoted against the United States Dollar"],
       ["XAU/USD", "Gold quoted against the United States Dollar"],
       ["XGBoost", "Extreme Gradient Boosting"]],
      [1700, 6500]))

NEW = []
A = NEW.append

# ============================================================ 1 INTRODUCTION
A(H0("Introduction"))
A(H1("Broad Area of Work"))
A(BODY("This dissertation falls within the interdisciplinary domain of financial time series analysis, artificial intelligence and computational finance. It focuses on the application of deep learning to model, analyse and forecast foreign exchange rate movements — and, equally important, on establishing rigorously what cannot be forecast. The second half of that sentence is not a hedge: a substantial part of the contribution here is a negative result obtained under controls that much of the applied literature omits, and the methodology needed to obtain it credibly."))
A(BODY("The project draws on the following areas, each of which contributes a specific component rather than being surveyed in the abstract:"))
for t in ["**Natural language processing** — retrieving financial headlines from three independent sources and scoring them with FinBERT, producing thirteen sentiment features aligned to the hourly bar on publication timestamp.",
          "**Knowledge representation** — encoding the technical and volatility structure of currency trading as eighteen indicators with explicitly stated windows, so that every feature is reproducible from the definition alone.",
          "**Data modelling** — acquiring live and historical price, macroeconomic and news data and assembling them into a single leak-free aligned panel of thirty-seven features.",
          "**Deep learning** — a hybrid dual-tower architecture for sequential, multi-modal, multi-step forecasting, combining convolution, cross-attention, causal self-attention and gated recurrence in one differentiable model.",
          "**Prediction analysis** — forecasting on two distinct axes, the direction of the next move and its magnitude, and treating them as separate questions rather than as one problem.",
          "**Statistical inference** — base-rate controls, block bootstrap, Diebold–Mariano tests and the Hansen Model Confidence Set, applied to decide whether a measured edge is genuine.",
          "**Uncertainty quantification** — distribution-free conformal prediction intervals with empirical coverage measured rather than assumed."]:
    A(BUL(t))

A(H1("Background"))
A(BODY("Foreign exchange markets are among the most liquid and volatile financial markets, influenced by macroeconomic indicators, geopolitical events and market sentiment. Traditional forecasting approaches such as ARIMA [1] and GARCH [2] remain foundational, but presuppose stationarity and linear dependence structures that high-frequency currency data routinely violate. Recent advances in deep learning — convolutional, recurrent and Transformer architectures — have shown promising capabilities in modelling sequential and temporal data, and provide an opportunity to improve multi-step forecasting, which is inherently harder than single-step because errors compound across horizons."))
A(BODY("A competing body of theory, beginning with Fama's efficient-market hypothesis [3], predicts that the direction of liquid FX returns should be close to unforecastable. If a reliable directional signal existed at hourly resolution in the most heavily traded market in the world, it would be arbitraged away. This tension between an active applied literature reporting high directional accuracy and a theoretical prediction that such accuracy should not exist is the starting point of this work, and resolving it required attending to how the accuracy is measured rather than to how the models are built."))
A(BODY("The resolution turns on a control that is frequently omitted. Much of the applied literature reports directional accuracy without stating the unconditional base rate of its test window. On a trending instrument an “always long” rule can appear highly accurate while containing no skill whatsoever: if an instrument rises in 53.4% of test bars, a model scoring 53% is performing worse than a rule that ignores its inputs entirely. A central design decision in this work is therefore to measure every directional claim against that base rate, and to treat volatility — the magnitude of the next move — as a separate and, as the results show, considerably more productive forecasting target."))
A(BODY("Three further choices shape the study. The **hourly horizon** was chosen because it is where the efficiency argument bites hardest and where the applied literature is most active, making it the most informative place to test the tension above. **Multi-step rather than single-step** forecasting was chosen because a one-step forecast is of limited practical use for risk management and hides the error-compounding problem entirely. And **three instruments rather than one** were chosen so that a finding could be distinguished from a property of a single series — gold, silver and the euro differ substantially in liquidity, volatility and news density, which makes agreement across them meaningful."))

A(H1("Objective"))
A(BODY("The primary objective is to design and develop an AI-driven framework for multi-step foreign exchange forecasting, and to evaluate it under controls strong enough to distinguish genuine skill from drift. The specific objectives, and the outcome of each, are set out below; the outcomes are stated here so that the introduction does not promise more than the results deliver."))
A(TBL([["Objective","Addressed in","Outcome"],
       ["Design a hybrid CNN-LSTM-Transformer with dual-tower multi-modal fusion","§ 3.1","Met — 4,401,767 parameters, implemented and trained in full"],
       ["Build a reproducible, leak-free pipeline over price, macro and sentiment","§ 3.1.1–3.1.2, § 4.7","Met — 37 features, controls enforced structurally at assembly"],
       ["Fuse GARCH and XGBoost experts through learned trust gates","§ 3.1.7","Met — nested convex blend, bounded by its best component"],
       ["Evaluate direction against the always-up base rate across seeds","§ 4.2, § 5.1","Met — and the result is negative on all three instruments"],
       ["Evaluate magnitude against ATR% and GARCH-σ","§ 5.2","Met — the hybrid beats both, on both metrics, on every seed"],
       ["Establish significance by bootstrap, Diebold–Mariano and MCS","§ 4.4, § 5.3","Met with qualification — the test families disagree, and both are reported"],
       ["Deliver calibrated uncertainty with measured coverage","§ 4.6, § 5.4","Met for gold; extension to silver and euro is the first item of § 6.2"],
       ["Extend the study from one instrument to three","§ 5.6–5.7","Met — independent pipelines and checkpoints per instrument"]],
      [3000,1100,4100]))
A(CAP("Table 1: Research objectives, where each is addressed, and the outcome of each."))
A(BODY("Two of these deserve a note. The fourth objective was met in the sense that matters methodologically — the evaluation was carried out correctly — while returning a negative answer, and that distinction between meeting an objective and obtaining a favourable result is maintained throughout this report. The sixth was met with a genuine qualification: two families of significance test reached different conclusions, and Section 5.3 reports the disagreement rather than selecting the more favourable of the two."))

A(H1("Scope of Work"))
A(BODY("The study covers three instruments — gold (XAU/USD), silver (XAG/USD) and the euro (EUR/USD) — at hourly resolution over 2016 to 2026, giving 62,049, 62,328 and 65,587 bars respectively. Each instrument has an entirely independent pipeline: its own price history, its own scored news archive and its own trained checkpoint, so that cross-instrument comparisons are like-for-like rather than artefacts of a shared fit."))
A(IMG("fig_study_scope", 6.1))
A(CAP("Figure 1: The study at a glance — three instruments, the two forecasting axes, the fixed experimental parameters, and what was deliberately excluded."))
A(BODY("Stating what the work does not cover is as useful as stating what it does, because several of the exclusions bound the conclusions directly."))
A(TBL([["In scope","Out of scope"],
       ["Data acquisition, preprocessing, feature engineering and leak-free alignment","Automated order execution and latency-sensitive high-frequency trading"],
       ["Design, training and multi-seed evaluation of the hybrid architecture","Portfolio construction and multi-asset allocation"],
       ["Directional and magnitude forecasting, each with its own control","Transaction costs, spread and slippage — so no figure here is a return claim"],
       ["Statistical significance testing and conformal uncertainty calibration","Order-flow and depth-of-market features, for which no historical source is obtainable"],
       ["A live dashboard serving the trained model with calibrated intervals","Reinforcement learning for execution, noted as future scope in § 6.3"]],
      [4100,4100]))
A(CAP("Table 2: Scope of the study. The exclusions in the right-hand column bound the conclusions and are revisited as limitations in Section 7.4."))

A(H1("Structure of the Dissertation"))
A(BODY("The remainder of this report is organised as follows. **Section 2** reviews the literature across five strands and identifies the four gaps that define this work's positioning. **Section 3** describes the implementation, first as a layered system design and then layer by layer through the architecture, with a diagram and a parameter budget for each stage. **Section 4** states the evaluation methodology in full — the chronological split, the base-rate control, multi-seed stability, the significance battery, the metrics, the interval calibration protocol and the leakage controls — and is deliberately placed before the results, because the protocol is what makes the results interpretable."))
A(BODY("**Section 5** presents the results on both axes, including the negative directional finding, the magnitude advantage and its significance testing, the conformal calibration outcome, the feature and architecture studies, and the per-instrument and cross-instrument comparisons. **Section 6** sets out the forward programme, ordered by the strength of the evidence behind each direction. **Section 7** concludes with the claims, contributions and limitations. **Section 8** lists the references."))
A(BODY("A reader interested only in the headline findings can read Section 4.2 for the control that makes the directional result meaningful, then Sections 5.1 to 5.4 for the results themselves, and Section 7.2 for the summary."))

A(H0("Literature Survey"))
A(BODY("The trajectory of foreign exchange and equity price forecasting research reveals a clear progression from linear econometric assumptions towards non-linear, data-driven and increasingly multi-modal architectures. The review below is organised into five strands, each of which contributed a specific design decision to this work, and closes with the four gaps that the dissertation is positioned against."))

A(H1("Classical Econometric Foundations"))
A(BODY("Classical models such as the Box–Jenkins ARIMA framework [1] and Bollerslev's GARCH formulation [2] remain foundational for modelling autocorrelation and volatility clustering respectively. Both presuppose stationarity and linear dependence structures that are routinely violated by high-frequency currency data, which is the standard motivation for the shift towards deep sequential learners."))
A(BODY("They are retained here for two reasons that go beyond convention. First, they are the correct baselines: GARCH in particular is purpose-built for the volatility forecasting task on which this work claims an advantage, so beating it is a meaningful claim in a way that beating a naive persistence model would not be. Second, they are fused into the architecture as trust-gated experts rather than only compared against it, on the reasoning that a model with a genuinely different inductive bias is more useful as a component than as a foil. Section 5.1 shows the value of the first decision unusually clearly: GARCH's apparently superior directional accuracy turns out to be its momentum drift reproducing the base rate, which is only visible because the base rate was computed."))

A(H1("Deep Sequential and Hybrid Architectures"))
A(BODY("Hochreiter and Schmidhuber's Long Short-Term Memory architecture [4] established the gating mechanisms that allow recurrent networks to retain information across long sequences while mitigating vanishing gradients, and remains the backbone of nearly every sequential forecasting study reviewed here; the standard reference treatment of the underlying methods is Goodfellow, Bengio and Courville [5]. Dave, Varastehpour and Shakiba [6] benchmark these three families across four currency pairs and conclude that no single architecture dominates across all market regimes — a finding that directly motivates this dissertation's hybrid, ensemble-of-experts design rather than a single-model design, and which is operationalised in the trust-gated expert fusion of Section 3.1.7."))
A(BODY("Yohannes et al. [7] show that windowed LSTM encoders fused with news sentiment outperform ARIMA baselines, and López-Herrera, González Maiz Jiménez and Reyes Santiago [8] evaluate directional forecasting across eight dollar pairs with machine-learning methods. Luangluewut and Thiennviboon [9] convert price sequences into image-like representations and report approximately 93% directional accuracy, evidencing that local pattern extraction surfaces information sequence-only models can miss, and justifying the CNN stage retained here — though in causal, non-pooling form, for the reasons given in Section 3.1.4."))
A(BODY("An important methodological caveat applies to this group of results, and it is the caveat from which much of this dissertation follows. Several of these studies report directional accuracy without stating the base rate of their test window, and a reported 93% on a trending instrument cannot be interpreted without it. The present work reproduces that style of measurement and then applies the base-rate control, and finds that the apparent skill largely disappears — a result reported in full in Section 5.1. This is offered as a methodological observation rather than as a criticism of any individual study: the control is inexpensive, and its absence makes an otherwise sound result impossible to assess."))

A(H1("Sentiment Fusion"))
A(BODY("Dash and Mishra [10] report that a trend-prediction model conditioned on macroeconomic and microeconomic sentiment surpasses 96% accuracy on Indian market data. Tadphale et al. [11] build a USD/INR model augmented with a sentiment index derived using FinBERT [12] and show it behaving as a leading indicator of exchange-rate movement; this is the principal precedent for the choice of FinBERT as the NLP backbone here."))
A(BODY("This dissertation tests that claim directly rather than assuming it. The modality ablation of Section 5.5 finds that for magnitude forecasting at hourly resolution, price and volatility structure carry essentially all of the usable signal, and the sentiment channel adds approximately nothing. That is a null result against the premise of the architecture, and it is reported as such. It does not contradict the cited work — the instruments, horizons and targets all differ — but it does indicate that the benefit of sentiment fusion is considerably more horizon-dependent and target-dependent than the literature generally acknowledges."))

A(H1("Volatility Forecasting"))
A(BODY("Because this dissertation's positive result lies on the volatility axis, the realised-volatility literature is directly relevant. The Financial Innovation survey of realised-volatility methods by Leushuis and Petkov [13] concludes that hybrid CNN-LSTM models are among the strongest performers, supporting the architecture retained here. HARNet [14] bridges the classical Heterogeneous AutoRegressive model and deep learning through hierarchies of dilated convolutions — the same mechanism used in the CNN stage of Section 3.1.4 — and hybrid HAR-LSTM-GARCH designs report gains on energy futures [15]. Transformer architectures have since been applied to volatility forecasting on U.S. equity indices [16], and realised-GARCH forecasts have been combined with deep LSTM encoders [17]."))
A(BODY("Corsi's HAR model [18] remains the canonical multi-timescale volatility benchmark, and was evaluated directly as a candidate feature set. That study is reported in Section 5.5 as a negative result with an instructive cause: the HAR-RV features pre-checked strongly, showing partial correlations of +0.11 to +0.17 with the target after controlling for ATR%, yet added nothing once inside the network. The dilated convolution stack was already extracting the same multi-timescale structure from raw returns, which is precisely what the HARNet line of work would predict."))

A(H1("Uncertainty Quantification and Forecast Evaluation"))
A(BODY("Point forecasts alone are of limited use for risk management, so this framework adopts conformal prediction. Ensemble Conformalized Quantile Regression [19] constructs distribution-free prediction intervals that remain valid for non-stationary and heteroskedastic series, building on the conformalized quantile regression of Romano, Patterson and Candès [20]. The Adaptive Conformal Inference of Gibbs and Candès [21] extends this to distribution shift by updating the working miscoverage level online — the mechanism that proves necessary here, because the test period is materially more volatile than the calibration period and split conformal alone under-covers as a result."))
A(BODY("For deciding whether one forecaster genuinely beats another, the standard instruments are the Diebold–Mariano test of equal predictive accuracy [22] and Hansen's Model Confidence Set [23], which returns the set of models statistically indistinguishable from the best. Both are applied in Section 5.3, alongside a block bootstrap. That this work applies all three rather than one turned out to matter: the bootstrap and the two squared-error tests reach different conclusions on the same data, a divergence traced in Section 4.4 to the difference between ordering magnitude and reducing squared error."))

A(H1("Synthesis: Four Gaps and How They Are Addressed"))
A(BODY("Four gaps emerge consistently across this body of work and define the positioning of the present dissertation."))
for t in ["The reviewed studies generally treat CNN-based local extraction, recurrent temporal modelling, Transformer attention and NLP sentiment fusion as separate, single-purpose pipelines rather than as complementary stages of one unified architecture.",
          "Almost none address multi-step ahead forecasting explicitly; most report single-step accuracy, leaving the compounding error-propagation problem largely unexamined.",
          "Directional accuracy is frequently reported without the unconditional base rate of the test window and without a significance test, so drift cannot be distinguished from skill.",
          "Few studies quantify whether their uncertainty bands achieve their nominal coverage out of sample."]:
    A(BUL(t))
A(IMG("fig_gaps", 6.1))
A(CAP("Figure 2: The four gaps identified in the literature review, and the specific component of this work that addresses each."))
A(BODY("The first two gaps are architectural and the second two methodological, and the distinction matters for how this dissertation should be read. The architectural gaps are closed by design decisions whose benefit is assumed until measured — and Section 5.5 shows that one of them, multi-modal fusion, delivered no measurable magnitude benefit at this horizon. The methodological gaps are closed by controls whose effect is immediate and, in this case, decisive: applying the base-rate control is what converted an apparently positive directional result into a negative one, and measuring coverage is what revealed the raw Gaussian bands to be badly mis-calibrated."))
A(BODY("It is worth being explicit that closing gaps three and four is what produced the negative findings of this report. A study that omitted those controls, using the same architecture and the same data, would have reported a directional success and an uncalibrated uncertainty band, and would have looked more favourable. The comparison table below summarises how the reviewed studies relate to this work on the dimensions that matter."))
A(TBL([["Study / line of work","Contribution taken forward","Base-rate control?","Coverage measured?"],
       ["ARIMA / GARCH (Box–Jenkins, Bollerslev)","Retained as walk-forward baselines and as fused experts","n/a","n/a"],
       ["LSTM / XGBoost / Transformer benchmark (2025)","No architecture dominates — motivates the expert blend","Not stated","No"],
       ["Sequential deep learning with sentiment (2025)","Windowed encoder fused with news sentiment","Not stated","No"],
       ["CNN for forex trend prediction (2023)","Local pattern extraction; adapted to causal, non-pooling form","Not stated","No"],
       ["Sentiment-augmented FX prediction (2023)","FinBERT as the NLP backbone","Not stated","No"],
       ["Realised-volatility survey (2025); HARNet (2022)","Dilated convolutions for multi-timescale volatility","n/a","No"],
       ["Conformal prediction (Romano; Gibbs and Candès)","Split and adaptive conformal calibration","n/a","Yes"],
       ["Diebold–Mariano (1995); Hansen MCS (2011)","Formal forecast-comparison tests","n/a","n/a"],
       ["**This work**","Unified architecture plus a controlled protocol","**Yes, on every claim**","**Yes, per horizon**"]],
      [2600,2700,1500,1400]))
A(CAP("Table 3: How the reviewed work relates to this dissertation on the two controls that determine whether a reported result can be interpreted."))
A(BODY("This dissertation's hybrid architecture, its multi-modal feature-fusion pipeline, its base-rate-controlled and significance-tested evaluation protocol, and its conformal uncertainty layer are designed specifically to close these four gaps — and the report is candid about which of the four turned out to matter most."))

# ============================================================ 3 IMPLEMENTATION
A(H0("Implementation Details"))
A(H1("Methodology"))
A(BODY("The methodology is organised as a five-stage pipeline that converts raw, heterogeneous market data into a regime-conditioned, multi-step, probabilistic foreign-exchange forecast. Each stage is implemented as an independently testable module so that ablation studies can isolate the marginal contribution of every component. Figure 3 summarises the complete architecture with the tensor shape produced at every hand-off; the sub-sections that follow specify each stage down to exact layer dimensions, so that the architecture is reproducible from this report alone."))
A(BODY("Two structural properties characterise the architecture. First, the quantitative and textual modalities travel in **separate towers** and meet at a single cross-attention fusion node rather than being concatenated at the input, so the price tower remains fully functional when news is absent. Second, **sequence length is preserved end to end**: no stage pools along the time axis, and the 60-bar axis survives intact until a single attention-pooling step immediately before the forecast heads."))
A(IMG("fig_architecture", 6.1))
A(CAP("Figure 3: Consolidated architecture — dual-tower multi-modal fusion, causal Transformer, parallel gated recurrent stage, trust-gated external experts and regime-aware probabilistic heads. Total trainable parameters 4,401,767."))

A(H2("Data Layer and Acquisition Pipeline"))
A(BODY("The data layer is specified here in full. All three streams are acquired independently for each instrument and aligned onto a common hourly grid."))
A(SUB("Price acquisition — MetaTrader 5"))
A(BODY("Prices are read from a MetaTrader 5 terminal attached in strictly read-only mode; the system never places an order. Two paths sit behind an environment-controlled router:"))
for t in ["**csv** (default for training) — the curated terminal export, containing genuine hourly bars back to 2010. This path is mandatory for historical work: the broker’s live API holds genuine intraday data only from 2023 and silently returns daily bars for older intraday requests, a defect that would have contaminated the training set had it gone undetected.",
          "**live** — a direct pull from the attached terminal for the freshest bars.",
          "**auto** — live first with CSV fallback; used by the dashboard’s live-inference path."]:
    A(BUL(t))
A(BODY("The panel is restricted to 2016 onwards because the news archive begins in 2016; earlier price bars would be sentiment-dead and would depress coverage without adding usable multi-modal history."))
A(SUB("News acquisition and FinBERT sentiment scoring"))
A(BODY("Headlines are harvested from three complementary sources: the GDELT DOC 2.0 API for historical depth, Google News RSS for recent density, and direct financial RSS feeds for the freshest items. Each headline is scored once by FinBERT, a BERT-family transformer pre-trained on financial text, producing a polarity and a confidence. Scores are cached per headline in a per-instrument archive so that re-runs never re-score existing text; the archives currently hold 22,833 headlines for gold, 11,413 for silver and 10,605 for euro. A per-instrument relevance filter removes cross-asset and off-topic items before alignment."))
A(SUB("Macroeconomic acquisition"))
A(BODY("The short-rate (^IRX), the ten-year yield (^TNX) and the dollar index are taken from Yahoo Finance, and CPI from the US Bureau of Labor Statistics. Each series is converted to a stationary form — z-scores, differences or returns — before use."))
A(SUB("Leak-free alignment"))
A(BODY("Three controls prevent look-ahead, each added in response to a defect found during development:"))
for t in ["Macro releases are **shifted forward by one day** before being forward-filled onto hourly bars. Without this shift a same-day macro value reaches bars that closed before the figure was published; the defect inflated one instrument’s directional accuracy to 0.62 and was caught by a leakage scan correlating each feature against the same-day close.",
          "News is aligned strictly on **publication timestamp** with a bounded trailing reach, so a bar never sees a headline published after it closed.",
          "Normalisation statistics are computed on the **training split only** and applied unchanged to validation and test."]:
    A(BUL(t))
A(IMG("fig_data_layer", 6.0))
A(CAP("Figure 4: Data layer — three independently acquired streams, their processing, and the leak controls applied before they are fused into the aligned feature panel."))

A(H2("Multi-Modal Feature Engineering"))
A(BODY("Every bar carries 37 engineered features across three groups. All are stationary transforms; the model never sees a raw price level, which the ADF test confirms is non-stationary."))
A(TBL([["Stream","Count","Features"],
       ["Technical","18","OHLC log-returns (4), RSI, MACD histogram, Bollinger width, volume z-score, ATR%, ROC-10, Stochastic %K, EMA12/26 ratio, envelope deviation, Bollinger %B, drift over 5/21/60 bars, drift t-statistic"],
       ["Macroeconomic","6","short-rate z-score, 10-year yield change, dollar-index return, CPI year-on-year, CPI month-on-month, days since CPI release"],
       ["Sentiment","13","FinBERT rolling mean/std/min/max, decayed EWMA score, sentiment momentum, sentiment volatility, diffusion breadth, headline-count z-score, and four one-hot signal states (buy/sell/hold/none)"]],
      [1150,620,6030]))
A(CAP("Table 4: Feature inventory by stream. All 37 features are aligned to the same hourly bar."))
A(BODY("Each indicator is defined below with the exact window used in the implementation."))
A(SUB("Technical stream (18 features)"))
A(TBL([["Feature","Definition","What it captures"],
       ["ret_open","log(open / previous close)","opening gap pressure carried in from the prior bar"],
       ["ret_high","log(high / previous close)","how far buyers extended price within the bar"],
       ["ret_low","log(low / previous close)","how far sellers extended price within the bar"],
       ["ret_close","log(close / previous close)","the bar’s net move — the primary price signal"],
       ["rsi","14-bar Relative Strength Index, scaled to [0,1]","momentum and overbought / oversold state"],
       ["macd_hist","(12/26 EMA difference − its 9-EMA signal) ÷ price","trend acceleration, normalised for price level"],
       ["bb_width","20-bar Bollinger band width (±2σ) ÷ price","volatility proxy — how wide the trading range is"],
       ["volume_z","tick volume z-scored over 20 bars","participation and conviction behind the move"],
       ["atr_pct","14-bar Average True Range ÷ price","the core volatility scale; also the ATR% baseline"],
       ["roc_10","log(close / close 10 bars ago)","medium-horizon rate of change"],
       ["stoch_k","position of close in the 14-bar high–low range","bounded mean-reversion gauge"],
       ["ema_ratio","log(EMA12 / EMA26)","smooth, scale-free trend direction"],
       ["env_dev20","(close ÷ 20-bar SMA) − 1","envelope deviation — how stretched price is from its mean"],
       ["bb_pctb","position of close within the Bollinger band (0 = lower, 1 = upper)","price position vs the band, complementing bb_width"],
       ["drift_5","mean log-return over 5 bars","short-horizon conditional mean"],
       ["drift_21","mean log-return over 21 bars","medium-horizon drift"],
       ["drift_60","mean log-return over 60 bars","drift across the full lookback window"],
       ["drift_tstat","drift_21 ÷ 21-bar return standard deviation","drift strength relative to noise — the GARCH-style conditional-mean state"]],
      [1300,3050,3450]))
A(CAP("Table 5: Technical indicators — definition and interpretation."))
A(SUB("Macroeconomic stream (6 features)"))
A(BODY("Every macro series is transformed to a stationary form and shifted forward by one day before it is forward-filled onto hourly bars, so no bar can see a figure published after it closed."))
A(TBL([["Feature","Definition","What it captures"],
       ["rate_z21","short rate (^IRX) z-scored over 21 days","where policy rates sit relative to their recent range"],
       ["yield_chg5","5-day change in the 10-year yield (^TNX)","direction of longer-term rate expectations"],
       ["dollar_ret5","5-day log return of the dollar index","USD strength — the dominant common driver for metals and EUR/USD"],
       ["cpi_yoy","CPI year-over-year, per cent","the prevailing inflation regime"],
       ["cpi_mom","CPI month-over-month, per cent","inflation surprise proxy"],
       ["days_since_cpi","days since the last CPI release, scaled and clipped","decay of impact after a macro print"]],
      [1300,3050,3450]))
A(CAP("Table 6: Macroeconomic indicators — definition and interpretation."))
A(SUB("Sentiment stream (13 features)"))
A(BODY("FinBERT assigns each headline a polarity and a confidence; their product is aggregated into a per-bar sentiment score, from which the following are derived."))
A(TBL([["Feature","Definition","What it captures"],
       ["sent_mean","5-bar rolling mean of the per-bar score","prevailing news tone"],
       ["sent_std","5-bar rolling standard deviation","disagreement between headlines"],
       ["sent_min","5-bar rolling minimum","the worst recent headline — downside shock"],
       ["sent_max","5-bar rolling maximum","the best recent headline — upside shock"],
       ["sent_decay","EWMA of the score, 3-bar half-life","smoothed tone that stays responsive to shifts"],
       ["sent_momentum","first difference of the score","rate of change of sentiment"],
       ["sent_vol","10-bar rolling standard deviation","sentiment volatility — how unstable the tone is"],
       ["sent_diffusion","EWMA of (bullish − bearish) ÷ total headlines","breadth of agreement, independent of score magnitude"],
       ["headline_count_z","headline count z-scored over 20 bars","news intensity — attention spikes around events"],
       ["sig_buy","one-hot: smoothed score above +threshold and positive","a decisive bullish news state"],
       ["sig_sell","one-hot: smoothed score below −threshold and negative","a decisive bearish news state"],
       ["sig_hold","one-hot: news present but inside the neutral band","news exists but carries no clear direction"],
       ["sig_none","one-hot: no headlines in the bar","explicit absence of news — see note below"]],
      [1300,3050,3450]))
A(CAP("Table 7: FinBERT sentiment indicators — definition and interpretation."))
A(BODY("Two design points deserve emphasis. The **drift t-statistic** encodes the GARCH-style conditional-mean state directly as a feature, giving the network access to the same trend information the econometric baseline exploits. The **none signal state** is explicit rather than implied: bars carrying no headlines are labelled as such, so the network learns that the absence of news is itself informative rather than treating it as neutral sentiment."))
A(BODY("The quantitative and sentiment groups are delivered to the model as two separate tensors — (B, 60, 24) and (B, 60, 13) — split by the data loader. This structural separation is what makes the dual-tower design possible and removes any risk of in-network slicing errors."))

A(H2("Dual-Tower Fusion with Cross-Attention"))
A(BODY("Price and news are not the same kind of signal. Price is dense, evenly spaced and numeric; news is sparse, irregularly timed and semantic. Concatenating them into one vector implicitly asserts that both are always present and equally informative, which is false for a large fraction of the hourly bars in this study. The architecture therefore keeps them in separate towers and lets them meet through an attention operator that can, in principle, decline the second stream entirely."))
A(BODY("**Tower A (quantitative).** The 24-dimensional technical and macro vector is projected 24 to 64 and passed to the dilated causal CNN of Section 3.1.4, giving local features of shape (B, 60, 128). A volatility **regime embedding** — a 2 to 128 projection of realised volatility and ATR at the forecast origin — is added at every position, so all downstream layers are aware of the prevailing volatility regime rather than having to infer it."))
A(BODY("**Tower B (textual).** The 13-dimensional sentiment vector is encoded by a GRU (13 to 64) and projected to 128, producing a text sequence aligned bar-for-bar with the quantitative tower. A GRU rather than a second convolutional stack is used here because the sentiment stream is short and sparse: its informative structure is the persistence of a mood across consecutive bars, which a recurrent state carries naturally and a fixed-width kernel does not."))
A(BODY("**Fusion node.** The towers meet through multi-head cross-attention with four heads over the 128-dimensional local space. The quantitative stream supplies the queries and the text stream the keys and values, so each price position retrieves the news context relevant to it rather than receiving a single window-level sentiment summary. The direction of this asymmetry matters: it is the price bar that asks the question and the news that answers, which is the correct causal reading for a forecasting task."))
A(BODY("The attention output re-enters through a **presence gate** — a sigmoid computed from the raw text features, only 14 parameters — giving the residual fused = LayerNorm( local + sigmoid(text_gate(text)) x CrossAttention(local, text, text) ). Because the gate multiplies the attention output while the residual carries the local representation unchanged, a closed gate reduces the whole node to the identity on the price tower. The graceful degradation is therefore structural rather than something the training run has to discover."))
A(BODY("This is reinforced by **modality masking**: the entire text stream is zeroed for a random 40% of training samples, forcing the network to remain accurate without news rather than becoming dependent on a stream that is sparse in the early years. The masking rate is deliberately close to the true fraction of news-poor bars, so the training distribution of gate states resembles the deployment distribution. This is the mechanism that allows a single checkpoint to serve both news-rich and news-poor periods, and it is why no separate news-free model had to be trained."))
A(IMG("fig_layer_fusion", 6.0))
A(CAP("Figure 5: Cross-attention fusion node. The price tower supplies queries, the news tower supplies keys and values, and a presence gate scales the attention output before the residual add, so a bar carrying no headlines falls back exactly to its price representation."))

A(H2("Dilated Causal CNN Layer"))
A(BODY("A conventional convolutional stage would pool along the time axis and pad symmetrically. This architecture does neither, for two reasons: pooling discards temporal resolution that the attention stages downstream can otherwise exploit, and symmetric padding lets each position see one step into its own future — a subtle leak at bar granularity that would inflate every metric reported in Section 5 without ever raising a visible error."))
A(BODY("The implemented layer uses three stacked causal dilated convolution blocks with dilations 1, 2 and 4 (the WaveNet pattern), each Conv1d then BatchNorm then ReLU, widening 64 to 128 channels in 124,032 parameters — 2.8% of the model:"))
for t in ["**Left-only padding** of (kernel minus 1) x dilation guarantees that position t is computed only from positions at or before t, making the stage strictly causal. The padding is applied before the convolution and the surplus right-hand positions are discarded afterwards, which is what makes the causality structural rather than a property that has to be checked after the fact.",
          "**Exponentially growing receptive field.** With kernel 3 and dilations 1, 2 and 4 the effective span is 1 + 2(1+2+4) = 15 bars, five times the 3-bar span of a single convolution and reached without any pooling. Fifteen hourly bars is a little over one trading session, which is the scale at which intraday motifs such as a breakout and its retracement actually complete.",
          "**Full temporal resolution preserved** — the output remains (B, 60, 128), so every subsequent stage still sees all 60 bars. The time axis is collapsed exactly once in the entire network, at the attention-pooling step of Section 3.1.6.",
          "**BatchNorm rather than LayerNorm** at this depth, because the channel statistics of technical indicators are stable across a batch of windows drawn from one instrument, and normalising per channel keeps indicators on very different natural scales — RSI in [0,100], log returns near zero — comparable to one another."]:
    A(BUL(t))
A(BODY("The practical consequence is that the CNN can represent compound local motifs, such as a sharp move followed by a partial retracement, over a meaningful window while remaining causal and lossless in time. Its role in the stack is deliberately narrow: it is a local feature detector, and every relation longer than fifteen bars is left to the attention stage that follows, where it can be modelled without the linear parameter growth a wider convolution would require."))
A(IMG("fig_layer_cnn", 6.1))
A(CAP("Figure 6: Dilated causal convolution stack. Tracing one output position backwards through the three blocks shows the receptive field opening to exactly 15 bars, with no connection ever reaching to the right of the position being computed."))

A(H2("Causal Transformer Block"))
A(BODY("The fused representation is projected 128 to 256 and passed through four Transformer encoder layers [24] with eight attention heads (d_head = 32) and a 1024-dimensional feed-forward sub-layer, using pre-norm residual connections. At 3,159,040 parameters this single stage carries 71.8% of the capacity of the model, which is a deliberate allocation: the fifteen-bar limit of the convolutional stage means that every relation spanning more than one session has to be represented here."))
for t in ["**Causal masking is enabled.** Each position attends only to itself and to earlier positions. A bidirectional encoder over an already-observed window is defensible in principle — the whole window is history at forecast time — but causal masking makes the training-time computation identical to the inference-time computation and removes any possibility of within-window future leakage. The cost is roughly half the available attention mass; the benefit is that no result in this report depends on an argument about whether a particular bidirectional read was admissible.",
          "**Multi-head specialisation.** With eight heads the model can simultaneously represent short-horizon momentum relations and long-range regime relations, which a single attention map could only average. Head width is 32, small enough that individual heads are pushed to specialise rather than each learning a diluted copy of the same relation.",
          "**Pre-norm residuals** normalise before each sub-layer rather than after, preserving a direct gradient path from the loss to the first layer. At four layers this is not strictly necessary for convergence, but it removes the warm-up schedule that post-norm Transformers typically require and makes the run reproducible across seeds — which matters because every headline result in Section 5 is reported over three seeds.",
          "**Scaling by the square root of d_head** prevents the dot products from saturating the softmax as head width grows, keeping the attention distribution responsive rather than collapsing onto a single position."]:
    A(BUL(t))
A(BODY("The output remains a full sequence of shape (B, 60, 256): attention relates positions to one another but does not collapse the time axis. Feeding a sequence rather than a summary into the recurrent stage that follows is what allows that stage to add anything at all, since a pooled vector would leave it nothing to recur over."))
A(IMG("fig_layer_transformer", 5.9))
A(CAP("Figure 7: One causal encoder layer, repeated four times, with the attention mask that enforces causality. Filled cells mark the query-key pairs the softmax is allowed to score; everything above the diagonal is set to negative infinity before normalisation."))

A(H2("Parallel Gated Recurrent Layer"))
A(BODY("Attention is permutation-equivariant: it relates positions through learned content similarity, not through adjacency. Recurrence supplies the complementary bias, processing bars in order and carrying an explicit state. Rather than choosing between the two standard recurrent cells in advance, both are run and the network is allowed to weight them."))
for t in ["A **bidirectional LSTM** (hidden size 128 per direction, 256 output, 395,264 parameters) models temporal structure through explicit input, forget and output gates and a persistent cell state, which suits slow-moving regimes where information must be retained across many bars.",
          "A **bidirectional GRU** (hidden size 128 per direction, 256 output, 296,448 parameters) models the same sequence with a lighter two-gate mechanism that tends to adapt faster to abrupt changes, which suits volatility bursts.",
          "A **learned temporal gate** consumes the mean-pooled state of each branch and produces a scalar lambda in [0,1] from just 513 parameters, giving the convex mixture lambda x LSTM + (1 minus lambda) x GRU. Because lambda is computed from the branch states themselves it is input-dependent: the mixture can differ between a quiet session and a volatile figure release within the same instrument."]:
    A(BUL(t))
A(BODY("Bidirectionality is admissible here and is not a leak. The backward pass runs over the sixty bars of the input window, every one of which is strictly in the past relative to the forecast origin; no future bar enters the window at any point. This is a different question from the causal masking of Section 3.1.5, which concerns whether a position may see later positions inside the window, and the two choices were made independently."))
A(BODY("Placing the recurrent stage after attention allows it to smooth and consolidate globally-contextualised representations rather than raw local features. An attention-weighted pooling step then collapses (B, 60, 256) to a single context vector (B, 256) using a learned query of 257 parameters — the only point in the network where the time axis disappears. Learning the pooling weights rather than taking the last hidden state matters at H1, where the most recent bar is frequently the noisiest one in the window."))
A(IMG("fig_layer_recurrent", 6.0))
A(CAP("Figure 8: Parallel gated recurrent stage. Both recurrent inductive biases are computed, mixed by an input-dependent scalar, and pooled by a learned attention query rather than by taking the final hidden state."))

A(H2("External Expert Fusion"))
A(BODY("The finding in the literature that no single architecture dominates is operationalised directly: rather than presenting classical forecasters only as baselines in a results table, two of them are fused into the network as parameterised components."))
for t in ["**XGBoost expert** [25] — a gradient-boosted tabular model trained on summary statistics of the same window, refitted walk-forward so that each test block is predicted by a model fitted only on data preceding it. It contributes a decision-tree inductive bias, namely axis-aligned thresholds on indicator levels, which the deep network composes only inefficiently out of smooth functions.",
          "**GARCH expert** — a walk-forward AR(1)-GARCH(1,1) conditional-mean forecast, refitted on a stride and forward-filled, again strictly causally. It contributes the volatility-clustering structure that is the single most reliable empirical regularity in this data, and Section 5.2 shows it to be a genuinely hard baseline to beat."]:
    A(BUL(t))
A(BODY("Each expert forecast is normalised, passed through dropout, and embedded to 32 dimensions in 2,784 parameters, then scaled by a **trust gate** — a sigmoid of the two-dimensional volatility regime context, 30 parameters per expert. The gate is conditioned on volatility specifically because that is the variable along which the relative competence of the experts is known to vary: GARCH is strongest exactly where realised volatility is autocorrelated, and the deep model has more to offer where it is not."))
A(BODY("The final forecast is a nested convex blend: inner = t_xgb x XGB + (1 minus t_xgb) x deep, then forecast = t_garch x GARCH + (1 minus t_garch) x inner. Because both stages are convex combinations with coefficients in [0,1], the output always lies inside the convex hull of its three inputs, so the worst case is deferral to the strongest single expert — the fusion cannot make the model worse than its best component. A deep-supervision term keeps the deep branch independently accurate so that it never degenerates into a passive pass-through of the classical experts, which is the failure mode this design would otherwise invite."))
A(IMG("fig_layer_experts", 6.0))
A(CAP("Figure 9: External expert fusion. The trust signal derived from the volatility regime scales both expert embeddings and sets the blending weights, so the network can shift its reliance between the econometric and the deep branch as conditions change."))

A(H2("Regime-Aware Probabilistic Heads"))
A(BODY("The context vector concatenates four sources — the deep context (256), a skip connection carrying the raw macro and sentiment values at the most recent bar (32), and the two trust-gated expert embeddings (32 each) — giving 352 dimensions, assembled in 131,328 parameters. The skip path exists because sixty bars of convolution, attention and recurrence is a long route for a single scalar such as the current short-rate level to survive intact; the skip guarantees that the most recent macro and sentiment readings reach the forecast head undiluted."))
A(BODY("Two decoder heads, one specialised for stable regimes and one for high-volatility regimes, are combined by a soft gate driven by the volatility context. The gate is a sigmoid rather than a hard threshold, so behaviour changes continuously as market conditions evolve rather than jumping discontinuously at an arbitrary cut-off. Keeping the path differentiable also means both heads receive gradient on every batch instead of only on the batches assigned to them. The complete output stage costs 132,265 parameters."))
A(BODY("Each head emits, for each of the k = 10 horizons, a mean and a log-variance, trained under a Gaussian negative log-likelihood. Predicting log-variance rather than variance keeps the output unconstrained while the exponential guarantees positivity without a clamp. The NLL objective is what makes the model probabilistic rather than merely a point predictor: it must widen sigma when it is genuinely uncertain, because over-confidence is penalised through the squared-error term and under-confidence through the log-variance term."))
A(BODY("This sigma head is the quantity later calibrated by adaptive conformal inference in Section 5.4, where the raw NLL sigma is shown to be substantially over-confident — 63.3% empirical coverage at a nominal 80% for gold — and the conformal layer is shown to repair it without retraining. An auxiliary directional head and a directional loss term (weight 0.35) are retained for diagnostic purposes; Section 5.1 explains why its output is reported as a negative result rather than as a headline metric."))
A(IMG("fig_layer_heads", 6.0))
A(CAP("Figure 10: Regime-aware probabilistic heads. Two decoders are blended continuously by a volatility-driven gate, and each horizon receives a mean and a log-variance trained under Gaussian negative log-likelihood."))

A(H2("End-to-End Integration and Training"))
A(BODY("Every stage is differentiable and trained jointly. The complete shape flow across the pipeline is:"))
A(TBL([["Stage","Output shape","Note"],
       ["Input (quant / text)","(B,60,24) / (B,60,13)","two separate tensors from the data loader"],
       ["Quant projection → dilated CNN","(B,60,128)","plus regime embedding; T preserved"],
       ["Cross-attention fusion","(B,60,128)","presence-gated residual"],
       ["Projection → causal Transformer","(B,60,256)","4 layers, 8 heads"],
       ["Bi-LSTM parallel Bi-GRU → gate","(B,60,256)","learned convex mixture"],
       ["Attention pooling","(B,256)","the only collapse of the time axis"],
       ["Context assembly","(B,352)","plus skip, XGBoost and GARCH embeddings"],
       ["Regime-aware heads","(B,10) mean and sigma","soft-gated dual heads"]],
      [2750,2050,3000]))
A(CAP("Table 8: End-to-end tensor shape flow. The time axis is collapsed exactly once, at the attention-pooling step."))
A(BODY("The 4,401,767 trainable parameters are not distributed evenly across those stages. Measuring each top-level module of the instantiated network gives the budget below, which makes explicit where the modelling capacity actually sits:"))
A(TBL([["Stage","Parameters","Share","Role"],
       ["Causal Transformer","3,159,040","71.8%","all relations longer than the 15-bar CNN span"],
       ["Bi-LSTM","395,264","9.0%","ordered state over the attended sequence"],
       ["Bi-GRU","296,448","6.7%","faster-adapting parallel recurrent branch"],
       ["Regime-aware heads","132,265","3.0%","dual decoders, mean and log-variance"],
       ["Context assembly","131,328","3.0%","352-dimensional context vector"],
       ["Dilated causal CNN","124,032","2.8%","local motifs within 15 bars"],
       ["Cross-attention fusion","66,048","1.5%","4 heads over the 128-d local space"],
       ["Projection to d_model","33,024","0.8%","128 to 256"],
       ["Auxiliary direction head","23,242","0.5%","diagnostic only"],
       ["Text tower (GRU + projection)","23,488","0.5%","13-d sentiment to 128-d sequence"],
       ["Expert embeddings and trust gates","5,668","0.1%","XGBoost and GARCH fusion"],
       ["All remaining gates and norms","11,920","0.3%","quant projection, regime embedding, pooling, presence gate"]],
      [2600,1500,900,2800]))
A(CAP("Table 9: Measured parameter budget by stage, read off the instantiated network and summing to 4,401,767."))
A(BODY("Two things follow from this table. First, the Transformer is the model: nearly three-quarters of the capacity is spent representing relations beyond one session, which is consistent with the design decision to keep the convolutional stage deliberately local. Second, the components that carry the distinctive behaviour of this architecture — the presence gate, the temporal gate, the trust gates and the pooling query — together account for well under one per cent of the parameters. They are cheap in capacity and expensive in effect, which is the intended trade: each is a small, interpretable control placed on a large, opaque representation."))
A(BODY("**Chronological splitting.** The data are split 70/15/15 in strict time order and never shuffled. For gold this yields 14,458 training origins after striding, 3,102 validation and 9,297 test. A random split would allow the model to interpolate between neighbouring bars and is invalid for time series; the test window is strictly the most recent period."))
A(BODY("**Two-stage training.** Stage 1 trains the quantitative tower with the text tower bypassed, over the full history. Stage 2 unfreezes the text tower, the fusion node and the decoder and fine-tunes at one-tenth of the learning rate on the news-dense later period. This prevents the sparse early-period sentiment stream from destabilising the quantitative backbone while still allowing the model to exploit news where it is dense."))
A(BODY("Training uses Adam (learning rate 1e-3, weight decay 1e-4), batch size 32, gradient clipping at 1.0, early stopping on validation loss, and a 25-epoch budget. Because consecutive hourly windows overlap by 59 of 60 bars, training origins are strided by three, cutting epoch cost roughly threefold with negligible information loss; the test set is never strided."))

A(H1("Design Overview"))
A(BODY("Architecturally the system is organised into five layers that map directly onto the methodology described in Section 3.1, and shown as a layered stack in Figure 11. The evaluation layer carries the base-rate controls, the multi-seed protocol, the significance tests and the conformal calibration that turn raw metrics into defensible claims, and the presentation layer serves a live forecast with a calibrated interval."))
A(IMG("fig_design_overview", 5.9))
A(CAP("Figure 11: Layered system design. The evaluation layer is where this project’s methodological contribution is concentrated."))
for t in ["**Data Layer** — MetaTrader 5 price acquisition (live and curated CSV), GDELT, Google News and RSS headline harvesting, Yahoo Finance and BLS macroeconomic series.",
          "**Processing Layer** — technical-indicator computation, FinBERT scoring with per-headline caching, stationary macro transforms, and the leak-free alignment controls of Section 3.1.1.",
          "**Modelling Layer** — the dual-tower hybrid architecture, the walk-forward XGBoost and GARCH experts, and the regime-aware Gaussian heads.",
          "**Evaluation Layer** — base-rate control, three-seed stability, block bootstrap, Diebold–Mariano tests, the Hansen Model Confidence Set, and conformal coverage measurement.",
          "**Presentation Layer** — a Streamlit dashboard exposing per-instrument results, a live forecast with an adaptive-conformal band, a data-lineage view showing raw bars becoming model tensors, and a per-stage timing breakdown."]:
    A(BUL(t))

A(H1("Tools and Platform"))
A(BODY("The implementation relies on an open-source, Python-centric deep learning stack chosen for reproducibility and for its support of the hybrid architecture described above."))
A(TBL([["Area","Tooling","Role"],
       ["Language and DL","Python 3.13, PyTorch","dual-tower hybrid: CNN, GRU, Transformer and LSTM modules"],
       ["Price data","MetaTrader 5 Python API","read-only live and historical H1 acquisition"],
       ["News","GDELT DOC 2.0, Google News RSS, financial RSS","historical depth plus fresh headline density"],
       ["Sentiment","Hugging Face Transformers, FinBERT","per-headline polarity and confidence, cached"],
       ["Macro","Yahoo Finance, US Bureau of Labor Statistics","rates, dollar index, CPI"],
       ["Classical experts","arch (GARCH), statsmodels (ARIMA)","walk-forward econometric baselines and the sigma baseline"],
       ["Tabular expert","XGBoost","walk-forward gradient-boosted expert"],
       ["Statistics","SciPy, arch.bootstrap (MCS)","block bootstrap, Diebold–Mariano, Model Confidence Set"],
       ["Presentation","Streamlit, Plotly","dashboard, live inference, lineage and timing views"],
       ["Compute","CPU (local) and CUDA (Colab T4)","device auto-detection in the training entry points"]],
      [1350,2150,4300]))
A(CAP("Table 10: Tools and platform by area of the system."))
A(BODY("Three tooling decisions are worth recording. **MetaTrader 5 supplies the price data** rather than a public web API, because those sources do not provide reliable long-history hourly bars for these instruments. **The arch package is a pinned, hard dependency**: during development its absence caused the GARCH expert to return zeros silently — an exception was being caught and converted into a zero forecast, so the model appeared to function while one of its three experts was inert. **A Temporal Fusion Transformer baseline was considered and not pursued**, the same compute being invested instead in statistical rigour — multi-seed runs and significance testing — for the two baselines that matter most here, ARIMA and GARCH."))

A(H1("Assumptions & Constraints"))
A(BODY("The findings and design choices presented in this report rest on the following explicit assumptions and operating constraints."))
A(SUB("Assumptions"))
for t in ["**Broker data is representative.** Prices come from a single retail broker’s feed; quotes may differ marginally from interbank mid prices, and the instrument trades on that broker’s session calendar.",
          "**Headline sentiment proxies market mood.** FinBERT polarity over headlines is treated as a usable proxy; it cannot capture unscheduled geopolitical shocks or the full content of long policy documents.",
          "**Publication timestamps are accurate**, since the leak-freedom of the news alignment depends on them.",
          "**Volatility regimes are adequately described** by realised volatility and ATR rather than by an externally validated regime classification."]:
    A(BUL(t))
A(SUB("Constraints"))
for t in ["**Order-book data is unavailable.** Spot FX and metals CFDs have no consolidated order book, and the broker exposes no depth for these symbols; the MetaTrader depth API is a live snapshot with no history, so no order-flow feature can be trained. CFTC Commitments-of-Traders positioning was evaluated as the only free historical proxy (Section 5.5).",
          "**News density is uneven over time.** Coverage is thin in 2016–17 and dense in recent years; modality masking and the explicit none state are the mitigations.",
          "**Compute is bounded.** Training is CPU-bound locally at roughly two hours per instrument per seed, with optional GPU on Colab, so the hyperparameter search is deliberate rather than exhaustive.",
          "**Overlapping windows reduce the effective sample.** Consecutive ten-bar-ahead forecasts share nine bars, so the effective number of independent observations is far below the nominal test count; all significance testing accounts for this through block resampling and HAC variance estimation.",
          "**Results are specific to H1 and to these three instruments** and should not be extrapolated to other bar sizes or asset classes without re-testing.",
          "**Regime labelling** uses rolling realised volatility and ATR thresholds rather than a ground-truth regime classification, which introduces a degree of labelling subjectivity."]:
    A(BUL(t))

# ============================================================ 4 EVALUATION
A(H0("Evaluation Methodology"))
A(BODY("Because the central results of this dissertation are partly negative, the protocol used to reach them carries at least as much weight as the architecture. A negative result is only credible if the measurement that produced it is above suspicion, so this section states the protocol in full — including the controls that turned two apparently positive findings into negative ones."))

A(H1("Chronological Splitting and Walk-Forward Protocol"))
A(BODY("The data are split 70/15/15 in strict time order and never shuffled. For gold this yields 14,458 training origins after striding, 3,102 validation origins and 9,297 test origins; silver contributes 9,339 and euro 9,828 held-out origins. The test window is always the most recent period, so the evaluation asks the question a practitioner would actually face: having fitted on the past, how does the system perform going forward?"))
A(BODY("A random split would be invalid here, and not marginally so. Consecutive hourly windows overlap by 59 of their 60 bars, so a shuffled split would place near-duplicate windows on both sides of the partition and let the model interpolate between neighbouring bars rather than extrapolate beyond them. The same overlap is why training origins are strided by three: it cuts epoch cost roughly threefold at negligible information loss. The test set is never strided, so no held-out origin is discarded for convenience."))
A(BODY("Three quantities are fitted, and each is confined to the split it belongs to. Normalisation statistics are computed on the training split alone and applied unchanged to validation and test. Model selection — early stopping — uses validation loss only. The test split is scored once per configuration and is never used to choose anything; where a configuration was revised, the revision was driven by validation evidence and the test set re-scored afterwards."))
A(BODY("The classical baselines are held to the same standard rather than being given a single in-sample fit. ARIMA, GARCH and XGBoost are re-fitted walk-forward, each block predicted by a model estimated only on data preceding it, and forward-filled between refits. This matters for the fairness of the comparison: a baseline fitted once on the whole series would be handed information the hybrid never sees, and any conclusion drawn against it would be worthless."))
A(IMG("fig_eval_split", 6.1))
A(CAP("Figure 12: Chronological splitting and the walk-forward protocol. Normalisation, model selection and scoring are each confined to one split, and every classical baseline is re-estimated on history alone before predicting the next block."))

A(H1("The Base-Rate Control"))
A(BODY("Directional accuracy is meaningless without the unconditional base rate of the test window. If an instrument rises in 53.4% of test bars, an unconditional “always long” rule scores 0.534 while containing no skill whatsoever. Every directional figure in this report is therefore reported against that base rate, and the quantity of interest is the **edge** — accuracy minus base rate — never the raw accuracy."))
A(BODY("The subtler half of the control is that the base rate must be recomputed on **whatever set of bars the claim is actually made on**. A selective strategy that trades only a filtered subset has changed its own benchmark: the correct comparison is the best fixed rule on that same subset, not the global base rate. Filters that select for trend quality select, almost by construction, for bars on which the prevailing direction persisted — which raises the subset base rate at the same time as it raises the strategy's accuracy."))
A(BODY("This is not a hypothetical concern; it reversed a headline result in this project. The Trend-Gated Committee trades only when the deep ensemble and the GARCH expert agree and a trend-quality gate is open. On gold it reaches 0.5637 directional accuracy on the 1,985 origins it selects — 21.4% coverage — which read as a clear success against the global 0.5344 base rate. Recomputing the base rate on those 1,985 bars gives 0.5697, so the true edge is **−0.59 pp**. The entire apparent gain was the drift of the selected subset. The equivalent figures are −1.74 pp for silver and −6.05 pp for euro."))
A(IMG("fig_base_rate", 6.0))
A(CAP("Figure 13: The base-rate control. The edge is computed against the best fixed rule on the same bars the claim is made on; the worked example shows a selective strategy whose apparent gain disappears once its own subset base rate is computed."))

A(H1("Multi-Seed Stability"))
A(BODY("Every headline result is run with three random seeds (9, 36 and 99) and reported as a mean plus or minus a standard deviation. The purpose is to separate a genuine effect from initialisation noise, and it is applied symmetrically: a positive result that survives only on one seed is not reported as a result, and a negative result is only stated once it has failed on all three."))
A(BODY("The observed dispersion is small enough to make the directional conclusion structural rather than incidental — the standard deviation of directional accuracy is 0.0005 for gold, 0.0018 for silver and 0.0015 for euro, one to two orders of magnitude smaller than the gap to the base rate. On the magnitude axis the evaluation harness additionally records how many seeds beat each baseline on **both** metrics, and reports a configuration as ROBUST only at three out of three. Anything less is reported as mixed."))

A(H1("Significance Testing"))
A(BODY("Point estimates are not proof, and a difference of two hundredths of a Spearman coefficient on autocorrelated data is exactly the kind of number that can arise by chance. Three complementary tests are applied to the frozen forecasts, each reproduction-guarded: the test script recomputes the point estimate from the stored arrays and aborts if it disagrees with the committed value, so a significance result can never be reported against forecasts that have since changed."))
for t in ["**Block bootstrap** — 2,000 resamples with block length 50, applied to the difference in the reported metrics. Blocks rather than individual observations are resampled because overlapping windows induce strong autocorrelation; resampling points independently would understate the variance and manufacture significance.",
          "**Diebold–Mariano** — a test on the squared-error loss differential with Newey–West HAC variance at lag 10, matching the forecast horizon so that the overlap-induced serial correlation is absorbed into the variance estimate.",
          "**Hansen Model Confidence Set** — at the 90% level, returning the set of forecasters that cannot be statistically separated from the best. Unlike the pairwise tests it controls for multiple comparisons across all three forecasters simultaneously."]:
    A(BUL(t))
A(BODY("These tests are deliberately not interchangeable, and the distinction turns out to matter for the results in Section 5.3. The bootstrap is applied to the rank and classification metrics that the work actually reports — how well the model **orders** future move sizes. Diebold–Mariano and the Model Confidence Set operate on squared-error loss, which is dominated by a handful of extreme moves and is sensitive to the absolute scale of the forecast. A model can order magnitude substantially better without reducing squared error, so the two families can disagree without either being wrong."))
A(IMG("fig_significance", 6.1))
A(CAP("Figure 14: The significance battery. The three tests consume the same frozen forecasts but score different losses, which is why the bootstrap and the squared-error tests can reach different conclusions on the same instrument."))

A(H1("Metrics and What Each One Answers"))
A(BODY("Each metric in this report answers one specific question, and is paired with the control that makes it interpretable. Stating them together prevents the common failure of quoting a number whose benchmark is unstated."))
A(TBL([["Metric","Question it answers","Control applied"],
       ["Directional accuracy","Does the sign of the next move get predicted?","Always-up base rate on the same bars"],
       ["Spearman rank skill","Are future move sizes ordered correctly?","Compared against ATR% and GARCH-σ on identical origins"],
       ["Large-move accuracy","Are the big moves flagged?","Adaptive rolling-median threshold, so the base rate is near 0.50 by construction"],
       ["Empirical coverage","Does a nominal 90% band contain the outcome 90% of the time?","Measured on test after calibrating on validation"],
       ["Interval width","What does that coverage cost?","Reported alongside coverage, since coverage alone can be bought with infinite bands"]],
      [1600,3400,3200]))
A(CAP("Table 11: Metrics, the question each answers, and the control that makes it meaningful."))
A(BODY("Two choices deserve justification. Spearman rank correlation is preferred to a scale-dependent error measure for magnitude because the practical use of a volatility forecast — position sizing, risk limits, option pricing — depends on ordering periods by expected movement rather than on the absolute calibration of the number. And interval width is reported next to coverage throughout, because coverage on its own is trivially gameable: an infinitely wide band achieves 100% coverage and is useless."))

A(H1("Interval Calibration Protocol"))
A(BODY("The Gaussian negative log-likelihood objective gives the model a sigma output, but nothing in the training procedure guarantees that a nominal 90% band contains the outcome 90% of the time. Calibration is therefore measured rather than assumed, using the validation split to calibrate and the test split to evaluate, separately for each of the ten horizons."))
A(BODY("**Split conformal** takes the normalised residuals |y − μ|/σ on the 3,102 calibration origins, reads off the empirical quantile at the desired level, and scales every future interval by it. Its guarantee is finite-sample and distribution-free, but it holds only while test residuals are exchangeable with calibration residuals — an assumption a volatility regime shift breaks outright, which is precisely what the 2024–2026 test window contains."))
A(BODY("**Adaptive conformal inference** drops the exchangeability assumption by making the working level a controlled variable. The interval is issued at a level α_t, the outcome is observed, and the level is updated by α_(t+1) = α_t + γ(α − err_t), where err_t indicates whether the outcome fell outside. A run of misses lowers the working level and widens subsequent intervals until empirical coverage recovers; a run of easy periods narrows them again. The guarantee changes character — long-run average coverage instead of finite-sample coverage — but it survives the regime shift that defeats the split method."))
A(IMG("fig_conformal_protocol", 6.0))
A(CAP("Figure 15: The two calibration procedures. Split conformal computes one fixed quantile from the calibration split; adaptive conformal inference closes a feedback loop around the miscoverage level so that coverage is controlled online."))

A(H1("Leakage Controls and Reproducibility"))
A(BODY("Leakage at bar granularity is easy to introduce and hard to detect after the fact, because it produces results that look good rather than results that look wrong. Each control below is enforced structurally, at the point where the data are assembled, rather than checked afterwards."))
A(TBL([["Risk","Control","Where enforced"],
       ["Macro release known before publication","Every macro series shifted +1 day before it can touch a bar","Feature assembly"],
       ["News known before it was published","Headlines aligned on publication timestamp only","Sentiment alignment"],
       ["Test statistics leaking into scaling","Normalisation fitted on the training split alone","Data loader"],
       ["A position seeing its own future","Left-only padding in the CNN; causal mask in the Transformer","Model definition"],
       ["Baselines given a full-sample fit","ARIMA, GARCH and XGBoost re-fitted walk-forward","Baseline harness"],
       ["Near-duplicate windows across the split","Chronological split, never shuffled","Split construction"],
       ["Test set used for tuning","Model selected on validation loss; test scored once","Training loop"]],
      [2300,3200,2700]))
A(CAP("Table 12: Leakage controls and the stage at which each is applied."))
A(BODY("Reproducibility is handled by freezing forecasts to disk. Every significance test, conformal calibration and cross-instrument comparison in Section 5 reads the same stored prediction arrays rather than re-running the model, so the numbers in this report are all traceable to a specific committed artefact and can be recomputed without a GPU."))

# ============================================================ 5 RESULTS
A(H0("Results & Discussions"))
A(BODY("Results are reported for all three instruments on frozen, chronologically held-out test sets: 9,297 forecast origins for gold, 9,339 for silver and 9,828 for euro, each covering the most recent 15% of the 2016–2026 history."))

A(H1("Directional Accuracy: An Honest Negative Result"))
A(BODY("Table 13 and Figure 16 report directional accuracy for the three-seed hybrid against the classical baselines and, critically, against the always-up base rate."))
A(TBL([["Instrument","Hybrid (3-seed)","GARCH","ARIMA","Base rate","Hybrid edge"],
       ["Gold XAU/USD","0.5178 ± 0.0005","0.5378","0.5063","0.5344","−1.7 pp"],
       ["Silver XAG/USD","0.5145 ± 0.0018","0.5237","0.4925","0.5354","−2.1 pp"],
       ["Euro EUR/USD","0.4984 ± 0.0015","0.5044","0.4875","0.5037","−0.5 pp"]],
      [1700,1600,1050,1050,1050,1350]))
A(CAP("Table 13: Directional accuracy at H1. No model exceeds the always-up base rate on any instrument."))
A(IMG("fig_directional", 5.6))
A(CAP("Figure 16: Directional accuracy against the base rate (amber). The gap between the bars and the amber line is the honest measure of skill, and it is negative everywhere."))
A(BODY("**The finding is unambiguous: hourly direction is not predictable by this system, and not by the classical baselines either.** The hybrid sits between 0.5 and 2.1 percentage points below the base rate on all three instruments. GARCH’s apparent lead is its momentum drift — it leans with the prevailing trend — and it too fails to clear the base rate. Results are extremely stable across seeds (standard deviation at most 0.002), so this is a property of the problem rather than of initialisation."))
A(BODY("The GARCH result deserves a moment, because at first glance it looks like the econometric model beats the deep one on direction — 0.5378 against 0.5178 on gold. It does, and the comparison is still uninformative. An AR(1)-GARCH conditional mean is close to a momentum rule: it leans in whichever direction the recent drift points. On a test window containing a strong bull market that behaviour reproduces the base rate almost by construction, which is exactly what the numbers show — GARCH's 0.5378 sits within half a percentage point of gold's 0.5344 base rate. What looks like an econometric model outperforming a neural one is two models converging on the same trivial strategy, one of them slightly less completely than the other."))
A(BODY("The stability across seeds is what makes this a statement about the problem rather than about one training run. A standard deviation of 0.0005 on gold means the three seeds landed within about a tenth of a percentage point of one another, while the gap to the base rate is seventeen times that. No plausible re-initialisation closes it."))
A(BODY("This conclusion was not reached from a single experiment. Approximately fifteen alternative framings were tested and all landed at the base rate: smoothed and de-noised targets, longer horizons, validation-calibrated decision thresholds, selective trading under a trend gate, session and volatility filters, ADX and candle-shape conditioning, Fair-Value-Gap microstructure features, and CFTC positioning. A representative case is the Trend-Gated Committee, which trades only when the deep ensemble and the GARCH expert agree and a trend-quality gate is open. On gold it reaches 0.5637 at 21.4% coverage — which looks impressive until the subset base rate is computed: the best fixed rule on those same gated bars scores 0.5697, so the true edge is −0.59 pp. The apparent gain was entirely the base rate of the selected subset. The equivalent figures are −1.74 pp for silver and −6.05 pp for euro."))
A(BODY("The pattern across those fifteen framings is consistent enough to be worth naming. Every one of them that appeared to work did so by one of two mechanisms: it selected a subset of bars whose own base rate was higher (the trend gate, the session and volatility filters, the ADX conditioning), or it changed the target into something smoother and easier to predict but no longer the quantity of interest (the de-noised and smoothed targets). Neither mechanism produces tradeable directional skill, and both are invisible unless the benchmark is recomputed on the transformed problem. This is why Section 4.2 defines the base rate on the set of bars the claim is made on rather than on the test set as a whole."))
A(BODY("This is consistent with market efficiency at hourly resolution and is reported as a substantive result rather than as a failed experiment. It also explains why several published directional accuracies should be read with care: without the base-rate control, drift is easily mistaken for skill."))

A(H1("Move-Magnitude Forecasting: Where the Hybrid Beats ATR% and GARCH"))
A(BODY("Direction and magnitude are different questions. A model may be unable to say whether price will rise, yet still say usefully how far it will move — which is precisely what risk management, position sizing and option pricing require. The magnitude target is the absolute cumulative ten-bar return, and the model is trained on it directly with the directional loss disabled."))
A(BODY("The comparison is against the two natural volatility benchmarks: **ATR%**, the standard technical volatility indicator, and **GARCH-sigma**, the conditional standard deviation from the same AR(1)-GARCH(1,1) fit used elsewhere in this report — the canonical econometric volatility forecast. Table 14 reports three-seed means."))
A(TBL([["Instrument","Metric","Hybrid","ATR%","GARCH-σ","Base rate","Edge vs ATR%","Edge vs GARCH-σ"],
       ["Gold","Spearman","0.3288","0.3086","0.3043","—","+0.0202","+0.0245"],
       ["Gold","Large-move acc.","0.5517","0.5406","0.5447","0.5046","+1.11 pp","+0.70 pp"],
       ["Silver","Spearman","0.4178","0.3771","0.3463","—","+0.0407","+0.0716"],
       ["Silver","Large-move acc.","0.5520","0.5183","0.5057","0.5119","+3.37 pp","+4.63 pp"],
       ["Euro","Spearman","0.2316","0.0894","0.1453","—","+0.1422","+0.0863"],
       ["Euro","Large-move acc.","0.5709","0.4886","0.4938","0.4969","+8.23 pp","+7.72 pp"]],
      [880,1420,880,830,930,900,1060,900]))
A(CAP("Table 14: Move-magnitude forecasting, three-seed means. The hybrid beats both volatility baselines on both metrics for all three instruments, on every seed. The base-rate column applies to the classification rows only: the threshold is an adaptive rolling median, so the base rate sits near 0.50 by construction and the hybrid clears it on all three instruments."))
A(IMG("fig_magnitude", 6.1))
A(CAP("Figure 17: Magnitude rank skill (left) and large-move classification accuracy (right). Amber lines mark the adaptive base rate."))
A(BODY("**The hybrid beats both ATR% and GARCH-sigma on both metrics, for all three instruments, on all three seeds** — a 3 of 3 outcome the evaluation harness labels ROBUST. The reason the same model can lose on direction and win on magnitude is structural: volatility is autocorrelated and clusters in time, so it carries genuine predictable structure, whereas the sign of the next return is close to a martingale. The architecture is well matched to that structure — the dilated CNN captures volatility bursts across a fifteen-bar receptive field, the regime embedding and gated heads condition explicitly on volatility state, and the Gaussian NLL objective trains sigma as a first-class output rather than as an afterthought."))
A(BODY("It is worth stating plainly what this does and does not mean. It does **not** mean the system predicts returns. It means that on the axis where predictable structure exists, the deep model extracts more of it than the classical volatility models — including GARCH, which is purpose-built for exactly this task and which beats the hybrid on direction."))
A(BODY("The asymmetry between the two axes is the central empirical result of this dissertation, and the two halves support each other rather than contradicting each other. The same architecture, the same features, the same test bars and the same evaluation protocol produce a negative result on direction and a positive one on magnitude. That rules out the most common explanations for a negative finding — a broken pipeline, an inadequate model, a leak-free but badly constructed test set — because any of those would have suppressed both results. What remains is the explanation the efficiency literature predicts: the sign of the next return carries almost no exploitable structure at hourly resolution, while its size carries a good deal."))

A(H1("Statistical Significance of the Magnitude Edge"))
A(BODY("Point estimates are not proof. The three tests of Section 4.4 were applied to each instrument, and it is worth being explicit about what they were applied to: the **frozen seed-9 forecast arrays**, not the three-seed means of Table 14. The two differ slightly — the seed-9 edge over ATR% on silver is +0.0387 against the three-seed mean of +0.0407 — because a significance test must run on one realised set of forecasts rather than on an average of three. The direction and magnitude of every conclusion is unaffected, but the numbers in Table 15 will not match Table 14 to the last digit, and that is expected rather than an inconsistency."))
A(TBL([["Instrument","Comparison","Metric","Edge","95% bootstrap CI","p"],
       ["Gold","vs ATR%","Spearman","+0.0204","[−0.0116, +0.0512]","0.0955"],
       ["Gold","vs GARCH-σ","Spearman","+0.0249","[−0.0065, +0.0571]","0.0555"],
       ["Gold","vs ATR%","Large-move acc.","+0.0112","[−0.0120, +0.0336]","0.1695"],
       ["Gold","vs GARCH-σ","Large-move acc.","+0.0070","[−0.0150, +0.0291]","0.2710"],
       ["Silver","vs ATR%","Spearman","+0.0387","[+0.0076, +0.0696]","0.0055"],
       ["Silver","vs GARCH-σ","Spearman","+0.0687","[+0.0379, +0.1012]","< 0.0001"],
       ["Silver","vs ATR%","Large-move acc.","+0.0345","[+0.0106, +0.0592]","0.0020"],
       ["Silver","vs GARCH-σ","Large-move acc.","+0.0469","[+0.0235, +0.0695]","< 0.0001"],
       ["Euro","vs ATR%","Spearman","+0.1503","[+0.0880, +0.2141]","< 0.0001"],
       ["Euro","vs GARCH-σ","Spearman","+0.0954","[+0.0440, +0.1458]","< 0.0001"],
       ["Euro","vs ATR%","Large-move acc.","+0.0860","[+0.0572, +0.1142]","< 0.0001"],
       ["Euro","vs GARCH-σ","Large-move acc.","+0.0809","[+0.0554, +0.1073]","< 0.0001"]],
      [1000,1250,1500,900,1800,900]))
A(CAP("Table 15: Block bootstrap on the frozen seed-9 forecasts — 2,000 resamples, block length 50. All four of gold's confidence intervals contain zero; none of silver's or euro's do."))
A(BODY("The bootstrap result is clean and reads directly off the intervals. **For gold, every one of the four confidence intervals contains zero.** The edge of +0.020 Spearman over ATR% has an interval running from −0.012 to +0.051, so an edge of exactly zero — or a small negative one — is entirely consistent with the data. The honest conclusion is that on gold the hybrid **matches** the classical volatility baselines rather than beating them, and the word “beats” is not available."))
A(BODY("**For silver and euro, none of the eight intervals contains zero.** Silver's weakest comparison is its Spearman edge over ATR% at p = 0.0055, with the interval running from +0.0076 to +0.0696; every other silver and euro comparison is significant at p < 0.0001 with comfortable margins. On the metrics the work actually reports, the improvement on these two instruments is not attributable to sampling variation."))
A(BODY("The squared-error tests tell a different story, and it is the same story on all three instruments. Table 16 gives the outcome."))
A(TBL([["Instrument","DM vs ATR% (stat, p)","DM vs GARCH-σ (stat, p)","MCS 90%: forecasters retained"],
       ["Gold","+1.11, p = 0.268","+1.13, p = 0.257","all three (Hybrid 0.577, GARCH-σ 0.577, ATR% 1.000)"],
       ["Silver","+0.76, p = 0.446","+1.24, p = 0.216","all three (Hybrid 0.512, GARCH-σ 0.719, ATR% 1.000)"],
       ["Euro","+1.15, p = 0.251","+1.14, p = 0.256","all three (Hybrid 0.634, GARCH-σ 0.642, ATR% 1.000)"]],
      [1100,1900,1900,3000]))
A(CAP("Table 16: Diebold–Mariano and Hansen Model Confidence Set on squared-error loss. Every Diebold–Mariano statistic is positive — the hybrid has the lower loss — but none reaches significance, and the Model Confidence Set separates nothing on any instrument."))
A(BODY("Two details in Table 16 are worth reading carefully. First, **every Diebold–Mariano statistic is positive**, meaning the hybrid does have the lower squared-error loss in each of the six comparisons; the tests fail on significance, not on sign. Second, the Model Confidence Set retains all three forecasters everywhere, and ATR% carries a p-value of exactly 1.000 in every case — it is never the eliminated model, because in squared-error terms the three are simply too close to separate at 9,000-odd observations with this much serial correlation."))
A(BODY("**This disagreement is itself a finding, and reporting only one side of it would be cherry-picking.** The two families of test measure different things, as set out in Section 4.4. The bootstrap evaluates the rank and classification metrics actually used — how well the model orders future move sizes and flags large moves. Squared error is dominated by a handful of extreme moves and is sensitive to the scale calibration of the forecast; the fitted scale factors differ substantially across the three forecasters (0.94 for the hybrid, 1.56 for ATR%, 0.66 for GARCH-σ on gold), which is exactly the kind of difference that rank metrics ignore and squared error does not. A model can order magnitude substantially better while not reducing squared error, and that is what is observed."))
A(BODY("The defensible claim is therefore stated with its scope attached: **on silver and euro the hybrid orders and classifies future move magnitude significantly better than ATR% and GARCH-σ, but is not demonstrably better in squared-error terms; on gold it is statistically indistinguishable from both.** A reader interested in ranking periods by expected movement should weight the first clause; a reader interested in minimising squared forecast error should weight the second."))
A(BODY("A further caveat applies to euro. Its edge is the largest of the three at +0.150 Spearman over ATR% on seed 9, but this partly reflects weak baselines rather than strong absolute performance: ATR% scores only 0.089 rank skill and 0.489 large-move accuracy on euro — below its own 0.497 base rate — so the classical indicator is close to useless there, while the hybrid's absolute skill on euro (0.232) is the lowest of the three instruments. A large edge over a broken baseline is a weaker claim than a modest edge over a good one. **Silver is the strongest genuine result**: the highest absolute skill (0.418) together with a significant edge over baselines that are themselves competent."))

A(H1("Calibrated Uncertainty through Adaptive Conformal Inference"))
A(BODY("The Gaussian NLL objective gives the model a sigma output, but nothing guarantees that a nominal 90% band actually contains the outcome 90% of the time. This was measured on gold by calibrating on the validation split and evaluating coverage on the test split, per horizon."))
A(TBL([["Nominal","Gaussian coverage","Split conformal","ACI coverage","Gaussian width","Split width","ACI median width","ACI infinite"],
       ["80%","63.3%","61.9%","79.9%","0.913%","0.914%","1.204%","2.2%"],
       ["90%","72.9%","75.8%","90.0%","1.172%","1.304%","1.558%","5.2%"],
       ["95%","79.0%","84.5%","95.0%","1.397%","1.697%","1.865%","10.8%"]],
      [740,1250,1120,980,1160,880,1200,870]))
A(CAP("Table 17: Interval calibration on gold — 3,102 calibration origins, 9,297 test origins. Widths are half-widths of the ten-bar log-return interval, expressed in per cent; the final column is the fraction of origins at which the adaptive controller widened to an unbounded interval."))
A(IMG("fig_conformal", 5.4))
A(CAP("Figure 18: Interval calibration. The Gaussian band under-covers badly; split conformal helps but is defeated by regime shift; ACI restores nominal coverage."))
A(BODY("Three findings follow. First, **the raw Gaussian band is badly mis-calibrated** — a nominal 90% interval contains the outcome only 72.9% of the time, because FX returns are fat-tailed relative to the Gaussian assumption. Second, **split conformal is not sufficient**: it improves the 90% and 95% levels but still under-covers, because the test period, a strong 2024–2026 gold rally, is materially more volatile than the calibration window, violating the exchangeability that split conformal requires. Third, **Adaptive Conformal Inference restores coverage almost exactly** at 79.9, 90.0 and 95.0 per cent, by updating the working miscoverage level online so that a run of misses widens subsequent intervals until coverage recovers."))
A(BODY("**The cost is visible in the same table, which is why width is reported next to coverage.** At the 90% level the ACI half-width is 1.558% against the Gaussian 1.172% — 33% wider — and the infinite fraction rises from 2.2% at the 80% level to 10.8% at the 95% level. Those unbounded intervals are not a defect but a refusal: the controller is declining to issue a finite band when recent coverage has collapsed, and the frequency with which it does so is itself a usable regime-stress flag. This layer is deployed in the live dashboard, where the forecast is shown with a 90% conformal band alongside the raw sigma band for contrast. **This is the component of the work least affected by market efficiency**: it does not attempt to predict returns, but to state honestly how uncertain a forecast is — a guarantee that GARCH’s parametric bands do not provide."))

A(H1("Feature and Architecture Studies, Including Negative Results"))
A(BODY("Several candidate improvements were pre-checked on training and validation data only, before any wiring, and are reported here regardless of outcome."))
A(TBL([["Study","Question","Outcome"],
       ["Modality ablation","Do news and macro add magnitude skill over price features?","No. Price-only is equivalent to all-features (0.321 vs 0.329 Spearman); both channels contribute approximately zero."],
       ["HAR-RV features","Do multi-timescale realised-volatility features help?","Pre-check strong (partial rho +0.11 to +0.17) but the retrained model did not improve (0.326 vs 0.329)."],
       ["CFTC COT positioning","Does institutional positioning predict returns or magnitude?","Direction dead (|rho| at most 0.014); magnitude signal largely redundant with ATR%."],
       ["Fair Value Gap","Do ICT-style three-candle imbalances predict direction?","Noise (|rho| at most 0.018); post-gap probability of an up move is below the base rate."],
       ["Quantile heads","Would pinball-loss heads improve calibration over sigma plus conformal?","No — conditional quantiles added only 0.8 pp of coverage; ACI already handles the dominant regime shift."],
       ["Order book / DOM","Can depth-of-market be used?","Unavailable: no consolidated book exists for spot metals and FX; MetaTrader depth is live-only with no history."]],
      [1400,2900,3500]))
A(CAP("Table 18: Candidate enhancements and their measured outcomes."))
A(BODY("Two lessons emerge. First, **a strong pre-check correlation does not guarantee model improvement**: HAR-RV features correlated well with the target after controlling for ATR%, yet added nothing once inside the network, because the dilated CNN already extracts multi-timescale volatility structure from raw returns. Second, **the multi-modal thesis is not supported on the magnitude axis**: the news and macro streams, despite covering 98 to 99.9 per cent of test bars, add approximately zero magnitude skill over price and volatility features. Their contribution, where it exists, is to robustness and to the directional diagnostics rather than to magnitude accuracy — an honest qualification of the fusion design."))
A(BODY("The modality ablation is the most uncomfortable result in this report, because it qualifies the premise of the architecture, and it is stated here rather than buried. A price-only model reaches 0.321 Spearman against 0.329 for the full multi-modal model — a difference well inside the bootstrap intervals of Section 5.3. The fusion machinery of Section 3.1.3, the sentiment tower, the FinBERT scoring pipeline and the macro alignment together buy approximately nothing on the magnitude axis."))
A(BODY("Three things are nonetheless worth saying about that. The fusion design is what makes the ablation *measurable*: because the presence gate and modality masking let the text stream be switched off cleanly, the price-only comparison runs on the same checkpoint architecture rather than on a different model, so the comparison is clean. The negative result is specific to the magnitude axis at H1 on these three instruments, and does not generalise to lower frequencies where macro releases move price over days rather than hours. And the honest reading of a null result is that the channel was not shown to help here — not that sentiment is uninformative in general, which this experiment cannot establish."))

A(H1("Instrument-Specific Results"))
A(SUB("Gold (XAU/USD)"))
A(BODY("Gold is the deepest dataset: 62,049 hourly bars from January 2016 to July 2026, with 22,833 scored headlines and 99.9% test-bar news coverage — the densest sentiment stream of the three. Directional accuracy is 0.5178 ± 0.0005 against a 0.5344 base rate, an edge of −1.7 pp. Magnitude skill is 0.3288 Spearman against ATR% at 0.3086 and GARCH-sigma at 0.3043; the edge is robust across seeds but not statistically significant. Gold’s test window coincides with a strong bull market, which raises its base rate to 0.534 and makes the directional illusion especially easy to fall into: an earlier daily-resolution run of this project recorded 0.548 directional accuracy and was initially read as a success, until the base rate for that window was computed at 0.564 — the model was in fact below an always-long rule."))
A(SUB("Silver (XAG/USD)"))
A(BODY("Silver has 62,328 bars, 11,413 scored headlines and 99.5% coverage. Directional accuracy is 0.5145 ± 0.0018 against a 0.5354 base rate, an edge of −2.1 pp and the weakest directional result of the three. **Magnitude is its strongest dimension and the strongest result in the project**: 0.4178 Spearman, the highest absolute magnitude skill of any instrument, against ATR% at 0.3771 and GARCH-sigma at 0.3463, and 0.5520 large-move accuracy against a 0.5119 base rate, with every bootstrap comparison significant (p ≤ 0.0055) and all confidence intervals excluding zero. Silver’s well-documented volatility clustering, more pronounced than gold’s, appears to give the model more structure to exploit while leaving direction no more predictable."))
A(SUB("Euro (EUR/USD)"))
A(BODY("Euro has the most bars (65,587), the smallest news archive (10,605 headlines, 98.0% coverage) and the lowest volatility of the three. It is the closest to a pure random walk directionally: 0.4984 ± 0.0015 against a 0.5037 base rate, both statistically indistinguishable from a coin flip, consistent with EUR/USD being the most liquid and most efficient currency pair in the world. Its magnitude edge is nominally the largest at +0.142 Spearman over ATR% with p < 0.0001, but as noted this is driven by unusually weak baselines: ATR% achieves only 0.089 rank skill on euro. The euro’s volatility is evidently structured in a way that a simple range-based indicator captures poorly but the deep model captures moderately well."))

A(H1("Cross-Instrument Comparison"))
A(IMG("fig_cross_currency", 5.8))
A(CAP("Figure 19: Magnitude edge over the classical volatility baselines by instrument, with bootstrap significance."))
A(TBL([["Dimension","Gold","Silver","Euro"],
       ["Hourly bars","62,049","62,328","65,587"],
       ["Scored headlines","22,833","11,413","10,605"],
       ["Test-bar news coverage","99.9%","99.5%","98.0%"],
       ["Directional accuracy (3-seed)","0.5178","0.5145","0.4984"],
       ["Directional edge vs base rate","−1.7 pp","−2.1 pp","−0.5 pp"],
       ["Magnitude Spearman (absolute)","0.3288","0.4178","0.2316"],
       ["ATR% baseline skill","0.3086","0.3771","0.0894"],
       ["GARCH-σ baseline skill","0.3043","0.3463","0.1453"],
       ["Magnitude edge vs ATR%","+0.0202","+0.0407","+0.1422"],
       ["Bootstrap significance","not significant","significant","significant"],
       ["Selective (TGC) edge vs subset base","−0.59 pp","−1.74 pp","−6.05 pp"]],
      [2900,1750,1750,1600]))
A(CAP("Table 19: Cross-instrument comparison across data, sentiment, direction and volatility dimensions."))
A(SUB("Sentiment"))
A(BODY("News density varies more than twofold across the instruments, from 22,833 headlines for gold to 10,605 for euro, yet directional and magnitude performance do not track it: euro, with the sparsest news, shows the largest nominal magnitude edge, and gold, with the densest, shows the smallest. Taken together with the modality ablation, the evidence indicates that at hourly resolution headline sentiment is not the operative driver of either axis for these instruments — a direct, and negative, test of the dissertation’s original multi-modal hypothesis."))
A(SUB("Macroeconomic sensitivity"))
A(BODY("The macro stream is shared in structure across instruments (US rates, dollar index, CPI) but differs in relevance: EUR/USD is a direct expression of the US–euro-area rate differential, whereas the metals respond to real yields and the dollar with a longer and less mechanical lag. The ablation nonetheless found macro adding approximately zero to magnitude skill for all three, suggesting that the price series already embeds macro information by the time it reaches an hourly bar."))
A(SUB("Volatility structure — the discriminating dimension"))
A(BODY("The clearest cross-instrument pattern is in how well classical volatility models work. ATR% achieves 0.377 rank skill on silver and 0.309 on gold, but only 0.089 on euro. Volatility predictability is therefore not a uniform property of financial series: the metals exhibit the pronounced, range-expressible volatility clustering that ATR% and GARCH were designed for, while euro volatility is structured in a way those models largely miss. The deep model narrows that gap on all three instruments, and the relative improvement is greatest precisely where the classical models are weakest. This is arguably the most transferable finding of the cross-instrument study: **the value added by a deep volatility model is inversely related to how well classical indicators already work on that instrument.**"))
A(SUB("Direction"))
A(BODY("Directionally the three instruments are alike: all sit at or below their base rate, with euro closest to a coin flip in absolute terms and silver furthest below its base rate. The consistency of this result across three instruments with different liquidity, volatility and news profiles is what makes the efficiency conclusion credible rather than an artefact of a single series."))
A(BODY("On magnitude the three separate, and they separate along an interpretable axis. Silver has the highest absolute skill (0.418) and the most pronounced volatility clustering; gold has intermediate skill (0.329) and the densest news coverage but the weakest and least significant edge; euro has the lowest absolute skill (0.232) and the largest nominal edge, because its classical baselines are the weakest. Absolute skill therefore tracks how much volatility structure the instrument has, while the *edge* tracks how badly the classical baselines handle that structure — and the two are not the same ranking. Reporting only the edge would have made euro the headline result; reporting only absolute skill would have hidden that ATR% is essentially broken on euro. Both are given here for that reason."))
A(BODY("Sentiment density does not explain any of it. Gold has twice silver's headline count (22,833 against 11,413) and the highest test-bar coverage at 99.9%, yet the weakest magnitude edge and the only non-significant one; euro has the smallest archive and the largest nominal edge. The ordering of magnitude performance follows volatility structure, not news volume — which is consistent with the modality ablation of Section 5.5 and is the second independent line of evidence pointing the same way."))

# ============================================================ 6 FUTURE
A(H0("Future Plan"))
A(BODY("The modelling programme is complete in the sense that every remaining lever identified during the project was tested and measured, as recorded in Table 18. That changes the character of the future plan: it is not a list of ideas that were never tried, but a ranking of the directions that the measured results actually justify. The ordering principle is deliberate — effort goes where the evidence says value exists, not where the original hypothesis expected it."))

A(H1("Where the Evidence Says Effort Should Go"))
A(BODY("Three results constrain the forward programme. Direction was shown not to be forecastable at hourly resolution across three instruments, three seeds and roughly fifteen framings, so further directional modelling is the least defensible use of effort available; it would be optimising against a target that this work has evidence is close to unforecastable. Magnitude was shown to carry structure the model extracts better than the classical baselines, so the axis is live. And interval calibration was the most robust contribution of all, being the one component untouched by the efficiency constraint — it does not attempt to predict returns, only to state honestly how uncertain a forecast is."))
A(BODY("A fourth constraint comes from the negative results rather than the positive ones. The modality ablation of Section 5.5 showed that the news and macro channels add approximately zero magnitude skill at H1. The productive response to that is not to add more text capacity in the hope that a larger model will find something, but to test the specific alternative explanations for why the channel was silent — which is what the exploratory lane below is built around."))
A(IMG("fig_roadmap", 6.1))
A(CAP("Figure 20: The forward programme in three lanes. Lane 1 follows from measured results, lane 2 tests specific alternative explanations for the null findings, and lane 3 records what cannot be started without data access that is not currently available."))

A(H1("Immediate Extensions"))
A(BODY("These follow directly from results already in hand and require no new data or architecture."))
for t in ["**Extend adaptive conformal inference to silver and euro.** The ACI layer is currently fitted for gold alone. Because calibrated uncertainty is the most robust finding in this report, completing it across all three instruments is the highest-value remaining work, and it is inexpensive: the layer operates on frozen forecasts, so no retraining is involved.",
          "**Build a volatility-targeted decision layer.** Since magnitude rather than direction is the predictable axis, the natural application is position sizing and risk budgeting rather than directional trading. The conformal interval width is already a per-origin, calibrated uncertainty estimate, and can drive exposure directly — a decision rule that consumes exactly the output this system was shown to produce well.",
          "**Instrument the gates for explainability.** The cross-attention weights between the price and news towers, the temporal gate λ and the two expert trust gates are all directly interpretable and already computed at inference; exposing them is instrumentation rather than modelling. The trust gates are the most informative, since they reveal when the network defers to GARCH rather than to its own deep branch. SHAP attribution over the 37 features would complement this.",
          "**Compare interval behaviour across instruments.** Once the conformal layer is fitted for all three pairs, the widths and the infinite-interval fractions become comparable, giving a cross-instrument measure of regime stress that this report can currently only report for gold."]:
    A(BUL(t))

A(H1("Exploratory Directions"))
A(BODY("Each of these tests a specific alternative explanation for a null result, rather than adding capacity in the hope of improvement. That distinction matters: the studies in Table 18 showed that added capacity and added features were repeatedly absorbed without benefit, so the useful experiments are the ones that could change an interpretation."))
for t in ["**Long-context encoding of full statements.** Headline-level polarity is a coarse summary of a central-bank communication. Encoding full statements with a long-context financial language model would test whether the null sentiment result is a property of markets or a limitation of headline granularity — two very different conclusions that the present evidence cannot separate.",
          "**A lower-frequency macro study.** The modality ablation is an H1 result. Macro releases plausibly act over days rather than hours, so the same features that are silent at hourly resolution may not be at daily resolution. This would establish whether the null is about the channel or about the horizon.",
          "**Cross-instrument transfer.** Silver has both the strongest volatility structure and the highest absolute magnitude skill. Whether a model trained on silver transfers usefully to gold or euro would indicate how instrument-specific the learned volatility representation is.",
          "**A reinforcement-learning execution layer.** As a longer-horizon extension beyond the supervised scope of this dissertation, the multi-step volatility forecasts could condition a policy that sizes positions and adjusts stop distances, moving the system from a forecasting tool towards a decision-support framework."]:
    A(BUL(t))

A(H1("Directions Blocked by Data Availability"))
A(BODY("Two directions that the literature suggests are recorded here as closed rather than omitted, because the reason they are closed is itself a finding about the retail research setting. Microstructure and order-flow features are among the most frequently cited sources of short-horizon predictive signal, and they were investigated and abandoned for reasons of data access, not of merit."))
A(BODY("There is **no consolidated order book for spot metals and FX**: the market is decentralised, each venue sees only its own flow, and no consolidated tape exists that a retail researcher can obtain. MetaTrader's depth-of-market feed is live-only with no history, which makes it unusable for a study whose entire evaluation rests on a chronological historical split. Tick-level microstructure data exists commercially, but the licensing and storage costs sit beyond the scope of a dissertation. These remain open questions rather than answered ones, and the distinction is stated so that the gap in this work is explicit."))

A(H1("Prioritisation, Effort and Risk"))
A(BODY("Ranking the candidates on the three dimensions that matter — the evidence behind them, the effort they require, and what could go wrong — gives the ordering below."))
A(TBL([["Direction","Evidence behind it","Effort","Principal risk"],
       ["Conformal for silver and euro","Strong — the gold result is the most robust in the report","Low — runs on frozen forecasts, no retraining","Coverage may not transfer as cleanly to a different volatility profile"],
       ["Volatility-targeted sizing","Strong — magnitude is the demonstrated axis","Medium — a decision layer, not a model","Backtest realism: costs and slippage were out of scope here"],
       ["Gate and attention readout","Strong — the quantities already exist at inference","Low — instrumentation only","Interpretability of a gate is not proof of causality"],
       ["Long-context statement encoding","Weak — motivated by a null result","High — new model, new pipeline","May confirm the null at greater cost"],
       ["Lower-frequency macro study","Moderate — the null is horizon-specific","Medium — reuses the existing panel","Fewer daily observations weakens every significance test"],
       ["Cross-instrument transfer","Moderate — silver is clearly strongest","Medium — retraining across pairs","Transfer failure would be uninformative about why"],
       ["Order-flow features","Cannot be assessed","Blocked","No historical source is obtainable"]],
      [1900,2400,1900,2000]))
A(CAP("Table 20: Forward directions ranked by the strength of the evidence supporting them, with the effort each requires and its principal risk."))
A(BODY("The ordering carries one deliberate implication. The three low-effort, strong-evidence items all concern uncertainty and magnitude — the parts of the system that worked — while the high-effort items all concern sentiment, the part that did not. A project continuing this work should complete the former before returning to the latter."))

A(H0("Conclusion and Future Scope of Work"))

A(H1("What Was Built"))
A(BODY("This dissertation set out to build and rigorously evaluate a hybrid CNN-LSTM-Transformer framework for multi-step foreign-exchange forecasting across gold, silver and the euro at hourly resolution. The architecture was implemented in full and is described layer by layer in Section 3: a dual-tower design fusing a dilated causal convolutional price encoder with a FinBERT sentiment encoder through gated cross-attention, followed by a four-layer causal Transformer, a parallel gated recurrent stage mixing Bi-LSTM and Bi-GRU branches, trust-gated XGBoost and GARCH experts in a nested convex blend, and regime-aware probabilistic heads trained under a Gaussian negative log-likelihood. The complete network holds 4,401,767 trainable parameters."))
A(BODY("Around it sits the infrastructure the evaluation required: a 37-feature multi-modal panel drawn from three independent sources across roughly 62,000 to 65,600 hourly bars per instrument, leak controls enforced structurally at assembly time, a walk-forward baseline harness, a three-test significance battery, an adaptive conformal calibration layer, and a live dashboard that serves the trained model with calibrated intervals and a per-stage timing and data-lineage view."))

A(H1("What Was Found"))
A(BODY("The evaluation produced a two-sided result, and both sides are reported without embellishment."))
A(BODY("**Direction is not forecastable at hourly resolution.** Across three instruments, three seeds and roughly fifteen alternative framings, no configuration exceeded the always-up base rate, and the classical baselines did not either. Apparent successes — including a 0.5637 selective-accuracy figure and an earlier 0.548 daily result — dissolved once the base rate of the relevant window was computed. This is consistent with market efficiency and stands as a methodological caution: directional accuracy reported without a base-rate control is not evidence of skill."))
A(BODY("**Magnitude is forecastable, and the hybrid beats the classical volatility models at it.** On the absolute size of the next ten-bar move, the model exceeds both ATR% and GARCH-sigma on rank skill and on large-move classification, for all three instruments and on every seed. On silver and euro the advantage is statistically significant under a block bootstrap, with all eight confidence intervals excluding zero; on gold all four intervals contain zero and the honest verdict is that the model matches rather than beats the baselines. The squared-error Diebold–Mariano and Model Confidence Set tests separate nothing on any instrument, a disagreement traced in Section 5.3 to the difference between ordering magnitude well and reducing squared error, and reported in full rather than resolved by selective quotation."))
A(BODY("**Calibrated uncertainty is the most robust contribution.** The model's Gaussian band under-covers substantially, containing the outcome only 72.9% of the time at a nominal 90% level, and adaptive conformal inference restores coverage to 90.0% under regime shift — a distribution-free guarantee that GARCH's parametric intervals do not provide, and one unaffected by the efficiency constraint that limits directional forecasting."))
A(IMG("fig_claims", 6.1))
A(CAP("Figure 21: The three claims of this dissertation, the evidence supporting each, what would overturn it, and how strongly each is therefore held."))

A(H1("Contributions"))
A(BODY("Separating what is genuinely new from what is competent application, the contributions are these."))
for t in ["**A base-rate-controlled negative result on hourly FX direction**, established across three instruments, three seeds and roughly fifteen framings — including the demonstration that subset selection silently raises the benchmark, which reversed a headline figure within this project.",
          "**A demonstrated magnitude advantage over ATR% and GARCH-sigma**, robust across all seeds on all three instruments and statistically significant on two, with the scope of the claim stated precisely rather than generalised.",
          "**An adaptive conformal layer that restores nominal coverage under regime shift**, deployed live rather than merely measured, together with the finding that split conformal is insufficient because the test window violates exchangeability.",
          "**A reproducible multi-instrument evaluation protocol** in which leak controls are enforced structurally, baselines are re-fitted walk-forward, forecasts are frozen to disk, and every significance test is reproduction-guarded against its committed point estimate.",
          "**A set of documented negative results** — the modality ablation, HAR-RV, CFTC positioning, Fair Value Gaps and quantile heads — reported with the same weight as the positive findings, which is where much of the practical value of this work sits for anyone continuing it."]:
    A(BUL(t))

A(H1("Limitations and Threats to Validity"))
A(BODY("Several limitations bound the claims above, and stating them is part of making the claims usable."))
A(TBL([["Limitation","Effect on the conclusions"],
       ["Single test window per instrument","The 15% held-out period is one realisation of one market regime. Gold's window is a strong bull market, which raises its base rate and makes the directional conclusion window-specific in degree, though not in direction."],
       ["Three seeds","Sufficient to separate a real effect from initialisation noise given the observed dispersion, but not a substitute for a full walk-forward re-training study."],
       ["Costs and slippage excluded","No transaction costs, spread or slippage are modelled. This weakens no result in the report, since none is a trading claim, but it means no figure here should be read as an achievable return."],
       ["Conformal fitted for gold only","The coverage result is demonstrated on one instrument; the claim is not yet shown to transfer, which is why extending it is the first item in Section 6.2."],
       ["Sentiment restricted to headlines","The null modality result is established for headline-level polarity and cannot distinguish a property of markets from a limitation of headline granularity."],
       ["No order-flow data","A well-evidenced source of short-horizon signal is absent for reasons of data access, so the directional conclusion is a statement about this feature set, not about all possible feature sets."],
       ["Significance on frozen seed-9 forecasts","Tests run on one realised forecast set rather than the three-seed mean, so the statistics in Tables 15 and 16 differ slightly from the point estimates in Table 14."]],
      [2300,5900]))
A(CAP("Table 21: Limitations and their effect on the scope of the conclusions."))
A(BODY("The most consequential of these is the first. A single test window means that the directional result, while consistent across three instruments and three seeds, is established on one decade of history ending in a specific market state. The consistency across instruments with different liquidity, volatility and news profiles is what makes it credible; a genuinely independent confirmation would require either a different period or a different asset class."))

A(H1("Closing Remarks"))
A(BODY("Taken together, the work delivers a complete, reproducible, multi-instrument forecasting system and, more importantly, a disciplined account of what such a system can and cannot do. The negative directional result, established under controls that much of the applied literature omits, is as substantive a contribution as the positive volatility result that accompanies it — and the two are load-bearing for each other, since the same architecture, features, test bars and protocol produced both. A broken pipeline or an inadequate model would have suppressed the positive result alongside the negative one."))
A(BODY("The forward programme in Section 6 — completing conformal calibration across all instruments, building a volatility-targeted decision layer, and exposing the attention and trust gates for explainability — aims to evolve the system from an accurate volatility model into a transparent and operationally useful decision-support tool for foreign-exchange risk management. That trajectory follows the evidence: it builds on the axis where signal was demonstrated, and it declines to keep optimising against a target this work has evidence is close to unforecastable."))

# ============================================================ 8 REFERENCES
A(H0("References"))
A(BODY("References are listed in IEEE style and numbered by order of first citation in the text. Bibliographic details \u2014 authors, venue, volume, pages and DOI \u2014 were verified against Crossref records rather than transcribed from secondary listings."))
_refs = [
 # --- classical econometrics and market theory
 "G. E. P. Box and G. M. Jenkins, *Time Series Analysis: Forecasting and Control*. San Francisco, CA, USA: Holden-Day, 1970.",
 "T. Bollerslev, “Generalized autoregressive conditional heteroskedasticity,” *Journal of Econometrics*, vol. 31, no. 3, pp. 307–327, 1986, doi: 10.1016/0304-4076(86)90063-1.",
 "E. F. Fama, “Efficient capital markets: A review of theory and empirical work,” *The Journal of Finance*, vol. 25, no. 2, pp. 383–417, 1970, doi: 10.2307/2325486.",
 # --- deep sequential learning
 "S. Hochreiter and J. Schmidhuber, “Long short-term memory,” *Neural Computation*, vol. 9, no. 8, pp. 1735–1780, 1997, doi: 10.1162/neco.1997.9.8.1735.",
 "I. Goodfellow, Y. Bengio and A. Courville, *Deep Learning*. Cambridge, MA, USA: MIT Press, 2016.",
 "Y. Dave, S. Varastehpour and M. Shakiba, “Predicting forex prices: An evaluation of long short-term memory, XGBoost and transformer architectures,” in *Proc. 2025 5th Int. Conf. on Advances in Electrical, Electronics and Computing Technology (EECT)*, 2025, pp. 1–6, doi: 10.1109/EECT64505.2025.10966964.",
 "E. Yohannes, A. Febriansyah, N. D. Septiyanti, Suparji, A. Wiyono, A. D. Indriyanti, F. Utaminingrum and C.-Y. Lin, “Forecasting stock prices with sequential deep learning: A long short-term memory approach,” in *Proc. 2025 8th Int. Conf. on Vocational Education and Electrical Engineering (ICVEE)*, 2025, pp. 177–183, doi: 10.1109/ICVEE66651.2025.11281457.",
 "F. López-Herrera, J. González Maiz Jiménez and A. Reyes Santiago, “Directional forecasting for eight forex pairs against the US dollar using machine learning techniques,” *Discover Artificial Intelligence*, vol. 5, no. 1, 2025, doi: 10.1007/s44163-025-00424-4.",
 "W. Luangluewut and P. Thiennviboon, “Forex price trend prediction using convolutional neural network,” in *Proc. 2023 20th Int. Conf. on Electrical Engineering/Electronics, Computer, Telecommunications and Information Technology (ECTI-CON)*, 2023, pp. 1–4, doi: 10.1109/ECTI-CON58255.2023.10153142.",
 # --- sentiment
 "A. S. Dash and U. Mishra, “Stock market trend prediction model using deep learning based sentiment analysis of financial data,” in *Proc. 2024 Int. Conf. on Integrated Intelligence and Communication Systems (ICIICS)*, 2024, pp. 1–7, doi: 10.1109/ICIICS63763.2024.10859730.",
 "A. Tadphale, H. Saraswat, O. Sonawane and P. R. Deshmukh, “Impact of news sentiment on foreign exchange rate prediction,” in *Proc. 2023 3rd Int. Conf. on Intelligent Technologies (CONIT)*, 2023, pp. 1–8, doi: 10.1109/CONIT59222.2023.10205534.",
 "D. Araci, “FinBERT: Financial sentiment analysis with pre-trained language models,” 2019, arXiv:1908.10063.",
 # --- volatility
 "R. M. Leushuis and N. Petkov, “Advances in forecasting realized volatility: A review of methodologies,” *Financial Innovation*, vol. 12, 2026, doi: 10.1186/s40854-025-00809-5.",
 "R. Reisenhofer, X. Bayer and N. Hautsch, “HARNet: A convolutional neural network for realized volatility forecasting,” 2022, doi: 10.2139/ssrn.4116642.",
 "W. Ben Romdhane and H. Boubaker, “A hybrid HAR-LSTM-GARCH model for forecasting volatility in energy markets,” *Journal of Risk and Financial Management*, vol. 19, no. 1, art. 77, 2026, doi: 10.3390/jrfm19010077.",
 "G. Taneva-Angelova and D. Granchev, “Deep learning and transformer architectures for volatility forecasting: Evidence from U.S. equity indices,” *Journal of Risk and Financial Management*, vol. 18, no. 12, art. 685, 2025, doi: 10.3390/jrfm18120685.",
 "Y. Zhang, P. Huang, P. Zhou and Y. Wu, “Forecast volatility based on realized GARCH and deep LSTM neural network,” in *Proc. 2020 Int. Conf. on Public Health and Data Science (ICPHDS)*, 2020, pp. 99–103, doi: 10.1109/ICPHDS51617.2020.00028.",
 "F. Corsi, “A simple approximate long-memory model of realized volatility,” *Journal of Financial Econometrics*, vol. 7, no. 2, pp. 174–196, 2009, doi: 10.1093/jjfinec/nbp001.",
 # --- uncertainty quantification and forecast comparison
 "V. Jensen, F. M. Bianchi and S. N. Anfinsen, “Ensemble conformalized quantile regression for probabilistic time series forecasting,” *IEEE Transactions on Neural Networks and Learning Systems*, vol. 35, pp. 9014–9025, 2024, doi: 10.1109/TNNLS.2022.3217694.",
 "Y. Romano, E. Patterson and E. Candès, “Conformalized quantile regression,” in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 32, 2019, arXiv:1905.03222.",
 "I. Gibbs and E. Candès, “Adaptive conformal inference under distribution shift,” in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 34, 2021, arXiv:2106.00170.",
 "F. X. Diebold and R. S. Mariano, “Comparing predictive accuracy,” *Journal of Business & Economic Statistics*, vol. 13, no. 3, pp. 253–263, 1995, doi: 10.1080/07350015.1995.10524599.",
 "P. R. Hansen, A. Lunde and J. M. Nason, “The model confidence set,” *Econometrica*, vol. 79, no. 2, pp. 453–497, 2011, doi: 10.3982/ECTA5771.",
 # --- architecture components
 "A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser and I. Polosukhin, “Attention is all you need,” in *Advances in Neural Information Processing Systems (NeurIPS)*, vol. 30, 2017, arXiv:1706.03762.",
 "T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,” in *Proc. 22nd ACM SIGKDD Int. Conf. on Knowledge Discovery and Data Mining (KDD)*, 2016, pp. 785–794, doi: 10.1145/2939672.2939785.",
]
for i, r in enumerate(_refs, 1):
    A(BODY(f"[{i}]\u2003{r}"))

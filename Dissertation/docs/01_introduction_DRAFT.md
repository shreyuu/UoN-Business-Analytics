# Chapter 1 — Introduction

> **DRAFT — revise into your own voice before sending. ~950 words ≈ 2 pages.**

## 1.1 Background and motivation

Machine learning models are now embedded in routine business decision-making, from credit scoring and demand forecasting to churn prediction and fraud detection. These models are trained on historical data under the implicit assumption that the relationships learned from the past continue to hold in the present. In practice, that assumption fails routinely: consumer behaviour shifts, market conditions change, and external shocks — the COVID-19 pandemic being a prominent recent example — can alter the relationship between a model's inputs and its target abruptly. This phenomenon is known as concept drift (Gama et al., 2014). When it occurs, the deployed model becomes progressively wrong, and the decisions built on its predictions deteriorate with it.

The standard operational response is monitoring: track the model's predictive performance and retrain when it falls. The weakness of this approach is that it is inherently reactive. By the time accuracy has visibly degraded, the organisation has already been acting on flawed predictions for some period, and in settings where ground-truth labels arrive with delay — a loan default is observed months after the lending decision — the degradation may go unmeasured long after it has begun. There is therefore clear business value in drift signals that fire earlier: before performance visibly falls, and ideally without waiting for labels to confirm the damage.

## 1.2 The proposed approach

This dissertation investigates whether such early-warning signals can be extracted from how a model uses its variables, rather than from how often it is wrong. The intuition is that when the input–output relationship changes, the pattern of feature reliance required to predict well changes with it, and this internal reorganisation may be observable before its consequences accumulate in the error rate.

Three candidate mechanisms are investigated. The first tracks shifts in variable-importance profiles over time, computed with SHAP (Lundberg and Lee, 2017), a game-theoretic attribution method. The second monitors vote dominance within a Random Forest ensemble (Breiman, 2001), detecting when the subset of trees casting the decisive votes changes. The third draws on Model Class Reliance and the Rashomon set — the set of near-optimal models for a given task (Fisher, Rudin and Dominici, 2019) — and asks whether the composition of that set, and the range of feature reliance within it, shifts when drift occurs. All three are evaluated against established error-based detectors, principally DDM (Gama et al., 2004) and ADWIN (Bifet and Gavaldà, 2007), which represent current standard practice.

A methodological point shapes the design of this investigation. Explanation methods describe the model, not the environment: a frozen deployed model, receiving inputs from a stationary distribution, produces a stable importance profile regardless of how the true input–output relationship has moved beneath it. Preliminary experimentation for this dissertation confirmed this empirically — importance recomputed on a periodically retrained model shifted markedly across a known drift point, while the same computation on the frozen deployed model barely moved. Detecting real concept drift from importance signals therefore requires deliberate design choices about which model is explained and what quantity (predictions or loss) is attributed. These choices are developed in the Methodology chapter and are themselves part of the dissertation's contribution.

## 1.3 Research questions and objectives

The dissertation addresses three research questions:

- **RQ1.** When real concept drift occurs, do variable-importance signals shift in a detectable way?
- **RQ2.** Do these signals shift earlier than predictive performance degrades — that is, do they provide useful early-warning lead time?
- **RQ3.** How do the SHAP-based, vote-dominance and MCR-based mechanisms compare against error-based baselines on detection delay, false-alarm rate and lead time?

These questions are pursued through the following objectives:

1. Review the concept-drift and explainability literatures to establish the research gap and select appropriate baselines and evaluation metrics.
2. Implement a windowed experimental pipeline over benchmark drift streams with known drift points (Losing, Hammer and Wersing, 2016), computing importance-based, vote-dominance and MCR signals alongside error-based baseline detectors.
3. Evaluate all detectors on detection delay, false-alarm rate and lead time relative to measurable performance degradation, on both synthetic streams (where drift onset is known) and real streams (where practical value is demonstrated).
4. Interpret the findings for model-monitoring practice, framing importance-based detection as a potential retraining trigger and quantifying the monitoring value it adds over current baselines.

## 1.4 Scope and data

The empirical work uses the publicly available benchmark concept-drift datasets of Losing, Hammer and Wersing (2016). Synthetic streams with known drift points — principally the rotating hyperplane stream, in which the input distribution is stationary while the decision boundary rotates — provide ground truth for validating whether each signal fires at the correct time, and isolate real concept drift from covariate shift by construction. As the data are open and contain no personal information, the project falls outside the scope of research ethics approval; this was confirmed with the project supervisor. [**← keep only if Gavin has actually confirmed this; otherwise change to "this is to be confirmed with the project supervisor".**]

## 1.5 Dissertation structure

Chapter 2 reviews the literature on concept drift, drift detection, variable importance and Rashomon sets, and states the research gap. Chapter 3 sets out the methodology: the datasets, the windowed experimental design, the construction of each detection signal, and the evaluation strategy. Chapter 4 reports the results of the experiments. Chapter 5 discusses the findings against the research questions, the literature and their business implications. Chapter 6 concludes with a summary of contributions, limitations and directions for future work.

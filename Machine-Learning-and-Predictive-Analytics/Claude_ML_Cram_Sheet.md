# ML Exam — Cram Sheet (last-day review)

Focused on **the patterns that recur every year** in Section I plus the Section II checklist.

---

## A. The 6-topic spine (Section I)

### 1 · Feature Importance & Selection
- **Univariate VIM:** fast, model-free, **misses interactions**, keeps redundant features.
- **Permutation (MDA):** drop performance when feature is shuffled. Model-agnostic, captures *model's* interactions, ideally on **held-out test set**. With correlated features → understates importance.
- **Hold-out (rebuild):** retrain without feature, compare. Closer to phenomenon-level but expensive; **can't infer multi-feature effects from single hold-outs**.
- **RFE** (3 steps): build → rank → remove worst → repeat. Result = *one* of several predictive relationships.
- **Boruta:** "all-relevant"; uses permuted shadow features + binomial test.
- **MCR (Model Class Reliance):** Rashomon set; MCR− = least relied on across equally-good models; MCR+ = max. Removes seed-dependence, lets you pick easy/causal/non-protected variables.
- **SHAP > permutation** when you need *direction*; ICE plot for systematic variation per data point; PDP = averaged ICE.
- **Selection vs. extraction:** selection saves collection cost (drop features). Extraction (PCA, NN) still needs all originals.

### 2 · Model Comparison & Preprocessing
- Three options: (1) single split + validation; (2) GridSearchCV inside train + single held-out test; (3) nested CV. Use Option 2 first.
- **Procedural overfitting:** using same test set to pick across many models → optimistic score. **Fix: third held-out test set or nested CV.**
- Always **split before scaling/imputing** (no leakage). Use `Pipeline`.
- **Categorical encoding:**
  - Nominal (gender) → OneHot
  - Ordinal (low/med/high) → manual numeric
  - High-cardinality (postcode 1.79M) → custom feature engineering
  - Continuous → StandardScaler
- **Missingness:**
  - postcode missing due to glitch = MCAR → kNN imputation
  - gender missing because people won't say = MNAR → encode "unknown"
  - spend_to_date missing when visits=0 = MAR → domain knowledge (set to 0)
- **RF does NOT need scaling.** Don't pipeline a StandardScaler in front of it.
- **List-kNN** (O(1) train, O(nd) predict): best for offline, batch, growing data.
- **Tree-kNN** (O(n log n) train, O(log n) predict): best for real-time/frequent prediction.
- **Reducing complexity** is usually the first move when RF overfits (train>>val).

### 3 · SVMs
- **Hyperplane = vector + offset** (w·x + b). Margin maximised. Only support vectors carry weight.
- **C** (penalty on misclassification): high C → small margin → more overfit. Low C → wide margin → more regularised.
- **γ (RBF):** high γ → narrow Gaussians → overfit (kNN-like). Low γ → wide → almost linear.
- **Which kernel/parameters when:**
  - d ≫ n (1000 features, 2000 points) → **Linear SVM (primal)**. Alternative: dual non-linear (less curse of dimensionality).
  - Noisy + highly non-linear → RBF, low C, high γ → kernel: 4 in the multi-choice.
  - Little noise + maybe linear → linear, high C → option 5.
  - Little noise + simple non-linear → RBF, high C, low γ → option 1.
- **SVM is globally optimal** (convex). Running 100 times with same X = 100 identical scores. Pointless to test for local minima on SVM (RF without seed *is* worth checking).
- **SVR ≠ SVC.** Use SVR for regression, SVC for classification. Common code-review bug.
- Multi-class SVMs: OvR or OvO; default in sklearn = OvO.

### 4 · Time Series
- **Two paradigms:** (a) non-temporal task with temporal features (predict NOW from past) vs. (b) temporal task (predict FUTURE).
- **Random CV fails on temporal** for two reasons: (1) future leaks into training; (2) global events (COVID, Christmas) shared across train+test.
- **Tumbling = less correlated than expanding** windows.
- **Cannot StandardScaler each lag independently** — destroys monotonic info. Scale lags collectively using the variable's overall mean/std.
- **Single temporal hold-out:** test ref date > train ref date.
- **Repeated temporal hold-out:** loop `now -= 1 month`, build train (now-2) and test (now-1), retrain each round.
- **Cross-validation for meta-params on temporal data:** use TimeSeriesSplit, **never KFold**.
- **Temporal baseline:** previous time point's value (NOT all-time mean).
- **Global model (RF + lags) beats ARIMA-per-customer** when:
  - You have demographic / signup features (ARIMA can't use globals).
  - Individuals have sparse data.
  - You need to pool info across customers.
- **What's "unseen" temporally?** A (thing, time) pair where the time is in the future.
- **ARIMA(p,d,q):** p = past-value lags, d = differences, q = past-error lags. Differencing extracts the **trend**.
- **A/B test prerequisites:** truly random group assignment, large enough samples, end-to-end intervention, single-variant per user, ethical considerations, transition plan, business actionability.

### 5 · Neural Networks
- **Universal approx thm:** shallow NN can approximate any function in theory. In practice fails due to depth-of-features, parameter explosion, training difficulty.
- **Output layer choice** (most common bug):
  - Regression → linear, MSE
  - Binary → sigmoid, binary cross-entropy
  - Multi-class → softmax, categorical cross-entropy
- **Vanishing gradients fixes:** different activation (ReLU/ELU), better init (He), batch normalisation.
- **Exploding gradients signs:** unusually large loss changes, NaN/Inf loss, huge weight updates, non-decreasing loss.
- **Slow convergence causes:** learning rate too small, poorly-scaled features, vanishing gradients (NOT "model overfitting").
- **Three meta-params** to list: depth, width, activation, init strategy, learning rate, optimiser, batch size, dropout rate, L1/L2 strength.
- **No-data options:** transfer learning + data augmentation (+ simpler model).
- **Data augmentation conceptual reason:** more *real* variation → parameters fit signal, not noise → less overfit.
- **Foundation models:** versatile + reduced dev time. Drawbacks: bias inheritance, data poisoning, can't use domain features.
- **Customise foundation models:** fine-tune, prompt engineering, RAG (NOT "change weights from domain knowledge"; NOT "add layers and retrain on original data").
- **Mitigate overfitting in fine-tuning:** data augmentation, dropout, early stopping, freezing layers (NOT add layers, NOT train longer, NOT larger batch).
- **Batch normalisation goes between every layer**, not just at input.
- **`use_bias=False` requires batch normalisation** for centring.
- **`validation_data = (X_test, y_test)`** in `model.fit` = procedural overfitting. Use a true validation set.
- **Initialisations:** He for ReLU/ELU; Xavier/Glorot for sigmoid/tanh; LeCun for SELU.
- **CNNs:** local receptive fields + weight sharing + pooling = solves spatial blindness, parameter explosion, translation invariance.
- **RNN limits → LSTM (gates: forget/input/output) → Transformers** (parallel attention, no recurrence).

### 6 · Causal Inference
- **Observational P(y|x) vs. causal P(y|do(x))** — light-sensor example.
- **Fundamental problem:** we observe one of y(treated) or y(untreated), never both per individual.
- **ATE** (whole population) vs. **ATT** (treated only).
- **Gold standard = RCT / A/B test** (random assignment removes confounding on average).
- **Simpson's paradox:** aggregate trend reverses subgroup trend due to **unmeasured confounder**. Consequence: wrong direction of effect reported.
- **Causal estimation from observational data REQUIRES** extra assumptions:
  - **Unconfoundedness** is the standard one (CEM, conditioning, propensity scores all assume this).
  - Refutations test these assumptions.
- **What permutation importance is NOT:** a causal measure.

---

## B. Section II checklist (~6-8 issues = full marks)

### Generic (apply to any problem)
- Scaling before split → leakage
- LabelEncoder on nominal → false ordering (use OneHot)
- KFold not StratifiedKFold on imbalanced
- No class imbalance handling
- accuracy_score on imbalanced → use balanced_accuracy_score
- Procedural overfitting (test set used to choose across models)
- No hyperparameter tuning for one of the compared models
- SVR for classification (use SVC)
- Pipeline missing scaler for SVM/kNN/NN
- shuffle=False on data ordered by some feature (or shuffle=True on temporal)
- n_estimators in RF grid search (not a complexity knob)
- Typos in imports / variable name mismatches (`X_train` vs `train_X`)

### Temporal-specific
- Random train/test split → use temporal hold-out
- GridSearchCV with default KFold → TimeSeriesSplit
- Single reference date → repeated temporal hold-out
- StandardScaler per-lag-independently → scale collectively
- Output windows overlap between train/test → ensure no overlap
- Wrong unit for `now - 1` (weeks vs. months)

### NN-specific
- Wrong output layer (sigmoid on regression, etc.)
- Wrong loss (MSE on classification, etc.)
- BatchNormalization only at input
- `use_bias=False` without BatchNormalization between layers
- `validation_data=(X_test, y_test)` for early stopping
- No regularisation on small dataset (add dropout + L2)
- No early stopping with fixed huge epoch count
- `epochs=500` and `patience=50` with `min_delta=0.1` too aggressive
- Scaling once on all of X before split
- Single hidden layer for clearly non-trivial problem
- Default SGD when Adam would converge

---

## C. Money sentences (for marks)

> "This is **data leakage** because the scaler was fit on the test set; the test score over-estimates real-world performance."

> "This is **procedural overfitting**: the same held-out test set was used to compare across model classes, so the reported score is optimistic. Use a third, never-touched test set or nested CV."

> "On temporal data, **random sampling places future points in training**, which can never happen in deployment; use out-of-time hold-out instead."

> "Univariate VIM **cannot capture interactions** — features that are only predictive jointly will each appear unimportant."

> "**Permutation importance** shows how the model relies on a feature; it doesn't show what would happen if the feature were never available. For that, you must rebuild the model without it."

> "SHAP is preferred here because, unlike permutation, it shows both **magnitude and direction** of the per-prediction effect."

> "The boundary is forced toward the minority class because the algorithm **minimises the sum of per-point errors equally across classes**; class re-weighting corrects this."

> "Under **unconfoundedness** — that all variables jointly affecting treatment and outcome are measured — conditioning, matching, and propensity-score methods can estimate the causal effect from observational data."

---

## D. Quick numbers / facts to memorise

- **List-kNN:** O(1) train, O(nd) predict
- **Tree-kNN:** O(n log n) train, O(log n) predict
- **Linear SVM (primal):** O(d² n) train
- **Kernel SVM (dual):** O(n² d) train
- **Adam defaults:** β₁=0.9, β₂=0.999
- **He init** for ReLU/ELU, **Xavier** for sigmoid/tanh
- **Dropout typical:** 0.2–0.5
- **CV folds typical:** 5 or 10, with `shuffle=True, random_state=42`
- **Train/test split typical:** 70/30 or 80/20

---

## E. Things examiners reward
1. **Always justify** — "Why?" gets you the second mark.
2. **Mention assumptions** — when assumptions are noted, the marker knows you understand the limits.
3. **State trade-offs** — "X works because Y, but at the cost of Z."
4. **Use the framework language** — "leakage", "procedural overfitting", "model-vs-phenomenon", "captures the interactions the model captures", "minimises sum of per-point errors equally".
5. **Be concise.** 1-mark answers want a single sentence; do not write a paragraph for them.
6. For numeric/code questions, **show the small piece of working** that supports your claim.

---

## F. Time management (2-hour exam)

- Section I: ~75 marks → ~80 minutes (about 1 min/mark + 5 min buffer).
- Section II: ~25 marks → ~30 minutes (read code carefully, list 6-8 issues, write three points per issue).
- **Leave 10 minutes** at the end to revisit anything skipped and check Section II for missed issues.

If you're stuck on a 1-mark question: skip and come back. If you're stuck on Section II, brute-force the checklist (§B) line by line — at least one of them will fit.

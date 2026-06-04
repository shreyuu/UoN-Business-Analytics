# Machine Learning & Predictive Analytics — Last-Night Revision Notes
### Beginner-friendly, exam-focused. Built from your slides + past papers (patterns only, no questions copied).

> **How to read this tonight:** Start with the **Study Plan** and **High-Priority List** below. Then read the **8 topic sections**. Keep the **Cheat Sheet** and **Comparison Tables** open at the end for last-minute glancing. Code blocks use the exact variables you'll see in the exam: `X_train`, `X_test`, `y_train`, `y_test`, `model`, `pipe`, `accuracy`, etc.

---

## ⏱️ PART 1 — LAST-NIGHT STUDY PLAN (very little time)

You have limited time, so spend it where marks live. The exam = **Section I (answer all 6 questions)** + **Section II (answer ONE big code-fixing question, ~24–25 marks)**.

**Suggested 4-hour plan:**

1. **(45 min) Section II code-review** — *highest single block of marks.* Memorise the "violation checklist" in Part 4. This question is almost guaranteed and is very learnable.
2. **(40 min) Feature Importance** (SHAP / permutation / ICE / PDP / MCR / selection vs extraction). This is **always Question 1**.
3. **(30 min) SVMs** (primal vs dual, C & gamma, scaling). Always asked.
4. **(30 min) Time Series** (tumbling vs expanding, temporal baseline, why random split is dangerous, temporal standardisation).
5. **(30 min) Neural Networks** (gradient descent types, vanishing gradients, regularisation, foundation models, training graph vs learning curve).
6. **(25 min) Evaluation & Causal** (procedural overfitting, GridSearchCV order, Simpson's paradox, ATE/ATT, DAG, refutation).
7. **(20 min) Preprocessing & Missing data** (MCAR/MAR/MNAR, one-hot, imputation, pipelines, complexity O()).
8. **(20 min) Bias–variance diagnosis** (high/low train & test error → what to do).
9. **(remaining) Cheat sheet + tables.** Sleep. A rested brain scores more than a tired one.

**Golden rule for the exam:** When asked "why is this a good/bad choice?", always answer in this shape → **(1) name the issue, (2) say the consequence, (3) say the fix.** That's exactly how marks are awarded.

---

## 🔥 PART 2 — HIGH-PRIORITY REVISION LIST

These appear *every year* or carry the most marks. Learn these first:

1. **Section II "find the best-practice violations in this code"** (24–25 marks). See checklist in Part 4.
2. **SHAP vs permutation importance vs ICE/PDP**, and **why univariate selection misses interactions.**
3. **MCR / Rashomon** ("importance in reality, not just in one model") and **Boruta (all-relevant) vs RFE (k-best)**.
4. **SVM: primal O(d²n) vs dual O(n²d)**, when to use each, **why scaling is needed**, **C and gamma effects**.
5. **Time series:** tumbling vs expanding windows; **previous-value baseline**; **why a random train/test split leaks the future (global events / COVID)**; temporal standardisation; ARIMA-per-series vs global Random Forest.
6. **Procedural overfitting vs ordinary overfitting**, and the correct **train_test_split → GridSearchCV → final test** order.
7. **Missing data: MCAR / MAR / MNAR** and matching fix (kNN impute / domain knowledge / "unknown" category).
8. **Unbalanced classes:** `class_weight='balanced'` (or sample weights) vs **threshold moving**; evaluate with **balanced accuracy**.
9. **Neural nets:** gradient descent (batch/stochastic/mini-batch), **vanishing gradients** (causes + fixes), **regularisation** (dropout, early stopping, L1/L2, data augmentation), **Adam vs AdaGrad**, **foundation models** (benefits, drawbacks, customisation).
10. **Bias–variance** diagnosis from train/test error, and **training-graph (error vs epochs) ≠ learning curve (error vs data size)**.
11. **Causal:** Simpson's paradox (hidden confounder flips the relationship), **ATE vs ATT**, **DAGs** (missing edges encode independence → minimum adjustment set), **refutation** (adding a random/dummy cause should NOT change the estimate).
12. **One-hot encoding vs manual numeric encoding vs standardisation** — which preprocessing for which feature type.

---

## 📝 PART 3 — MOST LIKELY EXAM QUESTIONS (paraphrased patterns, NOT copied)

Practise answering these in your own words. They mirror the *style* of past papers:

**Feature importance**
- "You ran permutation importance and one feature scored 0.2 — what does this number mean?" (Answer for accuracy *and* for MSE.)
- "Two SHAP plots from two models use different features. Why?"
- "You dropped low-univariate-importance features and the model got worse. Why?"
- "Match each technique (MCR, Boruta, ICE, RFE, Univariate VIM) to the scenario it best suits."
- "What do the grey lines, centre line, and dots on a PDP/ICE plot mean?"

**Real-world use / preprocessing**
- "Match preprocessing (one-hot, manual numeric, standardisation, feature engineering) to features (gender, income bracket, postcode, spend)."
- "Classify each missing feature as MCAR/MAR/MNAR and choose the best fix."
- "Given two complexity formulas, which algorithm suits batch yearly prediction on rapidly growing data?"
- "Model does well on train, poorly on validation — first thing to try, and justify why not the others."

**SVM**
- "1000 features, 2000 points, different scales, missing values, multi-class — is an SVM a good choice? Primal or dual? Why?"
- "Match data properties (noisy/non-linear, clean/unknown-shape, clean/low-complexity-non-linear) to kernel + C + gamma settings."
- "Why does SVM need scaling but a Random Forest doesn't?"

**Time series**
- "Which features can be lagged? Which could be but usually shouldn't?"
- "Give one reason to use tumbling instead of expanding windows, and vice versa."
- "Pre+post-COVID data — what's right/wrong about evaluating with a random split? Consequence and why?"
- "What's a better temporal baseline than the overall mean?"

**Neural networks**
- "Loss decreases very slowly — list possible causes." / "You see exploding gradients — what symptoms gave it away?"
- "Network is overfitting — list techniques to reduce complexity; which two can be combined?"
- "Best description of a foundation model? Benefits? Drawbacks? Ways to customise it?"
- "Interpret this training graph — would you use the model at epoch 100? Does it suggest fewer layers?"

**Evaluation & causal**
- "Explain ordinary overfitting vs procedural overfitting for an SVM example."
- "Explain how to use train_test_split + GridSearchCV (in order) to prevent both."
- "What is Simpson's paradox? What wrong conclusion would you draw? What causes it?"
- "What extra info do you need to claim X *causes* Y? If you can't get it, what else could you do (A/B test)?"

**Section II (one of these styles):**
- A **classification** code block with ~8 violations (label-encoding a nominal category, scaling before split, no stratification, SVR used for classification, no class weighting, wrong scoring, evaluating on train, etc.).
- A **temporal** code block (random split instead of temporal, non-temporal standardisation, varying `n_estimators` as if it controls complexity, linear SVM with a gamma loop, selecting model by *mean* class score, etc.).
- A **neural network** code block (no imputation, wrong output activation, wrong loss, too few epochs, validating on the test set, batch-norm placement, temporal scaling).

---

## 🛠️ PART 4 — SECTION II "CODE VIOLATION" CHEAT-CHECKLIST (memorise this!)

For **each** violation write: **(1) what & where, (2) why it's a problem, (3) the fix.** Scan the code top-to-bottom looking for these recurring mistakes:

| # | Violation (what to spot) | Why it's wrong (consequence) | Fix |
|---|---|---|---|
| 1 | `LabelEncoder` on a **nominal** category (e.g. payment method) | Invents a fake order → poor/unstable performance | Use `OneHotEncoder` |
| 2 | `StandardScaler().fit_transform(X)` **before** the split | **Data leakage** — test info leaks into scaling → inflated score | Split first, then fit scaler on `X_train` only, or put scaler in a `Pipeline` |
| 3 | `shuffle=False` when data is **ordered** (or `shuffle=True` on **temporal** data) | Non-random split / future leaks into past | Set `shuffle=True` for non-temporal; use **temporal holdout** for time series |
| 4 | Plain `KFold` on an **imbalanced** problem | Folds may miss the minority class | Use `StratifiedKFold` |
| 5 | `SVR` (regressor) used for **classification** | Wrong output type | Use `SVC` (and a regressor for regression) |
| 6 | No class weighting on imbalanced data | Model favours majority class → bad balanced accuracy | `SVC(class_weight='balanced')` or `sample_weight` |
| 7 | `scoring='accuracy'` when metric should be **balanced accuracy** | Misleading score on imbalanced data | `scoring='balanced_accuracy'` |
| 8 | Evaluating on `X_train` / reporting the **best CV score** as final | Over-optimistic, not generalisation | Evaluate the chosen model on the **held-out `X_test`** |
| 9 | Selecting the final model by **mean of each model class's scores** | Picks a class, not the best model | Compare the **best score over all models/params** |
| 10 | Choosing the final model **on the test set** after trying many | **Procedural overfitting** → inflated reported performance | Pick via validation/CV; use a **separate, untouched test set** only once at the end |
| 11 | Varying `n_estimators` to "control complexity" of a Random Forest | It barely changes complexity | Vary `max_depth`, `max_features` instead |
| 12 | Linear SVM with a **gamma** grid | Linear kernel has no gamma → wasted compute | Use `kernel='rbf'` or drop the gamma loop |
| 13 | Plain `StandardScaler` on **lagged temporal** features | Removes temporal information / scales each lag separately | Use **temporal-aware standardisation** (one mean/std across all lags of a variable) |
| 14 | NN: `sigmoid` output for **regression**, or `relu` output for classification | Wrong range / wrong probabilities | `linear` output for regression, `softmax` (multi-class) / `sigmoid` (binary) for classification |
| 15 | NN: `loss='mean_squared_error'` for classification | Wrong objective | Use `categorical_crossentropy` / `binary_crossentropy` |
| 16 | NN: `epochs=5` (too few) | Cannot converge | Increase epochs (+ early stopping) |
| 17 | NN: early stopping/checkpoint monitoring the **test set** | Test leakage | Monitor the **validation set** |
| 18 | Dropping rows with missing values instead of imputing | Lose data (bad for data-hungry NNs) | Impute (kNN / domain / "unknown" category) |
| 19 | `if rf_score < svc_score: best = rf` (wrong direction) | Picks the worse model | Flip the comparison for "higher is better" metrics |
| 20 | Best model not retrained on all available (or most recent) data | Weaker final model | Refit on the full/most-recent training data before deploying |

> **Tip:** If the same issue appears twice, you only get credit once — so spread your answers across *different* violation types.

---

# 📚 PART 5 — DETAILED TOPIC NOTES

Each topic follows your requested structure: **1) Beginner explanation · 2) Exam meaning · 3) Key terms/formulas · 4) sklearn example · 5) How it appears in exams · 6) Model answer structure · 7) Common mistakes · 8) Quick revision bullets.**

---

## TOPIC 1 — Real-World Model Use & Data Challenges

### 1A. Comparing models & measuring efficiency

**1) Beginner explanation.** "Efficiency" has two meanings: (a) *how good* the predictions are (accuracy, error), and (b) *how expensive* the model is to train/predict (time & memory). A good engineer balances both. Sabse accurate model agar bohot slow hai, toh woh real world me useless ho sakta hai.

**2) Exam meaning.** You compare models *fairly* (same data split, same metric) and justify a choice using **both** predictive performance and computational cost.

**3) Key terms.** `train_error`, `test_error`, accuracy, balanced accuracy, MAE/MSE, time complexity (Big-O).

**4) sklearn example.**
```python
from sklearn.metrics import balanced_accuracy_score
model.fit(X_train, y_train)
test_score = balanced_accuracy_score(y_test, model.predict(X_test))
```

**5) In the exam.** "Why choose model X over Y for this scenario?" → tie your answer to data size, dimensionality, scaling, interpretability, and runtime.

**6) Model answer structure.** *Scenario → which metric matters → which model fits the data shape → cost trade-off → conclusion.*

**7) Common mistakes.** Comparing models on different splits; ignoring runtime; reporting accuracy on imbalanced data.

**8) Quick bullets.** Compare on the *same* held-out test set · pick metric to match the business goal · always mention cost when data is huge.

### 1B. Data preprocessing & missing data

**1) Beginner explanation.** Models can't handle raw messy data. We clean it first: fix missing values, encode categories into numbers, and put features on similar scales.

**2) Exam meaning.** Choose the *right* preprocessing per feature *and* do it without leaking test data (use a Pipeline).

**3) Key terms.** Imputation, encoding, standardisation, **data leakage**.

**4) sklearn example.**
```python
from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
pipe = Pipeline([('impute', KNNImputer(n_neighbors=2)),
                 ('scale', StandardScaler()),
                 ('model', model)])
pipe.fit(X_train, y_train)   # fitting happens ONLY on training data
```

**5) In the exam.** "Build a suitable pipeline" or "what's wrong with scaling here?"

**6) Model answer structure.** *Identify feature type → choose technique → wrap in pipeline so fit() uses train only.*

**7) Common mistakes.** Scaling before splitting (leakage); label-encoding nominal categories.

**8) Quick bullets.** Pipeline = no leakage · fit on train, transform test · scale numeric, encode categorical.

### 1C. Missing-data mechanisms — MCAR / MAR / MNAR ⭐

**1) Beginner explanation.**
- **MCAR (Missing Completely At Random):** missingness is pure chance, unrelated to anything. *e.g. an app glitch randomly fails to record postcode.*
- **MAR (Missing At Random):** missingness depends on **other observed features**. *e.g. "spend to date" is missing exactly when "number of visits = 0".*
- **MNAR (Missing Not At Random):** missingness depends on the **missing value itself / something unobserved**. *e.g. people of a certain gender choose not to state gender.*

**2) Exam meaning.** Classify each feature's missingness, then pick the matching fix.

**3) Key terms + matching fixes.**
| Mechanism | Best fix |
|---|---|
| MCAR | kNN imputation (or mean) — safe, values are random |
| MAR | Domain knowledge (you *know* why it's missing, e.g. visits=0 → spend=0) or model-based impute |
| MNAR | Add an extra **"unknown"** category, because the missingness itself carries information |

**4) sklearn example.** `KNNImputer(n_neighbors=2)` for MCAR; manual fill for MAR; `SimpleImputer(strategy='constant', fill_value='unknown')` for MNAR categorical.

**5) In the exam.** "For each feature, state MCAR/MAR/MNAR and the best solution." (3 + 3 marks, very common.)

**6) Model answer structure.** *State mechanism → one-line justification → matching fix.*

**7) Common mistakes.** Mean-imputing MNAR (hides information); dropping rows you could impute.

**8) Quick bullets.** MCAR=luck · MAR=explained by other columns · MNAR=depends on the hidden value · MNAR→"unknown" category.

### 1D. One-hot encoding & encoding choices ⭐

**1) Beginner explanation.** Models need numbers. **One-hot** turns a category into separate 0/1 columns (no fake order). Use **manual numeric encoding** only for **ordinal** data (where order is real, e.g. income bracket low<med<high). High-cardinality text (e.g. 1.79M postcodes) → don't one-hot (too many columns); do **custom feature engineering** instead (e.g. map postcode → region/affluence score).

**2) Exam meaning.** Match each feature to the correct encoding/preprocessing.

**3) Key terms.** Nominal vs ordinal; cardinality; `OneHotEncoder`.

**4) sklearn example.**
```python
from sklearn.preprocessing import OneHotEncoder
X_gender = OneHotEncoder(handle_unknown='ignore').fit_transform(X_train[['gender']])
```

**5) In the exam.** "Match: one-hot / manual numeric / feature engineering / standardisation → gender / income bracket / postcode / spend." (Answer: gender→one-hot, income bracket→manual numeric, postcode→feature engineering, spend→standardisation.)

**6) Model answer structure.** *Feature type → encoding that respects (or doesn't impose) order → note cardinality issues.*

**7) Common mistakes.** One-hot on a million postcodes; manual encoding nominal categories.

**8) Quick bullets.** Nominal→one-hot · Ordinal→numeric in order · Huge text→engineer it · Continuous→standardise.

### 1E. Unbalanced classes ⭐

**1) Beginner explanation.** If 90% of customers don't churn, a lazy model that always says "no churn" gets 90% accuracy but is useless. We must rebalance the learning or change the metric.

**2) Exam meaning.** Know **two strategies** + their pros/cons, and use the right metric.

**3) Key terms + strategies.**
- **Class re-weighting / sample weights:** make minority-class errors count more. *+ directly optimises what we care about; − not always supported.*
- **Threshold moving:** change the 0.5 decision cutoff after training. *+ no retraining, works on any probabilistic classifier, stacks on top of weighting; − adds a meta-parameter to tune.*
- (Also: resampling / SMOTE.)
- **Metric:** `balanced_accuracy` (average of per-class recall). Or a **custom profit metric** if different correct answers earn different money.

**4) sklearn example.**
```python
from sklearn.svm import SVC
model = SVC(class_weight='balanced')          # strategy 1
# or weight by profit: weights[y==classA]=5; weights[y==classB]=1
model.fit(X_train, y_train, sample_weight=weights)
```

**5) In the exam.** "One benefit + one drawback of each strategy"; "which metric?"; profit-based weighting question.

**6) Model answer structure.** *Pick strategy → +ve / −ve → state metric (balanced accuracy / custom).*

**7) Common mistakes.** Using plain accuracy; forgetting `stratify`/`StratifiedKFold` in splits.

**8) Quick bullets.** Reweight OR move threshold · evaluate with balanced accuracy · stratify your folds.

### 1F. Multi-class classification using binary classifiers ⭐

**1) Beginner explanation.** Some models (like SVM) are naturally **binary** (2 classes). To handle many classes we combine binary models.
- **One-vs-Rest (OvR):** train one classifier per class ("is it class k or not?"); predict with all, pick the highest probability.
- **One-vs-One / All-vs-All:** train a classifier for every pair of classes; they vote, majority wins.

**2) Exam meaning.** Describe one approach clearly.

**3) Key terms.** OvR, OvO, voting.

**4) sklearn example.** `from sklearn.multiclass import OneVsRestClassifier; OneVsRestClassifier(SVC(probability=True))`.

**5) In the exam.** "Describe one approach to use a binary classifier on a multi-class problem." (3 marks.)

**6) Model answer structure.** *Name method → how many classifiers → how prediction is decided.*

**7) Common mistakes.** Saying "SVM can't do multi-class" (it can, via OvR wrapper).

**8) Quick bullets.** OvR = n classifiers, pick max prob · OvO = pairwise vote.

### 1G. sklearn pipelines ⭐

**1) Beginner explanation.** A pipeline chains preprocessing + model into one object, so when you call `.fit()` everything learns from the training data only — preventing leakage.

**2) Exam meaning.** Pipelines = the *correct* way to preprocess inside cross-validation.

**3) Key terms.** `Pipeline`, steps, `predictor__C` (double-underscore to reach a step's parameter in a grid).

**4) sklearn example.**
```python
pipe = Pipeline([('scale', StandardScaler()), ('predictor', SVC())])
param_grid = {'predictor__C': [0.1, 1, 10], 'predictor__gamma': [0.01, 0.1, 1]}
```

**5) In the exam.** Used as the *fix* for "scaling before split" in Section II.

**6) Model answer structure.** *Why leakage is bad → pipeline fits transforms on train fold only.*

**7) Common mistakes.** Using a Pipeline but still calling `scaler.fit_transform(X)` outside it.

**8) Quick bullets.** Pipeline = preprocessing + model together · stops leakage in CV · grid keys use `step__param`.

### 1H. Algorithmic complexity ⭐

**1) Beginner explanation.** Big-O tells us how *training* and *prediction* time grow as data grows. `n` = number of points, `d` = number of features.

**2) Exam meaning.** Pick the algorithm whose cost suits *how the system is used* (batch vs online, growing data, time-critical or not).

**3) Key terms / numbers to remember.**
- **kNN (list-based):** train `O(1)`, predict `O(nd)`.
- **kNN (tree-based):** train `O(n log n)`, predict `O(log n)`.
- **SVM:** primal training `O(d²n)`, dual training `O(n²d)`.

**4) Reasoning example.** "Predict a small batch once a year on rapidly growing data" → list-based kNN: training is free (`O(1)`) and you rarely predict, so the slow `O(nd)` prediction doesn't matter. (Tree-based wastes time rebuilding `O(n log n)` each year as data grows.)

**5) In the exam.** "Which is better for [usage pattern]?" — short 1-mark choices.

**6) Model answer structure.** *Identify how often you train vs predict → match to the cheaper operation for that pattern.*

**7) Common mistakes.** Ignoring whether the cost is in training or prediction.

**8) Quick bullets.** n=points, d=features · list-kNN: free train, slow predict · primal SVM O(d²n) hates big d · dual SVM O(n²d) hates big n.

---

## TOPIC 2 — Time Series ⭐⭐

### 2A. Lagged features

**1) Beginner explanation.** To predict the future with a normal model, we feed it the **past** as columns. A "lag" is a past value, e.g. `spend_t-1`, `spend_t-2`. This turns a time series into a normal table.

**2) Exam meaning.** Know which features *can* be lagged (things that change over time) and which *can't/shouldn't* (static or near-constant).

**3) Key terms.** Lag, reference point, output window.

**4) Example.** Lag `spend` and `visit_count`. You *can* lag age/item counts; you *can't usefully* lag `gender`, `postcode`, `birth city` (static). You *could* lag "items purchased" but at a monthly level it may be **almost constant**, so usually don't.

**5) In the exam.** "Which features could be lagged? Which could but typically wouldn't, and why?"

**6) Model answer structure.** *Lag = past value as a column → static features have no past variation → near-constant features add no info.*

**7) Common mistakes.** Lagging static demographics; assuming more lags always helps (it doesn't).

**8) Quick bullets.** Lag = past-as-feature · only lag time-varying things · more lags ≠ always better.

### 2B. Tumbling vs expanding windows ⭐

**1) Beginner explanation.** A **window** aggregates past data into a feature.
- **Tumbling (chunking) window:** fixed-size, non-overlapping chunks (e.g. each separate week).
- **Expanding window:** grows over time, always starting from the beginning (e.g. everything so far).

**2) Exam meaning.** Pick one and justify with a one-liner.

**3) Key trade-off.**
- **Tumbling →** features are **less correlated** with each other (each chunk is fresh).
- **Expanding →** **fewer edge effects / fewer missing values** at the start (always has data to aggregate).

**4) Example.** 4 tumbling 1-week windows of sales = `f1..f4`, each a distinct week.

**5) In the exam.** "One reason to use tumbling instead of expanding" (less correlation) and "vice versa" (fewer edge effects).

**6) Model answer structure.** *Define both → state the single trade-off relevant to the question.*

**7) Common mistakes.** Mixing the two reasons up.

**8) Quick bullets.** Tumbling = non-overlapping, less correlation · Expanding = cumulative, fewer edge effects.

### 2C. Standardisation of temporal features (temporal standardisation) ⭐

**1) Beginner explanation.** If you scale each lag column **separately** with a normal `StandardScaler`, you destroy the relationship between `spend_t-1` and `spend_t-2` (they should share one scale). So scale all lags of the **same variable together** using one mean & std.

**2) Exam meaning.** Plain `StandardScaler` on lagged features = **a violation**.

**3) Key terms.** Temporal standardisation (one mean/std across a variable's lags).

**4) Example.** For `spend_t-1..t-6`, compute one mean and one std across all six and apply to all.

**5) In the exam.** Section II fix; also "what preprocessing for lagged + non-temporal features?" → temporal standardisation for the lags, standard scaling for the non-temporal ones.

**6) Model answer structure.** *Lags share meaning → independent scaling loses temporal info → scale them jointly.*

**7) Common mistakes.** Using `StandardScaler()` directly on lagged columns.

**8) Quick bullets.** Lags of one variable → one shared scale · don't scale each lag alone.

### 2D. Appropriate temporal baselines ⭐

**1) Beginner explanation.** A baseline is a dumb model you must beat. For time series, the **overall mean is a bad baseline** because data drifts (non-stationary). A much better baseline is **"predict the previous value"** (persistence / naive forecast).

**2) Exam meaning.** Recommend the previous-step baseline and say *why* (non-stationarity).

**3) Key terms.** Persistence baseline, non-stationary.

**5) In the exam.** "What's a better temporal baseline than the mean? Why is it better?"

**6) Model answer structure.** *Mean ignores trend → previous value tracks drift → better because data is non-stationary.*

**7) Common mistakes.** Suggesting the global mean/mode as the baseline.

**8) Quick bullets.** Baseline = previous value, not the mean · reason = non-stationarity.

### 2E. Temporal evaluation methods ⭐

**1) Beginner explanation.** You must test on **the future**, never on the past. So hold out the **most recent** period as the test set, and validate using **time-ordered splits** (`TimeSeriesSplit`) where training is always earlier than validation.

**2) Exam meaning.** "Temporal holdout for model selection too" — not just the final test.

**3) Key terms.** Out-of-time split, `TimeSeriesSplit`, temporal holdout.

**4) sklearn example.**
```python
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
ts = TimeSeriesSplit(n_splits=5)
grid = GridSearchCV(model, param_grid, cv=ts)   # train always before validation
```

**5) In the exam.** "What's done right / wrong?" → right: temporal *test* set; wrong: using *non-temporal* CV for model selection.

**6) Model answer structure.** *Future must never train the past → use time-ordered CV for selection AND a temporal final test.*

**7) Common mistakes.** Temporal test set but random CV for tuning (still leaks).

**8) Quick bullets.** Most recent = test · `TimeSeriesSplit` for tuning · train always earlier than validate.

### 2F. Why random train-test split is DANGEROUS for time series ⭐⭐ (favourite question)

**1) Beginner explanation.** A random split can put a **future** point in training and a **past** point in testing — impossible in real life. Worse, **global events** (like COVID lockdown) leak: if some lockdown weeks are in training, the model "already knows" lockdowns exist when predicting other lockdown weeks in the test set, so it looks better than it ever could in reality.

**2) Exam meaning.** Explain **information leakage via global events** clearly.

**3) Key terms.** Information leakage, global events, look-ahead.

**5) In the exam.** "Pre+post-COVID data, random split — explain the leakage, its consequence, and why." (4 marks.)

**6) Model answer structure.** *Random split mixes future into training → before the first lockdown a real model couldn't foresee it, but CV gives it future lockdown info → reported performance is over-inflated and won't hold on truly new data.* Fix: temporal holdout.

**7) Common mistakes.** Saying only "it's not random" without the *future-leaks-into-past* mechanism.

**8) Quick bullets.** Random split = future trains the past · global events (COVID) leak · score inflated · fix = temporal split.

> **ARIMA vs global Random Forest (bonus, often asked):** Per-series **ARIMA** can't use cross-series info or extra (exogenous/global) features. A **global Random Forest with lagged features** *can* borrow strength across all series and use non-temporal features → often better, especially as you add sign-up info.

---

## TOPIC 3 — Applying Models (Bias–Variance & Diagnosis) ⭐

### 3A. The four error situations

**1) Beginner explanation.** Compare training error and test error to diagnose the model:

| Train error | Test error | Diagnosis | What it means | What to do |
|---|---|---|---|---|
| **Low** | **High** | **Overfitting (high variance)** | Memorised training noise | Reduce complexity, more data, regularise |
| **High** | **High** | **Underfitting (high bias)** | Model too simple / bad features | Increase complexity, better features |
| Low | Low | Good model | Generalises well | Ship it |
| High | Low | (rare/weird) | Usually a data/split bug | Investigate |

**2) Exam meaning.** Read the two numbers → name bias or variance → prescribe the fix.

**3) Key terms.** Bias (error from being too simple), Variance (error from being too sensitive to the training set), `train_error`, `test_error`.

**4) Example.** Linear SVM: `train_error` high and `test_error` twice as high → (a) increase complexity (go RBF) → expect train error to drop; (b) add data → expect test error to move closer to train error.

**5) In the exam.** "Model does great on train, poorly on validation — first thing to try?" → **reduce complexity** (then justify why not 'more data' = cost, why not 'change to regressor' = wrong problem type).

**6) Model answer structure.** *Read errors → bias or variance → 2–3 concrete fixes → predicted effect on each error.*

**7) Common mistakes.** Confusing bias and variance; "add more data" to fix *high bias* (it won't — the model is too simple).

**8) Quick bullets.** Low train+high test = overfit/variance → simplify · High both = underfit/bias → complexify · gap = variance.

### 3B. Learning curves

**1) Beginner explanation.** A **learning curve** plots error **as the training-set size grows**. Train and validation curves should **converge** as data increases.
- **Big gap that stays** → high **variance** (overfitting) → more data / regularise.
- **Both curves high and flat (converged)** → high **bias** → the model can't improve with more data; change the model/features.

**2) Exam meaning.** Diagnose from the shape; know it's about **data size**, not training time.

**3) Key terms.** Convergence, plateau, model limitation vs data limitation.

**5) In the exam.** "Does adding data help?" Use the curve: converged-and-high = no (bias); big-gap = yes (variance).

**6) Model answer structure.** *Look at gap and height → bias vs variance → data helps only if it's variance.*

**7) Common mistakes.** Confusing the learning curve (x = data size) with the training graph (x = epochs).

**8) Quick bullets.** x-axis = training-set size · gap = variance (more data helps) · both high = bias (more data won't).

### 3C. Deciding what to do when performance is bad (playbook)

1. Check the **error pattern** (3A). 2. **Underfit?** → more complex model, better/more features, less regularisation. 3. **Overfit?** → simpler model, more data, regularisation (dropout/L1/L2/early stopping). 4. Check **preprocessing** (scaling, encoding, leakage). 5. Check the **metric** (balanced accuracy on imbalanced data). 6. Check **features** (curse of dimensionality, weak features). 7. Try a **different model class** as a last resort.

---

## TOPIC 4 — Support Vector Machines (SVM) ⭐⭐

### 4A. What an SVM is

**1) Beginner explanation.** An SVM draws the **best separating line/boundary** between classes — the one with the **biggest margin** (widest gap) to the nearest points. Those nearest points are the **support vectors**; only they define the boundary.

**2) Exam meaning.** SVM = max-margin classifier; with kernels it draws non-linear boundaries.

**3) Key terms.** Margin, support vectors, hyperplane, soft margin, kernel.

**5) In the exam.** "What is an SVM?", "what extra assumption does a linear SVM add over logistic regression?" → **it maximises the margin** (controlled by `C`, trading off training misclassification).

**8) Quick bullets.** Max-margin boundary · support vectors define it · kernels → non-linear.

### 4B. Primal vs Dual ⭐⭐

**1) Beginner explanation.** Two equivalent ways to solve the SVM maths.
- **Primal:** works in the **feature space**. Training `O(d²n)` → cheap when **features d are few**, even if points n are huge.
- **Dual:** works in terms of **data points / support vectors**. Training `O(n²d)` → struggles when n is huge, but is **more robust to many features (curse of dimensionality)** and **enables the kernel trick** (non-linear boundaries).

**2) When to use which.**
- **Primal:** small `d`, very large `n`, and you only need a linear boundary / computation is the concern.
- **Dual:** very large `d` (many features), you need non-linear kernels, and `n` is manageable.

**3) Numbers to memorise.** Primal `O(d²n)`; Dual `O(n²d)`.

**5) In the exam.** "1000 features, 2000 points — primal or dual? Why? What's an alternative?" → Dual (robust to high d, allows kernel); alternative = kNN, or primal if compute is the worry.

**6) Model answer structure.** *State both complexities → compare to this dataset's n and d → pick → note kernels (dual only).*

**7) Common mistakes.** Swapping the complexities; thinking primal can use kernels (it's the dual that enables them).

**8) Quick bullets.** Primal O(d²n) loves small d · Dual O(n²d) loves small n + many features + kernels.

### 4C. Why SVM needs scaling/preprocessing ⭐

**1) Beginner explanation.** SVMs use **distances** to find the margin. If one feature is in millions (income) and another in single digits (age), the big-scale feature dominates the distance and the boundary is distorted. So we **standardise** every feature first. (Random Forests split one feature at a time, so they **don't** need scaling — a classic compare question.)

**2) Exam meaning.** "Why scale for SVM but not RF?" — distance-based vs split-based.

**5) In the exam.** Direct question + a Section II violation if scaling is missing.

**7) Common mistakes.** Saying "the kernel trick removes the need to scale" — **false**, you still scale.

**8) Quick bullets.** SVM = distance-based → must standardise · RF = splits → no scaling needed · kernel trick ≠ scaling.

### 4D. How C and kernel/gamma affect performance ⭐⭐

**1) Beginner explanation.**
- **C** = penalty for misclassifying training points. **High C** → small margin, fits training hard → **risk of overfitting**. **Low C** → large margin, more tolerant → simpler, may underfit.
- **gamma (RBF only)** = how far one point's influence reaches. **High gamma** → tiny bumps around each point → very wiggly boundary, **overfits** (acts like 1-NN). **Low gamma** → wide smooth influence → behaves almost **linear**.
- **Kernel:** `linear` for high-d / likely-linear data; `RBF` for non-linear data.

**2) Matching cheat (very common question):**
| Data property | First try |
|---|---|
| Noisy **and** non-linear | RBF, **low C** (big margin, tolerate noise), high-ish gamma — but keep C low to avoid fitting noise |
| Clean, shape unknown | **Linear**, high C (start simple, low noise so push margin) |
| Clean, non-linear, low complexity | RBF, **high C**, **low gamma** (smooth, simple curve) |

**3) Key terms.** Soft margin, overfitting, RBF, gamma.

**4) sklearn example.** `param_grid = {'C':[0.1,1,10], 'gamma':[0.01,0.1,1], 'kernel':['rbf']}` then `GridSearchCV`.

**5) In the exam.** "Is trying large gamma on noisy data a good idea?" → **No**, it overfits the noise (becomes 1-NN-like).

**6) Model answer structure.** *Map noise→C, complexity→gamma/kernel → state expected overfit/underfit.*

**7) Common mistakes.** Varying gamma on a **linear** kernel (no gamma); thinking high C = simpler.

**8) Quick bullets.** High C = overfit risk · high gamma = overfit/wiggly · low gamma ≈ linear · noisy data → don't crank gamma.

### 4E. What to change to adjust SVM performance

Underfitting → raise C, raise gamma (or switch to RBF). Overfitting → lower C, lower gamma (or switch to linear). Too slow with many features → feature selection / dimensionality reduction (cuts the `d²` term in primal). Multi-class → wrap in One-vs-Rest. Always scale first.


---

## TOPIC 5 — Causal Inference ⭐

### 5A. What causal inference means

**1) Beginner explanation.** Normal ML finds **correlation** ("when X is high, Y tends to be high"). Causal inference asks the harder question: **if I *change* X, will Y change?** Prediction ≠ causation. Ice-cream sales correlate with drownings, but ice cream doesn't cause drowning (hot weather causes both).

**2) Exam meaning.** To claim "X causes Y" you need extra information (a causal graph) or an experiment (A/B test) — you cannot get it from prediction accuracy or permutation importance.

**3) Key terms.** Correlation vs causation, treatment (T), outcome (Y), confounder, unconfoundedness.

**5) In the exam.** "What extra info do you need to know if product position *causes* sales change?" → **the causal graph** (or run an **A/B test**).

**8) Quick bullets.** Prediction ≠ causation · need a causal graph OR an experiment · permutation importance ≠ causal.

### 5B. Counterfactual

**1) Beginner explanation.** A **counterfactual** is the "what if" world that never happened: *what would this customer's spend have been if we had NOT sent the voucher?* We can only ever observe **one** reality per person (they got the voucher OR they didn't), so the other outcome must be **estimated**. This is the "fundamental problem of causal inference."

**2) Exam meaning.** Counterfactual = the unobserved alternative outcome; causal effect = observed − counterfactual.

**3) Key terms.** Potential outcomes Y(T=1) and Y(T=0); counterfactual = the one you didn't see.

**8) Quick bullets.** Counterfactual = the unseen "what if" · we observe only one outcome · estimate the other.

### 5C. ATE vs ATT ⭐

**1) Beginner explanation.**
- **ATE (Average Treatment Effect):** the average effect of the treatment **if you applied it to the *whole population*.**
- **ATT (Average Treatment Effect on the Treated):** the average effect **only for those who actually got the treatment.**

They differ when the treated group isn't representative of everyone (e.g. you only gave vouchers to already-loyal customers — their response isn't the same as a random person's).

**2) Exam meaning.** Define both; know ATT is easier to estimate (matching the treated to similar untreated), ATE needs more.

**3) Key terms.** Treatment, population vs treated subgroup.

**8) Quick bullets.** ATE = whole population · ATT = only the treated · equal only if treated ≈ representative.

### 5D. Simpson's Paradox ⭐ (common)

**1) Beginner explanation.** A trend that appears in the whole data **reverses** when you split into subgroups, because a **hidden confounder** wasn't accounted for. *Example:* overall "more daily exercise → more junk food", but within each subgroup it's the opposite — the confounder (e.g. age/course) was driving it.

**2) Exam meaning.** Identify it from a plot; say what wrong conclusion you'd draw; say what causes it.

**3) Key terms.** Confounding variable, subgroup reversal.

**5) In the exam.** "What is this an example of? When is it an issue? What happens?" → Simpson's paradox; an issue when the **confounder is unmeasured**; the **direction of the relationship is reported incorrectly**.

**6) Model answer structure.** *Relationship flips across subgroups → annotate groups on the graph → name the missing confounder → state the wrong conclusion avoided.*

**7) Common mistakes.** Calling it "just noise"; not naming the confounder.

**8) Quick bullets.** Trend reverses in subgroups · cause = hidden confounder · risk = wrong direction reported.

### 5E. DAGs and how they help ⭐

**1) Beginner explanation.** A **DAG (Directed Acyclic Graph)** is a diagram of arrows showing which variable affects which. It encodes **domain knowledge**. The important part is the **missing arrows** — a missing edge means "no effect / conditional independence" (this is testable).

**2) How DAGs encode conditional dependencies & find the adjustment set.** If a variable does **not** connect to the outcome, you **don't need to control for it**. So the DAG tells you the **minimum adjustment set** — the smallest group of variables you must control/stratify on to remove confounding (under the unconfoundedness assumption).

**3) Key terms.** Directed (arrows), Acyclic (no loops), edge = dependence, missing edge = independence, minimum adjustment set, unconfoundedness.

**5) In the exam.** "What is a DAG? How does it help identify the variables to adjust for?"

**6) Model answer structure.** *DAG = arrows of cause from domain knowledge → missing edges = independence → only variables linked to the outcome need adjusting → that's the minimum adjustment set.*

**7) Common mistakes.** Saying DAGs are learned automatically from data (they're mainly specified by domain knowledge); thinking you must adjust for *every* variable.

**8) Quick bullets.** DAG = arrows of effect · missing edge = independence · gives the minimum adjustment set · assumes unconfoundedness.

### 5F. Refutation testing ⭐

**1) Beginner explanation.** After estimating a causal effect, you **stress-test** it to check it's robust. The most common test: **add a random/dummy variable** that by construction causes nothing. If your causal estimate **barely changes**, good — that's expected. If it changes a lot, your method is unreliable. (Another: **placebo treatment** — replace the real treatment with a fake one; the effect should drop to ~0.)

**2) Exam meaning.** Refutations = evidence the estimate is trustworthy; they **test assumptions** (like unconfoundedness).

**3) Why a random/dummy variable shouldn't change the estimate.** It has no real causal link, so a sound method should ignore it and return almost the same effect. A big change signals the model is picking up noise/instability.

**5) In the exam.** True/false: "Refutations test modelled assumptions" → **True**.

**6) Model answer structure.** *Refutation = robustness check → add a random common cause / placebo → estimate should stay ~same (or drop to 0 for placebo) → confirms robustness.*

**8) Quick bullets.** Refute = stress-test the estimate · add a dummy cause → effect should not move · placebo → effect → 0.

---

## TOPIC 6 — Testing & Model Choice ⭐⭐

### 6A. Cross-validation

**1) Beginner explanation.** Instead of one lucky/unlucky validation split, **k-fold CV** splits the training data into k parts, trains on k−1 and validates on the last, rotating k times, then averages. This gives a **stable** estimate of how well a setting generalises — used to **tune meta-parameters**.

**2) Exam meaning.** CV sets meta-parameters (which control complexity) and guards ordinary overfitting; the average removes "lucky split" effects.

**3) Key terms.** k-fold, `StratifiedKFold` (imbalanced), `TimeSeriesSplit` (temporal), meta-parameter.

**4) sklearn example.** `GridSearchCV(model, param_grid, cv=StratifiedKFold(5), scoring='balanced_accuracy')`.

**8) Quick bullets.** CV = rotate folds, average · tunes complexity · stratify if imbalanced · time-split if temporal.

### 6B. train_test_split, GridSearchCV, and the correct order ⭐

**The correct, full procedure (memorise the order):**
1. `train_test_split` → hold out an **untouched test set** (`X_test`, `y_test`).
2. `GridSearchCV` on **`X_train` only** → repeatedly splits train into sub-train/validation for every parameter combo, averages, picks best (guards **ordinary overfitting**).
3. Refit best model on all of `X_train`, then **evaluate once on `X_test`** (guards **procedural overfitting** — the test set was never used to choose anything).

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                     stratify=y, random_state=42)
grid = GridSearchCV(pipe, param_grid, cv=5, scoring='balanced_accuracy')
grid.fit(X_train, y_train)
final_score = grid.score(X_test, y_test)   # touch the test set ONCE
```

### 6C. Hyperparameter / meta-parameter tuning

**1) Beginner explanation.** Meta-parameters are settings you choose *before* learning that **control model complexity** (SVM `C`, `gamma`; RF `max_depth`, `max_features`; NN layers/neurons/learning rate). You tune them with CV. (Note: RF `n_estimators` and `random_state` are **not** complexity controls — common trap.)

**5) In the exam.** "Which of these control complexity?" Pick `C`, `max_depth`, number of neurons — NOT `random_state`, NOT number of output classes, NOT the train/test split.

**8) Quick bullets.** Meta-params control complexity · tune with CV · n_estimators/random_state don't control RF complexity.

### 6D. Procedural overfitting vs ordinary overfitting ⭐⭐ (favourite)

| | Ordinary overfitting | Procedural overfitting |
|---|---|---|
| **When** | While **learning model parameters** (complexity too high) | While **choosing between models / meta-parameters** using the test set |
| **What's fit** | Noise in the **training** set | Noise in the **test/validation** set |
| **SVM example** | Learning the hyperplane placement too tightly | Tuning `C` (or picking SVM vs RF) by looking at the test score |
| **Consequence** | Bad generalisation | **Reported performance is higher than reality** |
| **Fix** | Reduce complexity, regularise, more data | Use a **validation set / CV** to choose, and a **separate untouched test set** for the final number |

**5) In the exam.** "You trained 10 RFs and 10 SVMs, scored all 20 on repeated hold-out, picked the best — what did you do wrong, the consequence, and the fix?" → **Procedurally overfit → expected performance over-reported → use a third independent test set to evaluate the chosen model.**

**8) Quick bullets.** Ordinary = fit train noise · Procedural = picked a model using the test set · fix = independent final test set.

### 6E. Why choose model X over Y (scenario reasoning)

Tie the choice to the data: **many features / high-d** → linear SVM or feature selection; **non-linear** → RBF SVM, RF, NN; **correlated lagged features** → tree models (robust to correlation) over SVM; **huge data + rare prediction** → cheap-train models; **need interpretability** → linear/trees over NN; **little data** → simple models (NOT a big NN); **only listen-time measured, multiple series** → global RF with lags over per-series ARIMA.

---

## TOPIC 7 — Neural Networks ⭐⭐

### 7A. Artificial neurons & shallow vs deep

**1) Beginner explanation.** An **artificial neuron** does: multiply inputs by **weights**, add a **bias**, then pass through an **activation function** to add non-linearity. Stack neurons into **layers**; stack layers into a network.
- **Shallow** = 1 hidden layer. **Deep** = many hidden layers (learns features hierarchically: edges → shapes → objects).

**2) Exam meaning.** Shallow nets can *theoretically* approximate any function (**universal approximation**) — but in practice: you need a *huge* number of neurons, you can't know the right size in advance, and training may get stuck in **local optima**. Deep nets learn richer features more efficiently.

**3) Key terms.** Weight, bias, activation, layer, universal approximation, local optima.

**5) In the exam.** "Shallow nets can approximate any function — why might you still not get the best model?" → can't know neuron/layer count in advance; huge parameter count (expensive); may hit local optima.

**8) Quick bullets.** Neuron = weighted sum + activation · shallow = 1 hidden layer · deep = many · universal approx ≠ easy to train.

### 7B. Activation functions

| Function | Use | Note |
|---|---|---|
| **ReLU** | Hidden layers (default) | Avoids vanishing gradients, fast |
| **Sigmoid** | Binary classification output | Squashes to (0,1) |
| **Softmax** | Multi-class output | Probabilities sum to 1 |
| **Linear** | Regression output | No squashing |
| Tanh | Older hidden layers | Can vanish gradients |

**Common trap (Section II):** sigmoid on a regression output (wrong), or relu/linear on a classification output (wrong).

### 7C. Training, gradient descent & its variants ⭐

**1) Beginner explanation.** Training = find weights that **minimise the loss**. **Gradient descent** repeatedly nudges weights downhill (opposite the gradient) by a step size = **learning rate**.

**2) Three variants:**
| Variant | Data per update | Pros / cons |
|---|---|---|
| **Batch GD** | All data | Stable but slow, memory-heavy |
| **Stochastic GD (SGD)** | 1 point | Fast, noisy, can escape local minima |
| **Mini-batch GD** | Small batch (e.g. 32) | Best of both — the standard |

**3) Key terms.** Loss function, learning rate, epoch, batch size, convergence.

**5) In the exam.** "Role of gradient descent?" → **minimise the loss by iteratively adjusting parameters.** True/false: "GD finds the global optimum for simple models like logistic regression but not NNs" → **False** (it's not guaranteed global even there in general; and the framing is wrong).

**8) Quick bullets.** GD minimises loss · batch=all/stable · SGD=1/noisy · mini-batch=standard · learning rate = step size.

### 7D. Vanishing (and exploding) gradients ⭐⭐

**1) Beginner explanation.** In deep nets, gradients are multiplied layer by layer going backwards. With saturating activations (sigmoid/tanh), they shrink toward **zero** → early layers **barely learn** → loss decreases very slowly / stalls. The opposite, **exploding gradients**, makes updates blow up.

**2) Symptoms.**
- **Vanishing:** loss decreasing very slowly; deep net no better than a shallow one.
- **Exploding:** unusually **large** loss jumps; loss becomes **NaN/Inf**; huge weight updates.

**3) Fixes for vanishing:** use **ReLU**, **better weight initialisation** (He/Glorot), **batch normalisation**, residual connections.

**5) In the exam.** "Loss decreases very slowly — causes?" (learning rate too small, poor scaling, vanishing gradients, too little data). "Exploding gradients — what tipped you off?" (huge loss changes, NaN/Inf loss, huge weight updates, non-decreasing loss).

**8) Quick bullets.** Vanishing = gradients→0, early layers stall → ReLU/He init/batch-norm · Exploding = NaN loss, huge updates.

### 7E. What to do when NN performance is bad + regularisation ⭐

**1) Beginner explanation.** First diagnose with the **training graph** (below). If **overfitting**, reduce complexity / regularise. If **underfitting/stalling**, check vanishing gradients, learning rate, scaling, more epochs.

**2) Regularisation techniques (reduce overfitting):**
- **Early stopping** — stop when **validation** error starts rising.
- **Dropout** — randomly switch off neurons during training.
- **L1 / L2 weight penalties**, **max-norm**.
- **Fewer layers / fewer neurons.**
- **Data augmentation** — create realistic new training examples (more *true* variation → params fit signal not noise).
- **Transfer learning / unsupervised pretraining / using a pretrained net** (when data is small).

**Combos that go together:** e.g. *dropout + early stopping*, or *reduce layers + data augmentation*.

**5) In the exam.** "Network overfitting — list 3 ways to reduce complexity; name 2 you can combine." Also: "If little data, what can you do instead of training from scratch?" → reuse a pretrained network / data augmentation.

**8) Quick bullets.** Overfit → dropout, early stopping, L1/L2, fewer layers, augmentation · little data → pretrained net / augment.

### 7F. Interpreting training graphs vs learning curves ⭐ (subtle, examined)

| | **Training graph** | **Learning curve** |
|---|---|---|
| **x-axis** | **Epochs / iterations** (training time) | **Training-set size** |
| **Shows** | Loss going down as the model trains | Error as you give the model more data |
| **Overfitting sign** | Validation error turns **upward** while training error keeps falling → use **early stopping** | Persistent **gap** between train and validation curves |
| **Connection** | The error values at the *final* iteration (e.g. x=100) become **one point** on the learning curve, at that training-set size | Made of many such end-of-training points |

**5) In the exam.** "What does the x-axis represent and why is it different from a learning curve?" / "Would you use the model at epoch 100?" → No, it has overfit by then; use early stopping. "Does the graph suggest fewer layers?" → Yes, fewer layers = less complexity = less overfitting.

**8) Quick bullets.** Training graph x=epochs · learning curve x=data size · val curve rising = overfit = early stop.

### 7G. AdaGrad and Adam optimizers

**1) Beginner explanation.** Smarter versions of gradient descent that **adapt the learning rate** automatically.
- **AdaGrad:** gives each parameter its own learning rate, shrinking it for frequently-updated params. Downside: the rate can shrink **too much** and stall.
- **Adam:** combines adaptive rates **+ momentum** (remembers past gradients). Fast, robust — the **default** choice today.

**8) Quick bullets.** AdaGrad = per-param adaptive rate (can decay too far) · Adam = adaptive + momentum, default.

### 7H. Foundation models (conceptual) ⭐

**1) Beginner explanation.** A **foundation model** is a (usually neural) model **pre-trained on huge general data** so it can be **adapted to many tasks** (e.g. large language models). You reuse it instead of training from scratch.

**2) Benefits.** Versatile across tasks; **saves development time/resources/data**.

**3) Drawbacks.** May **not use all your domain-specific features**; **inherits biases** from its training data; risk of **data poisoning / manipulation** in the pretraining data.

**4) Ways to customise.** **Fine-tuning** (continue training on your data), **prompt engineering**, **RAG** (retrieval-augmented generation). *(Not: hand-editing weights, or arbitrarily adding neurons/layers by "domain knowledge".)*

**5) In the exam.** "Best description?", "benefits?", "drawbacks?", "ways to customise?", and "it's overfitting on a small fine-tuning set — what helps?" → data augmentation, dropout, early stopping, **freezing layers**.

**8) Quick bullets.** Pretrained + adaptable · saves time/data · inherits bias · customise via fine-tune / prompt / RAG.

---

## TOPIC 8 — Variable Importance & Feature Understanding ⭐⭐ (always Question 1)

### 8A. Feature importance (permutation / MDA) ⭐

**1) Beginner explanation.** How much does each feature matter to the model? **Permutation importance** shuffles one feature's values and measures how much performance **drops** — bigger drop = more important.

**2) Reading the value.**
- For a **classifier** (accuracy): a score of **0.2 = a 20% drop in accuracy** when that feature's information is disrupted.
- For a **regressor** (MSE): a score of **0.2 = a 0.2 increase in MSE**.

**3) Why scores can change on retraining:** locally-optimal models, **correlated features sharing information**, and interaction effects, if the random seed isn't fixed.

**5) In the exam.** "Permutation importance = 0.2 — what does it mean?" (give both the accuracy and MSE versions). "Can permutation importance give causal effect?" → **No.** "Does it show importance *in reality* or *in this model*?" → **only in this learnt model.**

**8) Quick bullets.** Permutation = shuffle → measure performance drop · 0.2 acc = 20% drop · 0.2 reg = +0.2 MSE · model-specific, not causal.

### 8B. Univariate / k-best feature selection & its limits ⭐

**1) Beginner explanation.** **Univariate selection** scores each feature **on its own** (vs the target) and keeps the top ones — very **fast**, great for cutting huge feature sets quickly. **k-best (RFE-style)** = build model, drop the worst feature, rebuild, repeat until k remain.

**2) Big limitation.** Both can **miss interactions**: a feature that's useless alone but powerful **combined** with another gets dropped. So dropping low-univariate-score features can make the model **worse**. k-best is **greedy**, so it's **not guaranteed** to find the optimal subset.

**5) In the exam.** "You dropped low-univariate features and performance fell — why?" → **interaction effects weren't measured.** "Is k-best guaranteed optimal?" → **No, it's greedy (interactions).** "Cheaper alternatives to k-best?" → univariate selection; remove several features per round.

**8) Quick bullets.** Univariate = fast, per-feature, misses interactions · k-best = greedy, not optimal · use univariate for huge data + quick cut.

### 8C. Feature selection vs feature extraction ⭐

| | **Feature selection** | **Feature extraction** |
|---|---|---|
| **What** | **Keep a subset** of original features | **Create new combined** features (e.g. PCA, topics) |
| **Interpretability** | Keeps original meaning; VIM still interpretable | New features can be harder to interpret |
| **Collection cost** | **Reduces** which features you must collect | Still needs all originals to compute |
| **Choose when** | You want to cut **collection cost** / keep interpretability | You want to compress shared information / fewer dimensions |

**5) In the exam.** "Company only cares about reducing collection cost — selection or extraction first?" → **Selection** (extraction still needs all originals).

**8) Quick bullets.** Selection = pick originals (cheaper to collect) · Extraction = build new features (compresses, less interpretable).

### 8D. PDP, ICE — what they show ⭐

**1) Beginner explanation.**
- **ICE (Individual Conditional Expectation):** for **one data point**, vary one feature across its range (holding everything else fixed) and plot how the prediction changes. One **grey line per data point**.
- **PDP (Partial Dependence Plot):** the **average** of all those ICE lines — the **dark centre line**. The **dots** are each point's original prediction at its real value.

**2) Reading the plot.** Grey lines = per-point effect of varying the feature (others fixed); centre line = average effect; dots = original predictions.

**5) In the exam.** "What do the grey lines / centre line / dots represent?" (exact wording above earns the marks.)

**8) Quick bullets.** ICE = one line per point (vary 1 feature, others fixed) · PDP = average of ICE lines · dots = original predictions.

### 8E. SHAP ⭐⭐

**1) Beginner explanation.** SHAP shows, **per data point**, how much **knowing each feature** pushed the prediction up or down — giving both **magnitude AND direction**. It fairly splits credit among features.

**2) Key advantages (vs permutation):** shows **direction** (not just magnitude); per-data-point explanation.

**3) Watch-outs with correlated features.** With correlated inputs, the model may pick one of them during training; SHAP can then attribute importance to whichever was used — so two models (two stores) can show **different features** simply because they **selected differently among correlated features** (or the populations genuinely differ).

**5) In the exam.** "Justify choosing SHAP" → magnitude **and** direction; per-observation. "Two stores' SHAP plots differ — why?" → models selected differently among correlated features / populations differ. "Read this SHAP plot for alcohol" → e.g. *higher alcohol → higher predicted quality*, and *alcohol is the most predictive feature*.

**8) Quick bullets.** SHAP = per-point, magnitude + direction · sensitive to which correlated feature the model used · not causal.

### 8F. MCR & Rashomon sets ⭐

**1) Beginner explanation.** There's rarely ONE best model — many different models can be **almost equally good**. That set is the **Rashomon set**. **MCR (Model Class Reliance)** measures how important a feature is **across that whole set of good models**, not just one — so it tells you importance **"in reality"** rather than "in one learnt model."
- **MCR+** = the *most* a feature could matter in any good model. **MCR−** = the *least*.
- If a feature has **MCR+ near zero**, it's **never important in any good model** → safe to remove.

**5) In the exam.** "Match technique to scenario": *"understand importance as expressed in reality, not in one learnt model"* → **MCR**. "Remove features that in **no scenario** contribute" → MCR+ near zero (also Boruta for all-relevant). "Remove features but don't care which (interactions considered)" → **RFE**.

**8) Quick bullets.** Rashomon = many equally-good models · MCR = importance across all of them (reality) · MCR+≈0 → safe to drop.

### 8G. Technique-to-scenario matching (memorise this table)

| Technique | Best when… |
|---|---|
| **Univariate VIM** | Huge data, low compute — quick rough cut of features |
| **ICE plot** | See the effect of varying **one** variable per data point (joint = 2D PDP) |
| **MCR** | Importance **in reality** (across all good models), not one model |
| **RFE (recursive elimination)** | Remove unneeded features, **respecting interactions**, don't care which go |
| **Boruta** | Keep **all relevant** features (features that matter in *some* scenario) |
| **SHAP** | Per-observation explanation with **direction** |
| **Permutation importance** | Relative importance **within the learnt model**, variable selection |


---

## 📖 PART 6 — CHEAT SHEET OF DEFINITIONS (one-liners)

- **Overfitting:** model fits the **training noise** → low train error, high test error.
- **Underfitting:** model too simple → high train AND high test error.
- **Bias:** error from the model being too simple. **Variance:** error from being too sensitive to the training set.
- **Procedural overfitting:** choosing the model/meta-params using the **test set** → inflated reported performance.
- **Data leakage:** test information sneaks into training (e.g. scaling before split) → over-optimistic scores.
- **Cross-validation:** rotate train/validation folds and average → stable tuning of meta-parameters.
- **Meta-parameter (hyperparameter):** a setting that controls **model complexity**, tuned with CV.
- **Pipeline:** preprocessing + model in one object so transforms fit on training data only.
- **MCAR / MAR / MNAR:** missing by pure chance / explained by other observed features / depends on the missing value itself.
- **One-hot encoding:** turn a nominal category into 0/1 columns (no fake order).
- **Standardisation:** rescale features to mean 0, std 1 (needed for distance-based models like SVM/kNN).
- **Class imbalance fix:** `class_weight='balanced'` or move the decision threshold; evaluate with **balanced accuracy**.
- **Balanced accuracy:** average of per-class recall (fair metric for imbalanced data).
- **Recall (sensitivity, TPR):** TP / (TP + FN) — of the actual positives, how many you caught.
- **Specificity (TNR):** TN / (TN + FP) — of the actual negatives, how many you correctly rejected.
- **Precision:** TP / (TP + FP) — of predicted positives, how many were right.
- **SVM:** maximum-margin classifier; support vectors define the boundary.
- **Primal SVM:** O(d²n), good for small d / huge n. **Dual SVM:** O(n²d), robust to high d, enables kernels.
- **C (SVM):** misclassification penalty — high C = small margin = overfit risk.
- **gamma (RBF):** reach of each point — high gamma = wiggly/overfit (≈1-NN), low gamma ≈ linear.
- **Kernel trick:** draw non-linear boundaries by implicitly mapping to higher dimensions (still need scaling).
- **Lagged feature:** a past value used as an input column.
- **Tumbling window:** fixed, non-overlapping chunks (less correlation). **Expanding window:** cumulative (fewer edge effects).
- **Temporal baseline:** predict the **previous value** (persistence), better than the mean for drifting data.
- **Temporal standardisation:** scale all lags of one variable with a single shared mean/std.
- **Artificial neuron:** weighted sum of inputs + bias → activation function.
- **Activation:** ReLU (hidden), softmax (multi-class out), sigmoid (binary out), linear (regression out).
- **Gradient descent:** minimise loss by stepping downhill; learning rate = step size.
- **Batch / SGD / mini-batch:** update using all data / 1 point / a small batch (mini-batch is standard).
- **Vanishing gradients:** gradients shrink to ~0 in deep nets → early layers stall (fix: ReLU, He init, batch-norm).
- **Exploding gradients:** updates blow up → NaN/Inf loss, huge weight jumps.
- **Early stopping:** stop when **validation** error rises (a regulariser).
- **Dropout:** randomly disable neurons during training (regulariser).
- **Data augmentation:** create realistic new training examples to reduce overfitting.
- **AdaGrad:** per-parameter adaptive learning rate (can decay too far). **Adam:** adaptive + momentum (default).
- **Foundation model:** large pretrained model adaptable to many tasks (fine-tune / prompt / RAG).
- **Permutation importance:** drop in performance when a feature is shuffled.
- **Univariate VIM:** scores each feature alone — fast but misses interactions.
- **RFE:** recursively build → drop worst feature → rebuild (respects interactions, greedy).
- **Boruta:** all-relevant selection (keep every feature useful in some scenario).
- **SHAP:** per-point contribution of knowing each feature — magnitude + direction.
- **ICE plot:** vary one feature for one data point (others fixed). **PDP:** average of the ICE lines.
- **MCR (Model Class Reliance):** feature importance across the whole **Rashomon set** of near-best models.
- **Rashomon set:** the set of models that are all almost-equally good.
- **Causal inference:** estimating the effect of *changing* X on Y (not mere correlation).
- **Counterfactual:** the unobserved "what if" outcome.
- **ATE:** average treatment effect over the **whole population**. **ATT:** average effect on the **treated** only.
- **Confounder:** a hidden variable affecting both treatment and outcome.
- **Simpson's paradox:** a relationship reverses across subgroups due to an unmeasured confounder.
- **DAG:** directed acyclic graph of causes; **missing edges = independence**; gives the **minimum adjustment set**.
- **Unconfoundedness:** assumption that all confounders are measured/controlled.
- **Refutation:** robustness check; adding a random/dummy cause should barely change the estimate.
- **A/B test:** randomised experiment → the gold standard for causal effect.
- **One-vs-Rest:** n binary classifiers, pick the highest probability (multi-class via binary).
- **Algorithmic complexity:** Big-O of training/prediction in n (points) and d (features).

---

## 📊 PART 7 — COMPARISON TABLES (all the ones you asked for)

### Train error vs Test error
| | Train error | Test error |
|---|---|---|
| Measured on | Data the model **learned from** | **Unseen** held-out data |
| Tells you | How well it **fit** training data | How well it **generalises** |
| Low train, high test | — | **Overfitting** |
| High train, high test | **Underfitting** | **Underfitting** |
| Goal | Low | Low **and close to train** |

### Overfitting vs Underfitting
| | Overfitting | Underfitting |
|---|---|---|
| Cause | Complexity too high; fits noise | Complexity too low; misses signal |
| Train error | Low | High |
| Test error | High | High |
| Fix | Simplify, regularise, more data | More complex model, better features |
| AKA | High variance | High bias |

### Cross-validation vs Train-test split
| | Cross-validation | Train-test split |
|---|---|---|
| What | Rotate k folds, average | One single split |
| Used for | **Tuning** meta-parameters | **Final** generalisation estimate |
| Stability | High (averaged) | Depends on the one split (luck) |
| Cost | Higher (k fits) | Cheap |
| Temporal version | `TimeSeriesSplit` | Most-recent block as test |

### Feature selection vs Feature extraction
| | Selection | Extraction |
|---|---|---|
| Output | Subset of **original** features | **New combined** features (e.g. PCA) |
| Interpretability | High (originals kept) | Lower (transformed) |
| Collection cost | **Reduced** | Still needs all originals |
| Use when | Cut cost / keep meaning | Compress shared info / reduce dimensions |

### Recall vs Specificity
| | Recall (Sensitivity, TPR) | Specificity (TNR) |
|---|---|---|
| Formula | TP / (TP + FN) | TN / (TN + FP) |
| Question | Of actual **positives**, how many caught? | Of actual **negatives**, how many correctly rejected? |
| High when | Few false negatives | Few false positives |
| Matters when | Missing a positive is costly (e.g. disease) | False alarms are costly |

### Primal vs Dual SVM
| | Primal | Dual |
|---|---|---|
| Training complexity | **O(d²n)** | **O(n²d)** |
| Best when | Few features d, huge n | Many features d, manageable n |
| Curse of dimensionality | Worse | More robust |
| Kernels (non-linear) | No | **Yes** (kernel trick) |
| Pick if | Computation/linear is fine | Need non-linear / very high d |

### Shallow vs Deep neural networks
| | Shallow (1 hidden layer) | Deep (many layers) |
|---|---|---|
| Function approximation | Can approximate any function (in theory) | Learns hierarchical features efficiently |
| Practical issue | Needs huge neurons; size unknown; local optima | Vanishing gradients, more data/compute |
| Features | Hand-engineered help more | Learns features automatically |
| Use when | Simple problem / little data | Complex patterns, lots of data |

### PDP vs SHAP
| | PDP (with ICE) | SHAP |
|---|---|---|
| Granularity | ICE = per point; PDP = **average** | **Per data point** |
| Shows | Effect of **varying** a feature (others fixed) | Effect of **knowing** a feature's value |
| Direction | Yes (shape of curve) | Yes (push up/down) |
| Correlated features | Can show unrealistic combos | Attributes to whichever feature the model used |
| Causal? | No | No |

### ATE vs ATT
| | ATE (Average Treatment Effect) | ATT (…on the Treated) |
|---|---|---|
| Population | **Everyone** | **Only those treated** |
| Question | Effect if applied to all? | Effect on those who actually got it? |
| Estimation | Harder (needs whole-population assumptions) | Easier (match treated to similar untreated) |
| Equal when | Treated group ≈ representative of all | — |

### Bonus: Permutation importance vs SHAP vs MCR
| | Permutation | SHAP | MCR |
|---|---|---|---|
| Scope | One learnt model | One learnt model, per point | **All near-best models (Rashomon)** |
| Gives direction? | No | Yes | Range (MCR− to MCR+) |
| "Importance in reality"? | No | No | **Yes** |
| Handles correlation | Splits/duplicates poorly | Attributes to used feature | Captures across models |

---

## ✅ FINAL EXAM-DAY REMINDERS

1. **Answer shape for "why" questions:** name the issue → consequence → fix. Three marks, three parts.
2. **Section II:** scan top-to-bottom with the Part 4 checklist; each *distinct* violation = ~3 marks; don't repeat the same issue.
3. **Time series red flag:** if you see a **random split** or plain **StandardScaler** on lagged data → violation.
4. **Imbalanced red flag:** plain `accuracy`, no `class_weight`, plain `KFold` → violations.
5. **Procedural overfitting red flag:** the **test set** used to pick between models/params → violation.
6. **SVM:** memorise O(d²n) primal / O(n²d) dual, and C↑=overfit, gamma↑=overfit.
7. **NN output layer:** linear (regression), sigmoid (binary), softmax (multi-class) — and matching loss.
8. **Causal:** prediction ≠ causation; need a DAG or an A/B test.

*Good luck — you've got this. Read the high-priority list one more time before you sleep, and skim the cheat sheet in the morning.*

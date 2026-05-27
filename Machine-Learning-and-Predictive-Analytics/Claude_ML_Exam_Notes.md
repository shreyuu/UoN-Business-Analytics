# Machine Learning & Predictive Analytics — Exam Notes

**Module:** BUSI4373 / N14B78 — Machine Learning and Predictive Analytics  
**Exam date:** 4 June 2026 · 2 hours · in-person · closed book (handwritten notes allowed)  
**Structure:** Section I (all questions, ~70–75 marks) + Section II (choose 1 of 2 code-review questions, ~25 marks)

> The Section I topics are stable across years: (1) Feature Importance & Selection, (2) Model Comparison & Preprocessing, (3) SVMs, (4) Time Series, (5) Neural Networks, (6) Evaluation & Causal Inference. Section II is always a "find the bugs in this code" exercise — usually one temporal problem + one neural network problem.

---

## 0. The big-picture framework (everything connects to this)

Smith's core scaffolding for comparing/choosing models. Every exam answer ultimately maps back here.

**Differences in capabilities** (what the model *can* do, built-in or via processing):
- Handles missing values?
- Linear vs. non-linear decision boundaries?
- Robust to correlated features?
- Robust to irrelevant features?
- Handles input on arbitrary scales?
- Handles unbalanced classes?
- Binary vs. multi-class natively?
- Generates output class probabilities?
- Input types accepted (continuous, nominal, ordinal, binary)?

**Differences to know to use correctly:**
- Model structure & assumptions about the data
- Meta-parameters and what they control
- What are the learnt parameters
- How to deal with overfitting
- Approximate vs. optimal solution

**Efficiency:** training speed, prediction speed, amount of data required.

**Three goals of ML** (recur in answers):
1. Generalised predictive performance
2. Fairness
3. Understanding (model & phenomenon)

**Two types of ML problem:**
- **Traditional/observational:** P(y | x, z) — predict from observed inputs.
- **Causal:** P(y | do(x), z) — predict in a *hypothetical* world where we intervene.

---

# SECTION I

## 1. Feature Importance & Selection

### 1.1 Why care?
Two motivators (this exact pair has been asked):
1. **Understand the phenomenon** → understand how to *intervene*.
2. **Variable selection** → improve predictive quality (reduce curse of dimensionality, fewer local minima, lower data-collection cost, less feature drift).

### 1.2 Univariate / filter methods (VIM)
Rank features based on how they (individually) relate to the output: correlation, mutual information, variance threshold.

- **Quick & model-free.** Good for very large datasets where you need a fast cut.
- **Can miss relevant features that only matter in combination** (interactions). Example: A and B each predict y at baseline 50% alone, but together predict y with 100% accuracy — univariate VIM would score both as zero. *This is the classic XOR-style trap.*
- **Can keep redundant features.**

### 1.3 Model-based importance (intrinsic)
Each model has its own native measure:
- **Random Forest / trees:** mean decrease in impurity (Gini/info gain) — averaged over all trees, normalised to sum to 1.
- **Linear models:** absolute t-statistic on standardised coefficients.
- **Pros:** can incorporate the interactions the *model itself* captures; fast (free with training).
- **Cons:** model-specific; absolute values are in arbitrary units; relevance/redundancy may be misrepresented.

### 1.4 Permutation importance (MDA = Mean Decrease in Accuracy)
**The procedure:**
1. Train model, score on a test set → `baseline_score`.
2. Pick feature f. Randomly permute its values across data points (breaks the link to y).
3. Re-score the (already-trained) model → `permuted_score`.
4. MDA(f) = baseline_score − permuted_score. Repeat for each feature.

**Properties:**
- Easy to interpret.
- Applicable to any model.
- Investigates the importance of arbitrary feature *interactions* (those the model captures).
- More reliable if scored on a **held-out test set** (measures importance for *new* data — generalisation); scoring on training data only tells you about importance *in the model on data already seen*.

### 1.5 Hold-out / rebuilding importance
Hold a feature out, **rebuild** the model, score. Difference = importance.
- Directly simulates "what if I never had this feature?" — closer to phenomenon-level reasoning.
- Computationally expensive (one model per feature).
- **Cannot infer the effect of holding out multiple variables from individual hold-out scores** — you have to retrain with each subset.

### 1.6 The redundancy trap (a recurring exam point)
Consider features X and X' that are duplicates and predict Z perfectly together.
- Random Forest will use X in ~50% of trees, X' in the other 50%.
- **Permutation importance:** MDA(X) ≈ 0.5 × loss-when-X-used, MDA(X') ≈ similar. Looks unimportant.
- **Hold-out (rebuild):** drop X → model uses X', performance unchanged → MDA = 0. Drop X' → same. Both look unimportant.

**Lesson:** with correlated features, single-model importance lies. You can't tell from one model which is "the real" predictor — you may need MCR (see §1.10) or domain knowledge.

### 1.7 ICE plots vs. PDP vs. SHAP
| Tool | What it shows | Per data point? |
|---|---|---|
| **PDP** (Partial Dependence) | Average model response as feature varies | No — averaged |
| **ICE** (Individual Conditional Expectation) | Effect of varying the feature *for each data point* with all others held fixed | Yes |
| **SHAP** | Effect of *knowing* a feature's value on the model output, per data point — distributes credit fairly across features for the prediction | Yes |

- **ICE** shows *systematic variation* of the input variable while keeping others fixed → useful for seeing interactions visually (two-variable ICE plots).
- **SHAP** shows both **magnitude** and **direction** of effect per feature per prediction. Aggregate to global view. Unlike permutation, it can show direction.
- **SHAP plot interpretation** (e.g. the wine quality example): high alcohol → high SHAP (more red points on the positive side) means *higher alcohol increases predicted quality*; and the feature being at the top means *alcohol is the most predictive feature overall*.

### 1.8 Recursive Feature Elimination (RFE)
The three-step loop:
1. Build the model.
2. Compute a VIM and rank features.
3. Remove the worst feature; repeat.

Stop at the right point → result tells you about **one of many potential predictive relationships** (not THE truth — model dependent). Good for selecting "best k" with interaction awareness.

### 1.9 Boruta — "all relevant" selection
Goal: find *all* relevant features, not the smallest subset.
1. Duplicate each variable; permute the duplicates → "shadow features".
2. Train model (with permutation importance) on real + shadow features.
3. Record a "hit" each time the real feature beats its best shadow.
4. After many iterations, use the binomial distribution (with multiple-comparison correction) to mark features as confirmed-relevant, irrelevant, or tentative.
5. Remove confirmed-irrelevant features and repeat.
6. Stop when all features classified or iteration cap reached.

### 1.10 MCR — Model Class Reliance (Rashomon set)
**The motivation:** post-hoc VIM on a single model is arbitrary — different random seeds give different "important features" when features are correlated. We're explaining the model, not the phenomenon.

**Rashomon set:** the set of all models from a model class that achieve approximately the same performance (within ε).

For a feature v in model class C:
- **MCR−(C, v):** minimum MDA(v) over the Rashomon set — the *least* this variable is relied on across *any* equally-good model.
- **MCR+(C, v):** maximum MDA(v) over the Rashomon set — the *most* it could be relied on.

**Use cases:**
- MCR− ≈ 0 → some equally-good model exists that doesn't need this feature → can remove if you don't care which features carry the load.
- MCR+ ≈ 0 → in **no** good model is this feature important → safe to remove for sure.
- Pick from the Rashomon set: cheap-to-collect, more causal, actionable, or non-protected-attribute models.

### 1.11 Quick decision matrix (asked as a matching question)

| Scenario | Best tool |
|---|---|
| Lots of features, huge dataset, limited compute — quickly cut features | **Univariate VIM** |
| Understand joint effect of two variables | **2-variable ICE / PDP** |
| Understand importance of variables *in the phenomenon* (not in one model) | **MCR** |
| Remove features not needed for the best-performing model (interactions OK) | **RFE** |
| Remove features that in no scenario contribute | **Boruta** |
| Direction + magnitude of feature effect per prediction | **SHAP** |

### 1.12 Selection vs. extraction
**Selection** (pick a subset of original features): keep when collection cost matters, since you can stop collecting the dropped ones.
**Extraction** (PCA / autoencoder / NN layers): you still need all original features to compute the new ones, so it doesn't save collection cost. Use when you only care about predictive performance and want to compress representation.

---

## 2. Model Comparison, Evaluation & Preprocessing

### 2.1 The simulation principle
Evaluation is a **simulation of reality**. The test set simulates "data we wouldn't have known about if we started the task a month ago." If you violate "can't change things" after touching the test set, you no longer measure what you think you measure.

### 2.2 The three evaluation options (memorise these — they're the heart of every code-review question)

**Option 1 — Basic single split (with validation):**
```
Full data → Train / Test
Train → SubTrain / Validation
Tune meta-params on Validation, train final on full Train, evaluate on Test once.
```

**Option 2 — Cross-validation for meta-params, single test set:**
```
Full data → Train / Test
On Train: GridSearchCV with k-fold CV to pick best meta-params
Refit best model on full Train, evaluate on Test once.
```
This is the most commonly correct answer in practice. Use this first.

**Option 3 — Nested CV (outer + inner):**
```
Outer CV: gives an unbiased estimate of the *procedure's* performance
   For each outer fold:
     Inner CV (GridSearchCV) on outer-train → best meta-params → best model
     Score on outer-test
Report mean ± std of outer-test scores.
For deployment: retrain on all data with the chosen procedure.
```
Use when (a) data is precious and you want best estimate of generalisation, or (b) you want a confidence interval, not a single number.

### 2.3 Procedural overfitting (the most asked concept in Section I)
**Definition:** modelling noise in your *test set* by repeatedly using it to choose between many models.

**The classic violation:** running grid search separately for SVM and RF, picking the best of each on a test set, then comparing the two "best" models on the same test set and reporting the winner. **You've used the test set twice for selection → procedural overfitting → reported score is optimistic.**

**Fix:** use a third, independent held-out test set to evaluate the final selected model, OR run nested CV.

### 2.4 Why we retrain on all data after selection
Once meta-params are fixed, adding more data (i.i.d. sample) generally does **not** cause overfitting and **does** improve generalisation. So after Option 1/2 selection, retrain on the entire training+validation set with chosen meta-params before deploying. (For Option 3, retrain on ALL data with the chosen procedure.)

### 2.5 Meta-parameters — what they control & why CV
**Meta-parameters control model complexity.** CV selects the complexity that captures the generalisable relationship rather than noise — i.e. it picks the right point on the bias-variance tradeoff.

**Watch out (very-large-dataset pipeline question):**
```python
ss = StandardScaler()
rf = RandomForestRegressor()
pipe = Pipeline([('scaling', ss), ('model', rf)])
```
Two valid criticisms: (1) RF does not need scaling — it's based on splits, scale-invariant. (2) On a very large dataset, RF is expensive to train; consider a lower-complexity model first (Decision Tree, Linear regression) as baseline.

### 2.6 Standard ML preprocessing pipeline (in order)
1. **Splitting** — train/test split *first*, before anything else, to prevent leakage.
2. **Encoding categoricals** (one-hot, ordinal, target — see §2.9).
3. **Imputation** of missing values — *fit on train, transform test*.
4. **Scaling** (StandardScaler / MinMax) — *fit on train, transform test*.
5. **Optional:** feature selection / extraction.
6. **Model training.**

**Use a `Pipeline`** to wrap all the transformers + estimator so that during CV the fitting only sees the inner train fold — no leakage.

### 2.7 Missing data — the three regimes (MCAR / MAR / MNAR)
| Type | What it means | Detect by | Treat with |
|---|---|---|---|
| **MCAR** — Missing Completely At Random | Missingness independent of *all* variables (random glitch) | Often impossible to be sure; check no relationship with anything | kNN imputation, mean/median (deletion OK but wasteful) |
| **MAR** — Missing At Random | Missingness depends on *observed* variables (e.g. spend_to_date missing when visit_count=0) | Test conditional on observed features | Domain knowledge ("set to 0"), ML imputation conditioning on observed vars |
| **MNAR** — Missing Not At Random | Missingness depends on the *unobserved* value itself (e.g. high earners don't disclose income; older people don't disclose age) | Hardest — needs domain reasoning | Add an "unknown" category, or model the missingness mechanism |

**Worked example pattern:**
- postcode missing due to app glitch → MCAR → kNN imputation.
- gender missing in a non-trivial minority → MNAR (people choose not to disclose) → encode "unknown".
- spend_to_date missing because visit_count = 0 → MAR → domain knowledge says set to 0.

**Risks of imputation:**
- Don't expand the dataset with rows that depend on unknowns.
- Test data must be imputed using *training* stats only (no leakage).
- Deletion (drop rows) is OK for MCAR; for MAR/MNAR it biases the sample.

### 2.8 Why most algorithms can't handle missing values
- No concept of "NULL" in mathematics.
- Most algorithms place points in a geometric space — where do you put (calorie=5, exercise=UNKNOWN)?
- Decision trees CAN handle missing natively (surrogate splits / missing-as-its-own-branch), some other models can with extensions.

### 2.9 Categorical encoding decisions
| Categorical type | Encoder | Reason |
|---|---|---|
| **Nominal** (no order: gender, payment method) | One-hot encoding | LabelEncoder imposes false ordering → poor performance, esp. in linear / distance models |
| **Ordinal** (income bracket low/med/high) | Manual numeric / OrdinalEncoder | Preserves order |
| **High-cardinality** (postcode: 1.79M values) | Custom feature engineering — group, target-encode, or aggregate at coarser geography | One-hot would explode dimensionality |
| **Binary** | Direct 0/1 | Trivial |

**LabelEncoder on a nominal feature is one of the most common code-review violations.** It silently imposes an arbitrary order.

### 2.10 Scaling
- **Needed for:** distance-based (kNN), kernel methods (SVM with RBF/poly), gradient-based (NN, logistic regression), PCA.
- **Not needed for:** tree-based (Decision Tree, Random Forest, XGBoost) — they split on thresholds.
- **Fit on train only.** Scaling before train/test split is data leakage.
- Use `StandardScaler` (mean 0, std 1) for most continuous features. `MinMaxScaler` if you need bounded.

### 2.11 Algorithm efficiency (typical complexities to memorise)
| Model | Train | Predict |
|---|---|---|
| List-based kNN | O(1) | O(nd) |
| Tree-based kNN (KD-tree, Ball-tree) | O(n log n) | O(log n) |
| Linear SVM (primal) | O(d² n) | O(d) |
| Kernel SVM (dual) | O(n² d) | O(n_sv × d) |
| Random Forest | O(n log n × d × trees) | O(log n × trees) |

**The kNN classic question:** offline batch use, dataset grows daily, small number of predictions → **list-based kNN** (training is O(1), no need to rebuild the index each day; prediction is acceptable since infrequent). For real-time prediction or frequent queries → tree-based.

### 2.12 Stratified sampling
Use **StratifiedKFold** (not KFold) and `stratify=y` in train_test_split when:
- Classes are imbalanced.
- You want each fold's class distribution to match the full data.

Otherwise you risk a fold with very few minority-class examples → unstable scores.

### 2.13 Train/test split — `shuffle`
- `shuffle=True` (default): randomises before splitting. Use this **unless** your data has time ordering.
- `shuffle=False`: keeps order. Code-review violation: data ordered by some feature (e.g. contract_length) + shuffle=False → systematically biased split.
- **Temporal data:** shuffle is *wrong* — use temporal hold-out (see §4).

---

## 3. SVMs

### 3.1 Hyperplane intuition
A hyperplane in q dimensions = a vector **w** + an offset b. Decision rule: sign(**w·x** + b). It's the "fastest direction" between the two classes.

You never have to learn w explicitly in the dual formulation — you learn weights per data point (only the support vectors get non-zero weights).

### 3.2 The margin & the SVM trick
SVM picks **the hyperplane that maximises the margin** (gap between classes). This adds a "best neutral guess" assumption: place the boundary equidistant from both classes — when unsure, assume symmetric class density.

### 3.3 Soft-margin SVM and C
Real data is noisy → allow violations (slack variables ε_i):
- **Optimisation:** minimise `(1/margin) + C × Σ ε_i`.
- **C is a regularisation parameter** controlling the trade-off:
  - **High C** = high penalty on misclassification → **smaller margin**, fits closer to data → **more overfitting risk**. Less trust in the model assumption, more trust in the data.
  - **Low C** = tolerates more errors → **larger margin** → more regularised, *less* overfitting, possibly *underfitting*. More trust in the model assumption, less trust in the data.

### 3.4 Kernel trick & RBF
The decision rule depends only on dot products → replace dot products with a **kernel function** K(x, x') that implicitly maps to a higher-dimensional space *without computing the mapping*. Three points:
1. Selection of primal vs. dual depends on whether n or d is larger.
2. Dual is more robust to curse of dimensionality.
3. Non-linear SVMs via kernels.

**RBF intuition:** place a Gaussian over each data point with width inversely related to γ.
- **High γ** → narrow Gaussians → many isolated "islands" around each point → **overfit** (trusts data more, almost behaves like kNN with k=1).
- **Low γ** → wide Gaussians → very smooth boundary → behaves more like a **linear** SVM (so low γ → almost linear, *not* high γ as a common distractor says).

**Why default to RBF:**
- Subsumes linear (with right γ).
- Approximates sigmoid kernel with right γ.
- Fewer parameters than polynomial.
- Allows non-linearity.

### 3.5 When to pick which SVM kernel
| Situation | Kernel | Reason |
|---|---|---|
| d ≫ n (1000 features, 2000 points) | **Linear (primal)** | Data likely already linearly separable; cheaper |
| d ≪ n with non-linear data | **RBF** | Standard choice; subsumes linear |
| Lots of noise, non-linear | RBF, **low C**, **high γ** | Tolerate noise, allow flexibility (but careful with overfitting) |
| Little noise, possibly linear | **Linear, high C** | Trust data, no margin needed |
| Little noise, non-linear, low complexity | **RBF, high C, low γ** | Wide kernels with tight fit |

### 3.6 SVMs for multi-class (binary by design)
- **One-vs-Rest (OvR):** N binary classifiers, one per class. Predict argmax of their probability scores.
- **One-vs-One (OvO):** N(N−1)/2 binary classifiers. Vote.
- Either works; default in `sklearn.svm.SVC` is OvO. A correctly tuned SVM often beats RF on multi-class.

### 3.7 SVM is **globally optimal**
The optimisation is convex → **the optimiser always finds the global optimum**. So running it 100 times with the same X_train will give 100 *identical* scores. Pointless to do so for SVM. Doing it for RF (no seed) *is* meaningful — RF's randomness means each run differs.

### 3.8 Linear SVM vs. logistic regression
- Both linear, both regularised, both convex.
- LR penalises misclassifications via S-shaped log loss — outliers get bounded penalty close to 1.
- SVM hinge loss is linear — outliers attract penalty growing linearly with distance.
- **Linear SVM tends to win** if you're willing to tune C.

### 3.9 SVR (Support Vector *Regression*)
- Fits a centerline with an ε-tube; points inside the tube are "free" (no penalty).
- Outside the tube → linear penalty (controlled by C).
- **Common code-review error:** using `SVR` (regressor) for a *classification* problem. Use `SVC` for classification.

---

## 4. Time Series & Temporal Data

### 4.1 The two paradigms

**(a) Non-temporal problem with temporal features:**
- Fixed reference date. We're predicting a *current* property using *historical* (lagged) inputs.
- Example: predict region someone lives in *today* from their salary history over the last 5 years.
- A data point is a "thing" (person).

**(b) Temporal prediction problem:**
- Predicting a **future** value.
- A data point is a (thing, time) pair.
- The same physical thing can appear at many time points.
- Example: predict next month's spend given the last 3 months.

This distinction drives everything: when (a), random CV is still OK; when (b), random CV **fails** (information leakage).

### 4.2 Why random CV fails on temporal problems (two reasons)

**Reason 1 — Future info leaks into training:**
Random sampling can put future data points into training and past points into testing. In reality, when the model is deployed, we never have the future. So inflated scores.

**Reason 2 — Global events / shared temporal structure:**
Even within a single reference date setup, global events (recessions, COVID, Christmas) impart shared structure that the train and test sets both see — model "predicts" the crash because the held-out points share the same global state.

### 4.3 Lagged feature construction with windows
- **Tumbling window** — non-overlapping fixed-width chunks (e.g. week-1, week-2, week-3 each summed independently). **Less correlation** between lagged features.
- **Hopping / sliding window** — overlapping windows. More correlated features.
- **Expanding window** — chunk size grows (cumulative from start). Highly correlated lags.

**Tumbling windows create less correlated lagged features than expanding windows** — true statement.

### 4.4 Choice of arbitrary boundaries matters
The day boundary you pick (00:00 → 23:59 vs. 09:00 → 08:59) materially shifts which transactions fall in which bucket and can move features substantially. Always document and be aware.

### 4.5 Which features should you lag?
Lag a feature only if:
- It is naturally temporal (purchases, visits, spend, items bought).
- It is *expected to change* over your window size.

**Don't lag:**
- Non-temporal features (age has lag-version trivially = age − k months; usually pointless at fine granularity).
- Features with near-zero variation over the lag period (e.g. count_of_items_purchased at monthly granularity may be near-constant for many users).
- Things that physically can't change (sex, birth city, postcode if given once at signup).

### 4.6 Standardisation for lagged features — **MUST be careful**
- **You cannot use `StandardScaler` independently on each lagged variant.**
- If `f2_-1` and `f2_-2` are lags of the same variable, standardising independently destroys the meaningful information that `f2_-1 > f2_-2` indicates an *increase*.
- Correct fix: standardise each *original* variable's lags using **its overall mean and standard deviation across all its lag periods** (collectively).

### 4.7 Temporal hold-out (the only correct evaluation)

**Single temporal hold-out:**
```
1. Pick a test reference date.
2. Build the test set with data BEFORE that date as input, output from after.
3. Pick a train reference date strictly earlier than the test ref date.
4. Build train set the same way (input from before train ref date).
5. Train, evaluate on test.
```

**Repeated temporal hold-out:**
```python
for i in range(n_holdouts):
    test_X, test_y  = get_dataset(now - 1, w_in, w_out)
    train_X, train_y = get_dataset(now - 2, w_in, w_out)
    model.fit(train_X, train_y)
    scores.append(model.score(test_X, test_y))
    now = now - offset  # step the reference date back
```

This avoids "got lucky with one test month" while never letting the future leak in.

### 4.8 Meta-parameter learning on temporal data
- **Cannot use `cross_val_score` or `GridSearchCV` with random k-fold** — would mix future and past.
- Use `TimeSeriesSplit` from sklearn, OR a manual repeated-hold-out grid search where each train/test pair respects time order.

### 4.9 Temporal baselines (when asked for one)
- Mean / mode over all time is a **bad** baseline.
- **Good baseline:** the value at the time point immediately *prior* to the prediction point (a "naive" 1-step model). For a series with trend or seasonality, this is surprisingly strong.

### 4.10 Global vs. per-entity models
**Per-entity (e.g. ARIMA per customer):**
- Uses only that one customer's history.
- Cannot incorporate cross-customer features (age, sex, signup data) directly.
- Suffers when an individual has little data.

**Global (Random Forest with lagged features for everyone):**
- Pools information across customers.
- Can naturally use non-temporal features (demographics, signup info).
- Usually better when (a) per-customer data is sparse, (b) you have signup features, or (c) behaviour is partly shared.

### 4.11 Traditional time-series decomposition
A series is split into trend (T), seasonal (S), and error (E):
- **Additive:** y_t = T_t + S_t + E_t — use when seasonal amplitude is roughly constant.
- **Multiplicative:** y_t = T_t × S_t × E_t — use when seasonal swings grow with the level. (Take log → additive.)

### 4.12 Differencing
**Differencing** = new series of consecutive value differences: y'_t = y_t − y_{t−1}.
- Used to remove **trend** and induce stationarity.
- Multiple rounds for higher-order trends.
- The "I" in ARIMA.

### 4.13 ARIMA(p, d, q) in plain words
- **p** = number of past values used (auto-regressive lag).
- **d** = order of differencing.
- **q** = number of past forecast errors used (moving-average part).
- Underneath: it's effectively a linear regression on past values and past errors.

### 4.14 What's "unseen" in a temporal problem?
- Non-temporal: a "thing" (person, wine bottle) we've never met.
- Temporal: a **(thing, period) pair where the period is after now** — even a person we've seen before counts as a new instance at a new time.

### 4.15 Feature construction in SQL — the workflow
1. Decide what a row of your final dataset represents (one customer at month M).
2. List candidate features and where they come from.
3. Use `GROUP BY` to aggregate transactions to the customer-level.
4. Use **window functions** to compute lagged aggregates (true SQL: `SUM(...) OVER (PARTITION BY customer_id ORDER BY month ROWS BETWEEN N PRECEDING AND 1 PRECEDING)`).
5. Use CASE statements / sub-queries to compute aggregates per chunk size.
6. JOIN to the output label table by customer_id.

**Common gotcha — TIME types:** SparkSQL doesn't have a TIME data type. Workaround: convert to UNIX timestamp on a fixed date to compute mean/std of time-of-day.

### 4.16 Truth/false statements often asked
- ✅ SQL window functions can be used for temporal feature construction.
- ❌ A sklearn `StandardScaler` is appropriate for temporal data (only if you scale collectively, never per-lag-independently with the default constructor).
- ❌ Adding more lagged features always improves predictions (more correlated noise, more overfitting risk).
- ❌ Event series can never be converted to time series (they can — by aggregation).
- ❌ There is only one correct temporal evaluation strategy (multiple valid strategies).
- ❌ Events like COVID are typically easy for temporal models (they're disasters — non-stationary).
- ✅ Tumbling windows create less correlated lagged features than expanding windows.

---

## 5. Unbalanced classes (sub-topic of evaluation)

### 5.1 Why balanced-class assumption matters
- **Standard accuracy** = (correct) / (total). If 99% of customers don't churn, predict "no churn" always → 99% accuracy → useless.
- **The algorithm itself** optimises raw accuracy → boundary is pushed away from the majority class.

### 5.2 Four strategies (these *combine*)

**(1) Change the threshold (probabilistic classifiers only):**
- For a classifier giving P(class=1 | x), lower the decision threshold below 0.5 to predict the minority class more aggressively.
- No retraining needed — just re-score. Use ROC curves to pick the threshold.
- **Risk:** procedural overfitting — you're tuning on a test set. Use a separate held-out set.

**(2) Change the evaluation metric:**
- **Balanced accuracy** = (sensitivity + specificity) / 2 — weights each class equally.
- **F1**, **Matthews correlation coefficient (MCC)**, **PR-AUC** for highly imbalanced.
- Or a **custom profit metric** (see §5.5 below) — use this when the *business value* of each class is different.

**(3) Class re-weighting / cost-sensitive learning:**
- Pass `class_weight='balanced'` to SVC, LogisticRegression, RandomForestClassifier, etc.
- Or pass `sample_weight` per data point.
- The optimiser then treats each minority-class point as worth more (inversely proportional to class frequency).
- Equivalent to setting the cost matrix: `cost(FN)/cost(FP)` = ratio between class sizes.

**(4) Resampling:**
- **Oversampling** the minority (duplicate): cheap, but model may overfit duplicates.
- **Undersampling** the majority: loses information.
- **SMOTE** (Synthetic Minority Over-sampling): generate new minority points as convex combinations of existing ones (interpolate between k nearest neighbours).
  - Risk: SMOTE-generated points are not independent → if generated *before* splitting, leakage into test set. Generate **inside** the CV loop.
- **Data augmentation** for images: rotations, flips, etc. (see §6.10).

### 5.3 What strategy to choose when (Q from past exams)

**Profit-weighted classification, e.g. "offer A makes £5, offer B makes £1":**
- Use **class reweighting** with weights proportional to profit value (A=5, B=1).
- Evaluation metric: **a custom measure that captures profit per correct classification** (not balanced accuracy).

**Extreme imbalance:** consider switching to **anomaly detection** algorithms (one-class SVM, isolation forest, autoencoder reconstruction error).

### 5.4 Order of operations matters
- **Class weighting / SMOTE must happen on the training set only.**
- Otherwise → leakage into test → inflated score.

### 5.5 Multiple flavours of "balanced"
- Balanced accuracy → equal weight per class.
- Custom cost matrix → different weights per class, can encode business cost.
- Both → start with class_weight='balanced' as a safe default; move to custom if you have explicit costs.

---

## 6. Neural Networks

### 6.1 Building blocks
**A neuron (perceptron):**
- Weighted sum of inputs + bias.
- Apply an activation function.
- Output goes to the next layer.

**Universal approximation theorem:** a single hidden layer with enough neurons + a non-linear activation can approximate any continuous function to arbitrary accuracy.

But: *the theorem guarantees the perfect weights exist; it does not guarantee gradient descent finds them in reasonable time with limited data.* Hence we use depth, architecture, and inductive bias.

### 6.2 Why deep networks (in practice, not in theory)
- A shallow net needs **exponentially many** neurons for problems where features build hierarchically.
- A deep net learns **hierarchical features** layer by layer (edges → shapes → objects).
- Each layer reframes the input into a new feature space — similar in spirit to PCA but with arbitrary non-linear bases.
- This is also the basis for **transfer learning**: freeze the lower layers learned on a big dataset, retrain only the top layers on your small dataset.

### 6.3 Gradient descent (and friends)
**Stochastic GD (SGD):** update on one data point per step. Cheap, jumpy, can escape local minima.
**Mini-batch GD:** update on a small batch (typical: 32-256). Parallelisable, less noisy than SGD.
**Batch GD:** update on all data per step. Slow, memory-intensive, smooth.

**Better optimisers** (extensions of SGD):
- **Momentum:** carry forward gradient direction → faster convergence, escapes shallow local minima. Friction parameter ~0.9.
- **AdaGrad:** scales learning rate per parameter inversely to past gradient sum. Good for sparse problems; decays too fast for deep nets.
- **RMSProp:** like AdaGrad but with exponential decay of past gradients → doesn't slow down as drastically.
- **Adam:** RMSProp + Momentum. Default for most modern work. β₁=0.9, β₂=0.999 typical.

### 6.4 Vanishing & exploding gradients
**Backpropagation:** each weight's gradient = product of slopes back along the chain. In deep nets the multiplicative chain blows up or shrinks toward zero.

**Vanishing gradients (signs):**
- Lower-layer weights barely change.
- Loss decreases very slowly or plateaus.
- Often with sigmoid/tanh activations.

**Exploding gradients (signs):**
- Unusually large changes in loss.
- Loss becomes NaN or Inf.
- Systematic non-decreasing loss / weights blow up.
- Extremely large weight updates.

**Fixes:**
- **Better activations:** ReLU, ELU, Leaky ReLU (avoid sigmoid in deep nets).
- **Better initialisation:** Xavier/Glorot (for tanh/sigmoid), He (for ReLU/ELU).
- **Batch normalisation:** between layers.
- **Gradient clipping** for exploding gradients.
- **Skip connections** (ResNet-style) — not generally on this course but worth knowing.

### 6.5 Activation functions
| Activation | Use | Notes |
|---|---|---|
| **ReLU** | Default hidden layers | Fast; can suffer "dying ReLU" (~40% of neurons go to 0 permanently) |
| **Leaky ReLU** | When dying ReLU is a problem | Small negative slope (typ. 0.01) prevents death |
| **ELU** | Better generic choice | Smooth, exp(x)-1 below 0; faster convergence, slower forward pass |
| **SELU** | Self-normalising NNs | Special — requires LeCun normal init, no dropout/regularisation that breaks it |
| **Sigmoid** | **Binary** output layer | Avoid hidden layers in deep nets — saturation kills gradients |
| **Softmax** | **Multi-class** output layer | Outputs sum to 1, interpret as probabilities |
| **Linear (none)** | **Regression** output layer | Standard for unbounded continuous outputs |

### 6.6 Weight initialisation
**Do not initialise weights to 0 or all-same:** symmetry breaks gradient descent, no learning.

| Activation | Best initialiser |
|---|---|
| ReLU, ELU, Leaky ReLU | **He** (kaiming_normal / kaiming_uniform) |
| Tanh, Sigmoid | **Xavier / Glorot** |
| SELU | **LeCun normal** |

Practically: `kernel_initializer = keras.initializers.he_normal(seed=...)` on Dense layers using ReLU/ELU.

### 6.7 Batch Normalisation
- Standardises the inputs to each layer (mean 0, var 1, then learnable scale + shift).
- **Between every layer**, typically before the activation (or after — both used).
- Reduces internal covariate shift, allows higher learning rates, acts as light regularisation.
- **Common code-review error:** only one BatchNorm at the input; should be between every layer.

### 6.8 Choosing the output layer (the most common error)
| Problem | Output layer | Loss |
|---|---|---|
| Regression | 1 unit, **linear** activation | MSE or MAE |
| Binary classification | 1 unit, **sigmoid** activation | Binary cross-entropy |
| Multi-class classification | k units, **softmax** activation | Categorical cross-entropy (or sparse_categorical_cross_entropy if labels are integer-encoded) |

**Code-review trap:** "predict number of days until customer returns" (regression) with `Dense(1, activation="sigmoid")` and loss="mean_squared_error". Sigmoid forces output to [0,1] — wrong. Should be `activation="linear"` (or just omit).

### 6.9 Regularisation in NNs
| Method | What it does | When to use |
|---|---|---|
| **L1/L2 weight regularisation** | Penalty on weight size in cost function | Always worth trying; controlled by α |
| **Dropout** | Randomly drop neurons during training (prob. p) | Default for big nets; rate~0.2-0.5 |
| **Alpha Dropout** | Dropout that preserves mean/variance (for SELU) | With SELU only |
| **Early stopping** | Stop when val loss stops improving | Default — always use |
| **Batch normalisation** | (Side-effect) regularises slightly | See §6.7 |
| **Data augmentation** | Generate variants of existing data | Image / signal / time-series problems |
| **Max-norm constraint** | Cap each neuron's incoming weight vector size | Less common; useful with dropout |
| **Freezing layers** (transfer learning) | Don't train lower layers | Small dataset on top of a pre-trained model |

### 6.10 Data augmentation (conceptual explanation)
- **What it does:** generates new training instances from existing ones via transformations that preserve the label (rotate an image of a cat → still a cat; add small noise to audio → still the same speech).
- **Why it works:** provides more *true variation* for the model to learn, so the model's parameters fit real variation rather than noise → reduces overfitting.

### 6.11 Training dynamics — reading the loss curves
- **Train loss decreasing, val loss decreasing then increasing:** classic **overfitting**. Fixes: more regularisation, fewer layers/neurons, early stopping, more data.
- **Both flat/high:** underfitting. Increase capacity, train longer, check learning rate.
- **Very slow decrease:** learning rate too small / vanishing gradients / wrong scaling.
- **Wild fluctuations or NaN:** exploding gradients.

### 6.12 Early stopping & checkpoints (Keras pattern)
```python
es = EarlyStopping(monitor='val_loss', patience=20, min_delta=0.001, restore_best_weights=True)
mc = ModelCheckpoint('best.h5', monitor='val_loss', save_best_only=True)
model.fit(X_train, y_train, validation_data=(X_val, y_val),
          epochs=500, batch_size=32, callbacks=[es, mc])
```
**Important:** `validation_data` should be your *validation* set, **not** your test set. Using test in validation_data is procedural overfitting on the test set.

### 6.13 Meta-parameters of NNs (the list to know)
- Number of layers (depth)
- Number of neurons per layer (width)
- Activation function per layer
- Weight initialisation strategy
- Learning rate (& schedule)
- Optimiser type and its params
- Batch size
- Number of epochs (with early stopping)
- Regularisation: L1/L2 α, dropout rate, batch norm
- How neurons are connected (architecture: FCN, CNN, RNN…)

### 6.14 What to do with little data
Three ways to "realise a trained NN without huge data":
1. **Transfer learning** — reuse a pre-trained model's lower layers, only retrain the top.
2. **Data augmentation** — synthesise more training data.
3. **Use a simpler model** — sometimes the right answer is "don't use a deep net."

### 6.15 NN architectures (the why)
The Universal Approximation Theorem says shallow nets can in principle solve anything, but in practice this fails because:
- **Parameter explosion:** a 200×200×3 image with 1000 hidden units = 120M weights in the first layer alone.
- **Spatial blindness:** flattening an image loses 2D structure; FCN must relearn locality from scratch.
- **Lack of translation invariance:** FCN learns location-specific patterns; move the cat → re-learn.

Architectures **inject inductive bias** to fix these:
- **CNN** (Convolutional NN):
  - *Local receptive fields* (each neuron only sees a small patch): solves spatial blindness.
  - *Weight sharing* (same filter slides across image): solves parameter explosion.
  - *Pooling* (max-pool / avg-pool): solves translation invariance.
- **RNN** (Recurrent NN):
  - Hidden state at time t depends on input at t + hidden state at t-1.
  - Persistence + weight sharing across time.
  - **Short-term memory only:** information from far in the past decays.
- **LSTM** (Long Short-Term Memory):
  - Two memory pathways: heavily-modifiable short-term + lightly-modified long-term.
  - **Gates** (forget, input, output) control what enters/leaves long-term memory.
- **Transformers** (foundations of ChatGPT):
  - Drop recurrence; use **attention** instead.
  - Attention: "given this word, which other words in the input are relevant right now?" — computed in parallel.
  - Token + positional embeddings let words be processed independently while still encoding order.
  - Multi-head attention = multiple "experts" combined via a FCN.
  - Solves the LSTM's long-range decay and its non-parallelisable training.

### 6.16 Foundation models
- **Definition:** a model (typically a NN) pre-trained on huge amounts of data with the goal of being adaptable to many tasks.
- **Benefits:** versatility across tasks; reduced development time/resources.
- **Drawbacks:** may not use your domain-specific features; can inherit biases; may include data poisoning from training data; you don't control the training data.
- **Customising:** fine-tuning, prompt engineering, RAG (Retrieval-Augmented Generation).
- **Fine-tuning + overfitting on small dataset:** mitigate with data augmentation, dropout, early stopping, **freezing lower layers** (so only top layers train).

### 6.17 Gradient descent — the role
**Gradient descent minimises the loss function by iteratively adjusting the model's parameters.**
- It is **not** for finding hyperparameters (that's grid search).
- It is **not** for calculating accuracy (that's evaluation).
- It is **not** for preventing overfitting (that's regularisation).
- GD is not guaranteed globally optimal for neural nets (non-convex), but it *is* for convex models like logistic regression (with appropriate optimisers).

---

## 7. Causal Inference

### 7.1 Observational vs. causal
- **Observational/predictive:** P(y | x) — "if I observe x, what's y?"
- **Causal:** P(y | **do(x)**) — "if I *force* x, what's y?"

**Light-sensor example:**
- P(dark | light = on) = 1 (the light only switches on when it's already dark).
- P(dark | **do**(light = on)) = 0.5 (forcing the light on tells us nothing about whether it's actually dark — depends on time of day).

### 7.2 The fundamental problem of causal inference
For any individual, we observe **either** y(treated) **or** y(untreated), never both — the counterfactual is missing. We must *estimate* it.

### 7.3 Average effects
- **ATE** (Average Treatment Effect): average causal effect over the **whole population**.
- **ATT** (Average Treatment Effect on the Treated): average causal effect for **those who actually received treatment**.

Distinction matters: ATT generalises only to people *like the ones treated*. ATE generalises to the whole population.

### 7.4 Gold standard — Randomised Controlled Trial (RCT) / A/B test
Randomly assign treatment. Randomisation, "on average", makes confounders equally distributed between groups, so any difference in outcome is attributable to treatment.

**Real-world A/B test uses:**
1. Direct / targeted marketing campaigns.
2. Website layout / sales funnel design.
3. Product update testing.
4. Store layout, product placement.
5. Testing prices, discounts.

### 7.5 Setting up an A/B test — things that can go wrong
- **Group assignment must be truly random.** If by IP block, by time of day, etc. → systematic confound.
- **Sample sizes must be large enough for statistical power.**
- **Stratified sampling** for known important groups (new vs. returning customers).
- **Intervention must work end-to-end** — accidental side-effects (slowing the page, broken links) invalidate.
- **Users must get one variant only** — if logged-out users hit both, your test is broken.
- **Ethical / business risk:** what if the treatment is terrible? Can you afford the loss?
- **Plan to transition users back** (or to) the chosen variant — habits form.

### 7.6 Simpson's Paradox (the trap visualisation)
The aggregate trend reverses (or differs from) the within-subgroup trend when a confounder is unmeasured.

**Example:**
- Algorithm A: 5 / 100 (5%) overall.
- Algorithm B: 50 / 1000 (5%) overall — same conversion.
- But split by income: A wins **within each subgroup**, B's overall rate is inflated only because B happened to be tested on more high-income visitors.

**When is it an issue?** When a confounding variable is not measured / not controlled for. **What happens?** The direction of the reported association can be wrong.

### 7.7 Causal inference from observational data
Requires **extra assumptions**:
- **Unconfoundedness** (a.k.a. "ignorability" / "selection on observables"): we've measured *all* variables that jointly affect both treatment and outcome. Conditional on those, treatment is "as if" randomised.
- **Other assumptions** (out of scope but mention if asked): parallel trends (for difference-in-differences), instrumental variables.

### 7.8 Estimating the causal effect under unconfoundedness — four methods

**Method 1 — Conditioning:**
- Compute the treatment effect *within* each subgroup defined by the confounders.
- Re-weight by the subgroup's prevalence in the population.
- Gives ATE.

**Method 2 — Matching (e.g. CEM):**
- Find pairs of treated and untreated individuals identical on confounders.
- Average the per-pair difference.
- Gives ATT (use Mahalanobis distance if exact matches are rare).

**Method 3 — Propensity Score Stratification:**
- Estimate P(treated | confounders) for each individual.
- Stratify by propensity score, compute per-stratum effect, average.

**Method 4 — Propensity Score Matching + IPTW (Inverse Probability of Treatment Weighting):**
- Match on propensity scores rather than raw covariates.
- Re-weight to reconstruct the random-assignment world.
- Approximates ATE if all assumptions hold.

### 7.9 What conditioning / CEM / propensity methods all *assume*
**Unconfoundedness.** If a confounder is unmeasured, they all fail.

### 7.10 Refutations (sanity checks in causal inference)
Once you've estimated a causal effect, you should **test the assumptions** by:
- Adding a random common cause and re-estimating — should be near zero impact if assumptions hold.
- Substituting placebos for the treatment.
- Excluding sub-samples to test stability.

**Refutations are used to test modelled assumptions in causal inference.** ✅

### 7.11 Key true/false statements
- ✅ "If we knew the true causal graph and could measure all factors in it, we could determine the causal effect without an A/B test." — TRUE (this is the unconfoundedness ideal).
- ✅ "Many causal inference methods assume unconfoundedness." — TRUE.
- ✅ "Refutations test modelled assumptions." — TRUE.
- ❌ "How we select A/B participants doesn't matter." — Random assignment is the entire point.
- ❌ "Causal effects can be identified directly from observational data with no extra information." — Need assumptions.
- ❌ "Permutation importance scores can be used to determine causal effect." — Permutation tells you about model reliance, not causation.

---

## 8. Model Understanding (Session 13)

### 8.1 Why interpretability matters
Two reasons we explain models:
1. **Phenomenon understanding** — what drives the outcome in reality.
2. **Variable selection / data cost reduction** — drop features without losing performance.

### 8.2 ICE / PDP (Partial Dependence Plots)
**Procedure:**
1. Pick a feature f.
2. For each data point, hold all other features fixed at their actual values.
3. Vary f over its range. Get predictions.
4. **ICE:** plot one line per data point.
5. **PDP:** average the lines into one.

**Interpretation cautions:**
- We see what the *model* thinks, not necessarily the truth.
- Interactions are not visualised (only 2-variable plots).
- Choice of sampled points along f matters.

**Example interpretation patterns:**
- "Being young increases survival probability." (Titanic)
- "Higher fare → better survival odds" (a proxy for cabin location).

### 8.3 SHAP (Shapley Additive Explanations)
**For one data point:** how does knowing each feature's value (vs. averaging it out) change the prediction?
- Allocates credit fairly among features for *that particular* prediction.
- Aggregate across all points → global feature importance with direction.
- **In contrast to permutation importance:** SHAP shows both magnitude *and* direction.

### 8.4 The Rashomon set problem (recap)
- Different runs with different seeds give *different* "important features" when features are correlated.
- Single-model explanations are arbitrary.
- MCR (§1.10) is one solution — characterise the bounds of importance across the whole Rashomon set.

### 8.5 Reading a SHAP plot (the wine example)
- Each row = a feature, ordered top-to-bottom by importance.
- Each dot = one data point.
- x-axis: SHAP value (positive = increases prediction, negative = decreases).
- Colour: feature value (red = high, blue = low).
- **"Two things"-style answer for alcohol:** (1) higher alcohol → higher predicted quality (red dots on the right); (2) alcohol is the **most important** feature (it's at the top).

---

# SECTION II — The code-review question (25 marks)

## 9. How to score Section II

Three points per issue: (1) state the issue/where, (2) why it's a problem, (3) how to fix it. Don't have to write code — a clear English fix is fine. **Common code violations:**

### 9.1 Generic violations (apply to any code)

1. **Scaling before splitting** → leakage. Fix: split first, then `fit_transform` on train, `transform` on test (or use a Pipeline).
2. **LabelEncoder on nominal categories** → false ordering. Fix: OneHotEncoder.
3. **No stratification on imbalanced data** → unstable folds. Fix: StratifiedKFold + `stratify=y` in split.
4. **No class imbalance handling** → biased classifier. Fix: `class_weight='balanced'` or sample_weight, or SMOTE, or change metric.
5. **Wrong evaluation metric for imbalanced data** (`accuracy_score`) → optimistic. Fix: `balanced_accuracy_score`, F1, or custom.
6. **Procedural overfitting** — using the test set to pick between models. Fix: third held-out test set, or nested CV.
7. **No hyperparameter tuning for at least one model** when comparing. Fix: GridSearchCV for every model class.
8. **Comparing on train score** when one model has been tuned more than the other. Fix: compare on a separate validation set.
9. **Scoring with train data**. Fix: hold-out test set.
10. **Using SVR for classification** (regressor on a categorical target). Fix: SVC.
11. **Pipeline missing the scaler** for a scale-sensitive model. Fix: add StandardScaler step.
12. **shuffle=False on ordered data** (or shuffle=True on temporal data). Fix: appropriate to the data type.
13. **n_estimators in RF grid search** — n_estimators is NOT a complexity meta-parameter for RF (more trees ≈ better, asymptotically); it's a compute trade-off. Tune `max_depth`, `max_features`, `min_samples_leaf`, etc.
14. **Wrong/missing `random_state`** when comparing — non-reproducible.
15. **Typos and broken imports** — yes, these count if they break correctness.
16. **`X_train` vs. `train_X` mismatched names** — silent bug.

### 9.2 Temporal-problem-specific violations

17. **Random train/test split on temporal data** → future leaks into training. Fix: temporal hold-out (out-of-time split).
18. **GridSearchCV with default KFold on temporal data**. Fix: `TimeSeriesSplit` or manual temporal CV loop.
19. **Same reference date for all train/test pairs** (only one hold-out). Fix: repeated temporal hold-out across multiple reference dates.
20. **Independent StandardScaler on each lagged variable** → destroys monotonic information. Fix: scale lags collectively using overall mean/std across all lag periods.
21. **Building train/test from overlapping windows** → leakage. Fix: ensure output windows don't overlap.
22. **`now = now - 1` (one *week*) vs. `now - 1 month`** — make sure the offset matches the prediction horizon.

### 9.3 Neural-network-specific violations

23. **Wrong output layer** — sigmoid on regression, single linear on multi-class, etc.
24. **Wrong loss for the task** — MSE on classification, cross-entropy on regression.
25. **Batch normalisation only at input** — should be between every layer.
26. **`use_bias=False` without batch normalisation** between layers — needs BN to centre.
27. **Fixed seed in every He initialiser** with `use_bias=False` and no BN — symmetric weights and no compensation = bad.
28. **`validation_data = (X_test, y_test)`** → test-set leakage for early stopping. Fix: use a separate validation set.
29. **No regularisation despite small dataset** — add dropout, L2, early stopping.
30. **No early stopping but training for fixed huge epochs** — overfits. Add EarlyStopping callback.
31. **`min_delta` too high or `patience` too low** in EarlyStopping — stops too early or late.
32. **Scaling once on full X** (before split) — leakage. Fix: split first.
33. **`shuffle=True` on temporal data** in train/test split.
34. **Single hidden layer for clearly non-trivial problem** — under-capacity.
35. **`SGD` with default learning rate on a complex problem** — likely won't converge. Try Adam.

---

# 10. Quick-reference cheat sheet (last-day glance)

### 10.1 Things that look right but are wrong
- `StandardScaler().fit_transform(X)` *before* train/test split.
- `LabelEncoder` on a nominal categorical input feature.
- `RandomForest(class_weight=...)` with `accuracy_score` on imbalanced data.
- `cross_val_score` on temporal data.
- `Dense(1, activation='sigmoid')` for regression.
- `loss='mean_squared_error'` for classification.
- `n_estimators` in an RF grid search as a complexity knob.
- Choosing the best-scoring model *across model classes* on the same test set.

### 10.2 Default choices ("if in doubt, do this")
- Imbalanced classes → `class_weight='balanced'` + `balanced_accuracy_score`.
- Feature scaling → `StandardScaler` inside a Pipeline.
- Categorical (nominal) → `OneHotEncoder`.
- Categorical (ordinal) → `OrdinalEncoder`.
- CV → `StratifiedKFold(n_splits=5 or 10, shuffle=True, random_state=42)` for classification.
- Temporal CV → `TimeSeriesSplit` or manual temporal hold-out loop.
- NN hidden layer → ReLU + He initialisation + BatchNorm.
- NN regression output → linear, MSE loss.
- NN binary classification output → sigmoid, binary_crossentropy.
- NN multi-class output → softmax, categorical_crossentropy.
- NN optimiser → Adam.
- NN regularisation → start with early stopping + dropout 0.2-0.3 + a touch of L2.

### 10.3 Sentences that win marks
- **"This is leakage because the scaler used information from the test set, so the test score over-estimates real-world performance."**
- **"This is procedural overfitting: the same held-out set was used to choose between many candidate models, so the reported score is optimistic relative to the true generalised performance. Use a separate held-out set for final evaluation."**
- **"On temporal data, random sampling places future points in the training set; the model is then evaluated on the past, which doesn't simulate real deployment."**
- **"Univariate VIM cannot capture interactions: features that are only important together would each individually appear unimportant."**
- **"Permutation importance shows how reliant the model is on a feature; it does not show what would happen if the feature were never available — for that, you must rebuild without it."**
- **"SHAP is preferred to permutation importance here because it shows both magnitude and direction of the effect per data point."**
- **"The boundary is forced toward the minority class because the algorithm minimises the sum of per-point errors equally across classes; reweighting per class corrects this."**
- **"With unconfoundedness, conditioning / matching / propensity-score methods can estimate the causal effect from observational data."**

### 10.4 Topics to revise on the exam morning
1. The three evaluation options (Option 1/2/3) — be able to **write the code** for each.
2. Temporal hold-out loop pattern with `get_dataset(now-1, ...)` and `get_dataset(now-2, ...)`.
3. Permutation vs. rebuilding vs. univariate — when each fails.
4. SVM: C and γ interpretation, when linear vs. RBF, primal vs. dual.
5. Reading a SHAP / ICE / PDP plot.
6. NN code review checklist (§9.3).
7. Causal: ATE vs. ATT, unconfoundedness, Simpson's paradox.
8. Categorical encoding decision (nominal/ordinal/high-cardinality).
9. Missing data: MCAR/MAR/MNAR + treatment.
10. Class imbalance: which strategy when, especially when given profits per outcome.

---

# 11. Appendix — common past-exam question patterns & how to attack them

### 11.1 "Three models on subsets of features give the same accuracy — why?"
→ Because the feature sets share information / are correlated. (1-mark answer.)

### 11.2 "Permutation importance shows half features have MDA=0 — discard them?"
→ No, not immediately. Investigate (a) whether features are correlated with the kept ones — the model "chose" between equivalents, (b) which set is more causal / cheaper to collect / less prone to drift. Use MCR or domain knowledge to choose.

### 11.3 "Univariate importance ranks 4 features highly, model with just those 4 underperforms — why and what next?"
→ Univariate cannot capture interactions. Some "low-univariate" features may be relevant in combination. Use permutation importance or RFE instead.

### 11.4 "Should we use feature selection or feature extraction to reduce 100 features when collection is expensive?"
→ Selection. Extraction (e.g. PCA) still needs all originals to compute the new features → no saving on collection cost.

### 11.5 "Mean over all time is not a good baseline — what's a better temporal baseline?"
→ The output value at the previous time point (the "naive" prediction).

### 11.6 "Why can't we use traditional cross-validation on temporal data?"
→ Because random sampling can place future points in the training set and past points in the test set — impossible in real deployment, inflates scores.

### 11.7 "Unbalanced offer problem — A makes £5 right, B makes £1 right, 0 if wrong, more B than A — what to do?"
- **Method:** class reweighting (or sample_weight).
- **Extra info needed:** the weights — A=5, B=1 (proportional to profit).
- **Evaluation metric:** custom profit-based metric (not accuracy, not balanced accuracy).

### 11.8 "What three meta-parameters does an NN need?"
Pick any three from: number of layers, neurons per layer, activation function, weight initialisation, learning rate, optimiser, batch size, regularisation strength, dropout rate.

### 11.9 "Vanishing gradients — what can fix it?"
- Better activation (ReLU/ELU instead of sigmoid).
- Better initialisation (He for ReLU).
- Batch normalisation.
- Residual / skip connections.

### 11.10 "Data augmentation — what is it and why does it work?"
- **What:** generates new training instances from existing ones via label-preserving transformations.
- **Why:** more real variation in training → parameters fit signal, not noise → less overfitting.

### 11.11 "Plot shows training and validation loss diverging at epoch ~50, val loss rising — what now?"
- Don't use the epoch-100 model — it's overfit.
- At minimum, **early stopping**.
- If pattern repeats, **reduce model complexity** (fewer layers/neurons), increase regularisation, or get more data.

### 11.12 "You ran a grid search for RF, then a grid search for SVM, picked the best of each, reported the better — was that right?"
→ No, this is procedural overfitting. The same hold-out test set was used to compare *across* model classes. Fix: a third, never-touched test set, OR nested CV.

### 11.13 "Simpson's paradox plot — what is it and when an issue?"
- It's Simpson's paradox.
- Issue when an unmeasured confounder (e.g. customer income, class size) creates an aggregate trend opposite to the per-subgroup trend.
- Consequence: direction of the reported effect is wrong.

### 11.14 "Can we use CV for the meta-parameters of an RF on temporal data?"
→ No. Random folds put future data in training. Use temporal CV (TimeSeriesSplit or manual temporal hold-out).

### 11.15 Section II — generic attack plan
1. **Read the problem statement carefully** — note: temporal vs. non-temporal? Balanced or not? Categorical inputs? Mentioned ordering of data?
2. **Read every line of code.** Make a list (mental or on scrap paper).
3. **Cross-check each line against the §9 checklist.**
4. For each issue write three things: *what & where*, *why it's wrong*, *how to fix it*. One short sentence each is enough.
5. Aim for 6-8 distinct issues — that's typically 18-24 of the 25 marks. Don't double-count the same conceptual issue.

---

**Best of luck for 4 June.** The biggest single piece of advice for Section I is to **answer concisely and reach for the framework language** ("procedural overfitting", "leakage", "captures interactions the model captures", "minimises sum of per-point errors equally across classes"). For Section II the trick is to be systematic — work through the checklist line by line.

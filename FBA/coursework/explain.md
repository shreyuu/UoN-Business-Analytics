# Machine Learning Classification Notebook — Documentation

## 1. Overall Purpose (Big Picture)

### What this notebook does

This notebook builds, evaluates, and saves machine-learning classification models to predict whether a customer will subscribe to a product (`y = yes/no`) using **pre-call information only**.  
It performs exploratory data analysis (EDA), handles class imbalance, constructs robust preprocessing pipelines, compares **Logistic Regression**, **Decision Tree**, and **Random Forest** models using **stratified cross-validation**, selects the best model based on **F1-score**, saves the winning model as a reusable pipeline, and provides **decision-threshold guidance** for business profit optimization.

---

## 2. Notebook Metadata & Markdown Cells

```markdown
# Student ID: 20811152

# Files: cwk_data_20811152.csv

# Notes: duration is explored but excluded from predictive models
```

### Explanation

- Pure documentation
- States:

  - Ownership of the work
  - Dataset used
  - Critical rule: **`duration` must not be used for prediction**

### Python Concepts

- Markdown cells (Jupyter feature)

---

## 3. Package Requirements

```python
# %pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

### Explanation

- Installs required Python libraries inside Jupyter
- Commented out to avoid reinstalling on every run

### Libraries Used

- **pandas** → data handling
- **numpy** → numerical operations
- **scikit-learn** → ML models, pipelines, cross-validation
- **matplotlib / seaborn** → visualization
- **joblib** → saving models

### Best Practice

- ✔ Keep this commented
- ✔ Mention versions in `README.md`

---

## 4. Imports

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from pathlib import Path
```

### Explanation (Line by Line)

- `pandas` → DataFrames and tabular data
- `numpy` → arrays and numerical computation
- `matplotlib.pyplot` → plotting
- `seaborn` → enhanced plotting styles
- `joblib` → save/load ML models
- `Path` → safer, OS-independent file paths

---

## 5. scikit-learn Imports

### Data Splitting

```python
from sklearn.model_selection import StratifiedKFold, train_test_split, cross_val_predict
```

- Stratified splits preserve class balance

### Pipelines & Column Handling

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
```

- Pipelines chain preprocessing + model
- ColumnTransformer applies different preprocessing per column type

### Preprocessing

```python
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
```

- Missing value handling
- Scaling numeric data
- Encoding categorical data

### Models

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
```

### Metrics

```python
from sklearn.metrics import (...)
```

- Performance evaluation metrics

---

## 6. Plotting Configuration

```python
%matplotlib inline
plt.rcParams['figure.figsize'] = (9, 6)
sns.set_style('whitegrid')
```

### Explanation

- Plots render inline in the notebook
- Sets default figure size
- Applies a clean visual theme

### Concepts

- Jupyter magic commands
- Global plotting configuration

---

## 7. Loading the Dataset

```python
DATA_PATH = '...cwk_data_20811152.csv'
df = pd.read_csv(DATA_PATH)
df.columns = df.columns.str.strip()
```

### Explanation

- Loads CSV into a DataFrame
- Removes accidental whitespace from column names

```python
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df['y'].value_counts())
```

### Checks Performed

- Number of rows and columns
- Column names
- Class imbalance in target

### Edge Cases

- ⚠ Incorrect path → `FileNotFoundError`
- ✔ Improvement: `Path(DATA_PATH).exists()`

---

## 8. Initial Data Inspection

```python
df.head(8)
```

- Displays first 8 rows

```python
display(df.describe(include='all').T)
print(df.isnull().sum())
```

### Purpose

- Summary statistics
- Missing value inspection

### Concept

- Exploratory Data Analysis (EDA)

---

## 9. Class Imbalance Discussion

- Target distribution is approximately **80:20**
- Use **stratification**, **F1-score**, and **ROC / PR curves**

### Why This Matters

- Accuracy alone is misleading
- Precision and recall better reflect business impact

---

## 10. Exploratory Plots

### Target Distribution

```python
sns.countplot(x='y', data=df)
```

### Numeric Feature Distributions

```python
for c in num_cols:
    sns.histplot(df[c])
```

### Balance vs Target

```python
sns.boxplot(x='y', y='balance', data=df)
```

---

## 11. `duration` Analysis (Leakage Awareness)

```python
df.groupby('y')['duration'].agg(...)
```

### Purpose

- Demonstrates strong correlation with target
- **Not used in modeling**

### Key Concept

🚨 **Data Leakage**
Using information unavailable at prediction time invalidates results.

---

## 12. Feature / Target Split

```python
X = df.drop(columns=['y', 'duration'])
y = df['y'].map({'yes': 1, 'no': 0})
```

### Explanation

- `X` → predictors
- `y` → binary numeric target

### Concepts

- Label encoding
- Feature exclusion

---

## 13. Automatic Feature Typing

```python
numeric_features = X.select_dtypes(...)
categorical_features = X.select_dtypes(...)
```

### Why This Is Good

- ✔ Robust to schema changes
- ✔ Avoids hard-coded column names

---

## 14. Preprocessing Pipelines

### Numeric Pipeline

```python
SimpleImputer(strategy='median')
StandardScaler()
```

- Median imputation
- Feature scaling

### Categorical Pipeline

```python
SimpleImputer(fill_value='unknown')
OneHotEncoder(handle_unknown='ignore')
```

- Handles missing categories
- Prevents errors on unseen values

---

## 15. ColumnTransformer

```python
preprocessor = ColumnTransformer([...])
```

### Purpose

- Applies correct preprocessing per feature type

### Best Practice

- ✔ Prevents data leakage
- ✔ Reusable and production-ready

---

## 16. Model Definitions

```python
models = {
    'LogisticRegression': ...,
    'DecisionTree': ...,
    'RandomForest': ...
}
```

### Explanation

- Dictionary allows easy iteration
- Fixed random seeds ensure reproducibility

---

## 17. Cross-Validation Setup

```python
cv = StratifiedKFold(n_splits=5, shuffle=True)
```

### Why Stratified?

- Preserves class ratio in each fold

---

## 18. Model Evaluation Loop (Core Logic)

```python
for name, clf in models.items():
    ...
```

### Control Flow

- Iterates through models
- Builds a full pipeline each time

```python
y_pred = cross_val_predict(...)
y_proba = cross_val_predict(..., method='predict_proba')
```

### Why This Matters

- Out-of-fold predictions
- Avoids optimistic bias

### Metrics Computed

- Accuracy
- Precision
- Recall
- F1-score
- ROC AUC
- Confusion Matrix

### Edge Cases

- ✔ `zero_division=0` prevents crashes
- ⚠ Cross-validation can be slow on large datasets

---

## 19. Metrics Summary Table

```python
metrics_df = pd.DataFrame(results).T
metrics_df.sort_values(by='f1')
```

### Purpose

- Fair model comparison
- Selection based on F1-score

---

## 20. Final Model Training & Saving

```python
final_pipeline.fit(X, y)
joblib.dump(final_pipeline)
```

### Explanation

- Trains on full dataset
- Saves preprocessing + model together

### Best Practice

- ✔ Never save a model without preprocessing
- ✔ Production-ready artifact

---

## 21. Feature Importance Extraction

```python
if hasattr(clf, 'feature_importances_'):
    ...
```

### Explanation

- Applies to tree-based models
- Handles post-encoding feature names

### Edge Case

- ⚠ Logistic Regression uses coefficients, not importances

---

## 22. Interpretable Decision Tree Visualization

```python
DecisionTreeClassifier(max_depth=4)
plot_tree(...)
```

### Purpose

- Human-readable explanation
- Not used for final prediction

---

## 23. Precision–Recall Analysis

```python
precision_recall_curve(y, y_proba)
```

### Why PR Over ROC?

- Better for imbalanced datasets
- Focuses on positive class performance

---

## 24. Probability Calibration

```python
CalibratedClassifierCV(method='isotonic')
```

### Explanation

- Improves probability reliability
- Important for business decision thresholds

---

## 25. Expected Profit Function

```python
def expected_profit_at_threshold(...):
    ...
```

### Inputs

- `y_proba` → predicted probabilities
- `threshold` → decision cutoff
- `R` → revenue per success
- `C` → cost per contact

### Output

- Total expected profit

### Design Note

- ⚠ Uses global `y`
- ✔ Improvement: pass `y` explicitly

---

## 26. README Generation

```python
readme = """..."""
```

### Purpose

- Instructions for marker / user
- Ensures reproducibility

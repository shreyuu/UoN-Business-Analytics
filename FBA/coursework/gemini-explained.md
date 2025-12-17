# Explanation of `main.ipynb`

This notebook (`main.ipynb`) in the `FBA/coursework` directory is a comprehensive machine learning project designed to predict whether a client will subscribe to a term deposit (`y` column: 'yes' or 'no') based on various client and campaign data from the `cwk_data_20811152.csv` file.

## Key Steps and Workflow:

1.  **Setup and Imports:**
    *   It begins by importing all necessary Python libraries for data manipulation (`pandas`, `numpy`), visualization (`matplotlib`, `seaborn`), and machine learning (`scikit-learn`).

2.  **Data Loading and Initial Exploration:**
    *   The dataset is loaded from `cwk_data_20811152.csv`.
    *   Initial data exploration includes printing the data's shape, column names, and the distribution of the target variable (`y`), which immediately highlights a class imbalance.
    *   The first few rows (`.head()`) and a statistical summary (`.describe()`) are displayed to inspect data characteristics and potential missing values.

3.  **Exploratory Data Analysis (EDA) and Visualization:**
    *   The notebook generates plots to understand data patterns:
        *   A bar chart of the target variable to visualize class imbalance.
        *   Histograms for numerical features (e.g., `age`, `balance`, `campaign`) to examine their distributions.
        *   A boxplot comparing `balance` for clients with 'yes' and 'no' responses.

4.  **Feature Engineering and Preprocessing:**
    *   **Handling the `duration` column:** The `duration` feature, though a strong predictor, is excluded from predictive models due to being a "leaky" feature (its value is not known before the call's outcome). Statistical summaries of `duration` by target are reported separately.
    *   **Feature Identification:** Columns are automatically categorized into `numeric_features` and `categorical_features`.
    *   **Preprocessing Pipelines:** Robust pipelines are built for data transformation:
        *   **Numeric data:** Missing values are imputed using the median, followed by `StandardScaler` for scaling.
        *   **Categorical data:** Missing values are imputed with 'unknown', and then `OneHotEncoder` is applied to convert categories into a numerical format.
    *   **`ColumnTransformer`:** Both pipelines are integrated into a single `preprocessor` to ensure consistent transformations across training and new data.

5.  **Model Training and Evaluation:**
    *   **Model Selection:** Three classification models are defined for comparison: `LogisticRegression`, `DecisionTree`, and `RandomForest`.
    *   **Cross-Validation:** `StratifiedKFold` is used for cross-validation to maintain the target class proportion across folds, crucial for imbalanced datasets.
    *   **Model Evaluation Loop:** Each model undergoes evaluation:
        *   A full pipeline (preprocessor + classifier) is constructed.
        *   `cross_val_predict` generates out-of-fold predictions.
        *   Performance metrics calculated include: accuracy, precision, recall, F1-score, ROC AUC, and the confusion matrix.
        *   Results are printed for each model.

6.  **Model Comparison and Selection:**
    *   A pandas DataFrame summarizes the evaluation results, sorted by F1-score.
    *   `RandomForestClassifier` is identified as the best-performing model based on its F1-score.
    *   This summary is saved to `model_metrics_summary.csv`.

7.  **Final Model and Persistence:**
    *   The best model (`RandomForestClassifier`) is chosen.
    *   A final pipeline (preprocessor + best classifier) is trained on the entire dataset.
    *   This trained pipeline is saved as `final_pipeline.pkl` using `joblib` for future use and deployment.

8.  **Model Interpretation and Further Analysis:**
    *   **Feature Importance:** For the `RandomForest` model, feature importances are extracted and displayed.
    *   **Decision Tree Visualization:** A shallow `DecisionTreeClassifier` is trained and visualized to illustrate decision rules for interpretability.
    *   **Precision-Recall Analysis:** The precision-recall curve for the final model is calculated and plotted to understand the trade-off at various probability thresholds, offering insights for business decision-making based on cost/benefit analysis.

## Conclusion:

The `main.ipynb` notebook demonstrates a robust and well-structured approach to a machine learning problem. It incorporates best practices for data preprocessing, model evaluation (particularly for imbalanced datasets), and model persistence, providing a clear framework for building, interpreting, and deploying predictive analytics solutions.
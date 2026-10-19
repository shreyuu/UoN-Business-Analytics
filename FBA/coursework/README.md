# Foundational Business Analytics Coursework

A machine learning and business analytics coursework project for **BUSI4371 – Foundational Business Analytics**. The project focuses on building, evaluating, and explaining predictive models using structured coursework data.

Recommended GitHub repository name:

```text
foundational-business-analytics-ml
```

Other suitable repository names:

- `busi4371-predictive-analytics`
- `foundational-business-analytics-coursework`
- `business-analytics-ml-modeling`
- `busi4371-machine-learning-project`
- `predictive-modeling-business-analytics`

## Project Overview

This project applies a complete business analytics workflow, from data loading and exploration to model training, evaluation, explanation, and final model export. The analysis is implemented mainly in Jupyter notebooks and supported by saved machine learning model files, metrics outputs, documentation, and visualisations.

The project includes:

- Data preparation and exploratory analysis
- Predictive modelling using machine learning
- Model comparison and evaluation
- Final model selection
- Exported trained models and pipelines
- Decision tree visualisation
- Written coursework report and supporting explanation files

## Project Structure

```text
.
├── 20811152_BUSI4371_2526_final_model.joblib
├── 20811152_BUSI4371_2526.ipynb
├── 20811152_BUSI4371_2526.joblib
├── 20811152_BUSI4371_2526.pdf
├── 20811152_BUSI4371_2526.zip
├── Academic Integrity Slides 2020WithAudio1.pptx
├── BUSI4371 Foundational Business Analytics marking rubric - CW.xlsx
├── cwk_data_20796894-paras.csv
├── cwk_data_20811152.csv
├── decision_tree_viz.png
├── draft.docx
├── explain.md
├── FBA Coursework 25-26.pdf
├── final_model.joblib
├── gemini-explained.md
├── main01.ipynb
├── model_metrics_summary.csv
└── Rohit_cwk_data_20793079.csv
```

`final_pipeline.pkl` and `final_pipeline_calibrated.pkl` are also produced locally, but the root `.gitignore` excludes `*.pkl`, so they aren't in the repository.

## Files Description

| File                                                                | Description                                                                    |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `20811152_BUSI4371_2526.ipynb`                                      | Main coursework notebook containing the final analysis and modelling workflow. |
| `main01.ipynb`                                                      | Additional or development notebook used during analysis.                       |
| `cwk_data_20811152.csv`                                             | Main coursework dataset used for the project.                                  |
| `cwk_data_20796894-paras.csv`                                       | Additional coursework dataset for comparison or testing.                       |
| `Rohit_cwk_data_20793079.csv`                                       | Additional coursework dataset for comparison or testing.                       |
| `20811152_BUSI4371_2526.pdf`                                        | Final submitted coursework report or notebook export.                          |
| `FBA Coursework 25-26.pdf`                                          | Coursework specification document.                                             |
| `BUSI4371 Foundational Business Analytics marking rubric - CW.xlsx` | Marking rubric for the coursework.                                             |
| `decision_tree_viz.png`                                             | Visualisation of the decision tree model.                                      |
| `model_metrics_summary.csv`                                         | Metrics from `main01.ipynb`, where Random Forest led on F1. The submitted notebook compares more models and selects a Decision Tree on F0.5. |
| `20811152_BUSI4371_2526.joblib`                                     | The selected Decision Tree pipeline (scaling, one-hot encoding, `DecisionTreeClassifier(max_depth=5, min_samples_leaf=50)`), saved by Section E of the submitted notebook. |
| `20811152_BUSI4371_2526_final_model.joblib`                         | A Gaussian Naive Bayes pipeline from an earlier run. `predict_new()` loads it by default; see [Known issue](#known-issue). |
| `final_model.joblib`                                                | Another Gaussian Naive Bayes pipeline from an earlier run.                     |
| `explain.md`                                                        | Explanation notes for the `main01.ipynb` workflow (three models, selected on F1). |
| `gemini-explained.md`                                               | Additional model or project explanation notes.                                 |
| `draft.docx`                                                        | Draft version of the written coursework.                                       |
| `20811152_BUSI4371_2526.zip`                                        | Packaged coursework submission archive.                                        |
| `Academic Integrity Slides 2020WithAudio1.pptx`                     | Academic integrity reference material.                                         |

## Methodology

The project follows a typical predictive analytics workflow:

1. **Data Loading**
   - Import coursework CSV data.
   - Inspect the structure, columns, and target variable.

2. **Data Cleaning and Preparation**
   - Handle missing values.
   - Convert variables into suitable formats.
   - Prepare features for machine learning models.

3. **Exploratory Data Analysis**
   - Summarise key variables.
   - Identify patterns, distributions, and relationships in the data.
   - Understand the business meaning of important features.

4. **Feature Engineering**
   - Select relevant predictors.
   - Transform or encode features where needed.
   - Prepare data for modelling pipelines.

5. **Model Training**
   - Train machine learning models using the prepared dataset.
   - Compare model performance using suitable evaluation metrics.

6. **Model Evaluation**
   - Evaluate models using the metrics summary.
   - Review model accuracy, reliability, and practical usefulness.
   - Use visualisations such as the decision tree diagram to support interpretation.

7. **Final Model Export**
   - Save the selected model and pipeline using `.joblib` and `.pkl` formats.
   - Package the final coursework submission files.

## Tools and Technologies

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Pickle
- CSV data processing
- Machine learning pipelines
- Decision tree visualisation

## Outputs

The project produces:

- Trained machine learning model files
- Saved modelling pipelines
- Calibrated final pipeline
- Model metrics summary CSV
- Decision tree visualisation
- Final report / notebook export
- Packaged coursework ZIP file

## How to Run

1. Clone the repository and move into this folder:

   ```bash
   git clone https://github.com/shreyuu/UoN-Business-Analytics.git
   cd UoN-Business-Analytics/FBA/coursework
   ```

2. Install the required Python libraries. scikit-learn is pinned to 1.7.2, the version the `.joblib` files were saved with:

   ```bash
   pip install scikit-learn==1.7.2 pandas numpy matplotlib jupyterlab
   ```

3. Open the main notebook:

   ```bash
   jupyter lab 20811152_BUSI4371_2526.ipynb
   ```

4. Run the notebook cells from top to bottom. This retrains the models and overwrites `20811152_BUSI4371_2526.joblib`.

5. Review the generated metrics, model files, and visualisations.

## Known issue

The submitted notebook is kept as submitted, including one inconsistency. Section D selects a Decision Tree and Section E saves it as `20811152_BUSI4371_2526.joblib`, but `predict_new()` defaults to `20811152_BUSI4371_2526_final_model.joblib`, which holds a Gaussian Naive Bayes pipeline. The sample predictions at the end of Section E therefore come from Naive Bayes. To score with the selected Decision Tree, pass its file explicitly:

```python
result = predict_new("cwk_data_20796894-paras.csv", model_path="20811152_BUSI4371_2526.joblib")
```

## Notes

- The `.joblib` model files and the submission `.zip` are committed; `.pkl` and `.db` files are excluded by the root `.gitignore`.
- The coursework dataset and academic files are included for reproducibility within the coursework context.
- This repository is intended for educational and portfolio demonstration purposes.

## Author

**Shreyash Meshram**  
MSc Business Analytics  
University of Nottingham

## Module

**BUSI4371 – Foundational Business Analytics**  
Nottingham University Business School

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
├── .gitignore
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
├── final_pipeline_calibrated.pkl
├── final_pipeline.pkl
├── gemini-explained.md
├── main01.ipynb
├── model_metrics_summary.csv
└── Rohit_cwk_data_20793079.csv
```

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
| `model_metrics_summary.csv`                                         | Summary of model evaluation metrics.                                           |
| `final_model.joblib`                                                | Saved final machine learning model.                                            |
| `20811152_BUSI4371_2526_final_model.joblib`                         | Submitted version of the final saved model.                                    |
| `20811152_BUSI4371_2526.joblib`                                     | Additional exported model file.                                                |
| `final_pipeline.pkl`                                                | Saved machine learning pipeline.                                               |
| `final_pipeline_calibrated.pkl`                                     | Calibrated version of the saved machine learning pipeline.                     |
| `explain.md`                                                        | Explanation notes for the modelling workflow.                                  |
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

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/foundational-business-analytics-ml.git
   cd foundational-business-analytics-ml
   ```

2. Install the required Python libraries:

   ```bash
   pip install pandas numpy scikit-learn matplotlib joblib
   ```

3. Open the main notebook:

   ```bash
   jupyter notebook 20811152_BUSI4371_2526.ipynb
   ```

4. Run the notebook cells from top to bottom.

5. Review the generated metrics, model files, and visualisations.

## Notes

- Large generated files such as `.joblib`, `.pkl`, `.zip`, and `.db` files may be excluded from GitHub depending on repository size and submission requirements.
- The coursework dataset and academic files are included for reproducibility within the coursework context.
- This repository is intended for educational and portfolio demonstration purposes.

## Author

**Shreyash Meshram**  
MSc Business Analytics  
University of Nottingham

## Module

**BUSI4371 – Foundational Business Analytics**  
Nottingham University Business School

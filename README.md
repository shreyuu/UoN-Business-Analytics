# UoN-Business-Analytics

This directory contains comprehensive course materials for a Business Analytics program from the University of Nottingham. The materials are organized into three main modules with a focus on practical, hands-on learning through Jupyter notebooks and real-world datasets.

## 📚 Directory Overview

### **D@S/** - Data at Scale

A course focusing on large-scale data processing and web integration:

- Jupyter notebooks for data cleaning and API integration
- Web API practical exercises
- SQL-based data querying
- Lecture slides (PDF format)
- Real shopping receipt datasets for analysis

### **FBA/** - Foundational Business Analytics

The core analytics course with extensive Python practice:

- **Weekly Practice Notebooks** (`FBA_Week_01_*` through `FBA_Week_10_*`): Progressive Python and data analysis skills
- **Assessment Materials**: Python test notebooks (2023, 2025)
- **Datasets**: Multiple CSV files including admissions, credit card history, breast cancer, drinks data
- **Coursework Directory**: Advanced machine learning classification projects with detailed documentation
- **Key Notebook**: `balance.ipynb` - Financial data analysis and categorization

### **Supply-Chain-planning-and-management/**

Business process modeling with focus on supply chain optimization:

- Detailed flowcharts (Mermaid diagrams) showing supply chain workflows
- Solar panel manufacturing supply chain analysis
- Policy frameworks and compliance structures
- Lecture materials and exam preparation resources

## 📁 Key Files & Their Purpose

| File                                                  | Purpose                                                                |
| ----------------------------------------------------- | ---------------------------------------------------------------------- |
| `FBA/FBA_Week_01_Intro_&_Python_Practice.ipynb`       | Python fundamentals, variables, data types, conditionals               |
| `FBA/FBA_Week_07_Python_Practice.ipynb`               | Pandas, NumPy, correlation analysis, data manipulation                 |
| `FBA/FBA_Week_10_Python_Practice.ipynb`               | Machine learning models, cross-validation, classification              |
| `FBA/coursework/main.ipynb`                           | Advanced ML classification with feature engineering & model evaluation |
| `FBA/coursework/explain.md`                           | Comprehensive documentation of ML notebook structure                   |
| `FBA/balance.ipynb`                                   | Financial transaction analysis and expense categorization              |
| `FBA/admissions.csv`                                  | University admissions dataset (GRE, GPA, ranking)                      |
| `FBA/credit_card_history.csv`                         | Credit card default prediction dataset                                 |
| `Supply-Chain-planning-and-management/flowchart-3.md` | Comprehensive solar supply chain with policy & risk layers             |

## 🛠️ Technologies & Libraries

The coursework utilizes:

- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Machine Learning**: Scikit-learn (classification, pipelines, cross-validation)
- **Model Persistence**: Joblib
- **Notebook Environment**: Jupyter/Google Colab

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Running Notebooks

1. **Using Jupyter Lab:**

```bash
jupyter lab
```

2. **Using Google Colab:**
   - Upload `.ipynb` files to Google Colab
   - Or open directly: `colab.research.google.com`

3. **Local Python:**

```bash
python -m jupyter notebook
```

## 📊 Course Progression

### Week 1-6: Foundations

- Python basics and syntax
- Data types and control flow
- Introduction to Pandas and NumPy
- Data exploration and visualization

### Week 7-8: Data Analysis & Testing

- Correlation analysis and statistical measures
- CSV file handling
- Practical assessment (Python tests)

### Week 10: Machine Learning

- Classification algorithms (Logistic Regression, Decision Trees)
- Cross-validation and model evaluation
- Feature importance and interpretation
- Handling class imbalance

### Coursework: Advanced ML Project

- Complete pipeline from data loading to model deployment
- Feature engineering and preprocessing
- Comprehensive model comparison
- Business-focused metrics (F1-score, precision, recall, ROC)

## 📈 Dataset Summary

| Dataset                   | Rows   | Columns | Purpose                                           |
| ------------------------- | ------ | ------- | ------------------------------------------------- |
| `admissions.csv`          | 400+   | 4       | Predict university admissions (GRE, GPA, ranking) |
| `credit_card_history.csv` | 30,000 | 24      | Credit card default prediction                    |
| `breast_cancer_b.csv`     | -      | -       | Binary classification practice                    |
| `drinks.csv`              | -      | -       | Exploratory data analysis                         |
| `balance.csv`             | -      | -       | Personal finance analysis                         |

## 🔗 Project Highlights

### **FBA Coursework - ML Classification**

A production-ready machine learning pipeline featuring:

- Automated feature typing (numeric vs categorical)
- Preprocessing pipelines with column transformers
- Multiple model architectures (Logistic Regression, Random Forest, Gradient Boosting, SVM)
- Stratified cross-validation for imbalanced data
- Comprehensive evaluation metrics and profit analysis
- Model serialization for deployment

### **Supply Chain Optimization**

Detailed analysis of solar panel supply chain:

- 17-year mining lead times
- Global manufacturing concentration (94% in Asia)
- Risk mitigation strategies
- UK domestic manufacturing alternatives
- Policy alignment with Net Zero 2050 targets

## 📖 Usage Guide

### For Students

1. Start with `FBA/FBA_Week_01_*` notebooks sequentially
2. Practice with provided datasets
3. Reference `coursework/explain.md` for advanced concepts
4. Complete assessment notebooks for self-evaluation

### For Instructors

- All materials are self-contained and modular
- Datasets are included for reproducibility
- Markdown documentation provides context
- Assessment notebooks provide grading templates

### For Analysis

- Clone or download the repository
- Open notebooks in Jupyter environment
- Data files are relative-pathed for portability
- All dependencies are standard Python packages

## ⚙️ Configuration

- **Python Version**: 3.14.x (as specified in notebooks)
- **Notebook Format**: Jupyter Notebook (.ipynb)
- **Data Format**: CSV for tabular data
- **Documentation**: Markdown (.md)

## 📝 Notes

- All notebooks are self-contained and can run independently
- Data paths may need adjustment based on your local setup
- CSV files should be in the same directory as referenced notebooks
- Google Colab users should upload datasets before running cells

## 🔐 License

MIT License - See [LICENSE](LICENSE) file for details.

---

**Last Updated**: 2025
**Course Institution**: University of Nottingham
**Program**: Business Analytics (Foundational & Advanced)

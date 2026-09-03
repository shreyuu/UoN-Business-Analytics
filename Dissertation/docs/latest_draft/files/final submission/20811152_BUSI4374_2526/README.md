# MSc Business Analytics Dissertation

**University of Nottingham**  
**Module:** BUSI4374 – Data Driven Dissertation Project in Business Analytics  
**Academic Year:** 2025/26

## Dissertation

**Title:** Identifying feature drift using variable importance and MCR  
**Author:** Shreyash Chetan Meshram  
**Student ID:** 20811152

---

## Submission Contents

### 1. `20811152_BUSI4374_2526_main.ipynb`

Main experimental notebook for the rotating-hyperplane benchmark.

It contains the implementation and analysis used for:

- rotating-hyperplane concept-drift experiments;
- refitted SHAP feature-importance monitoring;
- frozen-model SHAP monitoring;
- random-forest ensemble vote-dominance monitoring;
- bootstrap null-band calibration;
- deployed-model performance degradation measurement;
- DDM and ADWIN baseline detectors;
- permutation negative controls;
- alarm-window and lead-time calculations; and
- generation of the principal experimental figures used in the dissertation.

### 2. `20811152_BUSI4374_2526_XOR.ipynb`

Boolean validation-harness notebook.

It contains the implementation used for:

- construction of the Boolean validation harness;
- controlled mutation of the feature structure;
- exhaustive enumeration of sufficient two-feature subsets;
- identification of relevant and strictly necessary features;
- refitted and frozen feature-importance analysis;
- ensemble disagreement / vote-dominance analysis; and
- validation of the proposed measurements against known ground truth.

### 3. `20811152_BUSI4374_2526.pdf`

Final submitted dissertation:

**Identifying feature drift using variable importance and MCR**

The dissertation is also submitted separately through the University's main dissertation submission link.

---

## Data

The supporting data are provided in:

`data/driftDatasets.zip`

This archive contains the drift benchmark datasets associated with the experimental work.

The rotating-hyperplane benchmark used by the main notebook contains **200,000 instances and 10 continuous features**.

The Boolean validation harness does not require a separate dataset because it is generated programmatically within `20811152_BUSI4374_2526_XOR.ipynb`.

---

## Computational Environment

The experiments were executed using:

- **Python:** 3.12.12
- **scikit-learn:** 1.9.0
- **NumPy:** 2.5.2
- **pandas:** 3.0.5
- **SHAP:** 0.52.0
- **River:** 0.25.0
- **matplotlib:** 3.11.1

The exact experimental configuration, random seeds, model parameters and calibration procedures are documented in **Appendix A** of the dissertation.

---

## Execution and Verification

Both notebooks were executed from top to bottom before submission.

The notebooks contain verification checks for the principal numerical results reported in the dissertation, including:

- null-band calibration values;
- degradation threshold and degradation window;
- candidate-signal alarm windows;
- DDM and ADWIN alarm locations;
- lead-time calculations; and
- negative-control outcomes.

The Boolean sufficient-subset enumeration is deterministic and is used to verify the reliance structure reported in the dissertation.

---

## Directory Structure

```text
20811152_BUSI4374_2526/
├── 20811152_BUSI4374_2526_main.ipynb
├── 20811152_BUSI4374_2526_XOR.ipynb
├── 20811152_BUSI4374_2526.pdf
├── data/
│   └── driftDatasets.zip
└── README.md
```

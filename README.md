# UoN-Business-Analytics

Coursework, practicals, and notes for the University of Nottingham Business Analytics MSc. The repo is not a software project — it is a collection of Jupyter notebooks, datasets, lecture PDFs, and submitted artefacts organised per module. Each top-level directory is an independent workspace.

## 📚 Modules

### `FBA/` — Foundational Business Analytics (BUSI4371)

Weekly Python practice (`FBA_Week_01_*` through `FBA_Week_10_*`), two practice tests (`FBA_Week_08_Python_Test_2023/2025`), and `balance.ipynb` for personal finance analysis. The submitted ML classification coursework lives under `coursework/` (`20811152_BUSI4371_2526.ipynb`) with serialised pipelines (`*.joblib`, `*.pkl`) and the marking rubric.

### `Machine-Learning-and-Predictive-Analytics/` — BUSI4373

Weekly practicals (`week-1/`, `Week 2 …` through `Week 11 …`) covering model evaluation, SVMs, feature construction in SQL, temporal data, model understanding, end-to-end ML, neural networks, causal inference, and foundation models. Submitted coursework under `cousework/` (directory name preserved as-is) operates on a multi-table retail dataset. Exam prep lives in `exam/`, `ML_NOTES/`, `Claude_ML_Cram_Sheet.md`, and `Claude_ML_Exam_Notes.md`.

### `Analytics-Specializations-and-Applications/` — BUSI4370

Two coursework submissions plus weekly material (`week-5/`–`week-7/`):

- **`BUSI4370_CW1/`** — customer segmentation via clustering. Multiple iterations coexist intentionally (`final_01.ipynb`, `final_02.ipynb`, `Customer_Segmentation_Technical_Notebook.ipynb`); the final submission is under `final/`.
- **`BUSI4370_CW2/`** — multi-stage social-media analytics pipeline. Notebooks in `notebooks/` run in order: `01_data_collection` → `02_data_cleaning` → `03_analysis` → `04_sentiment` → `05_topics_keywords` → `06_network_influencer` → `07_perceptual_map`. Outputs land in `outputs/`. This is the only module with a pinned `requirements.txt`.

### `D@S/` — Data at Scale

Databricks/SQL-flavoured notebooks (`shopping_data_small/`, `sql-test-2/`, `coursework/`) plus an exported Databricks HTML walkthrough of data cleaning and Web APIs.

### `Supply-Chain-planning-and-management/`

Non-code module: Mermaid flowcharts (`flowchart-1.md` … `flowchart-3.md`) covering solar panel supply chain analysis, policy frameworks, and risk layers, alongside lecture PDFs.

### `Leading-Big-Data-Business-Projects/` — BUSI4372

Group project deliverables: individual report PDF, group presentation (`.pptx`), recorded presentation (`.mp4`), and minutes of meeting (`.pdf`).

## ⚙️ Environment

- Shared `.venv/` at the repo root, **Python 3.14.0** (Homebrew). Activate with `source .venv/bin/activate` before running notebooks.
- Only `BUSI4370_CW2` has pinned dependencies:
  ```bash
  pip install -r Analytics-Specializations-and-Applications/BUSI4370_CW2/requirements.txt
  ```
  Notable pins: `pandas==3.0.2`, `numpy==2.4.4`, `scikit-learn==1.8.0`, plus NLP deps (`gensim`, `nltk`, `textblob`, `vaderSentiment`, `pyLDAvis`, `wordcloud`, `atproto`).
- Other modules use the ambient venv — install ad-hoc as needed:
  ```bash
  pip install pandas numpy matplotlib seaborn scikit-learn jupyter
  ```
- Launch with `jupyter lab` or `jupyter notebook`. Some notebooks were originally authored in Google Colab and may reference `/content/` paths that need adjusting locally.

## 🗂️ Conventions

- Datasets are colocated with the notebooks that use them; paths are relative — keep them that way for portability.
- `.gitignore` excludes most data formats wholesale (`*.csv`, `*.zip`, `*.pdf`, `*.xlsx`, `*.html`, `*.json`). Check before adding new data files.
- Submitted coursework artefacts use student-id-prefixed filenames (`20811152_*`) — preserve verbatim.
- Trained model artefacts (`*.joblib`, `*.pkl`) under `FBA/coursework/` are deliverables; do not re-train without being asked.
- Multiple iteration files (e.g. `final_01.ipynb`, `final_02.ipynb`, `main01.ipynb`) coexist intentionally.

## 🔐 License

MIT — see [LICENSE](LICENSE).

---

**Institution**: University of Nottingham
**Programme**: MSc Business Analytics

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

University of Nottingham Business Analytics MSc coursework. Not a software project — a collection of Jupyter notebooks, datasets, and PDFs organised per module. Treat each top-level directory as an independent workspace; there are no shared utilities, package manifests, or build steps spanning modules.

## Top-level modules

- `FBA/` — Foundational Business Analytics. Weekly practice notebooks (`FBA_Week_01_*` … `FBA_Week_10_*`) and `coursework/` (final ML classification submission `20811152_BUSI4371_2526.ipynb` with serialised `.joblib` / `.pkl` pipelines). CSVs live alongside notebooks; paths in cells are relative.
- `Machine-Learning-and-Predictive-Analytics/` — weekly practicals `week-1/` … `week-7/` plus `cousework/` (note: directory is misspelled — keep the spelling) with `main.ipynb` operating on a multi-table retail dataset (`customers.csv`, `products.csv`, `receipts.csv`, `receipt_lines.csv`, `stores.csv`).
- `Analytics-Specializations-and-Applications/` — two pieces of coursework:
  - `BUSI4370_CW1/` — customer segmentation (clustering); multiple iterations exist (`final_01.ipynb`, `final_02.ipynb`, `Customer_Segmentation_Technical_Notebook.ipynb`). The final submission lives under `final/`.
  - `BUSI4370_CW2/` — multi-stage social-media analytics pipeline. Notebooks under `notebooks/` are numbered and run in order: `01_data_collection` → `02_data_cleaning` → `03_analysis` → `04_sentiment` → `05_topics_keywords` → `06_network_influencer` → `07_perceptual_map`. Outputs (figures, intermediate CSVs) land in `outputs/`. This is the only module with a pinned `requirements.txt`.
- `D@S/` — Data at Scale. Databricks/SQL-flavoured notebooks (`shopping_data_small/`, `sql-test-2/`, `coursework/`) plus an exported Databricks HTML.
- `Supply-Chain-planning-and-management/` — non-code module: Mermaid flowcharts (`flowchart-1.md` … `flowchart-3.md`) and lecture PDFs.

## Environment

- Single shared `.venv/` at the repo root, Python **3.14.0** (Homebrew). Activate with `source .venv/bin/activate` before running notebooks or scripts.
- Only `BUSI4370_CW2` has a pinned dependency set (`Analytics-Specializations-and-Applications/BUSI4370_CW2/requirements.txt`) — install with `pip install -r Analytics-Specializations-and-Applications/BUSI4370_CW2/requirements.txt` when touching that pipeline. Notable pins: `pandas==3.0.2`, `numpy==2.4.4`, `scikit-learn==1.8.0`, plus NLP-specific deps (`gensim` from a git SHA, `nltk`, `textblob`, `vaderSentiment`, `pyLDAvis`, `wordcloud`, `atproto` for Bluesky data collection).
- Other modules rely on the ambient venv — install ad-hoc as needed (`pandas numpy matplotlib seaborn scikit-learn jupyter`).
- Run notebooks via `jupyter lab` or `jupyter notebook`; many were originally authored in Google Colab so cells may reference `/content/` paths that need adjusting.

## Working with notebooks

- Datasets are colocated with the notebooks that use them; relative paths are the convention. Don't refactor paths to be absolute — keep notebooks portable.
- The `.gitignore` excludes most data formats wholesale (`*.csv`, `*.zip`, `*.pdf`, `*.xlsx`, `*.html`, `*.json`, …). One explicit allow-list exists for `Analytics-Specializations-and-Applications/coursework-1/final/ASA_BUSI4370_20811152 /customer_segments_ASA_BUSI4370_20811152.csv` (note the trailing space in the directory name — preserve it). Before adding any data file, check it isn't ignored, and don't `git add -f` ignored artefacts unless the user asks.
- Coursework notebooks are submitted artefacts — preserve student-id-prefixed filenames (`20811152_*`) verbatim; don't rename or "clean up". Multiple iteration files (e.g. `final_01.ipynb`, `final_02.ipynb`, `main01.ipynb`) coexist intentionally; ask before consolidating.
- Trained model artefacts (`*.joblib`, `*.pkl`) are committed in `FBA/coursework/`. Treat them as the deliverable — re-train only when explicitly asked, and preserve the existing files.

## Conventions

- The repo also contains a `GEMINI.md` describing the same workspace for a different assistant; it predates several modules (no mention of `Machine-Learning-and-Predictive-Analytics` or `Analytics-Specializations-and-Applications`). Prefer this file and the README for current structure.
- `README.md` lists Python 3.14.x as the target — match that when writing new code.

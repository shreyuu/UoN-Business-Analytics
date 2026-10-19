# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

University of Nottingham MSc Business Analytics coursework (2025/26). Not a software project: Jupyter notebooks, datasets, figures and submitted artefacts organised per module. Treat each top-level directory as an independent workspace; no code is shared between modules. `README.md` is the human-facing overview.

## Top-level modules

- `Dissertation/` — BUSI4374 feature-drift study. Submitted notebooks (`*_main.ipynb` rotating-hyperplane benchmark, `*_XOR.ipynb` Boolean harness) are in `Dissertation/final submission/20811152_BUSI4374_2526/`, with a copy under `docs/latest_draft/files/final submission/`. Working notebooks are in `scripts/`, figures in `figures/`. Data: clone `vlosing/driftDatasets` into `Dissertation/driftDatasets/` (gitignored); the notebooks search parent folders for it and write figures to `../figures`.
- `FBA/` — BUSI4371. Weekly practice notebooks (weeks 1 and 6–10, two Week 08 tests), `balance.ipynb`, and `coursework/` (submission `20811152_BUSI4371_2526.ipynb`). `20811152_BUSI4371_2526.joblib` is the selected Decision Tree; `*_final_model.joblib` and `final_model.joblib` are Gaussian Naive Bayes; all were saved with scikit-learn 1.7.2. The `.pkl` pipelines exist only locally.
- `Machine-Learning-and-Predictive-Analytics/` — BUSI4373. The submission is `BUSI4373_CW/BUSI4373_20811152_2526.ipynb` (Databricks export; needs the course workspace `workspace.ml34`). `cousework/main.ipynb` is an empty stub (keep the misspelt folder). `BUSI4373_CW_databricks/` is the unmodified `default-python` bundle template. Weekly `Week N - …/` folders and `exam/` are gitignored; tracked practicals are in `other/`.
- `Analytics-Specializations-and-Applications/` — BUSI4370:
  - `BUSI4370_CW1/` — customer segmentation. Final: `final/ASA_BUSI4370_20811152 /` (five segments, RobustScaler); `main.py` is an earlier script (k = 6). Iteration notebooks coexist intentionally.
  - `BUSI4370_CW2/` — Bluesky brand-analytics pipeline; run `notebooks/01_…` to `07_…` in order. Only `outputs/figures/` is committed; `data/` and `outputs/tables/` are regenerated.
- `D@S/` — BUSI4369 Data at Scale: Databricks/SQL coursework, Tableau workbook, session PDFs.
- `Supply-Chain-planning-and-management/` — BUSI4496: Mermaid flowcharts and lecture PDFs.
- `Leading-Big-Data-Business-Projects/` — BUSI4372: group report, slides, recording, minutes.
- `Advanced-Operations-Analysis/` — BUSI4498, local only (PDF/DOCX, entirely gitignored).
- `fractal/` — scratch `main.py`, not coursework.

## Environment

- Separate venvs: root `.venv` (Python 3.14, general coursework), `Analytics-Specializations-and-Applications/BUSI4370_CW2/.venv` (3.14; its `requirements.txt` is an exact freeze without Jupyter), and `Dissertation/.venv` (3.12, pinned by `Dissertation/requirements.txt`; has no pip).
- The root `.venv` was moved from another path, so its `pip`/`jupyter` scripts have dead shebangs: use `.venv/bin/python3.14 -m pip` or `-m jupyter`, or recreate it.
- Run a notebook without modifying it: `jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=-1 "<notebook>" --output-dir /tmp/<dir>`.
- Many notebooks came from Google Colab or Databricks: `/content/` paths, `spark` and `%sql` cells won't run locally.

## Verification

- The dissertation notebooks contain canonical verification cells (asserts on the reported numbers); executing them is the regression test. CI: `.github/workflows/dissertation.yml` on a macOS runner, because forest-derived values differ on Linux (see `final_submission_audit.md`).
- There are no other tests, linters or CI.

## Working with notebooks

- Datasets sit next to the notebooks that use them; keep paths relative.
- `.gitignore` excludes most data and document formats (`*.csv`, `*.json`, `*.zip`, `*.pdf`, `*.docx`, `*.xlsx`, `*.pptx`, `*.pkl`, `*.html`) and re-includes specific submitted files with `!` lines. Run `git check-ignore -v <path>` before adding files; don't `git add -f` unless asked.
- Git LFS covers only `Machine-Learning-and-Predictive-Analytics/ML_NOTES/ML_NOTES.pdf`; don't broaden it.
- Submitted artefacts keep their `20811152_*` names and contents: document problems in the module README instead of editing graded notebooks, and don't re-train models unless asked.
- Quote paths with spaces or trailing spaces: `Dissertation/final submission/`, `ASA_BUSI4370_20811152 /`, `BUSI4370_CW2/final-submission /`.
- Never hardcode credentials. Bluesky logins use `input()`/`getpass()`; the Notion sync helper reads `Dissertation/.env` (template: `Dissertation/.env.example`).
- Rewriting a notebook with `json.dump(nb, indent=1, ensure_ascii=False)` keeps the diff small only if the file round-trips byte-identically; otherwise edit its lines in place.

## Conventions

- `AGENTS.md` mirrors this file for Codex; keep them in sync. `GEMINI.md` is older and incomplete.
- Target Python 3.14 for new coursework code, and 3.12 inside `Dissertation/`.

# BUSI4370 ASA — Coursework 1: Customer Segmentation

Market segmentation of a UK convenience-store chain's six-month transactional dataset (3,000 customers across four tables). Deliverable is a 5–7 segment solution with a cluster summary, pen profiles, and a `customer_number → segment_id` mapping for the marketing director.

Module: BUSI4370 Analytics Specialisations & Applications — University of Nottingham, 2025/26.

## Inputs

Four CSVs (samples kept under `data/`, full extract in `asa_cw1_data.zip`):

| File | Description |
| --- | --- |
| `customers_sample.csv` | One row per customer: basket count, quantity totals, total/average spend (£). |
| `baskets_sample.csv` | One row per basket: timestamp, quantity, spend (£), distinct categories. |
| `lineitems_sample.csv` | One row per item purchased: product id, category, quantity, spend (£). |
| `category_spends_sample.csv` | Per-customer spend (£) across 20 product categories. |

Currency columns are stored as `£`-prefixed strings and must be parsed before numeric work. The `BAKERY` column in `category_spends_sample.csv` is known-broken — recompute it from `lineitems` (see `main.py` §2). This is documented in `specifications/BUSI4370 CW1 QAs.pdf`.

## Pipeline

`main.py` is the canonical end-to-end script:

1. Load + parse currency, timestamps.
2. Recompute bakery spend from line items.
3. Engineer RFM features (`recency`, `frequency`, `monetary`, `avg_basket_spend`, `avg_items`).
4. Add per-category spend shares (`share_<category>`).
5. Log-transform skewed features, `StandardScaler`.
6. PCA at 85% variance retention.
7. Sweep k ∈ [2, 10] with KMeans; record inertia + silhouette → `elbow_plot.png`, `silhouette_plot.png`.
8. Fit final KMeans with `k_final = 6` (adjust after inspecting plots).
9. Export `cluster_summary.csv` and `customer_segments.csv` (`customer_number, segment_id`).

`RANDOM_STATE = 42` throughout for reproducibility.

## Notebooks

Multiple iterations are kept on purpose — do not consolidate without asking:

- `Coursework_1_clinic.ipynb` — early lab/clinic exploration.
- `Customer_Segmentation_Technical_Notebook.ipynb` — full technical write-up.
- `final_01.ipynb`, `final_02.ipynb` — submission iterations.
- `final/ASA_BUSI4370_20811152 /` (note the trailing space — preserve it) — submitted notebook, PDF, and final segment CSV.

## Running

From the repo root, with the shared `.venv` active (Python 3.14):

```bash
cd Analytics-Specializations-and-Applications/BUSI4370_CW1
python main.py
```

The script reads the sample CSVs from the working directory and writes plots and CSVs alongside them. For the notebooks, launch `jupyter lab` and open the file directly.

## Deliverables (per brief)

1. Report (PDF) with cover sheet (student ID, module, 2025/26).
2. Technical notebook.
3. `customer_segments.csv` mapping each `customer_number` to a `segment_id`.

Word limit 3,000 (excluding cover sheet). Submission deadline: 3pm, Thursday 5 March 2026. See `brief.md` and `specifications/` for the full rubric and Q&A.

## Outputs

- `elbow_plot.png`, `silhouette_plot.png` — k-selection diagnostics.
- `cluster_summary.csv` — per-segment customer count, avg recency/frequency/monetary.
- `customer_segments.csv` / `customer_segments_ASA_BUSI4370_20811152.csv` — final segment assignments.

CSV outputs are gitignored at the repo level except for the submission file under `final/ASA_BUSI4370_20811152 /`, which is explicitly allow-listed.

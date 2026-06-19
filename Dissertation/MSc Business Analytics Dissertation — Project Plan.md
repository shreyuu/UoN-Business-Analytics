# MSc Business Analytics Dissertation — Project Plan

**Module:** BUSI4374 — Data Driven Dissertation Project in Business Analytics (60 credits)
**Supervisor:** Gavin Smith — B79 North — gavin.smith@nottingham.ac.uk
**Primary topic:** Topic 3 — \*Identifying Feature Drift using Variable Importance and MCR**\*Backup topic:** Topic 6 — \*Evaluating Customer Segmentation via Consumer Stability**\*Final submission:** 3pm Thursday 3 September 2026 (Turnitin)
**Word count:** 8,000–15,000 (excl. references & appendices)
**Plan written:** 9 June 2026

---

## 0. The three things that matter most right now

1. **Proposal Form is due 3pm Monday 22 June 2026.** That is under two weeks away. Everything in Phase 0 below is time-critical.
2. **Confirm your topic with Gavin and lock in your first (“Refining your proposal”) meeting.** It is _your_ responsibility to reach out and arrange meetings. For routine support emails, the team only reads them **Fridays 9–11am**, so send anything non-urgent in that window and don’t expect instant replies otherwise.
3. **The “one week before” rule is a hard gate.** Work for each meeting must be emailed **at least one week before** the meeting, or the meeting can be cancelled and _not_ rescheduled. Build your whole timeline around this.

---

## 1. The research idea (Topic 3), in plain terms

**The problem.** In deployed models, the relationship between inputs and the target changes over time — _feature drift_ (a form of concept drift affecting P(y | X)). It can be gradual, sudden (e.g. COVID), or seasonal/cyclic. When it happens, models need retraining, but most drift detectors only react _after_ predictive performance has already dropped.

**Your angle (the contribution).** Detect drift earlier by watching **how the model uses its variables**, rather than waiting for accuracy to fall. Three candidate mechanisms to investigate:

- **(A) Data-point-level importance shift** — track SHAP (or permutation importance) distributions over time and detect when they move.
- **(B) Ensemble vote-dominance shift** — in a Random Forest, watch which trees/sub-models are “casting the winning votes” and detect when the dominant set changes.
- **(C) MCR / Rashomon-set shift** — use Model Class Reliance to detect when a _different_ model from the Rashomon set (the set of near-best models) is needed to maintain top accuracy, signalling the input–output relationship has moved.

**Data.** The benchmark concept-drift datasets at `github.com/vlosing/driftDatasets`. These include **synthetic** streams with _known_ drift points (use these to validate that your signal actually fires at the right time) and **real** streams (use these to demonstrate practical value). This is open data, so **research ethics approval is not required** — but confirm this with Gavin at the first meeting.

### Draft research questions (refine with Gavin)

- **RQ1.** When feature drift occurs, do variable-importance signals shift in a detectable way?
- **RQ2.** Do these signals shift _earlier_ than predictive performance degrades — i.e. do they give useful early warning (lead time)?
- **RQ3.** How do approaches A, B and C compare on detection delay, false-alarm rate, and lead time?

### Baselines to compare against

Performance-based detectors (DDM, ADWIN, Page–Hinkley) and a distribution-based detector (e.g. KS test on input features). Your importance-based detectors should be judged against these.

---

## 2. Literature to anchor the review

Map your reading into these clusters (this becomes the structure of your lit-review “story” — what exists, why it’s not enough, why your work is needed):

| Cluster                              | Why it matters                                | Starting points                                                    |
| ------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------ |
| Concept-drift taxonomy & surveys     | Defines real vs virtual drift; frames the gap | Gama et al. (2014); Lu et al. (2018)                               |
| Drift _detection_ methods            | Your baselines + the “reactive vs early” gap  | Gama et al. DDM (2004); Bifet & Gavaldà ADWIN (2007)               |
| Explainability / variable importance | The signal you’re proposing to use            | Lundberg & Lee SHAP (2017); Breiman permutation importance (2001)  |
| Rashomon sets & MCR                  | The novel detection mechanism                 | Breiman “Two Cultures” (2001); Fisher, Rudin & Dominici MCR (2019) |
| The benchmark datasets               | Justifies your data choice                    | Losing, Hammer & Wersing (2016)                                    |

Use **NUSearch** for peer-reviewed sources and the **Nottingham Harvard** referencing style throughout. Aim for the review to _synthesise_ (build an argument) rather than list paper-by-paper.

---

## 3. Dissertation structure & word budget

Targets from the NUBS structure table (you’re marked on content, not word count — these are guides):

| Section                                   | Target words | Core job                                                        |
| ----------------------------------------- | ------------ | --------------------------------------------------------------- |
| Abstract                                  | 250–500      | Problem, approach, main result in a few sentences               |
| Introduction (+ RQs)                      | 500–1,000    | Topic, focus, objectives, rationale                             |
| Literature Review                         | 2,500–4,000  | Synthesised argument leading to your RQs                        |
| Methodology (+ objectives)                | 1,000–2,500  | Data, feature definitions, the 3 detectors, evaluation strategy |
| Results                                   | 750–2,000    | Figures + factual description of findings                       |
| Discussion                                | 1,500–3,000  | What it means vs RQs, literature, and business use              |
| Conclusions, recommendations, future work | 500–2,000    | Summary, limitations, next steps                                |
| References / Appendix + Code              | —            | Harvard refs; **AI declaration**; replicable code               |

**Pass requirement:** a real analytics/coding component, with data source described, preprocessing justified, techniques justified, and a clear **train/validation/test (or drift-validation) strategy**. **To do well:** another MSc student should be able to approximately replicate your results from the write-up alone.

---

## 4. Timeline (anchored to the four supervision meetings)

Meeting dates are supervisor-dependent — **confirm exact dates with Gavin** and slot them in. The phases below are built backward from 3 September.

### Phase 0 — Now → 22 June · Proposal sprint _(URGENT)_

- [x] Email Gavin to confirm Topic 3 and arrange the **intro + first (“Refining your proposal”) meeting**.
- [x] Clone `vlosing/driftDatasets`; set up Python env (scikit-learn, `shap`, `river` for streaming/ADWIN).
- [ ] **Feasibility spike:** train a Random Forest on one synthetic dataset, compute SHAP, eyeball whether importance shifts near the known drift point. This de-risks the whole project before you commit.
- [ ] Skim 8–10 papers from §2; draft the RQs.
- [ ] **First supervision meeting:** refine objectives into a “do-able” project.
- [ ] If a secure N/LAB dataset is ever needed, sign the **N/LAB Data Sharing Agreement** (likely not needed for open driftDatasets — confirm).
- [ ] **Submit Dissertation Proposal Form via Moodle by 3pm Mon 22 June.**
- [ ] **Complete Supervision Record Form 1.**

### Phase 1 — Late June → early July · Literature review & foundations

- [ ] Write the **literature review chapter** (your “story” toward the RQs).
- [ ] Write a **2-page introduction** (purpose, objectives/questions).
- [ ] Prepare your **AI declaration**.
- [ ] **Email all of the above to Gavin ≥1 week before the early-July (2nd) meeting.**
- [ ] **Second meeting:** feedback on lit review + methodology discussion. Your **5-minute proposal presentation** typically happens here.
- [ ] After: revise lit review; begin drafting methodology. Confirm no ethics approval needed.
- [ ] **Complete Supervision Record Form 2.**

### Phase 2 — July · Methodology + build the pipeline

- [ ] Build: dataset loaders → periodic model retraining over windows → importance tracking (SHAP / permutation) → ensemble vote-dominance tracking → MCR/Rashomon detector → baseline detectors (DDM/ADWIN/PH/KS).
- [ ] Define evaluation metrics: **detection delay, false-alarm rate, lead time before performance drop.**
- [ ] Write the **methodology chapter**.
- [ ] **Email methodology chapter (+ code/implementation plan + AI declaration) ≥1 week before the late-July/early-Aug (3rd) meeting.**
- [ ] **Third meeting:** progress / methodology feedback.
- [ ] After: run _all_ experiments, collect results.
- [ ] **Complete Supervision Record Form 3.**

### Phase 3 — August · Results & discussion

- [ ] Finalise experiments; generate clean figures and tables.
- [ ] Write **Results** then **Discussion** (tie findings back to RQs, literature, and a business framing — e.g. retraining triggers / model-monitoring cost).
- [ ] **Email a Results or Discussion chapter (+ code as .zip + AI declaration) ≥1 week before the late-Aug (4th) meeting.**
- [ ] **Fourth meeting:** results discussion.
- [ ] **Complete Supervision Record Form 4.**

### Phase 4 — Late Aug → 3 Sept · Finalise & submit

- [ ] Write the **Conclusion** and the **Abstract** (write the abstract last).
- [ ] Refine every chapter; build table of contents, figure/table lists.
- [ ] Finalise **References (Harvard)**, **Appendix**, **AI declaration**, and **replication code**.
- [ ] **Target a complete draft ~2 weeks early (around 27 Aug)** per the module advice.
- [ ] Run the Turnitin checklist (below) and **submit before 3pm Thursday 3 September**.

> **Detailed feedback caveat:** Gavin gives in-depth feedback on **only two chapters** of his choosing across the four meetings. Treat every other chapter as something you finish independently — don’t bank on line-by-line feedback for all of them.

---

## 5. Writing standards (from the module’s writing guidance)

- **Don’t hedge.** “GenBank _is_ a searchable database,” not “_aims to_ provide.” Avoid “intends to / aims to / has the goal of.”
- **Active voice by default.** “The system tabulates results,” not “Results were tabulated.”
- **Tense signals status:** established facts in present tense; _your own_ new findings in past tense.
- **Don’t over-claim** — substantial claims need a citation.
- **Cut trivial steps** (where data was stored, etc.) unless needed to replicate.
- **Call it a “dissertation,” never a “paper.”**
- **Reference figures explicitly** (“Figure 3.1 shows…”), and **define acronyms** before using them — never expose raw variable names from code.
- **Subheadings must not directly follow headings** — put a sentence of text between them.

---

## 6. If results don’t come out (read this early, not in a panic)

A “no” answer is a legitimate dissertation: _importance-based signals may not reliably precede performance drop._ If so, the work becomes **why** — provided you’ve (1) justified features, (2) justified model choice, (3) tuned properly so it’s clearly an information limit not a training failure, (4) handled class imbalance / dimensionality / sparsity, and (5) argued from theory and literature why the signal might not lead performance. Decide the cutover point honestly, and route unfinished threads into **Future Work**. Knowing this now lets you keep good records throughout so the “no” story is defensible.

---

## 7. Submission logistics (Turnitin)

- Submit from a **laptop on Chrome**, well before 3pm — late = **−5 marks per working day**.
- **PDF** preferred; filename **under 40 characters, no spaces/special characters** (underscores OK).
- **Turn off Track Changes**; left-justified; avoid headers/multi-column.
- Extenuating Circumstances must be filed **before** the deadline; note late/extended work **won’t be marked in time for December graduation**.

---

## 8. Backup plan (Topic 6)

If Topic 3 proves infeasible after the Phase 0 spike, pivot to **Topic 6 — Evaluating Customer Segmentation via Consumer Stability** (dunnhumby _The Complete Journey_ dataset): segment customers, then study how they migrate between competing segments over time to judge segmentation quality and propose a stability-aware approach. Decide this _with Gavin at the first meeting_ — not later.

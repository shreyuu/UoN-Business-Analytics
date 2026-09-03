# Final Submission Audit

**Dissertation:** Identifying feature drift using variable importance and MCR
**Candidate:** Shreyash Chetan Meshram (20811152) — MSc Business Analytics, University of Nottingham
**Audit date:** 3 September 2026

---

## SUBMISSION STATUS

**READY FOR SUBMISSION — subject to one confirmation you must make yourself (word-count rule, see §9).**

All document, notebook and numerical checks pass: 65 of 65 automated checks, 0 failures. No material blocker remains in the files themselves. The single outstanding item is not a defect in the work but a rule I could not read, because the module handbook was not supplied.

---

## 1. Final files

| File | Notes |
|---|---|
| `dissertation_final_submission_READY.docx` | Primary deliverable. 73 pages, A4, validates clean against the original. |
| `dissertation_final_submission_READY.pdf` | Render used for visual verification. Secondary. |
| `main_final_draft_figures_simplified_FINAL.ipynb` | Executed outputs preserved; wording corrected. |
| `xor-validate_final_figures_simplified_FINAL.ipynb` | Executed outputs preserved; comments corrected. |
| `final_submission_audit.md` | This report. |

Originals were never overwritten.

---

## 2. Fixed

**Captions (Phases 8–9).** All 28 captions — 22 figures, 6 tables — split into two paragraphs. Paragraph 1 keeps Word's `SEQ` field and the `_Toc` bookmark in the `Caption` style and carries only a short title (4–12 words). Paragraph 2 carries the full explanatory text in a new `CaptionNote` style. No note contains a `SEQ` field, so neither automatic list can pull them in. No caption exceeds 14 words including its number.

Substantive detail was preserved rather than discarded. Where the original opening sentence was pure framing (Figure 3.1, "Why the measurement design determines what is observable"), it was folded into the title. Where it carried specifics — stream name, window count, panel structure — it was kept in the note. Nothing scientific was lost.

**S4 / reliance-structure description (Phase 7).** 15 edits across the Abstract, §3.3.2, §3.5.4, §3.9, §3.12, §4.2, §5.4.4, Appendix B.3 and the Table 3.1 caption.

The material defect was in Appendix B.3's pseudocode, which read:

> `for each subset S of {A, B, C, D, E}:`

implying all 32 subsets. `reliance_report` in fact iterates `combinations(FEATURES, 2)` — ten pairs — derives `relevant` as the union of features appearing in some sufficient **pair**, checks singletons in a separate loop, and tests necessity by leave-one-out `determines(snap, others)`. The pseudocode now reads `for each two-feature subset S of {A, B, C, D, E}:   (all 10)`, and the `singleton[t]` and `solvable[t]` lines the code actually computes have been added. Prose throughout now says "all ten two-feature subsets … exhaustively enumerated", with relevance defined from pair membership and necessity tested separately.

Your MCR framing needed no repair. §2.6, §3.5.4, §4.2, §5.4.4 and B.3 already stated correctly that no Rashomon set is enumerated under a loss tolerance and no MCR interval is estimated. That was left alone.

**Acknowledgements (Phase 5).** Added as an unnumbered `Heading1` section after the Abstract. 101 words, one page.

**Declaration of LLM Assistance (Phase 6).** Added as an unnumbered `Heading1` section after Acknowledgements. 271 words, one page, five parts (introduction, used for, not used for, tools, authorship). Sub-headings are bold body paragraphs with no outline level, so they stay out of the Table of Contents while the section itself appears as an unnumbered entry.

This also repaired a live dangling cross-reference: §3.11 already stated that AI use "is recorded in the accompanying declaration", and no such declaration existed.

**Abstract (Phase 4).** Compressed from 327 to 322 words and now fits one page. `P(X)` and `P(y | X)` were made explicit where the text previously said "stationary input distribution" and "the conditional relationship". Every finding listed in your brief is retained: rotating hyperplane, Boolean harness, refitted SHAP, frozen SHAP, vote dominance, DDM, ADWIN, stationary P(X) with changing P(y|X), labels required for refitting, the theoretical prediction of frozen-signal silence, the single-run qualification, and the one-window degradation sensitivity.

**Front-matter order (Phase 2).** Title → Abstract → Acknowledgements → Declaration → Contents → List of Figures → List of Tables → Chapter 1. All six front-matter sections are unnumbered. No "Chapter 0" exists. `Heading1` carries `outlineLvl 0` with no numbering attached, so Acknowledgements and the Declaration appear as unnumbered TOC entries automatically.

**Fields (Phases 10, 19).** All three lists remain genuine automatic fields — `TOC \o "1-3"`, `TOC \c "Figure"`, `TOC \c "Table"`. Nothing was converted to manual text and no page number was typed by hand.

Because LibreOffice does not regenerate Word index fields on conversion, the cached display content was stale after the caption restructuring. I rebuilt the cached entries programmatically and iterated — rebuild, render, re-measure, rebuild — until the page assignments stopped moving, which took three passes. Page numbers were read out of the render, never invented. `updateFields` is set to `true` and all three field starts carry `w:dirty="true"`, so Word refreshes everything on open regardless.

**Notebook wording (Phases 11, 13).** Main notebook: the opening description no longer claims "Label-free variable-importance and Rashomon-style signals", and now states that only the frozen-model signals are label-free while the refitted signal requires labels for the current window. The heading "Label-Free Signal Definitions" became "Signal Definitions".

XOR notebook: three comment corrections. The material one was `"n_pairs": len(sufficient_pairs),  # size of the Rashomon set` — calling the sufficient-pair count the size of a Rashomon set, when no Rashomon set is enumerated anywhere. The necessity comment was reworded to describe the structural property without implying an MCR bound, and the `cols -> Y` comment now says the columns *jointly determine* Y rather than describing it as game-theoretic notation, which risked reading as a logical AND.

Only Markdown and comments were touched in both notebooks. No analytical code was modified, so the saved outputs remain valid.

The commented absolute paths (`/Users/shreyu/...`) were already removed in the versions you re-uploaded. Zero absolute paths remain in either notebook's source.

**Word count (Phase 15).** Recalculated and the title-page statement rewritten so the number and its exclusion list are internally consistent. See §9 — this needs your confirmation.

---

## 3. Numerical verification

Both notebooks were re-executed by you between audit rounds. Both now pass their canonical verification cells with zero error outputs, and every value below was read from those saved outputs.

| Item | Expected | Notebook | Result |
|---|---|---|---|
| Benchmark dataset size | 200,000 × 10 | 200,000 × 10 | **PASS** |
| Class balance | 100,065 / 99,935 | 100,065 / 99,935 | **PASS** |
| Windows | 200 @ 1,000 | 200 | **PASS** |
| Deployed-model guard | predictions & trees unchanged | True / True | **PASS** |
| OOB reference | 0.8330 | 0.8330 | **PASS** |
| Degradation threshold | 0.8130 | 0.8130 | **PASS** |
| Degradation window | 8 | 8 | **PASS** |
| Accuracy at window 8 | 0.8100 | 0.8100 | **PASS** |
| Margin at window 8 | 0.0030 | 0.0030 | **PASS** |
| Refitted SHAP alarm / lead | window 1 / +7 | window 1 / 7 | **PASS** |
| Frozen SHAP alarm | none sustained | None | **PASS** |
| Mean vote dominance alarm | none sustained | None | **PASS** |
| DDM alarm | window 1, instance 1,748 | window 1, 1,748 | **PASS** |
| ADWIN alarm | window 14, instance 14,407 | window 14, 14,407 | **PASS** |
| DDM / ADWIN total alarms | 2 / 8 | 2 / 8 | **PASS** |
| Refitted SHAP null band | 0.1874 | 0.1874 | **PASS** |
| Frozen SHAP null band | 0.2162 | 0.2162 | **PASS** |
| OOB dominance reference / band | 0.7244 / 0.0189 | 0.7244 / 0.0189 | **PASS** |
| In-sample dominance (superseded) | 0.9372 / 0.0046 | 0.9372 / 0.0046 | **PASS** |
| Permuted refitted SHAP alarm | window 106 | window 106 | **PASS** |
| DDM permuted controls | w2 / w1 / silent | 2,173 / 1,157 / never | **PASS** |
| ADWIN permuted controls | silent ×3 | never ×3 | **PASS** |
| Frozen error stream | — | 51,557 / 199,000 (0.259) | **PASS** |
| Importance swing (Fig 3.2) | 0.417 / 0.035 | 0.417 / 0.035 | **PASS** |
| Boolean sufficient-pair structure | 6, 3×9, 6, 3×9, 4 | identical | **PASS** |
| D strictly necessary from | P2.01 | P2.01 | **PASS** |
| Refitted / frozen harness accuracy | 1.00 / 0.50 | 1.00 / 0.50 | **PASS** |
| Harness null bands | 0.103 / 0.071 | 0.1027 / 0.0712 | **PASS** |
| Harness first responses | P1.02 / P1.02 / P1.09 | P1.02 / P1.02 / P1.09 | **PASS** |
| Feature D SHAP (refitted / frozen) | 0.154→0.500 / 0.154→0.025 | identical | **PASS** |

Also verified as consistent between notebooks and dissertation: 100 trees on the benchmark and 300 on the harness, 100 bootstrap replicates of window 0, permutation seeds 0/1/2 for the detectors and 0 for the joint control, River defaults for both detectors, the out-of-bag score guard, 21 snapshots of 100 rows, and the `start=1` exclusion of window 0.

**No contradictory number remains anywhere in the dissertation.** A scan for stale values found none.

### A note on platform reproducibility

Before you re-ran the notebooks, I attempted independent verification in a Linux x86-64 container using the exact Appendix A.1 library versions and the dataset fetched from `vlosing/driftDatasets`. The dataset matched exactly, but the forest-derived values did not: OOB reference came out 0.8320 rather than 0.8330, and on the harness the frozen-SHAP first response shifted from P1.09 to **P1.08** — a reported result, not merely a calibration constant.

Structural results were unaffected: snapshot count, sufficient-pair sequence, D's necessity from P2.01, and refitted accuracy 1.00 all reproduced identically, because they are `groupby` combinatorics with no floating-point dependence.

This is scikit-learn's compiled tree splitter behaving differently across OS and architecture. It is worth knowing, because it means **your macOS environment is the authoritative one** and re-running elsewhere will not reproduce the canonical values. Appendix A.1 correctly pins the library versions; you may wish to note the platform too.

---

## 4. Notebook verification

| | main | xor |
|---|---|---|
| Cells (total / code) | 51 / 30 | 40 / 23 |
| Execution-count range | 1–30 | 24–46 |
| Sequential execution | **PASS** | **PASS** |
| Error outputs | **0** | **0** |
| Canonical assertion cell | **PASS** | **PASS** |
| Saved outputs | **YES** (22 cells) | **YES** (18 cells) |
| Portable paths | **PASS** | **PASS** |

One residual observation. The XOR notebook's counts run 24–46. They are sequential, but they do not start at 1, so the kernel had prior activity — it was a run-through rather than a restart-and-run-all. Appendix A.6 states that both notebooks "were restarted and executed from top to bottom in a single pass, with sequential execution counts and no errors". That is now literally true of the main notebook. For the XOR notebook it is defensible but not beyond question. **A Restart & Run All on the XOR notebook would reset its counts to 1–23 and remove any doubt.** This is the one thing I would still do if you have ten minutes.

---

## 5. Document verification

| Item | Value |
|---|---|
| Final page count | 73 |
| Eligible word count (as printed) | 13,910 |
| Title-page statement | "Word count: 13,910 (abstract and main text; excludes title page, acknowledgements, declaration, contents, lists, tables, captions, references and appendices)" |
| Abstract | 1 page (p2) |
| Acknowledgements | **YES** — 1 page (p3), 101 words |
| LLM Declaration | **YES** — 1 page (p4), 271 words |
| TOC automatic | **YES** |
| TOC page numbers verified | **YES** |
| List of Figures automatic / compact | **YES** / **YES** — 1 page (p7), 22 entries, one line each |
| List of Figures page numbers verified | **YES** |
| List of Tables automatic / compact | **YES** / **YES** — 8 lines (p8) |
| List of Tables page numbers verified | **YES** |
| Figures / tables | 22 / 6 |
| References verified | **YES** — 41 entries |
| Appendices verified | **YES** — A (p70–71), B (p72–73) |
| Tracked changes | **zero** |
| Comments | **zero** |
| Unexpected blank pages | **zero** |
| Clipping / overlap | **zero** |
| Page size / margins / font | A4 · 1 inch all round · Verdana 11pt · 1.5 line spacing |

**Page numbers were verified individually, not assumed.** All 119 cached `PAGEREF` values were checked against the rendered PDF by confirming each bookmarked heading or caption actually appears on the page its entry claims: **119 correct, 0 wrong.**

Pages were inspected visually as images, not only as XML. The title page is balanced and uncrowded. Figure pages show the intended structure — image, short bold centred caption, indented smaller-font note — with captions attached to their figures and no clipping or overlap.

### References audit (Phase 16)

Alphabetical order clean across all 41 entries. No duplicates. Every entry is cited at least once in the text, and every in-text citation resolves to an entry. Breiman 2001a and 2001b are both cited and correctly disambiguated. Spot-checked and correct: Dong and Rudin 2020, Fisher/Rudin/Dominici 2019, Lundberg and Lee 2017, Lundberg et al. 2020, Pedregosa et al. 2011, Saunders/Lewis/Thornhill 2019, Pawlicki/Kozik/Choraś 2026, Losing/Hammer/Wersing 2016, Montiel et al. 2021, and the DDM (Gama et al. 2004) and ADWIN (Bifet and Gavaldà 2007) sources.

Five entries carry no DOI or URL: Baena-García et al. 2006, Covert et al. 2020, Lundberg and Lee 2017, Pedregosa et al. 2011, Saunders et al. 2019. All five are NeurIPS proceedings, JMLR, or a book, where absence of a DOI is expected rather than an omission. No action taken. No new literature was introduced.

### Minor cosmetic item

Page 41 carries only two lines — the tail of the final bullet in §3.12, immediately before Chapter 4 begins on a fresh page. It is a widow, not a defect, and no content is affected. I left it rather than tighten body line spacing to chase it, since that could breach a spacing rule I cannot read. If you want it gone, the safest fix in Word is to trim a dozen words from the last §3.12 bullet, then refresh fields.

---

## 6. Scientific consistency

Confirmed:

- Dissertation agrees with the executed notebooks throughout; no contradictory value remains.
- The S4 description now matches the actual implementation: ten two-feature subsets exhaustively enumerated, relevance from pair membership, singleton sufficiency checked separately, necessity by leave-one-out.
- No unsupported MCR claim remains; "no Model Class Reliance interval is estimated anywhere in this dissertation" is retained.
- No benchmark S4 claim remains; S4 carries no benchmark alarm, no lead time, and no entry in the benchmark permutation control.
- No claim that refitted SHAP beats DDM. Both alarm at window 1 and the tie is stated explicitly.
- The frozen-model observability argument remains correctly qualified: frozen-signal silence is presented as theoretically predicted, not as a failure.
- The single-run limitation remains explicit, as do two synthetic sources, one learner family, no multi-stream replication, one window length, empirical null-band calibration, no significance interpretation, no multiple-testing control, qualitative negative controls, differing permutation procedures between candidate signals and baselines, no estimated false-positive rate, the one-window degradation resolution, that refitted SHAP requires labels, that ADWIN alarms after measurable degradation, that S4 is harness-only, and that no production readiness is claimed.
- The Boolean harness is still explicitly *not* offered as pure real concept drift; its realised input support changes, and the rotating hyperplane is identified as the arm serving that role.

No claim was strengthened during editing.

---

## 7. Phase 0 — university requirements NOT verified

**The handbook and module guidance were never uploaded.** Absent: the NUBS MSc Dissertation Handbook, `MSc Business Analytics Dissertation_2526.pdf`, the supervisory schedule, and the two writing-guidance PDFs.

I therefore could not establish the official rules for word-count inclusions, font, size, line spacing, margins, page size, front-matter order, title-page layout, or whether the LLM declaration belongs inside the dissertation or on a separate form. I did not guess.

What is verified from the file itself: A4 (11906 × 16838 twips), 1-inch margins, Verdana 11pt default, 1.5 line spacing. These were the established style and were preserved.

Two judgment calls to check against the handbook if you have it:

1. **Declaration bullet spacing.** To bring the Declaration onto one page I set its bullet list to 1.15 line spacing; body text remains 1.5 throughout. If a uniform 1.5 is mandated everywhere, revert this and let the Declaration run to two pages.
2. **Front-matter order.** I used the order in your brief. If the handbook mandates another arrangement, it takes precedence.

---

## 8. Submission-package check

| Item | Status |
|---|---|
| Final dissertation (DOCX) | Ready |
| Final dissertation (PDF) | Ready |
| Main notebook | Ready, executed, canonical cell passing |
| XOR notebook | Ready, executed, canonical cell passing |
| LLM declaration | Now embedded in the dissertation (p4) |
| Ethics | §3.11 states no human participants, no personal data, no approval required; proposal form countersigned 22 June 2026. **Confirm the signed form is on record where the module expects it.** |
| Rotating-hyperplane dataset | **Not bundled.** §3.10 cites Losing, Hammer and Wersing (2016) as the source. I confirmed the files are publicly retrievable from `vlosing/driftDatasets` at `artificial/hyperplane/` and that they reproduce the exact canonical shape and class balance. Decide whether the module wants the data files, or the citation and path as reproducible acquisition instructions. |
| Figures | Written by the notebooks to `../figures/`. Confirm whether the module wants them submitted separately. |

I have not fabricated any missing document.

---

## 9. Remaining manual actions

**1. Confirm the official word-count rule. This is the only item that could matter for a penalty.**

Your previous title page read *13,850, excluding title page, tables, figures, appendix and table of contents* — a list that does **not** mention references. Under that rule as literally written, the count is **15,679**, which exceeds a 15,000 ceiling. The 13,850 figure is only reachable if references are also excluded.

Measured breakdown of the final document (18,814 words total):

| Component | Words |
|---|---|
| Main text, Chapters 1–6 | 13,587 |
| Abstract | 323 |
| References | 1,208 |
| Appendices | 1,232 |
| Caption notes | 943 |
| Table of Contents | 424 |
| Table content | 289 |
| LLM Declaration | 271 |
| Figure/table captions | 189 |
| List of Figures | 155 |
| Acknowledgements | 101 |
| Title page | 58 |
| List of Tables | 34 |

Resulting figures under different rules:

- Abstract + main text only → **13,910** ← printed on the title page
- Main text only → 13,587
- Adding references back → 15,118
- Under the old parenthetical as literally written → 15,679

I set the title page to 13,910 with a parenthetical that now names every exclusion including references, so the number and the statement agree. **If references are not excluded by your module's rule, you are over 15,000 and must act.**

**2. Open the DOCX in Word once, let fields refresh, and save.** Word will update the TOC, both lists and all page numbers on open because `updateFields` is set. LibreOffice pagination can differ from Word's by a page on some sections, and Word's pagination is authoritative. The cached numbers I wrote are verified correct against the LibreOffice render, so any change should be nil or a single page.

**3. Restart & Run All the XOR notebook** so its execution counts start at 1 rather than 24. See §4. Optional but cheap, and it makes Appendix A.6 unambiguous.

**4. Confirm the ethics form and dataset expectations** per §8.

**5. If you have the handbook, check the two judgment calls in §7.**

# OraDigit Imaging AI Weekly Brief — November 16, 2026

**Status:** Published research note  
**Coverage window:** November 10–16, 2026  
**Prepared for:** OraDigit

## Executive signal

The strongest signal is a combination of **PSMA PET therapy-decision research** and **a major imaging supplier's move into interpretive AI**. Neither a retrospective algorithm nor FDA clearance establishes improved patient outcomes, reimbursement, or routine deployment. Prioritize validation and workflow economics over launch claims.

## 1. PET/CT and molecular imaging

### 1. PSMA radiopharmaceutical therapy: a PET-sparing decision rule

**Changed (November 12; peer-reviewed research):** The *Journal of Nuclear Medicine* published [SPARE](https://doi.org/10.2967/jnumed.126.273398), a retrospective evaluation of a SPECT/CT- and PSA-guided rule after cycle 2 of lutetium-177 PSMA therapy in 142 men. The authors report that interim PSMA PET could have been omitted for 84.5% under the proposed pathway, with 91.1% agreement with actual treatment decisions in the evaluable cohort. This is a proposed clinical decision algorithm, **not an FDA-cleared AI product**.

**Why it matters:** Post-therapy SPECT/CT may become a more structured response signal, potentially changing the volume and timing of repeat PET. Agreement with historical decisions is not proof of equivalent outcomes or safe PET omission.

**OraDigit decision:** Prototype a prospective, clinician-overridden response dashboard; require discordance review, treatment-outcome follow-up, and tracer/protocol harmonization before proposing PET reduction.

### 2. Report-informed AI for PSMA PET/CT segmentation

**Changed (November 12; early evidence):** A [JNM study](https://doi.org/10.2967/jnumed.126.272702) tested clinical-report semantics in a vision-language lesion-segmentation workflow. In a 284-case study with a 41-case held-out test set, report guidance reduced false-positive lesions by roughly 3–4 per case but traded away voxel-level sensitivity; matched-lesion contour accuracy did not improve.

**Why it matters:** Report text can filter false positives, but a model that consumes the report is not independent of the interpreting clinician. Leakage and workflow timing matter.

**OraDigit decision:** Evaluate independent image-only and report-assisted modes separately; measure missed lesions, false-positive review burden, and prospective performance across sites.

### 3. Copper-64 PSMA PET receives expedited-development designation

**Changed (November 12; sponsor announcement):** [Clarity Pharmaceuticals reports](https://www.claritypharmaceuticals.com/news/btd/) FDA Breakthrough Therapy designation for investigational Cu-64 SAR-bisPSMA PET in suspected biochemical recurrence of prostate cancer. This is a **radiopharmaceutical, not AI**, and designation is **not approval or coverage**. The sponsor describes favorable early comparative imaging results; pivotal outcomes remain pending.

**Why it matters:** Longer imaging windows and differing tracer kinetics would complicate longitudinal quantification and algorithm portability if the agent reaches practice.

**OraDigit decision:** Design PET metadata and validation around tracer, uptake interval, scanner, reconstruction, and reference standard; monitor trial readouts before making adoption claims.

### 4. FET brain PET receives appropriate-use criteria

**Changed (November 12; society guidance):** [JNM published appropriate-use criteria](https://doi.org/10.2967/jnumed.126.274081) for fluorine-18 floretyrosine PET in primary brain tumors, including appropriate scenarios for biopsy planning and distinguishing viable tumor from treatment effect. Guidance does not itself confer reimbursement.

**OraDigit decision:** Map ordering indications, prior MRI findings, structured interpretation, and payer documentation into any neuro-oncology PET workflow.

## 2. Radiology workflow and vendor watch

### 5. Bracco enters the interpretive-AI workflow

**Changed (November 13; clearance plus vendor announcement):** [Bracco and Avicenna.AI announced](https://www.bracco.com/article/bracco-and-avicennaai-announce-fda-clearance-uptunitytm-aneurysm) UPTUNITY Aneurysm under FDA 510(k)s K262062 and K262147. The [FDA K262062 summary](https://www.accessdata.fda.gov/cdrh_docs/pdf26/K262062.pdf) describes CINA-Aneurysm as a concurrent aid for head-CTA saccular aneurysms larger than 3 mm, with triage, localization, and measurement. Its retrospective standalone validation included 423 cases; an eight-reader crossover study assessed assisted reading. This is **clearance and controlled evaluation, not demonstrated real-world adoption**. The primary assisted-reader AUC comparison did not establish superiority (p=0.075).

**Why it matters:** A contrast supplier now packages interpretive AI within its imaging relationships, raising the importance of distribution and PACS-integrated review.

**OraDigit decision:** Compare partner versus build for CTA alert orchestration; require site-specific alert burden, turnaround time, false-negative, and follow-up audits rather than extrapolating reader-study gains.

## 3. Other modalities and regulation

**Lower-priority clearance:** [FDA K261512](https://www.accessdata.fda.gov/cdrh_docs/pdf26/K261512.pdf) covers Naitive OsteoSight Spine, an opportunistic low-bone-density assessment aid on routine frontal chest/spine radiographs for adults 50+. The [November 12 vendor announcement](https://naitive.com/news/fda-510(k)-clearance-osteosight-spine) is not evidence of deployment or fracture-outcome benefit. Consider only if OraDigit expands into incidental-finding pathways.

**U.S. reimbursement:** No new imaging-AI-specific Medicare coverage change was verified in this window. Do not infer payment from any clearance, designation, or society criteria above.

## Strategic takeaways

- **Build:** PET/SPECT therapy-response data plumbing, provenance, and clinician-review interfaces.
- **Partner:** Evaluate distribution through established imaging vendors, while retaining vendor-neutral workflow and performance auditing.
- **Monitor:** Prospective SPARE validation, PSMA segmentation external testing, Cu-64 pivotal data, and actual site deployments.
- **Avoid:** Claiming retrospective PET avoidance as proven safe, treating designation as approval, or treating clearance as adoption.

## Evidence gaps

Independent prospective outcomes and cost analyses for SPECT-guided PET omission; external and temporal validation of report-informed segmentation; actual clinical deployment and alert-burden data for UPTUNITY; coverage and payment details for new agents and applications.

## Sources

1. Kassas et al., *J Nucl Med*, November 12, 2026 — https://doi.org/10.2967/jnumed.126.273398
2. Pouromidi et al., *J Nucl Med*, November 12, 2026 — https://doi.org/10.2967/jnumed.126.272702
3. Clarity sponsor announcement, November 12, 2026 — https://www.claritypharmaceuticals.com/news/btd/
4. Johnson et al., *J Nucl Med*, November 12, 2026 — https://doi.org/10.2967/jnumed.126.274081
5. FDA CINA-Aneurysm 510(k) summary — https://www.accessdata.fda.gov/cdrh_docs/pdf26/K262062.pdf
6. Bracco/Avicenna announcement, November 13, 2026 — https://www.bracco.com/article/bracco-and-avicennaai-announce-fda-clearance-uptunitytm-aneurysm
7. FDA OsteoSight Spine 510(k) summary — https://www.accessdata.fda.gov/cdrh_docs/pdf26/K261512.pdf

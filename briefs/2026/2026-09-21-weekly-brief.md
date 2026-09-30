# OraDigit Imaging AI Weekly Brief — September 21, 2026

**Status:** Published research note  
**Coverage window:** September 14–21, 2026  
**Prepared for:** OraDigit

## Executive signal

This week produced two consequential regulatory signals. First, **MICSI-PET received FDA 510(k) clearance with a decision date of Sept. 11**, strengthening the trend toward software-assisted quantitative neuro-PET. Second, the FDA's Sept. 17 final order retained premarket notification requirements for the radiology CAD/triage categories addressed by a petition seeking partial exemption. Imaging AI is expanding, but intended use, validation and lifecycle controls remain central.

## 1. PET: MICSI-PET receives 510(k) clearance

**Verified development:** FDA 510(k) K261305 lists MICSI-PET from Microstructure Imaging with a decision date of Sept. 11, 2026 and a substantially equivalent determination.

Secondary reporting describes structural-MRI-guided enhancement and quantitative outputs for amyloid, tau and FDG PET. Those details should always be interpreted through the cleared labeling and official record.

**Why it matters:** neurodegenerative imaging is becoming increasingly quantitative, with value moving toward reproducible regional measurements, standardized scales and longitudinal comparison.

**OraDigit implication:** a PET analytics layer could verify required inputs, track acquisition/reconstruction metadata, monitor longitudinal comparability, normalize report structure and flag unsuitable studies.

Source: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K261305

## 2. Regulation: FDA retains premarket review for targeted radiology AI categories

**Verified development:** On Sept. 17, 2026, FDA published a final order concerning a petition for partial exemption from 510(k) requirements for certain radiology computer-aided detection/diagnosis and triage/notification devices. ACR reported that the petition was denied and the order completed the process.

**Why it matters:** common radiology AI should not be assumed to become unregulated software.

**OraDigit implication:** classify each planned function early: administrative workflow, clinical decision support, image processing, triage, diagnostic support or quantitative analysis.

Source: https://www.acr.org/News-and-Publications/2026/fda-final-order-ai-cad-petition

## 3. CCTA: acquisition quality is the hidden dependency

Downstream coronary analysis depends on source-study quality. Relevant failure modes include heart-rate variability, motion, poor contrast timing, heavy calcium, unsuitable reconstruction, incomplete indication and missing series/metadata.

**OraDigit opportunity:** create a pre-processing quality gate that determines whether a CCTA is technically and administratively ready for advanced analysis.

## 4. Broader CT: triage continues to broaden

FDA 510(k) K260906 for a2z-Abdo-Triage has a Sept. 16, 2026 decision date and is classified as radiological computer-assisted triage and notification software.

**Why it matters:** as products handle more findings, operational value increasingly depends on routing, prioritization and escalation.

Source: https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K260906

## Strategic takeaways

- **Build:** quantitative QA and workflow controls around PET and CCTA.
- **Partner:** with cleared image-analysis vendors where core algorithms are commoditizing.
- **Monitor:** regulatory product classification before claims expand.
- **Avoid:** assuming clearance proves superior clinical outcomes or guarantees reimbursement.

## Evidence gaps

Independent deployment and outcomes evidence may lag regulatory authorization. Adoption should be judged from prospective workflow data, not clearance alone.

## Sources

1. FDA K261305 — https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K261305
2. ACR regulatory summary — https://www.acr.org/News-and-Publications/2026/fda-final-order-ai-cad-petition
3. FDA K260906 — https://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpmn/pmn.cfm?ID=K260906
4. Radiology Business PET context — https://radiologybusiness.com/topics/medical-imaging/nuclear-medicine/pet-ct/fda-clears-ai-platform-pet-imaging-enhancement-and-quantification

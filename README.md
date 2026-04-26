# DengueML: High-Throughput Transcriptome Analysis Framework

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
DengueML is a formal computational framework designed for the high-throughput analysis of Dengue virus (DENV) transcriptomic data. The pipeline integrates differential expression analysis (DEA) with multi-algorithmic machine learning (ML) to identify diagnostic biomarkers, perform functional annotations, and map therapeutic targets.

This repository provides the implementation used in the study: *"A comprehensive machine learning framework for high-throughput Dengue transcriptome analysis, biomarker discovery, functional annotation, and visualization of therapeutic targets."*

## Methodology
The framework follows a systematic approach to host-virus interaction modeling:
1. **Bioinformatics Processing:** Normalization and DEA using `DESeq2` on RNA-seq counts (GSE140809).
2. **Machine Learning Pipeline:** Comparative evaluation of Random Forest, XGBoost, and LASSO-regularized Logistic Regression.
3. **Feature Selection:** Prioritization of discriminative gene signatures through intersectional analysis of ML importance scores and statistical significance.
4. **Systems Biology:** Protein-Protein Interaction (PPI) network construction and hub gene identification.
5. **Drug Repurposing:** Identification of inhibitory compounds via DrugBank and DisGeNET mapping.

## Key Performance Metrics
The models were validated using stratified cross-validation and achieved the following high-fidelity results:
* **Random Forest:** Accuracy: 0.978 | AUC: 0.999
* **LASSO Logistic Regression:** AUC: 0.999 | Log-loss: 0.067
* **XGBoost:** Accuracy: 0.971 | AUC: 0.997

## Installation
The framework requires **Python 3.10**. Install the necessary dependencies via pip:

```bash
pip install scikit-learn==1.6.1 xgboost pandas numpy matplotlib seaborn joblib
```

##Run
```bash
main.py
```

## Repository Structure
```text
├── notebooks/         # End-to-end analysis (Preprocessing to ML)
├── scripts/           # Modular Python scripts for model training
├── data/              # Metadata and processing links (GSE140809)
├── outputs/           # High-resolution figures and performance logs
└── README.md          # Project documentation
```


## Primary Biomarkers & Hub Genes
The framework identified **33 critical biomarkers**, with the following top regulatory hub genes:
* `GBP1`, `CXCL11`, `IFI27`, `USP18`, `MX1`, `AIM2`, `LAP3`, `SERPING1`.

## Citation
If you utilize this framework or its findings in your research, please cite the following publication:

> **Khandocar, M. P.** (2025). *A comprehensive machine learning framework for high-throughput Dengue transcriptome analysis, biomarker discovery, functional annotation, and visualization of therapeutic targets.* [In Press/Journal Details].

## Contact
For technical inquiries or collaboration, please contact:

**Md. Parvez Khandocar** Department of Biomedical Engineering, Islamic University, Kushtia, Bangladesh  
**Email:** [parvez.iu.bme@gmail.com](mailto:parvez.iu.bme@gmail.com)

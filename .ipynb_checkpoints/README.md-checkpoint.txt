# ECG Signal Processing Pipeline: Emotional Arousal & Cognitive Performance

> **M.Sc. Thesis in Cognitive Psychology | Phase 1: Physiological Feature Extraction**

## 📌 Project Context
This repository hosts the **Signal Processing Phase** of a Master's thesis titled:
*"Predicting Cognitive Performance based on Emotional Arousal using Electrocardiography Data."*

The project investigates the link between physiological arousal and cognitive functioning. This pipeline establishes the methodological framework for processing raw ECG signals recorded during **video-induced emotional arousal tasks**, transforming biological signals into validated predictors for subsequent Machine Learning modeling.

## 📚 Data Source
The analysis utilizes raw data from the **ECSMP Dataset** (Gao et al., 2021):
- **Source:** *ECSMP: A dataset on emotion, cognition, sleep, and multi-model physiological signals*.
- **Participants:** 89 healthy college students.
- **Experimental Condition:** Video-induced emotion elicitation tasks.
- **Sampling Rate:** 512 Hz.

## 🛠 Methodological Workflow
This repository focuses on the extraction of high-fidelity **Heart Rate Variability (HRV)** metrics, serving as the physiological inputs for the predictive model.

### 1. Data Ingestion
- Processing of raw binary data (`int16`) to preserve the integrity of the Analog-to-Digital Converter (ADC) values.
- Direct handling of the 512 Hz sampling rate to ensure temporal precision for R-peak detection.

### 2. Signal Preprocessing & Delineation
- **Noise Reduction:** Application of bandpass filters via `NeuroKit2` to remove power-line interference and baseline wander.
- **Morphological Segmentation:** Utilization of Discrete Wavelet Transform (DWT) to precisely delineate **P-waves, QRS complexes, and T-waves**, ensuring the validity of the detected cardiac cycles.

### 3. Feature Extraction (Cognitive Biomarkers)
The pipeline extracts specific HRV features relevant to Autonomic Nervous System (ANS) dynamics and emotional regulation:
- **Time-Domain:** `RMSSD` (Vagal Tone index) and `SDNN`.
- **Frequency-Domain:** `LF/HF Ratio` (Sympathovagal Balance/Arousal level).
- **Non-Linear Dynamics:** `Sample Entropy` and `Poincaré Plot (SD1/SD2)` to quantify the complexity of neuro-cardiac coupling during emotional states.

## 📂 Repository Structure
```bash
├── convert_sample_data.py       # Raw binary data loader
├── ECG_Analysis_Pipeline.ipynb  # Core preprocessing & feature extraction notebook
├── hrv_features.csv             # Extracted feature matrix (Input for Random Forest)
├── hrv_diagnostic_plot.png      # Poincaré plot for visual artifact inspection
└── requirements.txt             # Project dependencies

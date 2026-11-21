# Prognostics and Health Management on Li-ion Batteries

## Dataset
The analysis was conducted using the **Toyota Research Institute dataset**, released with the following paper:

> Severson et al. *Data-driven prediction of battery cycle life before capacity degradation*. Nature Energy, volume 4, pages 383–391 (2019). [doi:10.1038/s41560-019-0356-8](https://doi.org/10.1038/s41560-019-0356-8)

- **Data:** <https://data.matr.io/1/projects/5c48dd2bc625d700019f3204>
- **License of the data:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (attribution required)
- The raw `.mat` files are not included in this repository.
- The files in `Results/` are derived from the `2018-04-12` batch of this dataset and were produced by the processing and modeling steps described below. The original data remains under CC BY 4.0: please credit it as above when reusing these files.

## Overview of the Work
This project focuses on predicting the health and lifespan of Li-ion batteries through data analysis and modeling. Due to computational limitations, the study was restricted to a subset of the dataset for efficiency and feasibility.

### Key Steps

1. **Data Selection**
   - The dataset contains `.mat` files with information on battery charging policies.
   - To simplify the analysis, I identified batteries charged using a one-step policy and worked exclusively with this subset. The selection process is detailed in the notebook: **`same_policy.ipynb`**.

2. **Data Cleaning and Preprocessing**
   - All anomalies described by the dataset provider were treated and corrected.
   - The data preprocessing pipeline is outlined in:
     - **`csv_concatenation.ipynb`**
     - **`data_clean.ipynb`**

3. **Model Development**
   - I designed an ensemble learning model to predict battery health.
   - The ensemble model was optimized using a **Genetic Algorithm** for weight optimization.
   - The modeling process is documented in:
     - **`first_modele.ipynb`**
     - **`Genetic_algorithm.ipynb`**

## Technologies and Tools
- Python
- Jupyter Notebooks
- Machine Learning (Ensemble Learning, Genetic Algorithms)

## Limitations
The scope of this work was constrained by computational resources, which limited the analysis to a subset of the dataset. Future work could expand on this to include the full dataset and explore additional charging policies.

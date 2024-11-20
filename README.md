Prognostics and Health Management on Li-ion Batteries
Dataset
The analysis was conducted using the Toyota Research Institute dataset.

Overview of the Work
This project focuses on predicting the health and lifespan of Li-ion batteries through data analysis and modeling. Due to computational limitations, the study was restricted to a subset of the dataset for efficiency and feasibility.

Key Steps
Data Selection

The dataset contains .mat files with information on battery charging policies.
To simplify the analysis, I identified batteries charged using a one-step policy and worked exclusively with this subset. The selection process is detailed in the notebook: same_policy.ipynb.
Data Cleaning and Preprocessing

All anomalies described by the dataset provider were treated and corrected.
The data preprocessing pipeline is outlined in:
csv_concatenation.ipynb
data_clean.ipynb
Model Development

I designed an ensemble learning model to predict battery health.
The ensemble model was optimized using a Genetic Algorithm for weight optimization.
The modeling process is documented in:
first_modele.ipynb
Genetic_algorithm.ipynb
Technologies and Tools
Python
Jupyter Notebooks
Machine Learning (Ensemble Learning, Genetic Algorithms)
Limitations
The scope of this work was constrained by computational resources, which limited the analysis to a subset of the dataset. Future work could expand on this to include the full dataset and explore additional charging policies.
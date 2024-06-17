import h5py
import numpy as np

# Charger le fichier .mat avec h5py
file_path = r'C:\Users\pc\Desktop\data-driven-prediction-of-battery-cycle-life-before-capacity-degradation-master\combined_batchdata.mat'
mat = h5py.File(file_path, 'r')

# Extraire le tableau 'batch_combined'
batch_combined = mat['batch_combined']

# Extraire les références des politiques
policy_refs = batch_combined['policy']

# Créer un dictionnaire pour stocker les politiques uniques
policy_dict = {}

# Parcourir les références de politiques et accéder aux données réelles
for ref in policy_refs:
    # Accéder à l'objet référencé
    policy_obj = mat[ref[0]]

    # Extraire les données réelles de l'objet référencé
    policy_data = policy_obj[()]

    # Convertir les valeurs numériques en caractères et les joindre pour former une chaîne
    policy_str = ''.join(chr(item) for item in policy_data.flatten())

    # Ajouter ou incrémenter la politique dans le dictionnaire
    if policy_str in policy_dict:
        policy_dict[policy_str] += 1
    else:
        policy_dict[policy_str] = 1

# Afficher les politiques uniques et leur nombre
print(f"Politiques de recharge uniques : {list(policy_dict.keys())}")
print(f"Nombre de politiques de recharge uniques : {len(policy_dict)}")
print(f"Occurrences de chaque politique : {policy_dict}")

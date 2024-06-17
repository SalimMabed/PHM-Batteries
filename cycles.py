import h5py

# Chemin vers le fichier .mat
mat_file = r'C:\Users\pc\Desktop\data-driven-prediction-of-battery-cycle-life-before-capacity-degradation-master\combined_batchdata.mat'

# Charger le fichier .mat avec h5py
with h5py.File(mat_file, 'r') as mat_data:
    # Accéder aux cycles de la première batterie
    first_battery_cycles_ref = mat_data['batch_combined']['cycles'][0]

    # Parcourir les références des cycles et extraire le temps (t) pour chaque cycle
    for cycle_ref in first_battery_cycles_ref:
        t = mat_data[cycle_ref]['t'][:]
        print(f"Temps (t) pour ce cycle : {t}")

    # Tu peux ajouter d'autres colonnes comme Qc, Qd, etc., en suivant un modèle similaire

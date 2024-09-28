import re
import matplotlib.pyplot as plt

# Lire le fichier HTML
with open('graphe.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Utiliser une expression régulière pour extraire les années et les chiffres associés
pattern = r'<title>(\d{4}): (\d+)</title>'
matches = re.findall(pattern, html_content)

# Extraire les années et les nombres de publications
years = [int(match[0]) for match in matches]
counts = [int(match[1]) for match in matches]

# Créer le graphique avec des lignes reliant les sommets
plt.figure(figsize=(10, 6))
plt.plot(years, counts, marker='o', color='skyblue', linestyle='-', markersize=8, label='Nombre de publications')

# Ajouter des annotations pour chaque sommet
for i in range(len(years)):
    plt.text(years[i], counts[i], str(counts[i]), ha='center', va='bottom', fontsize=10)

# Ajouter des lignes horizontales tous les 20 unités
plt.yticks(range(0, max(counts) + 20, 20))  # Ajuste les ticks du graphique
for y in range(0, max(counts) + 20, 20):
    plt.axhline(y=y, color='gray', linestyle='--', linewidth=0.7)

# Ajouter des labels et un titre
plt.xlabel('Année')
plt.ylabel('Nombre de publications')

plt.xticks(rotation=45)
plt.tight_layout()

# Enregistrer le graphique en PNG
plt.savefig('publications_par_annee.png', format='png')

# Afficher le graphique
plt.show()

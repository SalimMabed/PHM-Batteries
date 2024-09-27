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

# Créer le graphique
plt.figure(figsize=(10, 6))
plt.bar(years, counts, color='skyblue')
plt.xlabel('Année')
plt.ylabel('Nombre de publications')
plt.title('Nombre de publications par année')
plt.xticks(rotation=45)
plt.tight_layout()

# Afficher le graphique
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Ouvrir le fichier et lire les lignes
with open("tets.txt", "r") as file:
    lines = file.readlines()

# Initialiser une figure pour les 10 graphiques
fig, axs = plt.subplots(5, 2, figsize=(12, 10))
fig.suptitle("Utilisation du processeur par cœur")

# Parcourir chaque ligne et extraire les valeurs
for i, line in enumerate(lines):
    core_data = line.split(",")
    core_usage = [int(entry.split("%")[0]) for entry in core_data]

    # Créer un tableau numpy pour l'axe X (le temps)
    x = np.arange(len(core_usage))

    # Tracer le graphique sur la sous-figure correspondante
    row, col = i // 2, i % 2
    axs[row, col].plot(x, core_usage, marker='o')
    axs[row, col].set_title(f'Cœur de processeur {i + 1}')
    axs[row, col].set_xlabel('Temps')
    axs[row, col].set_ylabel('% d\'utilisation')

# Ajuster l'espacement entre les graphiques pour une meilleure lisibilité
plt.tight_layout()

# Afficher les graphiques
plt.show()

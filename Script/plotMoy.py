import matplotlib.pyplot as plt
import numpy as np

# Ouvrir le fichier et lire les lignes
with open("./tegrastatCpuData.txt", "r") as file:
    lines = file.readlines()

# Nombre de cœurs
num_cores = len(lines[0].split(","))
all_core_data = []

# Parcourir chaque cœur et créer un graphique dans sa propre fenêtre
for core in range(num_cores):
    core_data = [line.split(",")[core] for line in lines]
    core_usage = [int(entry.split("%")[0]) for entry in core_data]
    all_core_data.append(core_usage)

# Calculer la moyenne des données de chaque cœur
average_data = np.mean(all_core_data, axis=0)

# Créer un nouveau graphique pour la moyenne
plt.figure(figsize=(6, 4))

# Créer un tableau numpy pour l'axe X (le temps)
x = range(len(average_data))

# Tracer le graphique pour la moyenne
plt.plot(x, average_data, marker='o')
plt.title('Moyenne des cœurs de processeur')
plt.xlabel('Temps')
plt.ylabel('% d\'utilisation')

# Afficher les graphiques
plt.show()

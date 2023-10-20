import matplotlib.pyplot as plt

# Ouvrir le fichier et lire les lignes
with open("../tegrastat_Data/tegrastat_CpuData.txt", "r") as file:
    lines = file.readlines()
import matplotlib.pyplot as plt

# Nombre de cœurs
num_cores = len(lines[0].split(","))

# Parcourir chaque cœur et créer un graphique dans sa propre fenêtre
for core in range(num_cores):
    core_data = [line.split(",")[core] for line in lines]
    core_usage = [int(entry.split("%")[0]) for entry in core_data]

    # Créer une nouvelle figure pour chaque cœur
    plt.figure(figsize=(6, 4))
    
    # Créer un tableau numpy pour l'axe X (le temps)
    x = range(len(core_usage))

    # Tracer le graphique pour chaque cœur
    plt.plot(x, core_usage)
    plt.title(f'Cœur de processeur {core + 1}')
    plt.xlabel('Temps')
    plt.ylabel('% d\'utilisation')

# Afficher les graphiques
plt.show()

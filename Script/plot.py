import matplotlib.pyplot as plt

# Ouvrir le fichier et lire les lignes
with open("tets.txt", "r") as file:
    lines = file.readlines()

# Initialiser des listes pour stocker les valeurs
cores = []
usage = []

# Parcourir chaque ligne et extraire les valeurs
for line in lines:
    core_data = line.split(",")
    core_usage = [int(entry.split("%")[0]) for entry in core_data]
    cores.append(list(range(1, len(core_usage) + 1))
    usage.append(core_usage)

    # Tracer le pourcentage d'utilisation pour chaque cœur
    for core, core_usage in zip(cores, usage):
        plt.plot(core, core_usage, marker='o')

    # Ajouter des étiquettes et un titre
    plt.xlabel('Cœur de processeur')
    plt.ylabel('% d\'utilisation')
    plt.title('Utilisation du processeur par cœur')

    # Afficher le graphique
    plt.show()

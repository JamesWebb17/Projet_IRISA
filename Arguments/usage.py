import argparse


def usage():
    parser = argparse.ArgumentParser(description="Programme de suivis des performances d'un processus.")

    # Ajoutez ici vos options
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='Active le mode verbeux')
    parser.add_argument('-p', '--pid',
                        help='PID du processus à inspecter',
                        type=int,
                        required=True,
                        dest='PID',
                        default=0)
    parser.add_argument('-f', '--frequence',
                        help='Fréquence d\'échantillonnage en seconde',
                        type=float,
                        dest='Frequence',
                        default=0.1)
    parser.add_argument('-cpu', '--cpu',
                        help='Affiche l\'utilisation du CPU',
                        action='store_true',
                        dest='CPU',
                        default=False)
    parser.add_argument('-mem', '--mem',
                        help='Affiche l\'utilisation de la mémoire',
                        action='store_true',
                        dest='MEM',
                        default=False)
    parser.add_argument('-power', '--power',
                        help='Affiche la consommation d\'énergie',
                        action='store_true',
                        dest='POWER',
                        default=False)
    parser.add_argument('-n', '--nombre',
                        help='Nombre d\'échantillons',
                        type=int,
                        dest='Nombre',
                        default=100)
    parser.add_argument('-a', '--all',
                        help='Affiche tous ce qui est possible',
                        action='store_true',
                        dest='ALL',
                        default=False)
    parser.add_argument('-plot', '--plot',
                        help='Affiche les graphiques',
                        action='store_true',
                        dest='Plot',
                        default=False)
    parser.add_argument('-s', '--save',
                        help='Écrit toute les data dans un fichier',
                        type=str,
                        dest='Save')
    args = parser.parse_args()

    return args

# Préparation de l'environement de travail

## Miniconda

Miniconda est un gestionnaire de venv pour python, il permet de créer un environnement virtuel pour chaque projet ce qui évite de polluer le PYTHON PATH avec des packages ayant des requirements différens.

### Linux
il faut commencer par téléchager l'installeur conda a l'addresse suivante
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

puis l'executer (pendant l'installation séléctionner deux fois 'yes')

``
bash Miniconda3-latest-Linux-x86_64.sh
``

### Windows
pour windows il existe un exe [ICI](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)
### Création du venv
pour la suite de ce tuto vous devez avoir un venv
``
conda create -n le_nom_de_votre_env python=3.6
``

Apres la création vous pouvez installer les paquets nécessaires avec la commande
``
pip install nom_du_paquet_a_installer
``
Les paquets dont vous avez besoin sont:
* numpy
* pandas
* matplotlib
* tensorflow
* keras
* jupyter
* kaggle

### Récupération des jeux de données

Les jeux de données sont fournis par Kaggle. Pour les obtenir nous allons utiliser l'outil installer dans le chapitre précédent. Mais avant cela il faut générer une clé sur le site de kaggle (My account > Create new API Token).
Créer un dossier *.kaggle* dans votre home puis copier la clé *kaggle.json* dedans

Enfin pour télécharger les données lancez la commande
``
mkdir titanic_dataset/
kaggle competitions download -c titanic -p titanic_dataset/
ls titanic_dataset/
``

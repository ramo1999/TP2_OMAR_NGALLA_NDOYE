# TP : Création et Manipulation d'une Image Personnalisée avec Docker

### Objectifs du TP
- Comprendre comment créer une image Docker personnalisée à partir d'un `Dockerfile`.
- Manipuler l'image avec des commandes Docker.
- Lancer un conteneur à partir de cette image.

---

## Étape 1 : Préparation du Projet

1. **Structure du projet** :

Comme vu auparavant notre projet sera structurer en utilisant le principe de programmation modulaire. 
Ce projet contient une application streamlit. C'est une web app écrite en python qui permet la visualisation et l'interaction avec le script. C'est un façon de mise à dispostion d'un modèle de manière simple et rapide. 

2. **Creation d'image personnalisé**

Ouvrez le fichier Dockerfile. Ce fichier est appelé Dockerfile (comme son nom) permet de crée une image docker personnalisée. Il permet la construction des couches d'une image. Chaque ligne dois contenir une command. 

> **Important** La manière la optimale d'écire le docker file c'est de commencer avec les choses qui ne bouge pas souvant dans note projet. Exemple les requirements, les variables d'environement les config. Le code python écrit evoluera souvant on doit le laisser à la fin.

En effet docker utilise le cache pour construire les images. On doit tirer avantage de ça pour qu'à chaque fois on crée une image on utilisera le cache des couches déjà construite. 

3. **Dockefile**

Observer les command dans les lignes du Dockerfile et essayez de comprendre ce qu'on fait dans chaque une. Appyez vous sur cette [documentation](https://docs.docker.com/build/concepts/dockerfile/#dockerfile-syntax) pour moieux comprendre les Dockerfile.
Pour voir les autres commandes possibles réferez vous à cette [page](https://docs.docker.com/reference/dockerfile/)

## Étape 2: Docker commands

1. **Build de l'image**

Rendez vous sur la racinde du dossier si nous y êtes pas encore avec :

```bash
cd docker_tp
```
Construisez l'image Docker à partir du Dockerfile :

```bash
docker build -t mon-app-streamlit:1.0 .
```
- -t: permet de nommer et tagger l'image (mon-app-streamlit:1.0).

- . : indique que le Dockerfile est dans le répertoire courant.

Observez le comportement à la création du docker. On remarque que l'execution ce fait en couche. Les premières couches provienne de notre image python déjà contruite. Les autres de nos commandes écrites dans le dockerfile.

à la fin du build vérfiez l'existance de l'image avec : 

```bash
docker images
```

Qu'observez vous ? 

2. **Lancement d'un Conteneur**

``` bash
docker run -p 8501:8501 --name mon-app-conteneur mon-app-streamlit:1.0
``` 
- -p 8501:8501 : mapper le port 8501 de votre machine au port 8501 du conteneur.

- --name : nommer le conteneur.

Accédez à l'application : Ouvrez votre navigateur et accédez à http://localhost:8501.

Qu'aubservez vous dans le terminal ?

- Revenez sur le terminal et arrêtez l'execution du container avec en appyant sur ctrl+C.

2. **Lancement d'un en mode détaché Conteneur**

```bash
docker run -d -p 8501:8501 --name mon-app-conteneur mon-app-streamlit:1.0
```
Accédez à l'application encore une fois : Ouvrez votre navigateur et accédez à http://localhost:8501.

- Qu'elle est la différence entre les deux commande avec "-d" et sans ? 
- Quel est la meilleur façon de mise en production ?  
- Créez un autre container à partitr de la même image.
- Rappelez la différence entre image docker et container docker.

## Étape 4 : Manipulation de l'image et du Conteneur

1. **Montoring des container**

```bash
docker ps
```

- Qu'observez vous ?

2. **Arret du container**

```bash
docker stop mon-app-conteneur
```

3. **Redémarrer le conteneur**

```bash
docker start mon-app-conteneur
```

4. **Supprimer le conteneur**

```bash
docker rm -f mon-app-conteneur
```
- Verifier si le container et bien arrêté.

5. **Exécuter un conteneur interactivement (pour debugger ou tester) :**

```bash
docker run -it --rm mon-app-streamlit:1.0 /bin/bash
```
- Ou on se trouve à ce moment par rapport au container ?

6. **Logs du container**

- Executez la commande :

```bash
docker logs mon-app-conteneur
```
Qu'est ce que vous observez ? 

7 **Optionnel: Supression**

- Supprimez le container avec :
```bash
docker rm -f mon-app-conteneur
```
- Supprimez l'image avec :

```
docker rmi mon-app-streamlit:1.0
```
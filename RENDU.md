# TP : Création et Manipulation d'une Image Personnalisée avec Docker

## DOCKER COMMAND

1. **Build de l'image**
Voici la sortie de la commande `docker build` :

![Sortie de la commande docker build](im1.png)

**Interprétation :**

- Début de la Construction : La sortie commence par indiquer que Docker a lancé le processus de construction ([+] Building ... FINISHED). Il a fallu 322.7 secondes pour terminer la construction, et le processus a été découpé en 10 étapes.
- Chargement du Dockerfile : Docker a d'abord chargé la définition de construction à partir du Dockerfile (=> [internal] load build definition from Dockerfile). Cela a pris très peu de temps, car le fichier est petit (567 octets).
- Chargement du .dockerignore : Docker a chargé le fichier .dockerignore, qui spécifie les fichiers et répertoires à exclure du contexte de construction.
- Transfert du Contexte de Construction : Docker a transféré le contexte de construction, c'est-à-dire les fichiers nécessaires à la construction de l'image.
- Définition de l'Image de Base : Docker a spécifié l'image de base à utiliser (=> [1/5] FROM docker.io/library/python:3.11-slim). L'identifiant SHA256 garantit que la même version de l'image de base est utilisée à chaque fois.

2. **Docker images**
![Sortie de la commande docker images](imdoc.png)
on voit les images dockeurs qu'on a crééés qui s'affichent avec le nom, le TAG, l'ID de limage, la date de creation et la taille.

3. **Lancement d'un conteneur**
![sortie de la commande docker run -p 8501:8501 --name mon-app-conteneur mon-app-streamlit:1.0](cont.png)

une fois qu'on lance l'application on voit toutes les informations à savoir les executions qui ont été faites.
- L'application Streamlit a démarré avec succès.
- Les données ont été chargées correctement à partir du fichier CSV spécifié.
- L'analyse exploratoire des données a été effectuée.
- L'application s'est terminée sans erreurs.
- Les logs fournissent des informations utiles pour le débogage et le suivi de l'exécution de l'application.

4. **Lancement d'un conteneur en mode detaché**
![Sortie de la commande docker run -d -p 8501:8501 --name mon-app1-conteneur mon-app-streamlit:1.0](det.png)
On voit juste un code. Mais le conteneur a été lancer sur le navigateur.

-Différence entre docker run avec et sans l'option -d :

    docker run sans -d (mode attaché) :
        Lorsque vous exécutez un conteneur sans l'option -d, Docker démarre le conteneur en mode attaché.
        Cela signifie que le terminal dans lequel vous avez exécuté la commande est attaché au conteneur.
        Les sorties (logs) du conteneur sont affichées directement dans ce terminal.
        Vous ne pouvez pas utiliser ce terminal pour d'autres commandes tant que le conteneur est en cours d'exécution.
        Si vous fermez le terminal, le conteneur s'arrête.
    
    docker run -d (mode détaché) :

        L'option -d indique à Docker de démarrer le conteneur en mode détaché.
        Le conteneur s'exécute en arrière-plan, et le terminal est immédiatement libéré.
        Vous pouvez continuer à utiliser le terminal pour d'autres commandes.
        Les logs du conteneur ne sont pas affichés dans le terminal. Vous devez utiliser la commande docker logs pour les consulter.
        C'est le mode le plus utilisé pour les application en production.

-Meilleure façon de mise en production :
    La meilleure façon de mettre en production une application Docker est d'utiliser le mode détaché (-d).
    En mode détaché, le conteneur s'exécute en arrière-plan, ce qui permet à votre serveur de continuer à fonctionner même si vous fermez votre terminal.
    En production, on utilise souvent des outils d'orchestration de conteneurs comme Docker Swarm ou Kubernetes, qui permettent de gérer et de mettre à l'échelle les conteneurs de manière automatisée.

-Différence entre une image Docker et un conteneur Docker :

    Image Docker :
        Une image Docker est un modèle statique et immuable.
        Elle contient les instructions nécessaires pour créer un conteneur, y compris le système d'exploitation, les bibliothèques, le code de l'application et les paramètres de configuration.
        Elle est stockée dans un registre Docker (comme Docker Hub) ou localement sur votre machine.
    Conteneur Docker :
        Un conteneur Docker est une instance en cours d'exécution d'une image Docker.
        Il est isolé du système d'exploitation hôte et des autres conteneurs.
        Il peut être démarré, arrêté, redémarré et supprimé.
        Un conteneur est la couche inscriptible d'une image.

## MANIPULATION DE L'IMAGE DOCKER

1. **docker ps**
![f](ps.png)
on voit les conteneurs dockers creees à partir de l'image.

2. **Arret du conteneur**
![](stop.png)
3. **redamarrer le conteneur**
![](start.png)
4. **supprimer le conteneur**
![](rm.png)
5. **Exécuter un conteneur interactivement (pour debugger ou tester)**
![](int.png)
6. **Logs du container**
![](log.png)


    





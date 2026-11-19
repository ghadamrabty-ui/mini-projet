# EduResources – Gestion des ressources pédagogiques

## 1. Présentation du projet

EduResources est une plateforme web développée avec Django qui permet de gérer et consulter des ressources pédagogiques.

## 2. Technologies utilisées

- Python
- Django
- HTML
- CSS
- SQLite

## 3. Fonctionnalités

- Afficher les ressources pédagogiques.
- Ajouter une ressource.
- Modifier une ressource.
- Supprimer une ressource.
- Rechercher une ressource.
- Filtrer par catégorie.
- Consulter les détails d'une ressource.
- Afficher les catégories.

## 4. Installation

1. Installer Python.
2. Ouvrir le dossier du projet.
3. Créer un environnement virtuel :

```bash
py -m venv venv
```

4. Activer l'environnement :

```bash
venv\Scripts\activate
```

5. Installer les dépendances :

```bash
py -m pip install -r requirements.txt
```

6. Appliquer les migrations :

```bash
py manage.py migrate
```

## 5. Lancer le serveur

Exécuter la commande :

```bash
py manage.py runserver
```

Ouvrir le navigateur :

http://127.0.0.1:8000/

## 6. Tester l'application

L'utilisateur peut consulter les ressources, effectuer une recherche, ajouter, modifier et supprimer des ressources, ainsi que consulter les catégories.

## 7. Base de données

Le projet utilise SQLite pour enregistrer les catégories et les ressources pédagogiques.

## 8. Auteur

Projet réalisé dans le cadre d'un projet académique.
# Générateur de facture

Application Django permettant de gérer des produits et de générer des factures associant ces produits.

## Fonctionnalités

- Création / modification / suppression des produits (nom, prix, date de péremption)
- Création de factures en sélectionnant plusieurs produits / Supression de factures
- Affichage des détails de chaque facture avec prix figés au moment de la création
- Pagination pour les listes de produits et de factures

## Installation

1. Cloner le dépôt  
2. Créer un environnement virtuel Python et l’activer  
3. Installer les dépendances :  
   ```bash
   pip install -r requirements.txt
4. Appliquer les migrations : 
   ```bash
   python manage.py migrate
5. Lancer le serveur : 
   ```bash
   python manage.py runserver


## Tests

Pour lancer les tests unitaires :
   ```bash
   python manage.py test
   ```

## Remarques 
-> Les prix de produits sont figés au moment de la création d'une facture.
-> Les formulaires sont protégés contre les attaques CSRF.

## Captures d’écran

Des captures d’écran de l’application sont disponibles dans le dossier [`screenshots/`](screenshots) du dépôt.

## Structure du projet

Voici un aperçu de l’organisation des fichiers principaux :

generateur_facture/
├── generateur_facture/ # Répertoire principal du projet Django
│ ├── settings.py # Configuration du projet
│ ├── urls.py # Routeur principal
│ └── wsgi.py # Point d'entrée du serveur
├── produits/ # Application Django "produits"
│ ├── migrations/ # Fichiers de migration de la base de données
│ ├── templates/produits/ # Templates HTML spécifiques à l'app produits
│ ├── forms.py # Formulaires Django
│ ├── models.py # Modèles de données
│ ├── views.py # Vues Django
│ ├── urls.py # Routes spécifiques à l'app produits
│ └── tests.py # Tests unitaires
├── db.sqlite3 # Base de données SQLite (générée)
├── manage.py # Script de gestion du projet
└── requirements.txt # Liste des dépendances Python (générée automatiquement avec pip freeze > requirements.txt)


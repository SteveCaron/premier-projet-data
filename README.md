# Simple projet python : Decouverte Data Engineering

## Description

Ce projet est un projet de découverte de la Data Engineering. il a pour but de mettre en place un pipeline de traitement de données.


Nous chargons un fichier CSV qui contien des informations utilisateurs et leurs informations. Nous allons ensuite le traiter pour en extraire des informations, puis stocker dans une base de données.

## Prérequis

- Python 3.7
- Docker
- Docker-compose
- Git

## Installation

- Cloner le projet
- Creer un environnement virtuel

    ```bash
    # Linux
    python -m venv .venv
    # Windows
    py -m venv .venv
    ```

- Activer l'environnement virtuel

    ````bash
    # Linux
    .venv/bin/activate
    # Windows (batch/cmd)
    .venv/Scripts/activate.bat
    # Windows (powershell)
    .venv/Scripts/Activate.ps1
    ````

- Installer les dépendances

    ``` bash
    pip.install -r requirement.txt
    ```

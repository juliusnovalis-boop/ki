# RENTAL GABON CAR — Revue & Présentation Complète du Projet

Bienvenue dans la suite interactive de **RENTAL GABON CAR** (système de gestion de location de véhicules basé à Libreville, Gabon).

L'application web interactive est **actuellement lancée et accessible en direct dans votre panneau « Live Preview »** (sur le port `3000`).

---

## 🧭 Ce qui est disponible dans l'interface interactive

L'interface web regroupe 6 espaces de travail pour explorer le projet sous tous ses angles :

### 1. 🖥️ Application Interactive Complète
Une réplique interactive, moderne et fonctionnelle du système de gestion Access, avec :
- **Tableau de bord** :
  - Bandeau avec photographie haute définition de la flotte automobile de Libreville.
  - **3 KPIs en temps réel** :
    - Chiffre d'affaires : **104 261 200 FCFA** (calculé sur les 25 réservations).
    - Flotte : **60 véhicules** (dont **8 en location active** à la date de référence du 28/09/2026).
    - Clients : **200 clients enregistrés** (Meilleur client : *Cynthia Kombila* avec 18 457 500 FCFA).
  - Tableau interactif des **Voitures actuellement réservées** (avec redirection directe vers la fiche).
  - Classement des **5 meilleurs clients** avec médailles et montants.
  - Répartition de la flotte par carburant : **Essence (51,7 % · 31 véhicules)**, **Diesel (38,3 % · 23 véhicules)**, **Hybride (10,0 % · 6 véhicules)**.
- **Réservations (25 réservations réelles)** :
  - Fiche détaillée avec sélecteurs de client et véhicule (mise à jour instantanée du téléphone, email, modèle, marque et tarif journalier).
  - Calcul automatique de la durée et du montant total en FCFA.
  - Barre de navigation d'enregistrements Access (`⏮`, `◀`, `X sur 25`, `▶`, `⏭`).
  - **Bannière d'alerte et outil de correction en 1 clic** pour l'anomalie de la réservation n° 11.
  - Recherche et filtres (Toutes, En cours, Terminées, À venir, Anomalies).
- **Clients (200 clients enregistrés)** :
  - Fiche complète avec CIN, n° de permis gabonais, prénom, nom, sexe, adresse (Libreville, Glass, Akébé, etc.), téléphone et email.
  - Moteur de recherche instantané et historique des locations passées par client.
- **Voitures (60 véhicules)** :
  - Fiche technique (Matricule, Année, Couleur, Puissance fiscale, Coût/jour, Modèle, Marque, Carburant).
  - Statuts dynamiques : *Disponible*, *En location*, *En entretien*.
- **Marques (5)**, **Carburants (3)** et **Modèles (60)** :
  - Tables et fiches complètes avec gestion des associations.
- **Écran de Connexion (Login)** :
  - Formulaire scindé avec photographie du front de mer de Libreville et compte administrateur.

---

### 2. ⚖️ Comparatif Avant / Après (Access Original vs Nouveau Design)
- **Curseur glissant interactif** : Faites glisser la barre horizontale pour comparer pixel par pixel la capture initiale de Microsoft Access 2016 (`Capture001.png` - commit `96479ee`) et la maquette modernisée (`01-tableau-de-bord.png` - commit `f01aae5`).
- **Vue côte à côte** commutable en un clic.
- **Matrice des 6 améliorations clés** :
  1. *Palette de couleurs* : Remplacement des couleurs disparates (cyan/fuchsia/gris) par une charte corporate Bleu Marine `#1E3A8A` et Bleu Primaire `#2563EB`.
  2. *Bandeaux photographiques* : Intégration de 9 photographies gabonaises haute définition pré-teintées.
  3. *Grille Access standardisée* : Calage systématique sur une grille de marges de 0,63 cm.
  4. *Indicateur Carburants* : Ajout du graphique de répartition énergétique de la flotte.
  5. *Correction SQL locations en cours* : Ajout de la condition `DateDebut <= Date()` (auparavant seules les dates de fin étaient vérifiées).
  6. *Intégrité des données* : Détection et résolution de l'inversion de date sur la réservation n° 11.

---

### 3. 🎨 Galerie des 8 Maquettes Access (Fidélité 100 %)
Visionneuse haute résolution pour les 8 écrans conçus pour Microsoft Access :
1. `00-connexion.png` — Écran d'accueil et d'authentification
2. `01-tableau-de-bord.png` — Tableau de bord général
3. `02-reservations.png` — Gestion des réservations et contrats
4. `03-clients.png` — Répertoire des 200 clients
5. `04-voitures.png` — Flotte automobile de 60 véhicules
6. `05-marques.png` — Gestion des marques
7. `06-carburants.png` — Motorisations
8. `07-modeles.png` — Catalogue des modèles
*Bouton direct permettant d'ouvrir la maquette HTML brute correspondante.*

---

### 4. 📐 Guide Access & Cotes Exactes (COTES.md)
Pour répliquer les formulaires dans Microsoft Access sans aucune ligne de code VBA :
- **Tableau interactif des 168 contrôles** avec coordonnées exactes en centimètres (`Gauche`, `Haut`, `Largeur`, `Hauteur`).
- **Nuancier officiel** : Cliquez sur une couleur pour copier instantanément son code hexadécimal dans le presse-papiers (`#1E3A8A`, `#2563EB`, `#EEF2F9`, etc.).
- **Guide des propriétés natives** : Paramétrage des formulaires à thème Windows, mode d'affichage *Découpage*, images partagées réutilisables.

---

### 5. 🗄️ Explorateur de la Base `Database20.accdb` & Audit
- Consultation en direct des données brutes des 5 tables relationnelles : `Client` (200), `Reservation` (25), `Voiture` (60), `Modele` (60), `Marque` (5), `Carburant` (3).
- **Rapport d'audit sur les 4 anomalies identifiées** dans la base Access d'origine :
  - **AUDIT-01 (Gravité Haute)** : Inversion de date sur la réservation n° 11 (`13/02/2027` au lieu de `06/12/2026`).
  - **AUDIT-02 (Gravité Moyenne)** : Requête « Voitures réservées » sans filtre sur `DateDebut <= Date()`.
  - **AUDIT-03 (Gravité Faible)** : Double jointure redondante Marque-Modèle dans la requête de liste des réservations.
  - **AUDIT-04 (Gravité Haute)** : Mots de passe stockés en clair dans la table Users.

---

### 6. 📦 Bibliothèque des Assets & Ressources
- Téléchargement et prévisualisation des **9 photos haute définition** adaptées aux dimensions d'Access.
- Bibliothèque de **plus de 40 icônes PNG transparentes** (Lucide icons) optimisées pour les boutons de commande Access.

---

## 🚀 Accès Rapide

Le serveur web local est actif sur :
```
http://0.0.0.0:3000
```
Il est automatiquement accessible dans l'onglet **Live Preview** de votre environnement de travail.

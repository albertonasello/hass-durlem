# Home Assistant - Durlem Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz/)

---

## Français

### Description
Cette intégration permet de connecter votre **adoucisseur d’eau Durlem** à Home Assistant.  
Elle utilise l’API cloud officielle (`connect.durlem.be`) afin de récupérer les principales informations de votre appareil et les rendre disponibles sous forme de capteurs dans HA.

### Fonctionnalités
- Récupération automatique de l’état de l’adoucisseur toutes les 5 minutes
- Capteurs disponibles :
  - **Durlem Remaining Capacity** (% de capacité restante)
  - **Durlem Low Salt** (alerte manque de sel : vrai/faux)
  - **Durlem Working** (en régénération : vrai/faux)
  - **Durlem Last Regeneration** (date/heure de la dernière régénération)
  - **Durlem Next Regeneration** (date/heure de la prochaine régénération)
- Attributs supplémentaires : dureté, fuite détectée, état de service, batterie faible, etc.

### Installation
1. Copiez le dossier `durlem` dans `config/custom_components/`.
2. Redémarrez Home Assistant.
3. Dans **Paramètres → Intégrations → Ajouter une intégration**, cherchez **Durlem**.
4. Entrez vos identifiants Durlem (email + mot de passe).
5. Les capteurs apparaîtront automatiquement.

👉 Option HACS : ajoutez ce repo comme dépôt personnalisé et installez depuis HACS.

### Remarques
- L’intégration utilise l’API cloud, une connexion Internet est donc nécessaire.
- Les identifiants sont stockés uniquement dans Home Assistant, jamais transmis ailleurs que vers l’API Durlem.

---

## English

### Description
This integration connects your **Durlem water softener** to Home Assistant.  
It uses the official cloud API (`connect.durlem.be`) to fetch device information and expose it as sensors in HA.

### Features
- Automatic update every 5 minutes
- Available sensors:
  - **Durlem Remaining Capacity** (% of remaining softening capacity)
  - **Durlem Low Salt** (salt alarm: true/false)
  - **Durlem Working** (currently regenerating: true/false)
  - **Durlem Last Regeneration** (date/time of the last regeneration)
  - **Durlem Next Regeneration** (date/time of the next regeneration)
- Extra attributes: hardness, leak detection, service mode, low battery, etc.

### Installation
1. Copy the `durlem` folder into `config/custom_components/`.
2. Restart Home Assistant.
3. Go to **Settings → Integrations → Add integration**, search for **Durlem**.
4. Enter your Durlem account credentials (email + password).
5. The sensors will appear automatically.

👉 HACS option: add this repository as a custom repository and install via HACS.

### Notes
- The integration relies on the official cloud API, so an Internet connection is required.
- Your credentials are only stored locally in Home Assistant and transmitted securely to Durlem’s API.

---

## Screenshots (optional)
_Add a screenshot of the sensors in Home Assistant UI once it’s running._

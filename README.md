# Durlem - Intégration Home Assistant

## 🇫🇷 Description

Cette intégration personnalisée pour **Home Assistant** permet de connecter votre **adoucisseur d’eau Durlem** directement dans votre tableau de bord domotique.  
Elle interroge l’API officielle et expose différentes informations utiles sous forme de **capteurs Home Assistant**.

Vous pourrez ainsi suivre en temps réel : la capacité restante, l’état du sel, les régénérations, la dureté de l’eau, etc.

### 🚀 Fonctionnalités
- Connexion avec identifiant/mot de passe à votre compte Durlem.  
- Récupération automatique des informations de l’adoucisseur.  
- Mise à jour régulière via un DataUpdateCoordinator.  
- Capteurs disponibles dans Home Assistant.  

### 🔧 Installation
1. Copier le dossier `durlem` dans `config/custom_components/` de votre installation Home Assistant.  
2. Redémarrer Home Assistant.  
3. Ajouter l’intégration via **Paramètres > Appareils & Services > Ajouter une intégration > Durlem**.  
4. Entrer vos identifiants **Durlem (email & mot de passe)**.  

### 📊 Capteurs disponibles
- **Durlem Remaining Capacity** (% de capacité restante)  
- **Durlem Low Salt** (alerte manque de sel : vrai/faux)  
- **Durlem Working** (en régénération : vrai/faux)  
- **Durlem Last Regeneration** (date/heure de la dernière régénération)  
- **Durlem Next Regeneration** (date/heure de la prochaine régénération)  
- **Durlem Regeneration Count** (nombre de régénérations depuis le reset)  
- **Durlem Hardness** (dureté de l’eau en °f)  
- **Durlem Installation Date** (date d’installation de l’appareil)  

---

## 🇬🇧 English Description

This custom integration for **Home Assistant** allows you to connect your **Durlem water softener** directly into your smart home dashboard.  
It communicates with the official API and exposes useful data as **Home Assistant sensors**.

You can monitor in real time: remaining capacity, salt status, regenerations, water hardness, etc.

### 🚀 Features
- Login with your Durlem account (email & password).  
- Automatic retrieval of softener information.  
- Periodic update via a DataUpdateCoordinator.  
- Exposed sensors in Home Assistant.  

### 🔧 Installation
1. Copy the `durlem` folder into `config/custom_components/` of your Home Assistant installation.  
2. Restart Home Assistant.  
3. Add the integration via **Settings > Devices & Services > Add Integration > Durlem**.  
4. Enter your **Durlem credentials (email & password)**.  

### 📊 Available Sensors
- **Durlem Remaining Capacity** (remaining capacity in %)  
- **Durlem Low Salt** (low salt alert: true/false)  
- **Durlem Working** (currently regenerating: true/false)  
- **Durlem Last Regeneration** (date/time of last regeneration)  
- **Durlem Next Regeneration** (date/time of next regeneration)  
- **Durlem Regeneration Count** (number of regenerations since reset)  
- **Durlem Hardness** (water hardness in °f)  
- **Durlem Installation Date** (device installation date)  

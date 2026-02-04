## 🇫🇷 Description

Cette intégration personnalisée pour **Home Assistant** permet de connecter votre **adoucisseur d’eau Durlem** directement dans votre tableau de bord domotique.  
Elle interroge l’API officielle et expose différentes informations utiles sous forme de **capteurs Home Assistant**.

Vous pourrez ainsi suivre en temps réel : la capacité restante, l’état du sel, les régénérations, la dureté de l’eau, etc.

### ⚠️ Important
**Votre adoucisseur doit impérativement être connecté à l’application _Durlem_.**  
Même si l’appareil peut être lié à la fois aux applications **Durlem** et **My Durlem**, il est **obligatoire** qu’il soit au minimum connecté à **Durlem** pour que l’intégration Home Assistant fonctionne correctement.

### 🚀 Fonctionnalités
- Connexion avec identifiant/mot de passe à votre compte Durlem
- Récupération automatique des informations de l’adoucisseur
- Mise à jour régulière via un `DataUpdateCoordinator`
- Capteurs disponibles dans Home Assistant

---

## 🇬🇧 English Description

This custom integration for **Home Assistant** allows you to connect your **Durlem water softener** directly into your smart home dashboard.  
It communicates with the official API and exposes useful data as **Home Assistant sensors**.

You can monitor in real time: remaining capacity, salt status, regenerations, water hardness, etc.

### ⚠️ Important Notice
**Your water softener must be connected to the _Durlem_ mobile application.**  
Even if the device can be linked to both **Durlem** and **My Durlem**, it **must at least be connected to the Durlem app** for the Home Assistant integration to work.

### 🚀 Features
- Login with your Durlem account (email & password)
- Automatic retrieval of softener information
- Periodic updates via a `DataUpdateCoordinator`
- Sensors exposed in Home Assistant

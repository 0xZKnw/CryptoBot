🚀 CryptoBot - Un Bot Discord pour suivre les cryptos !



📌 Description

CryptoBot est un bot Discord permettant d'obtenir facilement des informations sur les cryptomonnaies : prix en direct, liste des exchanges, solde d'un portefeuille et bien plus encore !

🌟 Fonctionnalités principales

📈 Obtenez le prix en temps réel d'un token avec /price <token>

💰 Vérifiez le solde d'un portefeuille BTC, ETH ou SOL avec /btcwallet, /ethwallet, /solwallet

🔄 Liste des principaux exchanges avec /exchanges

🔐 Liste des wallets les plus populaires avec /wallets

🔢 Calculez la valeur d'un montant de token avec /calc <quantité> <token>

🤣 Petite touche d'humour avec /quoi

🔗 Lien vers mon site avec /zknw

🛠️ Installation

Clonez ce repo :

git clone https://github.com/votre-utilisateur/cryptobot.git
cd cryptobot

Installez les dépendances :

pip install discord requests cryptocompare

Ajoutez votre token Discord dans le fichier config.py (ou remplacez 'TOKEN' dans bot.run())

Lancez le bot :

python bot.py

📜 Commandes

Commande

Description

/price <token>

Donne le prix actuel d'un token en USD

/btcwallet <adresse>

Vérifie le solde d'un wallet Bitcoin

/ethwallet <adresse>

Vérifie le solde d'un wallet Ethereum

/solwallet <adresse>

Vérifie le solde d'un wallet Solana

/exchanges

Liste des plateformes d'échange principales

/wallets

Liste des wallets crypto populaires

/calc <quantité> <token>

Calcule la valeur en USD d'un montant de token

/quoi

Répond "feur" à chaque fois

/zknw

Envoie le lien de mon site

/help

Liste toutes les commandes disponibles

🤖 Technologies utilisées

Discord.py - Gestion de l'API Discord

CryptoCompare - Récupération des prix crypto

BlockCypher API - Infos blockchain Ethereum

Blockstream API - Infos blockchain Bitcoin

📌 Contribuer

Les contributions sont les bienvenues ! Forkez ce repo et proposez vos améliorations via une PR.

📄 Licence

Ce projet est sous licence MIT.

👨‍💻 Développé par @tonpseudo | 🌐 0xZKnw.me


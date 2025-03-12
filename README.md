# 🚀 CryptoBot - Un Bot Discord pour suivre les cryptos !

![CryptoBot Banner](https://cdn.pixabay.com/photo/2016/11/29/09/08/bitcoin-1866740_960_720.jpg)

## 📌 Description
CryptoBot est un bot Discord permettant d'obtenir facilement des informations sur les cryptomonnaies : prix en direct, liste des exchanges, solde d'un portefeuille et bien plus encore !

### 🌟 Fonctionnalités principales
- 📈 Obtenez le prix en temps réel d'un token avec `/price <token>`
- 💰 Vérifiez le solde d'un portefeuille BTC, ETH ou SOL avec `/btcwallet`, `/ethwallet`, `/solwallet`
- 🔄 Liste des principaux exchanges avec `/exchanges`
- 🔐 Liste des wallets les plus populaires avec `/wallets`
- 🔢 Calculez la valeur d'un montant de token avec `/calc <quantité> <token>`
- 🤣 Petite touche d'humour avec `/quoi`
- 🔗 Lien vers mon site avec `/zknw`

## 🛠️ Installation
1. **Clonez ce repo** :
   ```bash
   git clone https://github.com/votre-utilisateur/cryptobot.git
   cd cryptobot
   ```
2. **Installez les dépendances** :
   ```bash
   pip install discord requests cryptocompare
   ```
3. **Ajoutez votre token Discord** dans le fichier `config.py` (ou remplacez `'TOKEN'` dans `bot.run()`)
4. **Lancez le bot** :
   ```bash
   python bot.py
   ```

## 📜 Commandes
| Commande       | Description |
|---------------|-------------|
| `/price` `<token>` | Donne le prix actuel d'un token en USD |
| `/btcwallet` `<adresse>` | Vérifie le solde d'un wallet Bitcoin |
| `/ethwallet` `<adresse>` | Vérifie le solde d'un wallet Ethereum |
| `/solwallet` `<adresse>` | Vérifie le solde d'un wallet Solana |
| `/exchanges` | Liste des plateformes d'échange principales |
| `/wallets` | Liste des wallets crypto populaires |
| `/calc` `<quantité>` `<token>` | Calcule la valeur en USD d'un montant de token |
| `/quoi` | Répond "feur" à chaque fois |
| `/zknw` | Envoie le lien de mon site |
| `/help` | Liste toutes les commandes disponibles |

## 🤖 Technologies utilisées
- [Discord.py](https://discordpy.readthedocs.io/en/stable/) - Gestion de l'API Discord
- [CryptoCompare](https://min-api.cryptocompare.com/) - Récupération des prix crypto
- [BlockCypher API](https://www.blockcypher.com/) - Infos blockchain Ethereum
- [Blockstream API](https://blockstream.info/) - Infos blockchain Bitcoin

## 📌 Contribuer
Les contributions sont les bienvenues ! Forkez ce repo et proposez vos améliorations via une PR.

## 📄 Licence
Ce projet est sous licence MIT.

---
👨‍💻 Développé par **@tonpseudo** | 🌐 [0xZKnw.me](https://0xZKnw.me)


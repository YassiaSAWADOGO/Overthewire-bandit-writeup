# 🎯OverTheWire – Bandit Wargame

Ce dépôt documente ma progression complète sur **[Bandit](https://overthewire.org/wargames/bandit/)**, le wargame d'introduction d'OverTheWire consacré aux bases de la sécurité système sous Linux : permissions, manipulation de fichiers, réseau, scripting, et contournement de shells restreints.

> 🏁 **Statut : terminé** — Level 0 → Level 33 (dernier niveau du wargame)

---

## 📖 À propos de Bandit

Bandit est une série de défis progressifs accessibles en SSH, où chaque niveau donne les indices nécessaires pour trouver le mot de passe du niveau suivant. Les sujets couverts vont des commandes shell de base jusqu'à des techniques plus avancées : brute-force réseau, manipulation de Git, interblocages de shells restreints, cron jobs, et plus encore.

```
Host : bandit.labs.overthewire.org
Port : 2220
```

---

## 🧠 Compétences pratiquées

| Catégorie | Exemples de notions abordées |
|---|---|
| **Shell & permissions** | navigation, `find`, `grep`, permissions Unix (`chmod`, SUID), redirections |
| **Réseau** | `nc`, sockets, ports, brute-force sur service TCP persistant |
| **Scripting** | Bash, Python (`socket`, `pwntools`), automatisation de tâches répétitives |
| **Git** | clone/push via SSH, `.gitignore`, hooks côté serveur, nettoyage d'historique |
| **Cron & tâches planifiées** | lecture de configuration cron, droits d'exécution, pièges de permissions sur dossiers temporaires |
| **Contournement de shells restreints** | échappement via pager (`more`/`vi`), shells "uppercase", variables spéciales (`$0`) |
| **Cryptographie de base** | encodage/décodage, bases numériques, chiffrement simple |

---

## 🛠️ Outils utilisés

- `ssh`, `scp` — connexion et transfert de fichiers
- `nc` (netcat) — interaction avec des services réseau bruts
- Python (`socket`, `pwntools`) — automatisation d'attaques par force brute
- `git` — gestion de dépôt et contournement de hooks
- Outils Unix standards : `cat`, `grep`, `find`, `od`/`xxd`, `stty`, `chmod`

> ⚠️ **Aucun mot de passe de niveau n'est publié dans ce dépôt**, dans l'esprit du wargame : chacun doit trouver ses propres mots de passe. Les scripts prennent les mots de passe en paramètre plutôt que codés en dur.

---

## Pour ce qui est des fichiers sripts:

| Fichier | Niveau | Description |
|---|---|---|
| [`level24_cron_exfil.sh`](./scripts/level24_cron_exfil.sh) | 24 | Script déposé dans un dossier surveillé par un cron job, pour exfiltrer un mot de passe accessible uniquement par l'utilisateur cible. |
| [`level25_bruteforce_socket.py`](./scripts/level25_bruteforce_socket.py) | 25 | Brute-force d'un code PIN (10 000 combinaisons) sur une connexion TCP persistante, avec le module standard `socket`. |
| [`level25_bruteforce_pwntools.py`](./scripts/level25_bruteforce_pwntools.py) | 25 | Même brute-force, réécrit avec `pwntools`, la bibliothèque de référence pour ce type d'interaction réseau en CTF. |

---

## ✨ Quelques défis marquants

**Niveau 24 — Brute-force sur un daemon réseau**
Écriture d'un script Python exploitant une connexion TCP persistante pour tester 10 000 combinaisons de code PIN en quelques secondes, sans rouvrir de connexion à chaque essai.

**Niveau 26 — Échapper à un shell restreint**
Le shell de l'utilisateur cible n'était pas `bash` mais un script lançant `more` sur un fichier texte. En réduisant la taille du terminal pour forcer l'activation du pager, puis en utilisant l'éditeur interne (`vi`) accessible depuis `more`, il est possible d'obtenir un shell complet.

**Niveau 31 — Hook Git trompeur**
Un `git push` rejeté avec `pre-receive hook declined` peut malgré tout afficher le mot de passe recherché dans les messages `remote:` précédant le rejet — une leçon sur l'importance de lire l'intégralité d'une sortie console, pas seulement le code de retour final.

**Niveau 33 — Shell "majuscules"**
Un shell convertissant toute entrée en majuscules avant exécution, rendant toute commande usuelle invalide. Contournement via la variable spéciale `$0`, qui échappe à la transformation.

---

## 🙋 À propos

Projet réalisé dans le cadre de ma formation en cybersécurité (spécialisation STI, INSA Centre Val de Loire), en complément de mes cours de sécurité système et réseau.

**Prochaine étape :** [Natas](https://overthewire.org/wargames/natas/) (sécurité web) ou [Narnia](https://overthewire.org/wargames/narnia/) (exploitation binaire).

---

## 📜 Licence / Mentions

Ce dépôt est partagé à des fins pédagogiques. OverTheWire et Bandit appartiennent à leurs auteurs respectifs — voir [overthewire.org](https://overthewire.org).

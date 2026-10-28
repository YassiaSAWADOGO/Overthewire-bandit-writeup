#!/bin/bash
#
# Bandit level 24 — script exécuté par un cron job tournant sous l'identité
# de l'utilisateur cible (ici bandit24), déposé dans un dossier temporaire
# surveillé par ce cron (/var/spool/bandit24/foo/ dans l'énoncé original).
#
# Le script lit le mot de passe du niveau suivant (accessible uniquement
# par l'utilisateur cible) et le recopie dans un fichier lisible par tous,
# dans le même dossier que le script lui-même — ce qui permet de le relire
# depuis son propre compte une fois le cron passé.
#
# Usage : placer ce script dans le dossier surveillé par le cron, puis
# attendre son exécution automatique (généralement toutes les minutes).

OUTPUT_DIR="$(dirname "$0")"
PASSWORD_FILE="/etc/bandit_pass/bandit24"
OUTPUT_FILE="${OUTPUT_DIR}/passwd24"

cat "$PASSWORD_FILE" > "$OUTPUT_FILE"
chmod 666 "$OUTPUT_FILE"

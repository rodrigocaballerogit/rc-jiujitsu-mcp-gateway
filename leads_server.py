import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path(__file__).parent / "leads.db"


def _init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                name       TEXT    NOT NULL,
                phone      TEXT    NOT NULL,
                city       TEXT    DEFAULT '',
                professor  TEXT    DEFAULT '',
                created_at TEXT    NOT NULL
            )
        """)
        conn.commit()


_init_db()


def save_lead(name: str, phone: str, city: str = "", professor: str = "") -> dict:
    ts = datetime.now().isoformat()
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            "INSERT INTO leads (name, phone, city, professor, created_at) VALUES (?,?,?,?,?)",
            (name, phone, city, professor, ts),
        )
        conn.commit()
        lead_id = cur.lastrowid

    print(f"[{ts}] Lead #{lead_id} guardado: {name} | {phone} | {city} | profesor: {professor}")
    return {"ok": True, "id": lead_id, "name": name, "professor": professor}


def list_leads() -> list[dict]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("SELECT * FROM leads ORDER BY id DESC").fetchall()
    return [dict(r) for r in rows]

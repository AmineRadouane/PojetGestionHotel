import os
import time

def remove_db_with_retries(path, retries=5, delay=1):
    for i in range(retries):
        try:
            os.remove(path)
            print("Fichier supprimé.")
            return True
        except PermissionError:
            print(f"❌ Le fichier est utilisé par un autre processus, tentative {i+1}/{retries}...")
            time.sleep(delay)
    print("❌ Impossible de supprimer le fichier après plusieurs essais.")
    return False

if remove_db_with_retries("hotel.db"):
    import sqlite3

    db_path = "hotel.db"
    sql_file_path = "BaseSQLLITE.sql"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(sql_file_path, 'r', encoding='utf-8') as f:
        sql_script = f.read()

    cursor.executescript(sql_script)

    conn.commit()
    conn.close()

    print("✅ Base de données initialisée.")
else:
    print("❌ Veuillez fermer tous les programmes utilisant hotel.db et réessayez.")

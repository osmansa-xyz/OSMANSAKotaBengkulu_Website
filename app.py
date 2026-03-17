from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('osmansa.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = sqlite3.connect('osmansa.db')
    cursor = conn.cursor()
    
    # Buat tabel yang diperlukan
    cursor.execute('''CREATE TABLE IF NOT EXISTS visi_misi (id INTEGER PRIMARY KEY, kategori TEXT, isi TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS proker (id INTEGER PRIMARY KEY, judul TEXT, deskripsi TEXT, icon TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS pengurus (id INTEGER PRIMARY KEY AUTOINCREMENT, nama TEXT, jabatan TEXT, divisi TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS event 
                      (id INTEGER PRIMARY KEY, nama_event TEXT, foto TEXT, deskripsi TEXT)''')
    
    cursor.executemany("INSERT INTO event (nama_event, foto, deskripsi) VALUES (?, ?, ?)", event_data)
    
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('osmansa.db')
    cursor = conn.cursor()

    # Visi
    cursor.execute("SELECT isi FROM visi_misi WHERE kategori='visi'")
    visi_row = cursor.fetchone()
    visi = visi_row[0] if visi_row else "Visi belum diatur."
    
    # Misi
    cursor.execute("SELECT isi FROM visi_misi WHERE kategori='misi'")
    misi_list = [row[0] for row in cursor.fetchall()]
    
    # Proker
    cursor.execute("SELECT judul, deskripsi, icon FROM proker")
    proker_list = cursor.fetchall()

    # Pengurus
    cursor.execute('SELECT nama, jabatan, divisi FROM pengurus')
    rows = cursor.fetchall()

    # Event
    cursor.execute("SELECT nama_event, foto, deskripsi FROM event")
    event_list = cursor.fetchall()
    
    conn.close()

    # pengolahan data pengurus
    pengurus_data = {}
    seen = set()
    for nama, jabatan, divisi in rows:
        key = (nama, jabatan, divisi)
        if key not in seen:
            if divisi not in pengurus_data:
                pengurus_data[divisi] = []
            pengurus_data[divisi].append(f"{nama} - {jabatan}")
            seen.add(key)

    print("Isi event_list:", event_list)
    return render_template('index.html', 
                       visi=visi, 
                       misi_list=misi_list, 
                       proker_list=proker_list, 
                       pengurus=pengurus_data, 
                       event_list=event_list)

if __name__ == '__main__':
    app.run(debug=True)

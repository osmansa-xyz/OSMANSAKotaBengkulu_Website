import sqlite3

def setup_visi_misi():
    conn = sqlite3.connect('osmansa.db')
    cursor = conn.cursor()
    
    # tabel visi_misi
    cursor.execute('''CREATE TABLE IF NOT EXISTS visi_misi 
                      (id INTEGER PRIMARY KEY, kategori TEXT, isi TEXT)''')
    
    cursor.execute("DELETE FROM visi_misi") 
    cursor.execute("INSERT INTO visi_misi (kategori, isi) VALUES ('visi', 'Mewujudkan OSIM MAN 1 Kota Bengkulu yang aktif, kreatif, dan inovatif, serta menjadikan OSIM sebagai wadah pengembangan potensi dan bakat siswa. Guna membentuk generasi yang berprestasi, berkarakter, dan berkontribusi positif bagi lingkungan sekolah.')")
    cursor.execute("INSERT INTO visi_misi (kategori, isi) VALUES ('misi', 'Menanamkan nilai ketakwaan sebagai fondasi utama dalam setiap kegiatan OSIM, untuk membentuk siswa yang tidak hanya cerdas, tapi juga berakhlak mulia.')")
    cursor.execute("INSERT INTO visi_misi (kategori, isi) VALUES ('misi', 'Menyelenggarakan kegiatan yang edukatif serta kreatif demi pengembangan bakat dan potensi siswa, sekaligus mendorong semangat berprestasi di lingkungan sekolah.')")
    cursor.execute("INSERT INTO visi_misi (kategori, isi) VALUES ('misi', 'Menjadikan OSIM sebagai wadah aspirasi siswa dan menjembatani komunikasi antara siswa dengan pihak madrasah, agar setiap suara dan pendapat siswa dapat ditampung dan dipertimbangkan secara adil.')")
    cursor.execute("INSERT INTO visi_misi (kategori, isi) VALUES ('misi', 'Meneruskan program kerja OSIM yang positif, dengan penyesuaian dan penyempurnaan guna memberikan dampak positif yang lebih luas bagi seluruh warga madrasah.')")
    cursor.execute("INSERT INTO visi_misi (kategori, isi) VALUES ('misi', 'Mewujudkan kepengurusan OSIM yang berdedikasi tinggi, sehingga seluruh anggota dapat menjadi teladan dalam bersikap, berorganisasi, dan berkontribusi di lingkungan madrasah.')")
    
    conn.commit()
    conn.close()

setup_visi_misi()

def setup_proker():
    conn = sqlite3.connect('osmansa.db')
    cursor = conn.cursor()
    
    # tabel proker
    cursor.execute('''CREATE TABLE IF NOT EXISTS proker 
                      (id INTEGER PRIMARY KEY, judul TEXT, deskripsi TEXT, icon TEXT)''')
    
    # data proker
    cursor.execute("DELETE FROM proker")
    proker_data = [
        ('Pekan Islami Madrasah', 'Meningkatkan pemahaman keagamaan dan mempererat ukhuwah Islamiyah melalui lomba islami, kajian, dan aksi sosial untuk menumbuhkan akhlak mulia.', 'calendar-heart'),
        ('Kompetisi Akademik', 'Penyelenggaraan lomba Ranking 1, Cerdas Cermat, dan kompetisi pengetahuan umum lainnya pada perayaan hari besar untuk memacu semangat intelektual.', 'trophy'),
        ('Madrasah Bersih & Sehat', 'Menciptakan lingkungan belajar yang nyaman melalui kerja bakti rutin dan lomba kebersihan kelas yang melibatkan seluruh warga madrasah.', 'leaf'),
        ('Kotak Saran Siswa', 'Wadah aspirasi terbuka di lokasi strategis untuk menampung kritik dan saran siswa yang akan ditindaklanjuti secara berkala bersama pihak madrasah.', 'message-square-plus'),
        ('Evaluasi Rutin', 'Kegiatan evaluasi berkala terhadap program kerja dan kinerja pengurus guna meningkatkan efektivitas, partisipasi, dan dampak positif bagi seluruh siswa.', 'clipboard-check')
    ]
    cursor.executemany("INSERT INTO proker (judul, deskripsi, icon) VALUES (?, ?, ?)", proker_data)
    
    conn.commit()
    conn.close()

setup_proker()

def init_db():
    conn = sqlite3.connect('osmansa.db')
    cursor = conn.cursor()
    
    # tabel pengurus
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pengurus (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT NOT NULL,
            jabatan TEXT NOT NULL,
            divisi TEXT NOT NULL
        )
    ''')
    
    data = [
        ('Yutia Gustari, S.Sn.', 'PEMBINA', 'PEMBINA'),
        ('Hamzah Fansyuri', 'KETUA', 'PENGURUS INTI'),
        ('M. Azzam Kurniawan', 'WAKIL KETUA', 'PENGURUS INTI'),
        ('Faiza Adzka Afdhalia', 'SEKRETARIS', 'PENGURUS INTI'),
        ('Diah Melati Lubis', 'BENDAHARA', 'PENGURUS INTI'),
        ('Syauqi Raudhah F.', 'KOORDINATOR', 'HUMAS MULTIMEDIA'),
        ('Chelsha Kinah R.', 'ANGGOTA', 'HUMAS MULTIMEDIA'),
        ('El Fahri Pradipta', 'KOORDINATOR', 'KESENIAN & KEAGAMAAN ISLAMI'),
        ('Adella Hesti M.', 'ANGGOTA', 'KESENIAN & KEAGAMAAN ISLAMI'),
        ('Anggun Rahmadani', 'ANGGOTA', 'KESENIAN & KEAGAMAAN ISLAMI'),
        ('M. Faizul Haq', 'ANGGOTA', 'KESENIAN & KEAGAMAAN ISLAMI'),
        ('Carine Syahira Z.', 'ANGGOTA', 'KESENIAN & KEAGAMAAN ISLAMI'),
        ('Zlatan Rahcel S.', 'KOORDINATOR', 'OLAHRAGA SATUAN KEAMANAN'),
        ('M. Ahza Bayhaqi', 'ANGGOTA', 'OLAHRAGA SATUAN KEAMANAN'),
        ('Azza Fadillah P. J.', 'ANGGOTA', 'OLAHRAGA SATUAN KEAMANAN'),
        ('M. Daffa Khairan', 'ANGGOTA', 'OLAHRAGA SATUAN KEAMANAN'),
        ('Leo Prabowo', 'KOORDINATOR', 'PERLENGKAPAN & PEMBEKALAN'),
        ('Bunga Dzahirah', 'ANGGOTA', 'PERLENGKAPAN & PEMBEKALAN'),
        ('M. R. Almico C. D.', 'ANGGOTA', 'PERLENGKAPAN & PEMBEKALAN'),
        ('Alfaizah Luthfia S.', 'ANGGOTA', 'PERLENGKAPAN & PEMBEKALAN'),
    ]
    cursor.executemany('INSERT INTO pengurus (nama, jabatan, divisi) VALUES (?, ?, ?)', data)
    
    conn.commit()
    conn.close()

def setup_event():
    conn = sqlite3.connect('osmansa.db')
    cursor = conn.cursor()
    
    # Tambahkan kolom 'foto'
    cursor.execute('''CREATE TABLE IF NOT EXISTS event 
                      (id INTEGER PRIMARY KEY, nama_event TEXT, foto TEXT, deskripsi TEXT)''')
    
    cursor.execute("DELETE FROM event")
    event_data = [
        ('Isra Miraj', 'isra.jpg', 'Peringatan perjalanan suci Nabi Muhammad SAW yang diisi dengan kajian mendalam untuk meningkatkan keimanan dan ketakwaan siswa.'),
        ('Bulan Bahasa', 'bahasa.jpg', 'Perayaan untuk mengapresiasi kekayaan bahasa dan sastra melalui berbagai lomba kreatif seperti ranking 1, dongeng, dan sayembara maskot.'),
        ('Liga MAN', 'liga.jpg', 'Kompetisi olahraga tahunan antarkelas yang dirancang untuk membangun sportivitas, kerjasama tim, dan kesehatan fisik siswa.'),
        ('Maulid Nabi', 'maulid.jpg', 'Perayaan hari lahir Nabi Muhammad SAW yang dirayakan dengan penuh syukur melalui lantunan shalawat, tausiyah, serta aksi sosial.'),
        ('Social Project Ramadan: MABAR#1 (Madrasah Berburu Amal Ramadan)', 'spr.jpg', 'Proyek sosial mandiri OSIM MAN 1 Kota Bengkulu yang diisi dengan penyaluran bantuan ke panti asuhan dan pembagian takjil gratis di sekitar lingkungan madrasah selama bulan Ramadan.'),
        ('Class Meeting', 'clm.jpg', 'Kegiatan rutin pasca-ujian semester yang berfungsi sebagai sarana penyegaran sekaligus wadah penyaluran bakat siswa di bidang olahraga, seni, dan kreativitas.')
    ]
    cursor.executemany("INSERT INTO event (nama_event, foto, deskripsi) VALUES (?, ?, ?)", event_data)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_visi_misi()
    setup_proker()
    init_db()
    setup_event()
    print("Semua data berhasil dimasukkan ke osmansa.db!")

import psycopg2
import csv

# PostgreSQL veritabanına bağlan
conn = psycopg2.connect(
    host="localhost",
    database="sendpython",
    user="postgres",
    password="1973852"
)

# Cursor nesnesi oluştur
cur = conn.cursor()

# CSV dosyasını okumak için aç
with open("yeni_veriler.csv", "r", encoding="utf-8") as f:
    # csv.reader nesnesi oluştur
    reader = csv.reader(f)
    # CSV dosyasındaki her satır için
    next(reader)
    
    for row in reader:
        # PostgreSQL veritabanına veri ekle
        cur.execute("INSERT INTO tablo VALUES (%s, %s, %s, %s, %s, %s, %s)", row)

# İşlemi onayla
conn.commit()

# Bağlantıyı kapat
conn.close()

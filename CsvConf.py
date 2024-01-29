import csv
with open("ilan.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    with open("yeni_veriler.csv", "w", encoding="utf-8", newline="") as g:
        writer = csv.writer(g)
        for row in reader:
            column = row[4]
            column = column.replace(".", "")
            column = column.replace(" TL","")
            row[4] = column
            writer.writerow(row)

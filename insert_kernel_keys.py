import csv
import MySQLdb as MyCl

db = MyCl.connect('localhost', 'root', 'manhee33338', 'test')
db.set_character_set('utf8')
cursor = db.cursor()

with open("porter_all_keys_not_sorted.csv", newline='') as f:
    reader = csv.reader(f, delimiter =",")
    for row in reader:

        q = "INSERT INTO kernel_keyword (kernel_keyword, chastot) VALUES(%s,%s)"
        cursor.execute(q,(row))

        print(row)
    db.commit()
    f.close()
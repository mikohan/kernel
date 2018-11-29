import csv
import MySQLdb as MyCl

db = MyCl.connect('localhost', 'root', 'manhee33338', 'test')
db.set_character_set('utf8')
cursor = db.cursor()

with open("engine_cat.csv", newline='') as f:
    reader = csv.reader(f, delimiter =",")
    for row in reader:

        q = "INSERT INTO category_olesya (parent_id, category_name) VALUES(%s,%s)"
        cursor.execute(q,(row))

        print(row)
    db.commit()
    f.close()
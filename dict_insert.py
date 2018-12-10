import MySQLdb as MyCl
import csv



# Open database connection
db = MyCl.connect('localhost', 'root', 'manhee33338', 'test')
db.set_character_set('utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()


#название таблицы в Mysql
table = "dict"
def insertDict(row):


    q = "INSERT INTO " + table + " (`id`, `category_id`, `category_name`, `subcat_id`, `subcat_name`, `filter_id`, `filter_name`, `group_id`, `group_name`, `key_plus`, `key_minus`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print(q,row)
    cursor.execute(q,row)

delquery = "TRUNCATE TABLE " + table
cursor.execute(delquery)
db.commit()


with open('groups_dictionary.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        line_count += 1
        insertDict(row)
    print("Processed {} lines.".format(line_count))

db.commit()













db.close()
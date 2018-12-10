import MySQLdb as MyCl

# Open database connection
db = MyCl.connect('localhost', 'root', 'manhee33338', 'test')
db.set_character_set('utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()


#название таблицы в Mysql
table_to = "names_all_nocat"
table_from = "names_all"
params = ('names_all_nocat','names_all')

d = "TRUNCATE TABLE " + table_to
cursor.execute(d)
db.commit()


q = "INSERT INTO " + table_to + " (ang_name, category_id, category_name, subcat_id, subcat_name, group_id, group_name) SELECT ang_name, category_id, category_name, subcat_id, subcat_name, group_id, group_name FROM " + table_from + " WHERE group_id = ''"

cursor.execute(q)
db.commit()
print("Не Категоризировалось  = {}".format(cursor.rowcount) + " позиций")
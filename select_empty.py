import MySQLdb as MyCl

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Open database connection
db = MyCl.connect('localhost', 'root', 'manhee33338', 'test')
db.set_character_set('utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()

print("="*80)
table_from = input(bcolors.WARNING + "Введите название таблицы MySql с которой работаем:" + bcolors.OKBLUE + bcolors.BOLD + "[cat_starex]").strip()
table_from = table_from or 'cat_starex'
print("="*80)
table_to = input(bcolors.WARNING + "Введите название таблицы MySql с которой работаем:" + bcolors.OKBLUE + bcolors.BOLD + "[cat_starex_empty]").strip()
table_to = table_to or 'cat_starex_empty'
print(bcolors.OKBLUE + bcolors.BOLD + "Работаем с таблицей:" + table_from + " и таблицей: " + table_to)
print("="*80)

#название таблицы в Mysql
#table_to = "names_all_nocat"
#table_from = "names_all"

params = (table_to,table_from)

d = "TRUNCATE TABLE " + table_to
cursor.execute(d)
db.commit()


q = "INSERT INTO " + table_to + " (ang_name, category_id, category_name, subcat_id, subcat_name, group_id, group_name) SELECT ang_name, category_id, category_name, subcat_id, subcat_name, group_id, group_name FROM " + table_from + " WHERE group_id = ''"

cursor.execute(q)
db.commit()
print("Не Категоризировалось  = {}".format(cursor.rowcount) + " позиций")
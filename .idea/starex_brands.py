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
q = "SELECT ang_name,cat,brand FROM cat_starex WHERE cat REGEXP '[A-Za-z0-9]{10,11}'"
#q = "DELETE FROM cat_starex WHERE cat NOT REGEXP '^[A-Za-z0-9]{10,11}$'"
#q = "SELECT ang_name,cat,brand FROM cat_starex ORDER BY ang_name"
#q = "DELETE FROM cat_starex WHERE ang_name LIKE '%жидкость%' OR ang_name LIKE '%антифриз%'"
#q = "DELETE FROM cat_starex WHERE group_id = ''"
cursor.execute(q)
for c in cursor:
    print(bcolors.BOLD + bcolors.OKBLUE)
    print(c)
print("Выдернулось строк: ",cursor.rowcount)
#db.commit()
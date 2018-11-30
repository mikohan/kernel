import pprint
import MySQLdb as MyCl

p = pprint.pprint

table = "names_all"


keyPlus = input("Введите ключевые слова через запятую:").split(",")
keyPlus = list(map(str.strip, keyPlus))
keyMinus = input("Введите минус слова через запятую:").split(",")
keyMinus = list(map(str.strip, keyMinus))

db = MyCl.connect('localhost', 'root', 'manhee33338', 'test')
db.set_character_set('utf8')
cursor = db.cursor()


def addPercent(myList):
    newList = []
    for l in myList:
        n = "%" + l + "%"
        newList.append(n)
    return newList





def getSearch(cursor,keyPlus,keyMinus =[]):




        if len(keyPlus) == 1:
            q = "SELECT ang_name FROM " + table + " WHERE ang_name LIKE %s"
        else:
            q = "SELECT ang_name FROM " + table + " WHERE (ang_name LIKE %s"
        iterable = iter(keyPlus)
        next(iterable)
        for plus in iterable:

            an = " OR ang_name LIKE %s"

            q += an
        if len(keyPlus) != 1:
            q = q + ")"
        print(q)
        args = addPercent(keyPlus)
        if keyMinus[0] == "":
            return(q, args)
        else:
            if keyMinus[0] !="":
                if len(keyMinus) == 1:
                    mq = " AND ang_name NOT LIKE %s"
                else:
                    mq =" AND (ang_name NOT LIKE %s"

                it = iter(keyMinus)
                next(it)
                for minus in it:

                    mn = " AND ang_name NOT LIKE %s"
                    mq += mn
                if len(keyMinus) != 1:
                    mq = mq + ")"
                queryList = keyPlus + keyMinus
                args = addPercent(queryList)
                return(q+mq, args)



exec = getSearch(cursor, keyPlus, keyMinus)

print(exec[0])
print(exec[1])

cursor.execute(exec[0],exec[1])

p(cursor.fetchall())













    # for row in reader:
    #
    #     q = "INSERT INTO category_olesya (parent_id, category_name) VALUES(%s,%s)"
    #     cursor.execute(q,(row))
    #
    #     print(row)
    # db.commit()
    # f.close()


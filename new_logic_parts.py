import pprint
import MySQLdb as MyCl

p = pprint.pprint

table = "names_all"


keyPlus = input("Введите ключевые фразы или слова, через запятую:").split(",")
keyPlus = list(map(str.strip, keyPlus))

superPlus = []
for i in range(0,len(keyPlus)):
    key_each = keyPlus[i].split(' ')
    superPlus.append(key_each)


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


#Если есть толко одна фраза или одно слово в ключевых словах. Минус слов нет.
if len(superPlus) == 1 and keyMinus[0] =='':
    q = "SELECT ang_name FROM " + table + " WHERE ang_name LIKE %s"
    for s_one in range(1,len(superPlus[0])):
        an = " AND ang_name LIKE %s"
        q += an
    cursor.execute(q,addPercent(superPlus[0]))
    bigQuery = p(cursor.fetchall())
    print("Строк соответсвует запросу:" + str(cursor.rowcount))

#Если есть одна фраза и минус слова
if len(superPlus) == 1 and len(keyMinus) >= 1:

    q = "SELECT ang_name FROM " + table + " WHERE (ang_name LIKE %s"
    for s_one in range(1,len(superPlus[0])):
        an = " AND ang_name LIKE %s"
        q += an
    q = q + ')'
    for m in range(0,len(keyMinus)):
        if m == 0:
            mn = " AND (ang_name NOT LIKE %s"
        else:
            mn = " AND ang_name NOT LIKE %s"
        q += mn
    q = q + ')'
    args = addPercent(superPlus[0]) + addPercent(keyMinus)
    cursor.execute(q,args)
    bigQuery = p(cursor.fetchall())
    print("Строк соответсвует запросу:" + str(cursor.rowcount))


#Если есть несколько фраз и минус слова

if len(superPlus) > 1 and keyMinus[0] != '':

    q = "SELECT ang_name FROM " + table + " WHERE (("
    an = ''
    for prase in range(0,len(superPlus)):
        #p(prase)

        for plus in range(0,len(superPlus[prase])):
            num = plus+1
            if len(superPlus[prase]) == num:
                an += " ang_name LIKE %s"
            else:
                an += " ang_name LIKE %s AND "
        if len(superPlus) == prase +1:
            an = an + ")"
        else:
            an = an + ") OR ("

    q = q + an
    q = q + ')'
    q = q + " AND ("
    mq = ''
    for minus in range(0,len(keyMinus)):
        if minus == 0:
            mq += " ang_name NOT LIKE %s"
        else:
            mq += " AND ang_name NOT LIKE %s"

    q = q + mq + ")"

    newList = []
    for keyArray in range(0,len(superPlus)):
        for mn in range(0,len(superPlus[keyArray])):
            newList.append(superPlus[keyArray][mn])

    for nms in range(0,len(keyMinus)):
        newList.append(keyMinus[nms])
    args = addPercent(newList)


    cursor.execute(q,args)
    bigQuery = p(cursor.fetchall())
    print("Строк соответсвует запросу:" + str(cursor.rowcount))

#Если есть несколько слов плюс но нет минус слов

if len(superPlus) > 1 and keyMinus[0] == '':

    q = "SELECT ang_name FROM " + table + " WHERE (("
    an = ''
    for prase in range(0,len(superPlus)):

        for plus in range(0,len(superPlus[prase])):
            num = plus+1
            if len(superPlus[prase]) == num:
                an += " ang_name LIKE %s"
            else:
                an += " ang_name LIKE %s AND "
        if len(superPlus) == prase +1:
            an = an + ")"
        else:
            an = an + ") OR ("

    q = q + an
    q = q + ')'

    newList = []
    for keyArray in range(0,len(superPlus)):
        for mn in range(0,len(superPlus[keyArray])):
            newList.append(superPlus[keyArray][mn])


    args = addPercent(newList)



    cursor.execute(q,args)
    bigQuery = p(cursor.fetchall())
    print("Строк соответсвует запросу:" + str(cursor.rowcount))



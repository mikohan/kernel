import pprint
import MySQLdb as MyCl

p = pprint.pprint

table = "kernel_keyword"
field_name = "kernel_keyword"


keyPlus = input("Введите ключевые фразы или слова, через запятую:").split(",")
keyPlus = list(map(str.strip, keyPlus))

superPlus = []
for i in range(0,len(keyPlus)):
    key_each = keyPlus[i].split(' ')
    superPlus.append(key_each)
#p(superPlus)


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
    q = "SELECT " + field_name + ", chastot FROM " + table + " WHERE " + field_name + " LIKE %s"
    for s_one in range(1,len(superPlus[0])):
        an = " AND " + field_name + " LIKE %s"
        q += an
    cursor.execute(q,addPercent(superPlus[0]))
    bigQuery = p(cursor.fetchall())
    p(bigQuery)
    print("Строк соответсвует запросу:" + str(cursor.rowcount))

#Если есть одна фраза и минус слова
if len(superPlus) == 1 and keyMinus[0] != '':

    q = "SELECT " + field_name + ", chastot FROM " + table + " WHERE (" + field_name + " LIKE %s"
    for s_one in range(1,len(superPlus[0])):
        an = " AND " + field_name + " LIKE %s"
        q += an
    q = q + ')'
    for m in range(0,len(keyMinus)):
        if m == 0:
            mn = " AND (" + field_name + " NOT LIKE %s"
        else:
            mn = " AND " + field_name + " NOT LIKE %s"
        q += mn
    q = q + ')'
    args = addPercent(superPlus[0]) + addPercent(keyMinus)
    print(q,args)
    cursor.execute(q,args)
    bigQuery = p(cursor.fetchall())
    p(bigQuery)
    print("Строк соответсвует запросу:" + str(cursor.rowcount))


#Если есть несколько фраз и минус слова

if len(superPlus) > 1 and keyMinus[0] != '':

    q = "SELECT " + field_name + ", chastot FROM " + table + " WHERE (("
    an = ''
    for prase in range(0,len(superPlus)):
        #p(prase)

        for plus in range(0,len(superPlus[prase])):
            num = plus+1
            if len(superPlus[prase]) == num:
                an += " " + field_name + " LIKE %s"
            else:
                an += " " + field_name + " LIKE %s AND "
    #p(an.replace("AND", "", 1))
        if len(superPlus) == prase +1:
            an = an + ")"
        else:
            an = an + ") OR ("
    #p(an)

    q = q + an
    q = q + ')'
    #p(q)
    #p(superPlus)
    q = q + " AND ("
    mq = ''
    for minus in range(0,len(keyMinus)):
        if minus == 0:
            mq += " " + field_name + " NOT LIKE %s"
        else:
            mq += " AND " + field_name + " NOT LIKE %s"

    q = q + mq + ")"
    print(q)

    newList = []
    for keyArray in range(0,len(superPlus)):
        for mn in range(0,len(superPlus[keyArray])):
            newList.append(superPlus[keyArray][mn])

    for nms in range(0,len(keyMinus)):
        newList.append(keyMinus[nms])
    args = addPercent(newList)
    p(newList)


    cursor.execute(q,args)
    bigQuery = p(cursor.fetchall())
    p(bigQuery)
    print("Строк соответсвует запросу:" + str(cursor.rowcount))

#Если есть несколько слов плюс но нет минус слов

if len(superPlus) > 1 and keyMinus[0] == '':

    q = "SELECT " + field_name + ", chastot FROM " + table + " WHERE (("
    an = ''
    for prase in range(0,len(superPlus)):
        #p(prase)

        for plus in range(0,len(superPlus[prase])):
            num = plus+1
            if len(superPlus[prase]) == num:
                an += " " + field_name + " LIKE %s"
            else:
                an += " " + field_name + " LIKE %s AND "
    #p(an.replace("AND", "", 1))
        if len(superPlus) == prase +1:
            an = an + ")"
        else:
            an = an + ") OR ("
    #p(an)

    q = q + an
    q = q + ')'
    #p(q)
    #p(superPlus)

    print(q)

    newList = []
    for keyArray in range(0,len(superPlus)):
        for mn in range(0,len(superPlus[keyArray])):
            newList.append(superPlus[keyArray][mn])


    args = addPercent(newList)
    p(args)


    cursor.execute(q,args)
    bigQuery = p(cursor.fetchall())
    p(bigQuery)
    print("Строк соответсвует запросу:" + str(cursor.rowcount))



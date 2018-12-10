import pprint
import MySQLdb
import os

p = pprint.pprint






db = MySQLdb.connect('localhost', 'root', 'manhee33338', 'test')
db.set_character_set('utf8')
cursor = db.cursor()


#название таблицы в Mysql
#table = "porter_test_progon"
table = "names_all"
dictTable = "dict"


def addPercent(myList):
    newList = []
    for l in myList:
        n = "%" + l + "%"
        newList.append(n)
    return newList

def getItems(keyPlus,keyMinus):


    #Разбираем плюс слова
    keyPlus = keyPlus.rstrip(',')
    keyMinus = keyMinus.rstrip(",")
    keyPlus = keyPlus.split(",")
    keyPlus = list(map(str.strip, keyPlus))

    #Разбираем минус слова
    keyMinus = keyMinus.split(",")
    keyMinus = list(map(str.strip, keyMinus))

    #Разбираем плюс фразы на отдельные слова
    superPlus = []
    for i in range(0, len(keyPlus)):
        key_each = keyPlus[i].split(' ')
        superPlus.append(key_each)

    #Основная логика.....

    #Если есть толко одна фраза или одно слово в ключевых словах. Минус слов нет.
    if len(superPlus) == 1 and keyMinus[0] =='':
        q = "SELECT id,ang_name FROM " + table + " WHERE ang_name LIKE %s"
        for s_one in range(1,len(superPlus[0])):
            an = " AND ang_name LIKE %s"
            q += an
        cursor.execute(q,addPercent(superPlus[0]))
        bigQuery = cursor.fetchall()
        #p(bigQuery)
        #print("Строк соответсвует запросу:" + str(cursor.rowcount))
        return bigQuery

    #Если есть одна фраза и минус слова
    if len(superPlus) == 1 and len(keyMinus) >= 1:

        q = "SELECT id,ang_name FROM " + table + " WHERE (ang_name LIKE %s"
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
        bigQuery = cursor.fetchall()
        #p(bigQuery)
        #print("Строк соответсвует запросу:" + str(cursor.rowcount))
        return bigQuery


    #Если есть несколько фраз и минус слова

    if len(superPlus) > 1 and keyMinus[0] != '':

        q = "SELECT id,ang_name FROM " + table + " WHERE (("
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
        bigQuery = cursor.fetchall()
        #p(bigQuery)
        #print("Строк соответсвует запросу:" + str(cursor.rowcount))
        return bigQuery


    #Если есть несколько слов плюс но нет минус слов

    if len(superPlus) > 1 and keyMinus[0] == '':

        q = "SELECT id,ang_name FROM " + table + " WHERE (("
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
        bigQuery = cursor.fetchall()
        #p(bigQuery)
        #print("Строк соответсвует запросу:" + str(cursor.rowcount))
        return bigQuery
#Конец функции присваивания категорий по словарю


#Функция очистки таблицы

def clearTable():
    q = "UPDATE " + table + " SET category_id = 0, category_name = '', subcat_id = '', subcat_name = '', group_id = '', group_name = '' ;"
    cursor.execute(q)
    db.commit()


#Функция вставки в бд

def mysqlInsert(row,id):
    q = "UPDATE " + table + " SET category_id = %s, category_name = %s, subcat_id = CONCAT(subcat_id,%s), subcat_name = CONCAT(subcat_name,%s), group_id = CONCAT(group_id,%s),group_name = CONCAT(group_name, %s) WHERE id =%s;"
    param = [row[1],row[2], ',' + row[3], ',' + row[4],',' + row[7], ',' + row[8],id]
    print(param)
    cursor.execute(q,param)
    db.commit()

#Очищаем таблицу от старого присваивания субкатегорий и групп

clearTable()


#Выбираем по порядку из таблицы словаря строку и вставляем в базу

def getDictRow(dictTable):
    q = "SELECT * FROM " + dictTable + ";"
    cursor.execute(q)
    rows = cursor.fetchall()
    for row in rows:
        #print(row)
        #mysqlInsert(row)

        items = getItems(row[9],row[10])
        for item in items:
            mysqlInsert(row,item[0])
            # p(row)
            # print(' | ')
            # p(item[0])



getDictRow(dictTable)

db.close()


duration = 1  # second
freq = 440  # Hz
os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % (duration, freq))



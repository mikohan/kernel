import csv
with open("PorterOlesyaCopy.csv", newline='') as f:
    reader = csv.reader(f, delimiter =",")
    for row in reader:
        print(row)
    f.close()
import csv

def read():
    file = open("filehandling.csv", "r")
    data=[]
    try:
        cr = csv.reader(file)
        for i in cr:
            data.append(i)
        print("\n")
        for i in data[1:]:
            print(i)
        print("\n")
    except Exception as e:
        print("An Error occured....... Error: ",e)
    file.close()
def write():
    file=open("filehandling.csv","w",newline="")
    cw=csv.writer(file)
    list=[["roll no","name"]]
    roll_no = int(input("enter roll no: "))
    name = input("enter name: ")
    print("Written Successfully\n")
    list.append([roll_no, name])

    x=int(input("Press 1 to Enter More Records\nPress 2 to Exit\n\nYour Choice:"))
    while True:
        if x==1:
            roll_no=int(input("enter roll no: "))
            name=input("enter name: ")
            list.append([roll_no,name])
            print("\nRecords Added Successfully.\n")
        if x==2:
            cw.writerows(list)
            print("Exited successfully.")
            break
        x = int(input("Press 1 to Enter More Records\nPress 2 to Exit\n\nYour Choice:"))
    file.close()
def append():
    file = open("filehandling.csv", "a", newline="")
    list = [["roll no", "name"]]
    roll_no = int(input("enter roll no: "))
    name = input("enter name: ")
    cw=csv.writer(file)
    data=[roll_no,name]
    cw.writerow(data)
    file.close()
def search():
    file = open("filehandling.csv", "r")
    cr=csv.reader(file)
    roll_no=input("enter roll no to search: ")
    for i in cr:
        if i[0]==roll_no:
            print("Data Found.")
            print(i)
def update():
    data=[]
    file = open("filehandling.csv", "r")
    cr=csv.reader(file)
    for i in cr:
        data.append(i)
    file.close()
    roll_no=input("\nRoll no to update: ")
    name=input("Name to change to: ")
    for i in data:
        if i[0]==roll_no:
            i[1]=name

    file = open("filehandling.csv", "w",newline='')
    cw=csv.writer(file)
    cw.writerows(data)
    print("\nData Updated Successfully.")
    file.close()
def delete():
    data = []
    file = open("filehandling.csv", "r")
    cr = csv.reader(file)
    for i in cr:
        data.append(i)
    file.close()
    roll_no = input("\nRoll no to delete: ")
    for i in data[1:]:
        if i[0]== roll_no:
            index=data.index(i)
            data.remove(data[index])

    file = open("filehandling.csv", "w",newline='')
    cw = csv.writer(file)
    cw.writerows(data)
    file.close()

    print("\nData Deleted Successfully.")

a=int(input("---Menu---\n\nPress the number corresponding to the functions written below to execute them.\n\nReading(1)\nWriting(2)\nAppending(3)\nSearching(4)\nUpdating(5)\nDeleting(6)\nPress 7 to Exit\n\nYour Choice: "))
while True:
    if a==1:
        read()
    if a==2:
        write()
    if a==3:
        append()
    if a==4:
        search()
    if a==5:
        update()
    if a==6:
        delete()
    #if a!=1 or a!=2 or a!=3 or a!=4 or a!=5 or a!=6:
        #exit()
    if a==7:
        exit()
    a = int(input("---Menu---\n\nPress the number corresponding to the functions written below to execute them.\n\nReading(1)\nWriting(2)\nAppending(3)\nSearching(4)\nUpdating(5)\nDeleting(6)\nPress 7 to Exit\n\n Your Choice: "))

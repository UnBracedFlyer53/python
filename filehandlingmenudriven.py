import pickle
lst=[]

def read():
    try:
        file=open(r"C:\Users\h\Desktop\fileaditya.dat", "rb")
        data=pickle.load(file)
        print(data)
        file.close()
    except EOFError:
        print("no data in file !")


def write():
    file = open(r"C:\Users\h\Desktop\fileaditya.dat", "wb")
    x = int(input("1 to write more data, 2 to break: "))
    while True:
        if x==1:
            roll_no = int(input("enter roll no : "))
            name = str(input("enter name : "))
            l = [roll_no, name]
            lst.append(l)
            print("written successfully")

        if x==2:
            pickle.dump(lst, file)
            break

        x=int(input("1 to write more data, 2 to break: "))
    file.close()

def append():
    with open(r"C:\Users\h\Desktop\fileaditya.dat","rb+") as file:
        data=pickle.load(file)
        roll_no=int(input("enter roll no: "))
        name=input("enter name: ")
        l1=[roll_no,name]
        data.append(l1)
        #data.append([roll_no,name])
        file.seek(0)
        pickle.dump(data, file)
        
       # return data

def search():
    file=open(r"C:\Users\h\Desktop\fileaditya.dat", "rb")
    data=pickle.load(file)
    s=int(input("Roll no to search: "))
    for i in data:
        if i[0]==s:
            print("Element found:  ",i[1])
        

def update():
    file = open(r"C:\Users\h\Desktop\fileaditya.dat", "rb+")
    data=pickle.load(file)
    roll_no=int(input("Roll no to update: "))
    name=input("Name to change to: ")
    for i in data:
        if i[0]==roll_no:
            i[1]=name
            print(data)
    file.seek(0)
    pickle.dump(data, file)
    print("Updated Sucessfully.")

def delete():
    file = open(r"C:\Users\h\Desktop\fileaditya.dat", "rb+")
    data=pickle.load(file)
    roll_no=int(input("Enter roll no to delete : "))
    for i in data:
        if i[0]==roll_no:
            j=data.index(i)
            data.remove(data[j])
    file.seek(0)
    pickle.dump(data, file)
    print("Data after deletion: ",data)
    print("Record deleted successfully.")

def format():
    f=open(r"C:\Users\h\Desktop\fileaditya.dat","wb")
    d=""
    pickle.dump(d,f)
    print("Format successful.")

print("---Menu---\n Reading(Press 1)\n Writing(Press 2)\n Appending(Press 3)\n Search(Press 4)\n Update(Press 5)\n Exiting(Press 6)\n Formatting the file(Press 7)\n Delete a record(Press 8)\n")
a=int(input(" Your Choice: "))
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
        print("exited successfully")
        break
    if a==7:
        format()
    if a==8:
        delete()

    print("---Menu---\n Reading(Press 1)\n Writing(Press 2)\n Appending(Press 3)\n Search(Press 4)\n Update(Press 5)\n Exiting(Press 6)\n Formatting the file(Press 7)\n Delete a record(Press 8)\n")
    a = int(input(" Your Choice: "))

import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if c==1:
            value=input("type here\n")
            with open("keval-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
                print("succsessfully written")
        elif c==2:
            value=input("type here\n")
            with open("keval-food.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
                print("succsessfully written")
    
    elif k==2:
        c=int(input("enter 1 for ex and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("keval-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("keval-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")

try:
    print("health management system: ")
    a=(input("Press 1 for log the value and 2 for retrieve"))
    if a==1:
        b = int(input("Press 1 for keval 2 for rohan 3 for hammad "))
        take(b)
    else:
        b = int(input("Press 1 for keval 2 for rohan 3 for hammad "))
        retrieve(b)
except:
    print("type only numbers (1,2)")
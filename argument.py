print("....geetesh kumbalkar...")
print("Demonstrite of types of function argument ")

def Batches1(name,fees):
    print("Batch name is",name)
    print("Fees are",fees)

print("Demonstration keyword of arguments")

Batches1('Python',5000)
Batches1(5000,'angular')

def Batches2(name,fees):
    print("Batch name is", name)
    print("Fees are", fees)

print("Demonstration keyword of arguments")

Batches2(fees=9000,name='PPA')
Batches2(name='lb',fees=7500)

def Batches3(name,fees=5000):
    print("Batch name is", name)
    print("Fees are", fees)

print("Demonstration keyword of arguments")

Batches3('Angular',7500)
Batches3('Angular')
Batches3(fees=9000,name='ppa')
Batches3(name='lb')


def Add(*no):
    ans=0
    for i in no:
        ans=ans+i
        return ans
print("Demonstration keyword of arguments")

ret=Add(10,20,30)
print("Addition is",ret)


ret=Add(10,20,30,40,50,60)
print("Addition is",ret)

ret=Add(10,20)
print("Addition is",ret)

def Studentinfo(**other):
    print(other)
    for i,j,in other.items():
        print(i,j)

print("Demonstration keyword of arguments")
Studentinfo(age=28,address="Sinhagad road", mobile=7447376717,company="geetest xerox")




import module

def main():

    print("Value of __name__from main is :",__name__)
    print("enter first number :")
    no1=int(input())
    print("enter second number :")
    no2=int(input())
    iret=module.Addition(no1,no2)
    print("addition is :", iret)

if __name__=="__main__":
    main()
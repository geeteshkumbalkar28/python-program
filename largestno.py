#Application to findout the maximum no

def Maximum(no1,no2):
    if no1>no2:
        return no1
    else :
        return no2


def main():
    print("Enetr the number")
    value1=int(input())

    print("Enetr the 2nd number")
    value2=int(input())

    iret=Maximum(value1,value2)

    print("Maximum no is :",iret)

if __name__ == "__main__":
    main()
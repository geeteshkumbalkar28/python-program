

def main():
    print("Enetr the no")
    no=int(input())
    print("factor are:")
    for i in range(1,no,1):
        if no%i==0:
            print(i)
        i=i+1    
if __name__=="__main__":
    main()
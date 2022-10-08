def main():
    print("enter the element you create")
    i=int(input())
    values =list()
    for no in range(0,i):
        values.append(int(input()))
    print(values)
   # for i in range(0,len(values)):
   #    print(values[i])

if __name__ =="__main__":
    main()
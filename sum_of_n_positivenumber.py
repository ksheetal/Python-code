def sum_int(n):
    total=0
    for i in range(1,n+1):
        total+=i

    return total

def main():
    number = int(input("Enter Number : "))
    print("Total is : ",sum_int(number))


if __name__=="__main__":
    main()

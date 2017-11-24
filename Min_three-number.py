def find_min(n1,n2,n3):
    def min2(n1,n2):
        if(n1<n2):
            return n1
        else:
            return n2

    return min2(min2(n1,n2),n3)

def main():
    n1 = int(input("Enter First Number : "))
    n2 = int(input("Enter Second Number : "))
    n3 = int(input("Enter Third Number : "))
    print("Entered Number are :",n1,n2,n3)
    print('Minimum Number is :',find_min(n1,n2,n3))

if __name__=="__main__":
    main()

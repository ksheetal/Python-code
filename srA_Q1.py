def count_one(num):
    x1=bin(num)
    count = 0
    for i in range(1,len(x1)-1):
        count =x1.count('1')

    return count

def main():
    x = int(input("Enter any number :"))
    y=count_one(x)
    if(y%2==0):
        print("Evil Number")
    else:
        print("not Evil Number")
    

if __name__=='__main__':
    main()

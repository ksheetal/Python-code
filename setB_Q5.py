def add_list(list1):
    total=0
    for i in list1:
        if type(i)==list:
            total=total+add_list(i)
        else:
            total+=i
    return total

def main():
    list1 = [1,4,[5,3],2]
    print("total is :",add_list(list1))

          
if __name__=='__main__':
    main()

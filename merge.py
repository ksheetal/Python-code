import pdb
pdb.set_trace()

def merge(list1, list2):
    '''
    objective : merge two sorted list and return third list after sorting
    input parameter : list1 and list2
    return value : list3
    '''
    #approach : using recursion
    
    list3 = []

    if list1 == [] and list2 == []:
       return list3
    if list1 != [] and list2 == []:
       return list3 + list1
    if list1 == [] and list2 != []:
       return list3 + list2
    if list1 != [] and list2 != []:
       if list1[0] <= list2[0]:
          list3.append(list1[0])
          return list3 +  merge(list1[1:], list2)
       if list1[0] > list2[0]:
          list3.append(list2[0])
          return list3 +  merge(list1, list2[1:])

def main():
    list1=[int(x) for x in input("Enter list1 : ").split()]
    list2=[int(x) for x in input("Enter list2 : ").split()]
    merge(list1,list2)
    print("list after sorting",merge(list1,list2))

if __name__=="__main__":
    main()

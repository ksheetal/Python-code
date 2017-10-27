#import pdb
#pdb.set_trace()

def merge(list1, list2):
    '''
    objective : merge two sorted list and retrun third list after sorting
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
          list3 = list3 +  merge(list1[1:], list2)
       if list1[0] > list2[0]:
          list3.append(list2[0])
          list3 = list3 +  merge(list1, list2[1:])
    return list3

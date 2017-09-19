def find_index(list1, lower_bound, upper_bound,mini_index):
    '''
    Objective : to find the index of minimum number of sublist of list
    intput parameters :
    list1 : given list
    lower_bound : starting index of given sublist
    upper_bound : last index of given sublist
    mini_index : minimum index of given sublist
    return value : minimum index
    '''
    #approach : by comparing one element to another recursively

    if (lower_bound==upper_bound+1):
        return mini_index
    if (list1[mini_index]>list1[lower_bound]):
        mini_index=lower_bound
        lower_bound=lower_bound+1
        return find_index(list1,lower_bound,upper_bound,mini_index)
    else:
        return find_index(list1,lower_bound+1,upper_bound,mini_index)


def find_index_minimum(list1,lower_bound,upper_bound):
    '''
    objective : to call find_index function by adding lower bound value
    input parameter : none
    return value : find_index funciton by adding lower_bound
    '''
    return find_index(list1,lower_bound,upper_bound,lower_bound)


def sort_list1(list1,index=0):
    '''
    objective: to sort the list using minimum index of function
    input parameter :
                     list1 = list to be sorted
    return value : list after sorting
    '''
    if (len(list1)==index):
        return list1
    else:
        min_index=find_index_minimum(list1,index,len(list1)-1)
        temp=list1[index]
        list1[index]=list1[min_index]
        list1[min_index]=temp
        return sort_list1(list1,index+1)
    
def main():
    '''
    objective : to call find_index_minimum function
    input parameter :
    lower_bound = lower bound of sublist
    upper_bound = upper bound of sublist
    list1 = given list
    return value : none
    '''
list1 = [12,13,7,9,8,17,19,0]
print("YOUR LIST IS : ",list1)
print("LIST AFTER SORTING  : ",sort_list1(list1))
      
if __name__=='__main__':
      main()

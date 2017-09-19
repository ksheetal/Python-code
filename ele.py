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

def main():
'''
objective : to call find_index_minimum function
input parameter :
lower_bound = lower bound of sublist
upper_bound = upper bound of sublist
list1 = given list
return value : none

'''
list1 = [12,13,7,9,8,17,19]
print("YOUR LIST IS : ",list1)

lower_bound=int(input("ENTER THE VALUE OF LOWER BOUND : "))
upper_bound=int(input("ENTER THE VALUE OF UPPER BOUND : "))
print("INDEX OF MINIMUM ELEMENT OF SUBLIST IS : ",find_index_minimum(list1,lower_bound,upper_bound))
if __name__=='__main__':
main()

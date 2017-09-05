def mul(num1,num2):
    '''
    objective : to perform multiplication using predecessor
    '''
    if num2 == 0 :
         return 0
    else:
        return num1 + mul(num1,predecessor1(num2))

def pred(num2,i):
    '''
    objective : to find the predecessor of the given number
    input parameter:
        num : first number
        i: second number for increment
    return value : value of predecessor
    '''

    #approach : incremental approach.
    
    if num2 == 0 : 
        return 0
    if(inc(i)==num2):
        return i
    else:
        i=i+1
        return pred(num2,i)

def predecessor1(num2):
    i=0
    return pred(num2,i)

def inc(num1):
    '''
    objective : to increment number

    intput parameter :
        number num1

    return value : incremented number num1 

    '''
    # Approach : using incremental method in which we are incrementing number num1 by adding 1.

    num1=num1+1
    return num1   

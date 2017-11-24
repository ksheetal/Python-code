def change1(str1):
    str11 = str1[len(str1)-3:len(str1)]
    if(str11 == "ing"):
        str1=str1+'ly'
      #  print(str1)
    else:
        str1 = str1+'ing'
        
    return str1


def main():
    s = input("Enter String : ")
    if(len(s)<3):
        print(s)
    else:
        print(change1(s))
        
if __name__=='__main__':
    main()
    
    

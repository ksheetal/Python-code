def rev(str):
    if str =="":
        return str
    else:
        return rev(str[1:])+str[0]

def main():
    x=input("ENTER STRING :")
    print(rev(x))

if __name__=='__main__':
    main()
    

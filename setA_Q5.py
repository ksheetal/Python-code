def data():
    f=open("poem.txt","r")
    s=f.read()
    #print(s.split())
    s1=s.split()
    #print(s1)
    sortedWord = sorted(s1,key=len)
    print("Longest word : ",sortedWord[-1])
    print("Length is :",len(sortedWord[-1]))
def main():
    data()

if __name__=='__main__':
    main()

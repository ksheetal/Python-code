from collections import Counter
def data(s):
    s=s.split()
    counts = Counter(s)
    print(counts)
def main():
    s = str(input("Enter string: " ))
    data(s)

if __name__=='__main__':
    main()

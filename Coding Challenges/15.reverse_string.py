string=input("Enter a sentence:")
def rev_string(item):
    print(' '.join(item.split()[::-1]))
rev_string(string)    
if __name__ == '__main__':
    s = input()
    print(any([i.isalnum() for i in s])) #any function checks and returns TRUE if one of the input is true it works with tuples,lists,dictonaries
    print(any([i.isalpha() for i in s]))
    print(any([i.isdigit() for i in s]))
    print(any([i.islower() for i in s]))
    print(any([i.isupper() for i in s]))

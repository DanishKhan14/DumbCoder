#!/usr/bin/python

data = {}

def test():
    #data['Name'] = name
    print "Test Function\n"
    print data

def main():
    name = 'Danish'
    data['Name'] = name
    test()
    print "Main Function\n"
    print data

if __name__ == '__main__':
    main()

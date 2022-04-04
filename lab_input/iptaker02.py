#!/usr/bin/env python3
'''
Alta3 Research | RZFeeser
print() - display data to std out
'''

def main():
    # all code should appear within a function
    user_input = input('Please enter an IPv4 IP address: ')

    # the line below creates a single string that is passed to print()
    # print('You told me the IPV4 address is: ' + user_input)
    
    # print() can be given a series of objects separated by a comma
    print('You told me the IPV4 address is:', user_input)


# calling main() using this technique allows others to import your code
if __name__ == '__main__':
    main()

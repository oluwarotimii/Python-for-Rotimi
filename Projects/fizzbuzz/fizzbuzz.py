# Here I try to solve the FizzBuzz  multiples of 3 and 5 problem.


number = int(input('ENTER THE NUMBER: '))

def FizzBuzz() :
    fizzCounter = 0
    buzzCounter = 0
    fzbzCounter = 0 
    for x in range(number) :
        if x%3 == 0 :
            print('Fizz')
            fizzCounter = fizzCounter + 1
        elif x%5 == 0:
            print('Buzz')
            buzzCounter = buzzCounter + 1
        elif x%3 and x % 5 == 0 :
            print('FizzBuzz')
            fzbzCounter = fzbzCounter + 1
        else:
            print(x)

    print('Mulitples of 3 in ', number, 'is ', fizzCounter, '\nThe Total Number of number of Multiple of 5 is ', buzzCounter, '\nAnd for multiples of 3 and 5 is ', fzbzCounter)

FizzBuzz()
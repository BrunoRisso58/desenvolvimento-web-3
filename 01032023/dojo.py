def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    elif numero % 3 == 0:
        return 'Fizz'
    elif numero % 5 == 0:
        return 'Buzz'
    else:
        return numero

assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(3) == 'Fizz'
assert fizzbuzz(4) == 4
assert fizzbuzz(5) == 'Buzz'
assert fizzbuzz(6) == 'Fizz'
assert fizzbuzz(7) == 7
assert fizzbuzz(8) == 8
assert fizzbuzz(9) == 'Fizz'
assert fizzbuzz(10) == 'Buzz'
assert fizzbuzz(15) == 'FizzBuzz'
assert fizzbuzz(20) =='Buzz'
assert fizzbuzz(30) == 'FizzBuzz'
assert fizzbuzz(40) == 'Buzz'
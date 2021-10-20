'''
| Created on 20th October 2021
| Author : Aditya Hegde
| Github : xadityahx
'''
import timeit

setup = '''
import random
'''

fact = '''
def factor():
    a = random.choice(range(1000, 1000000))
    c = 0
    for i in range(1, a/2):
        if i % a == 0:
            c += 1
        else:
            pass
'''

time = timeit.timeit(setup=setup, stmt=fact, number=100000)

print('--- ' + str(time) + ' seconds ---')

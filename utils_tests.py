from utils import *

tests=utils()

print("TEST 1:")
try:
    print(tests.reversed("abc"))
except:
    print("Input String Has Type Error!")

print("TEST 2:")
try:
    print(tests.reversed(123.75))
except:
    print("Input Float Has Type Error!")

print("TEST 3:")
try:
    print(tests.reversed(123))
except:
    print("Input Integer Has Type Error!")

print("TEST 4:")
try:
    print(tests.formatter("abc"))
except:
    print("Input String Has Type Error!")

print("TEST 5:")
try:
    print(tests.formatter(64.5))
except:
    print("Input Float Has Type Error!")

print("TEST 6:")
try:
    print(tests.formatter(64))
except:
    print("Input Integer Has Type Error!")
x =  [i for i in range(10000)]

# for j in x:
#     print(j**2)

import sys           # for checking memory allocation 
sys.getsizeof(x)

#output = 85176      # allocation size

x = range(10000)       #range function returns a generator example

# for i in x:
#     print(i ** 2)

sys.getsizeof(x)      

#48                  # allocation size



def gen_demo():

    yield "first statement"
    yield "second statement"
    yield "third statement"

gen = gen_demo()
# print(next(gen))
# print(next(gen))
# print(next(gen))\

        #or
for i in gen:
    print(i)



def square(num):
    for i in range(1 ,num + 1):
        yield i ** 2

gen = square(10)
print(next(gen))
print(next(gen))

#it will start from where it left off in above next() calls 2nd time so it will print from 3rd square
for i in gen:
    print(i)

import sys
sys.getsizeof(i)


# range function using generator

def mera_range(start,end):
    
    for i in range (start,end):
        yield i

gen = mera_range(3,9)

for i in gen:
    print(i)


# generator experssion

#list comperhension

L = [i ** 2 for i in range(1,20)]
L


gen = (i ** 2 for i in range(1,20))       # It's a generator experssion ,aslo annonymous function
gen              #now this is a generator object

for i in gen:
    print(i)




# The practical example demonstrates loading large image datasets, such as 4830 images, one-by-one for deep learning model training without
#  loading all images into memory simultaneously. s s

# Problem Being Solved
# Large datasets like VGG or CIFAR are too big for typical RAM limits such as 8GB, making it impossible to
#  load thousands of images at once into memory. s s These images must be processed sequentially for
#  model training. s

# Generator Solution
# A generator function named image_generator takes a folder path, iterates through all files in the 
# folder, opens each image one by one, converts it to a numpy array, yields the array, and then frees 
# the memory. s s

# Usage Pattern
# The generator is called with the dataset folder path to create a generator object. s Each next(gen)
#  call retrieves exactly one image array: the first call gets the first image, the second gets the
#  second image, and so on. s

# Key Benefit: This approach handles 4,000+ images or even 4 crore images using memory for only 
# one image at a time. Keras implements the same concept through

import os
import cv2

def 
import time
import math
#import matplotlib.pyplot as plt

elapsed_time = 0;

total_time = 1

def round_to_nearest(number, base=1):
	if number % base == 0:
		return number
	if base < 1:
		num_digits = str(base)[::-1].find('.')
		return round(base * number / base, num_digits)
	return base * round(number / base)

def print_sin_cos_art(total_length = int(10*3.14), amp_scale = 10, offset = 1, precision = 5):
        string_length_max = (1 + offset) * amp_scale

        #Set pi precision
        pi = math.pi
        pi = round(pi, 3)
        print(pi)
        pi = 3.14

        for i in range(total_length):
                amplitude_string = ""
                
                #First equation
                x1 = math.sin((i / precision) + pi * 1.5)
                #Dots length 1
                dots_length = int((x1 + offset) * amp_scale)
                for j in range(dots_length):
                        amplitude_string += "."
                #Spaces length 1
                spaces_length = string_length_max - len(amplitude_string)
                for k in range(spaces_length):
                        amplitude_string += " "
                        
                #Second equation
                x2 = math.cos((i / precision) + pi)
                #Spaces length 2
                spaces_length = int((x1 + offset) * amp_scale)
                for m in range(spaces_length):
                        amplitude_string += " "
                #Dots length 2
                #Multiplying string_length_max by 2 is important
                dots_length = string_length_max * 2 - len(amplitude_string)
                for n in range(dots_length):
                        amplitude_string += "."
                        
                print(amplitude_string + str(len(amplitude_string)))

        
print_sin_cos_art()

"""
#print(round_to_nearest(1374,25))
#print(time.time())
loading_string_length = 10
loaded_pct = 0
print("Loading...")
start_time = time.time()
while elapsed_time < total_time:
        string = ""
        for i in range(loading_string_length):
                string += "."
        string = string.replace(".", "|", int(elapsed_time * (loading_string_length/total_time)))
        string += " " + str(loaded_pct) + "%"
        print(string)
        #print(elapsed_time)
        loaded_pct = int(100 * elapsed_time / total_time)
        elapsed_time = time.time() - start_time

string = ""
for i in range(loading_string_length):
        string += "|"
print(string + " 100%")
print("Loaded!")
"""
"""
for i in range(10):
	string = ""
	for j in range(i):
		string += "|"
	elapsed_time = 10000*(time.time() - start_time)
	round_time = round_to_nearest(elapsed_time,.01)
	print(string + str(round_time))

def fibonacci(n=10):
	lst = [0,1]
	for i in range(n-2):
		lst.append(lst[i]+lst[i+1])
	return lst
"""
#print(fibonacci())

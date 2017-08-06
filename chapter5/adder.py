#adder.py

result = 0

def adder(num):
	global result
	result += num
	return result

print(adder(4))
print(adder(3))
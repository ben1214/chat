import random

numbers = []
while len(numbers)<6:
	b = random.randint(1,49)
	if b not in numbers:
		numbers.append(b)
print(numbers)

lis = eval(input('輸入6個號碼,用逗點隔開: '))
for number in numbers:
	for li in lis:
		if number == li:
			print(number)


#intersection = [x for x in a for y in lis if x == y]
#print(intersection)










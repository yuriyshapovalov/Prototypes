# ProjectEuler.net/problem=1

def MultipleOfThreeAndFive():
	count = 0
	for i in range(1, 1000):
		if i % 3 == 0 or i % 5 == 0:
			count = count + i
	
	print(count)

if __name__ == '__main__':
	MultipleOfThreeAndFive()

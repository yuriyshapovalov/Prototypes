# projecteuler.net/problem=30

def main():
	answer = DigFifthPowers()
	print(answer)

def DigFifthPowers():
	sm = 0
	for i in range(2, 1000000):
		s = str(i)
		#print(s) #1
		tsum = 0
		for j in range(0, len(s)):
			#print(pow(int(s[j]), 4)) #2,3
			tsum += pow(int(s[j]), 5)
		#print(tsum) # 4

		if tsum == i:
			print(i)
			sm += i
	return sm

if __name__ == '__main__':
	main()

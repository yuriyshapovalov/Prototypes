# projecteuler.net/problem=1
from lib.profilehooks import timecall

# @title: Multiples of 3 and 5
# @description: If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

class Problem1:
	def answer(self):
		result = self.MultipleOfThreeAndFive()
		print("Answer: {}".format(result))

	@timecall
	def MultipleOfThreeAndFive(self):
		count = 0
		for i in range(1, 1000):
			if i % 3 == 0 or i % 5 == 0:
				count = count + i
	
		return count

if __name__ == '__main__':
	Problem1().answer()

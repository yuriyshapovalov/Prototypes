
def main():
	d = lambda x: x*x-x*2
	xax = [x for x in range(100)]
	yax = list(map(d, xax))

	plot(xax, yax)

if __name__ == '__main__':
	main()
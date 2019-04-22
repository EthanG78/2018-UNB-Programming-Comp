import sys

def main():
	f = open(sys.argv[1], "r")

	smallestNum = 20.0
	z = 0

	for num, x in enumerate(f):
		line = float(x)
		if line < smallestNum:
			smallestNum = line
			z = (num + 1) * 10 + 10


	print(z)

	f.close()

if __name__ == '__main__':
	main()
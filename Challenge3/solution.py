from math import ceil
import sys

def tubs(scoops):
	return (((scoops * 1.05) * 31) / 96)

def main():
	f = open(sys.argv[1], "r")

	vanilla_scoops, chocolate_scoops, cookie_dough_scoops = 0,0,0

	for num, x in enumerate(f):
		value = int(x)
		if num == 0:
			vanilla_scoops += value
		elif num == 6:
			vanilla_scoops += value
			chocolate_scoops += value
		elif num == 7:
			vanilla_scoops += value
			cookie_dough_scoops += value
		elif num == 1:
			vanilla_scoops += (2*value)
		elif num == 2 or num == 6:
			chocolate_scoops += value
		elif num == 3:
			chocolate_scoops += (2*value)
		elif num == 4 or num == 7:
			cookie_dough_scoops += value
		elif num == 5:
			cookie_dough_scoops += (2*value)


	vanilla = tubs(vanilla_scoops)
	chocolate = tubs(chocolate_scoops)
	cookie_dough = tubs(cookie_dough_scoops)

	print(ceil(vanilla))
	print(ceil(chocolate))
	print(ceil(cookie_dough))

	# print(vanilla_scoops)
	# print(chocolate_scoops)
	# print(cookie_dough_scoops)

	f.close()

if __name__ == '__main__':
	main()
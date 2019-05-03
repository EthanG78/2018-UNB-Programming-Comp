import sys

def weight_division(x):
	weight = float(x)
	weight /= 2.2
	if weight <= 52:
		return("FLY WEIGHT")
	elif weight <= 60 and weight > 52:
		return("LIGHT WEIGHT")
	elif weight <= 75 and weight > 60:
		return("MIDDLE WEIGHT")
	elif weight <= 91 and weight > 75:
		return("HEAVY WEIGHT")
	elif weight > 91:
		return("SUPER HEAVYWEIGHT")

def main():
	f = sys.stdin.read().splitlines()
	for x in f:
		print(weight_division(x))

if __name__ == "__main__":
	main()

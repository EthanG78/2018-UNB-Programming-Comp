import sys

def gRate(strList):
	list = [ float(x) for x in strList ]
	gRate1 = (list[1] - list[0]) / list[0]
	gRate2 = (list[2] - list[1]) / list[1]
	gRate3 = (list[3] - list[2]) / list[2]
	gRate4 = (list[4] - list[3]) / list[3]

	gRateAvg = (gRate1 + gRate2 + gRate3 + gRate4) / 4.0

	return gRateAvg

def main():
	f = open(sys.argv[1], "r")

	nFish = int(f.readline())

	for x in range(nFish):
		adult = f.readline().split(" ")
		child = f.readline().split(" ")

		if gRate(adult) > 0.05:
			adultHealth = "healthy"
		elif gRate(adult) < -0.05:
			adultHealth = "danger"
		else:
			adultHealth = "stable"

		if gRate(child) > 0.05:
			childHealth = "promising"
		elif gRate(child) < -0.05:
			childHealth = "concerning"
		else:
			childHealth = "stable"

		print("%s %s" % (adultHealth, childHealth))

	f.close()

if __name__ == '__main__':
	main()
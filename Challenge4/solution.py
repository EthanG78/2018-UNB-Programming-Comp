import sys

def main():
	input = sys.stdin.read()

	#words repeated more than twice throughout the input
	words = 0

	#input.split(".") returns a list of the input split at the periods.  
	#access the first index of this list for the first sentence.
	firstSentence = input.split(".")[0] 
	#print(firstSentence)

	#create a list of each word in the first sentence
	firstSentenceWords = firstSentence.split(" ")
	#print(firstSentenceWords)

	for word in firstSentenceWords:
		if len(word) >= 4:
			isRepeated = input.count(word)
			if isRepeated >= 3: #set to three to account for first sentence
				words += 1 #if the word is repeated more than 2 times, increment

	print(str(words) + " out of 7")


if __name__ == '__main__':
	main()
# Challenge Four: Perfect Paragraph Structure 
---

When writing a text in plain English, a good paragraph structure is to have the first sentence somewhat summarizing the idea in the paragraph, and then the rest of the paragraph just adds the details to the main point in the first sentence. Fancy text editors or word processors could evaluate how well this rule is followed by simply counting how many words (of at lease 4 character - to avoid words such as "the", "an", etc) of the first sentence are repeated at lease 2 more times in the rest of the paragraph (not including the first sentence). For simplicity, we check only for words re-spelled exactly in the same way (including uppercase/lowercase characters).</br>

The input is a single paragraph to be evaluated. Your program should identify all long-enough words (i.e., at least 4 characters long) in the first sentence, and count how often each of those appear in the rest of the paragraph. For the example input below, there would be 7 such words ("This", "programming", "competition", "students", "from", "high", AND "school"). The counts of each of these words are (respectively): 0 ("this" is not considered the same as "This"), 3, 2, 1, 0, 0, and 0. The output should indicate how many of those words are repeated at least twice, out of how many long-enough words we have. So the output here would be "2 out of 7" (you should use this wording exactly).</br>

Notes on the input:</br>
- The whole paragraph is on a single line of text, for simplicity. In the example below, the text has been "wrapped" in order for you to be able to read it all on this page, bot that is not how it is stored in the input file used for testing. </br>
- The paragraph (or line of text) does not contain more than 500 characters.</br>
- The long words in the first sentence are never repeated within that first sentence.</br>
- The first sentence always terminated with a period (".", no other characters such as "?" or "!"), and does not have other punctuation marks(i.i., all words are simply separated by a single space).</br>

EXAMPLE INPUT:</br>
This programming competition is for students from high schools. Do you like competition? DO you like programming? Of you like both and you are a student in New Brunswick, this competition is for you. You will meet many other students with the same passion for programming as yours, and hopefully you will make new friends! Let's have fun programming!</br>

EXMAPLE OUTPUT:</br>
2 out of 7</br>
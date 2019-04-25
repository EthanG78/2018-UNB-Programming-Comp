# Challenge Five: Sustainable Fishing
---

Determining fishing quotas for each species depends on how healthy the fish population is. More precisely, we look at whether the population is growing or shrinking in general, over a number of years. We also look at the population of young fish as an indication of future overall population. Indeed, if the overall population has been stable or slightly decreasing, but that the young population is growing, then we would be less worried about the population of that species in the next few years. So your goal here is to identify how healthy the population is (overall and young one) for various species, so as to help with quotas determination.</br>

The firs line of input contains the number of species to be analyzed. Then for each of them, there are 2 lines: one for the overall (adult) population and one for the young population. Each line contains the estimated population in a given fishing are for the past 5 years (as 5 positive integers separated by a space). Your program should identify how healthy the populations are based on the average growth rate. The growth rate between two consecutive years is the difference between the two (second number minus first number) divided by the first number. For example, the growth rate for the two first years in the first line of such data in the example input below (i.e., 300 and 350) is (350 - 300) / 300, You need to calculate such rate for each of the 4 pairs of consecutive number within the line, and then take the average of those rates.</br>

Such calculations has to be done for each line of estimated populations. For the data below (example input), the average rates are: 0.0145, -0.061, -0.080, and 0.392. Then, for each species, we have one line of output with 2 words, separated by one space. The first word is related to the average rate of the overall population:</br>

"healthy": rate is > 5%</br>
"danger": rate is < -5%</br>
"stable": otherwise</br>

The second word is related to the young population:</br>

"promising": rate is > 5%</br>
"concerning": rate is < -5%</br>
"stable": otherwise</br>

So for the first specie in the example input below, we get "stable" (0.0145 is between -0.05 and 0.05) and "concerning"(-0.061 is smaller than -0.05), while the ssecond specie is in "danger" (-0.080 is smaller than -0.05) but "promising" (0.392 is larger than 0.05).</br>

EXAMPLE INPUT:</br>
2</br>
300 350 305 290 310</br>
100 80 85 70 75</br>
500 400 425 375 350</br>
50 60 100 150 180</br>

EXAMPLE OUTPUT:</br>
stable concerning</br>
danger promising</br>
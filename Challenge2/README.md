# Challenge Two: Best Fuel Consumption
---
Fuel consumption for cars depends on the speed the car is going. There is actually a typical pattern: fuel consumption is typically high at very low speeds, and then decreases gradually up o some optimum speed, and then increases again gradually as speed increases past this optimal point. Your goal for this problem is to identify such optimal speed, and print it.</br>

The example input below contains data collected about a group of similar cars over a period of a few years. Each of the numbers is the average consumption (in L/100km) for different speeds: the first line is for 20 km/h, the second line is of 30 km/h, the third line is for 40 km/h, and so on until the last line which is for 120 k/h. As one can see, the numbers are going down until the fifth row, and then they go up again. Since the fifth row corresponds to the average fuel consumption at 60 km/h, the output is 60.</br>

Note: Consumptions numbers are all between 1.0 and 20.0. You are guaranteed to have the patter described above (i.e., data going down and then up), and no two consecutive numbers are the same (i.i., the solution cannot be more than one speed).</br>

EXAMPLE INPUT:</br>
10.5</br>
9.0</br>
8.0</br>
7.5</br>
7.0</br>
7.4</br>
7.7</br>
8.0</br>
8.6</br>
9.3</br>
10.0</br>

EXAMPLE OUTPUT:</br>
60</br>

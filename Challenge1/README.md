# Challenge One: Weight divisions in boxing
---
In boxing, the two players who are fighting must be of similar weight in order for the fight to be fair. More precisely, the players are placed into categories based on their weight (called "weight division"), and they can only fight opponents of the same category. Here are teh weight divisions used for men in the last Olympic Games:</br> 

| Name of weight division | Weight thresholds |
|-------------------------|-------------------|
| FLY WEIGHT              | up to 52kg        |
| LIGHT WEIGHT            | up to 60kg        |
| MIDDLE WEIGHT           | up to 75kg        |
| HEAVY WEIGHT            | up to 91kg        |
| SUPER HEAVYWEIGHT       | more than 91kg    |

Note: there were actually 10 wegith divisions, but we reduced it to 5 for simplicity.</br>

Your goal here is to identify the weight divisions corresponding to the weights given in input. More precisely, the input contains 3 integers (one per line) corresponding to the weights of 3 boxers. These weights are in pounds though (between 100 and 250), so first you need to convert them into kg (1kg = 2.2 pounds). For the example input below, here are the corresponding weights in kg:</br>

220 lbs -> 100.0 kg</br>
140 lbs -> 63.6 kg</br>
185 lbs -> 84.1 kg</br>

The ouput should be the weight division for each of these boxers, one per line, in the same order as they appear in the input.</br>

EXAMPLE INPUT:</br>
220</br>
140</br>
185</br>

EXAMPLE OUTPUT:</br>
SUPER HEAVYWEIGHT</br>
MIDDLE WEIGHT</br>
HEAVY WEIGHT</br>

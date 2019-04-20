# Challenge Three: Ice Cream Ordering 
---
You decide that for your summer job, you will create a small business and sell ice cream cones. You need to order enough ice cream to cover for the whole month of July, based on some daily estimates. For simplicity here, we will have only 3 flavors: vanilla, chocolate, and cookie dough. The cones can be of 1 scoop or 2 scoops. The 2 scoops ones can be of a single flavor only, or be a mix: vanilla-chocolate or vanilla-cookie-dough. In the input (see the example input below), you get the estimate of the number of cones to be sold per day of each type, in the following order:</br>

- 1-scoop vanilla cones</br>
- 2-scoops vanilla cones</br>
- 1-scoop chocolate cones</br>
- 2-scoops chocolate cones</br>
- 1-scoop cookie-dough cones</br>
- 2-scoops cookie-dough cones</br>
- vanilla-chocolate cones</br>
- vanilla-cookie-dough cones</br>

Using such estimates, you want to know how many tubs of ice cream of each flavor (vanilla chocolate, and cookie-dough - in this order) you need to order for the whole month of July. FOr your information, there are approximately 96 scoops of ice cream in a "3-gallon" tub (approx. 11.3 liters). And just to be on the safe side, you decide to order for 5% more scoops than needed, just in case sales are higher than predicted.</br>

Here is an example of the calculations for the vanilla ice cream, based on the estimates provided in the example input below:</br>

``` 
Number of scoops needed per day: 5 + (2 x 15) + 22 + 12 = 69 scoops.
5% of 69 is 3.45, so you need to cover for 72.45 scoops per day (just to be safe).
For the 31 days of July, this is 2245.95 scoops (72.45 x 31),
thus we need 24 tubs of vanilla ice cream (2245.95 / 96 = 23.4).

```

In a similar way, we can calculate the number of tubs needed of the chocolate flavor and the cookie-dough flavor, and we get 28 and 19 respectively. These 3 numbers make up the output below.</br>

EXAMPLE INPUT:</br>
5</br>
15</br>
8</br>
25</br>
3</br>
20</br>
22</br>
12</br>

EXAMPLE OUTPUT:</br>
24</br>
28</br>
19</br>

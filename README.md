# lotto
The library allows you to create games similar to the popular lottery game in Poland. It allows you to create single draws, a specific number of draws and draws until the "6" is hit. Of course, provided that we set 6 random numbers, because you can actually enter numbers from 1 to ..

# how to use
## 1. firstly import class lotto
```python
from lotto import Lotto 
```
## 2. Next create your Lotto class object, e.g. 
```python
my_lotto = Lotto()
```
---
This creates an object with default parameters. You can also define your own parameters when creating an object:
Keyword Arguments:
1. number_of_numbers_drawn {int} -- _description_ (default: {6})
2. min_number {int} -- _description_ (default: {1})
3. max_number {int} -- _description_ (default: {49})
## 3. From now on, you can:
### 1. make a single draw
```python
one_draw_numbers = my_lotto.draw()
```
### 2. perform a certain number of draws

Args:
- wanted_numbers (set): the numbers you bet on in the draw
- number_of_draws (int): number of draws. Defaults to 6.

Returns:
- bool: Returns True if the set of numbers is drawn up and False if not.

e.g.
```python
my_numbers = {5, 8, 14, 21, 34, 45}

check_i_win = my_lotto.draw_for(
    wanted_numbers=my_numbers,
    number_of_draws=100
)
```
### 3. run the draw until your numbers are drawn
Args:
- wanted_numbers (set): Yours numbers

Returns:
- int: Number of draw attempts

e.g.
```python
draws_to_win = my_lotto.draw_until_win(
    wanted_numbers=my_numbers
)
```
### 4. You can also check the game statistics
how many times the numbers has been drawn, e.g.
```python
draw_statistics = my_lotto.statistics
print(draw_statistics)

{'14': 128161, '12': 127751, '29': 127874, '45': 127060, '11': 127017, '26': 127693, '9': 127443, '44': 127505, '15': 127189, '22': 127294, '17': 127244, '38': 128207, '35': 126985, '31': 128013, '34': 127208, '42': 126660, '6': 127428, '16': 127307, '25': 127652, '20': 127461, '49': 127040, '41': 127637, '32': 127659, '4': 127585, '40': 126532, '10': 127068, '48': 127732, '1': 127638, '43': 127798, '21': 127334, '36': 126840, '27': 127387, '23': 126868, '5': 127195, '39': 127517, '47': 127014, '37': 126912, '8': 126783, '46': 127667, '3': 126906, '19': 126883, '24': 126782, '30': 126640, '28': 127777, '2': 127250, '13': 127615, '18': 127486, '33': 127598, '7': 127651}
```
'drawn number': how many times it has been drawn

how many times the sets of numbers has been drawn, e.g.
```python
hits_statistics = dict(sorted(my_lotto.hits.items()))
print(hits_statistics)

{'0': 4188568, '1': 3965694, '2': 1272111, '3': 169556, '4': 9215, '5': 183, '6': 1}
```

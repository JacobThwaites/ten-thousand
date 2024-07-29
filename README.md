# Ten Thousand
An automation of the dice game [Ten Thousand](https://en.wikipedia.org/wiki/Dice_10000) for statistical analysis of different strategies.

## Running Locally 

```bash
$ python3 main.py
```

## Testing

To run tests locally:

```bash
$ python3 run_tests.py 
```


## Basic Strategy

If only 1 combination then choose that
If a combination uses all dice then choose that.\
Otherwise: \
    Find the next combination by the highest percentage of score/number of dice ratio.\
    If that would leave fewer than 4 dice choose the max.\
    Otherwise take highest score/num_dice ratio.

# Ten Thousand


## Running Locally 

```bash
$ python3 main.py
```

## Testing

To run tests locally:

```bash
$ python3 run_tests.py 
```


### Choosing which dice to take

If only 1 combination:
    Take that
If a combination uses all dice:
    Take that
Else:
    Find next by percentage of score to num_dice used
    If that leaves fewer than 4 dice:
        Take max
    else:
        Take that


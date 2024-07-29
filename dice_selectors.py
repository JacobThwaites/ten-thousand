def basic_selection(combinations, dice_rolled, max_dice_to_leave=3):
    if len(combinations) == 1:
        return combinations[-1]
    
    highest = combinations[-1]
    
    if highest[1] == dice_rolled:
        return highest

    best_dice_score_ratio = best_by_dice_score_ratio(combinations)
    
    if dice_rolled - best_dice_score_ratio[1] < max_dice_to_leave:
        return combinations[-1]
    
    return best_dice_score_ratio


def best_by_dice_score_ratio(combinations):
    best_ratio = 0
    best_combination = None
    
    for (score, dice) in combinations:
        ratio = score / dice
        if ratio > best_ratio:
            best_ratio = ratio
            best_combination = (score, dice)
            
    return best_combination
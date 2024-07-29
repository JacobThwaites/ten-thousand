import random
from collections import Counter
from itertools import combinations
from dice_selectors import basic_selection

class TenThousand:
    def __init__(self):
        self.is_first_players_turn = True 
        self.dice_remaining = 7
        self.current_score = 0
        self.player_1_score = 0
        self.player_2_score = 0
    
    def run_game(self):
        while self.player_1_score < 10_000 and self.player_2_score < 10_000:
            self.turn()
            
        return 1 if self.player_1_score > self.player_2_score else 2
        
    def turn(self):
        while True:
            dice = [random.randint(1, 6) for _ in range(self.dice_remaining)]
            valid_combinations = self.valid_combinations(dice)
            
            if not len(valid_combinations):
                self.setup_next_turn()
                break 
            
            combination = self.select_combination(valid_combinations)
            self.add_dice(combination)
            
            if self.should_stick():
                self.setup_next_turn()
                break
        
    def valid_combinations(self, roll):
        def calculate_score(dice):
            counts = Counter(dice)
            score = 0
            dice_used = 0

            # Check for triples and higher multiples
            for num in range(1, 7):
                if counts[num] >= 3:
                    dice_used += 3
                    if num == 1:
                        score += 1000 * (2 ** (counts[num] - 3))
                    else:
                        score += 100 * num * (2 ** (counts[num] - 3))
                    counts[num] -= 3

            # Add scores for remaining 1s and 5s
            dice_used += counts[1] + counts[5]
            score += counts[1] * 100
            score += counts[5] * 50

            return score, dice_used

        valid_combos = set()

        # Generate all non-empty subsets of the roll
        for num_dice in range(1, len(roll) + 1):
            for subset in combinations(roll, num_dice):
                score, dice_used = calculate_score(subset)
                if score > 0:
                    valid_combos.add((score, dice_used))

        return sorted(valid_combos, key=lambda x: (x[1], x[0]))

    def select_combination(self, combinations):
        return basic_selection(combinations, self.dice_remaining)
    
    def add_dice(self, combination):
        self.dice_remaining -= combination[1]
        self.current_score += combination[0]
        
    def should_stick(self):
        return self.dice_remaining < 4
        
    def setup_next_turn(self):
        self.dice_remaining = 7
        if self.is_first_players_turn:
            self.player_1_score += self.current_score
        else: 
            self.player_2_score += self.current_score
            
        self.is_first_players_turn = not self.is_first_players_turn
        self.current_score = 0
    
    def reset_game(self):
        self.is_first_players_turn = True
        self.dice_remaining = 7
        self.current_score = 0
        self.player_1_score = 0
        self.player_2_score = 0
        
from ten_thousand import TenThousand

def main():
    game = TenThousand()
    player_1_wins = 0
    player_2_wins = 0
    
    for _ in range(100):
        game.reset_game()
        winner = game.run_game()
        if winner == 1:
            player_1_wins += 1
        else: 
            player_2_wins += 1

    print(f'Player 1: {player_1_wins}')
    print(f'Player 2: {player_2_wins}')
    
    

if __name__ == '__main__':
    main()

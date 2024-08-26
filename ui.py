def manage_scoreboard(rounds: list[tuple[int, int]]) -> dict:
    scoreboard = {}
    for player, score in rounds:
        if player in scoreboard:
            scoreboard[player] += score
        else:
            scoreboard[player] = score
    
    for player in sorted(scoreboard.keys()):
        print(f"Player {player}: {scoreboard[player]}")

    return scoreboard

rounds1 = [(1, 10), (2, 15), (3, -5), (1, 20), (2, -10)]
manage_scoreboard(rounds1)

rounds2 = [(1, 5), (2, 10), (1, 15)]
manage_scoreboard(rounds2)
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def render_grid(grid):
    rows = len(grid[0])
    cols = len(grid)

    for i in range(cols):
        for j in range(1, rows + 1):
            if j % 3 != 0:
                print(grid[i][j-1], end="  |  ")
            else:
                print(grid[i][2])
        
        if i != 2:
            print("---------------")

def check_win(player, grid):
    def check_player_win(i):
        if i == player:
            return True

    # horizontal
    vertical1 = []
    vertical2 = []
    vertical3 = []

    for i in grid:
        if all(list(map(check_player_win, i))):
            return True

        vertical1.append(i[0] == player)
        vertical2.append(i[1] == player)
        vertical3.append(i[2] == player)
    
    # vertical
    for i in range(3):
        if vertical1[i] and vertical2[i] and\
            vertical3[i]:
            return True

    # diagonally
    if vertical1[0] and vertical2[1] and\
        vertical3[2]:
        return True
    
    elif vertical1[2] and vertical2[1] and\
        vertical3[0]:
        return True

    return False

def add_pos(player, pos):
    try:
        pos = int(pos)
        if 1 <= pos <= 9:
            row = (pos - 1) // 3
            col = (pos - 1) % 3
            if grid[row][col] == " ":
                grid[row][col] = player
                return True
    except ValueError:
        pass

    return False

def main():
    curr = "X"

    while True:
        position = input(
            f"Enter The Position you Want to Put {curr} (1-9): "
        )
        while not add_pos(curr, position):
            position = input(
                f"Please Enter A Valid Postion: "
            )

        render_grid(grid)

        if check_win(curr, grid):
            print(f"{curr} Win 🥳!")
            break

        if curr == "X":
            curr = "O"
        else:
            curr = "X"
        


main()
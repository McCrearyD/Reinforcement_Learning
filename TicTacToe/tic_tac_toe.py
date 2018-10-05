import numpy as np


class Environment:
    def __init__(self, size=3):
        # Generate board in a matrix
        self.tiles = [[None]*size for _ in range(size)]
        self.winner = None
        self.size = size

    def draw(self):
        for row in self.tiles:
            temp = ""
            for tile in row:
                temp += "- " if tile == None else tile + " "
            print(temp)

    def update_and_get_winner(self, x, y, char):
        # If already won, ignore all inputs and return winner.
        if not self.winner == None:
            return self.winner

        self.tiles[y][x] = char

        # Horizontal win
        if self.tiles[y].count(char) == len(self.tiles[y]):
            self.winner = char
            return True

        # Vertical win
        vert = [row[x] for row in self.tiles]
        if vert.count(char) == len(vert):
            self.winner = char
            return True

        # Slant win
        winP = True
        winN = True
        for i in xrange(self.size):
            if winN:
                if self.tiles[self.size-i-1][self.size-i-1] is not char:
                    winN = False
            if winP:
                if self.tiles[self.size-i-1][i] is not char:
                    winP = False

        self.winner = char if winN or winP else None

        # Check for draw
        if self.winner is None:
            draw = True
            for row in self.tiles:
                for tile in row:
                    if tile is None:
                        draw = False
                        break
            self.winner = "draw" if draw else self.winner

        return self.winner


env = Environment()
env.update_and_get_winner(0, 0, "X")
env.update_and_get_winner(1, 1, "O")
env.update_and_get_winner(2, 2, "O")
env.update_and_get_winner(0, 1, "X")
env.update_and_get_winner(1, 2, "j")
env.update_and_get_winner(2, 0, "O")
env.update_and_get_winner(0, 2, "f")
env.update_and_get_winner(1, 0, "g")
env.update_and_get_winner(2, 1, "X")
env.draw()
print(env.winner)
# env.draw()

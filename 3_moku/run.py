import random


class board(object):
    def __init__(self):
        self.b = [0 for i in range(9)]
        self.next_color = 1
        self.space = 9

    def is_win(self, color):
        for i in range(0, 9, 3):
            if self.b[0+i] == self.b[1+i] == self.b[2+i] == color:
                return True
        for i in range(0, 3):
            if self.b[0+i] == self.b[3+i] == self.b[6+i] == color:
                return True
        for i in range(0, 9, 4):
            if self.b[i] == self.b[i] == self.b[i] == color:
                return True
        for i in range(2, 7, 2):
            if self.b[i] == self.b[i] == self.b[i] == color:
                return True
        return False

    def put_stone(self):
        rnd = random.randrange(self.space)
        for i in range(9):
            if self.b[i] == 0:
                rnd -= 1
                if rnd == 0:
                    self.b[i] = self.next_color
                    self.next_color = 3 - self.next_color
                    return

    def run_game(self):
        for _ in range(9):
            self.put_stone()
            if self.is_win(1):
                return 1
            if self.is_win(2):
                return 2
        return 0


if __name__ == '__main__':
    result = [0 for _ in range(3)]
    for i in range(10000):
        b = board()
        res = b.run_game()
        result[res] += 1
    print(result)

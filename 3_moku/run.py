import random


class board(object):
    def __init__(self):
        self.b = [0 for i in range(9)]
        self.next_color = 1
        self.space = 9

    def __repr__(self):
        res = ""
        for i in range(0, 9, 3):
            s = "{} {} {}\n".format(self.b[0+i], self.b[1+i], self.b[2+i])
            res += s
        return res

    def is_win(self, color):
        for i in range(0, 9, 3):
            if self.b[0+i] == self.b[1+i] == self.b[2+i] == color:
                return True
        for i in range(0, 3):
            if self.b[0+i] == self.b[3+i] == self.b[6+i] == color:
                return True
        if self.b[0] == self.b[4] == self.b[8] == color:
            return True
        if self.b[2] == self.b[4] == self.b[6] == color:
            return True
        return False

    def put_stone(self):
        rnd = random.randrange(0, self.space)
        for i in range(9):
            if self.b[i] == 0:
                if rnd == 0:
                    self.b[i] = self.next_color
                    self.next_color = 3 - self.next_color
                    self.space -= 1
                    return
                rnd -= 1

        print("error cannot put")
        exit(1)

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

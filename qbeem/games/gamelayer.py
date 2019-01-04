class Layer(object):

    def __init__(self, field_arr, x1, x2, x3, y1, y2, y3):
        self.field = field_arr
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def is_player_won(self):
        return 1 == self.field[self.x1][self.y1] and 1 == self.field[self.x2][self.y2] and 1 == self.field[self.x3][
            self.y3]

    def is_possible_won(self):
        return (1 == self.field[self.x1][self.y1] and 1 == self.field[self.x2][self.y2] and 0 == self.field[self.x3][
            self.y3]) or (1 == self.field[self.x1][self.y1] and 0 == self.field[self.x2][self.y2] and 1 ==
                          self.field[self.x3][self.y3]) or (
                           0 == self.field[self.x1][self.y1] and 1 == self.field[self.x2][self.y2] and 1 ==
                           self.field[self.x3][self.y3])

    def is_player_loose(self):
        return -1 == self.field[self.x1][self.y1] and -1 == self.field[self.x2][self.y2] and -1 == self.field[self.x3][
            self.y3]

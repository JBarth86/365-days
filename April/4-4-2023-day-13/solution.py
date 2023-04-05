class User:

    def __init__(self, rank=-8, progress=0):

        self.rank = rank
        self.progress = progress

    def inc_progress(self, level):
        valid_levels = [-8, -7,  -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

        if level not in valid_levels:
            raise Exception("invalid input")

        # the following two if/elif statements
        # account for the absences of a 'level 0'
        if (self.rank < 0 < level):
            level -= 1

        elif (self.rank > 0 > level):
            level += 1

        # there is no progress to be made if self.rank == 8 or
        # if the challenge more than two levels below self.rank
        if (level < self.rank - 1 or self.rank == 8):
            return

        diff = level - self.rank

        if (diff == -1):
            points = 1

        elif (diff == 0):
            points = 3

        else:
            points = diff * diff * 10

        self.progress += points

        while (self.progress >= 100 and self.rank < 8):

            self.progress -= 100
            self.rank += 1

            # we have to add an extra rank moving from -1 to 1 to account for no level 0
            if (self.rank == 0):
                self.rank += 1
            # if we're already at level 8 there is no more progress to be had   
            if (self.rank == 8):
                self.progress = 0

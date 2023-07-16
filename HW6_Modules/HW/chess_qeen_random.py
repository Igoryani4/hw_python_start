import random
import chess as ch


def successful_position(count_successful):
    position = []
    n = 8
    count = 1
    count_iter = 0
    while count <= count_successful:
        count_iter += 1
        i = 0
        while i < n:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
            if [x, y] not in position:
                position.append([x, y])
                i += 1

        if ch.chess(position):
            print(position, 'iter = ', count_iter)
            count += 1
        position.clear()
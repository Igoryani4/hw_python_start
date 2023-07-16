

def chess(position: list[list[int]]) -> bool:
    n = len(position)
    x = []
    y = []
    for i in range(n):
        new_x , new_y = position[i][0] , position[i][1]
        x.append(new_x)
        y.append(new_y)

    correct = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False

    if correct:
        return False
    else:
        return True
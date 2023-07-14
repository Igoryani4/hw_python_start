

def chess(txt):
    n = txt.split()
    x = []
    y = []
    
    for i in range(0, len (n) , 2):
        new_x , new_y = int(n[i]) , int (n[i + 1])
        x.append(new_x)
        y.append(new_y)

    correct = True
    for i in range(len (x)):
        for j in range(i + 1, len (x)):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False

    if correct:
        return False
    else:
        return True
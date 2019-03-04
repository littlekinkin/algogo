import numpy as np

def queen1():
    #init
    choice = range(8)
    re = [[x] for x in range(8)]
    for tmp in re:
        for now in choice:
            if now in tmp:
                continue
            #new = tmp + [now]
            #if is_ok(new):
            if is_tmp_ok(tmp, now):
                #print('ok', new)
                re.append(tmp + [now])
    for x in re:
        if len(x) == len(choice):
            print(x)

def is_ok(arr):
    for i, v1 in enumerate(arr):
        for j in range(i + 1, len(arr)):
            v2 = arr[j]
            if abs(v2 - v1) == abs(j - i):
                return False
    return True

def is_tmp_ok(arr, value):
    j = len(arr)
    for i, v1 in enumerate(arr):
        if abs(i-j) == abs(value-v1):
            return False
    return True



##queen2

def queen2():
    pass



queen1()


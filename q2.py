
def f(i):
    rtn = []
    for i in range(1,i+1):
        isDby3 = i % 3 == 0 
        isDby5 = i % 5 == 0 
        if isDby3 and isDby5:
            rtn.append(i)
        elif isDby3:
            pass
        elif  isDby5:
            pass
        else:
            rtn.append(i)
    return len(rtn)

if __name__ == '__main__':
    print("results of f(15):", f(15))
    print("results of f(3):", f(3))
    print("results of f(1):", f(1))
    print("results of f(0):", f(0))
    
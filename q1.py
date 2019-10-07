def f(s):
    s = s.split(" ")
    rtn = []
    for item in s:
        item = item[::-1]
        rtn.append(item)
    
    return " ".join(rtn)

if __name__ == '__main__':
    print('results of f(“flipped class room is important”):', f("flipped class room is important"))
    
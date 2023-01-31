from collecting import Point

if __name__ == '__main__':
    p = Point()
    p.run(True)
    for x in p.collections:
        print(x.get(2))

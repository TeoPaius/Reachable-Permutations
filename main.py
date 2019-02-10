def run():
    pass


def reachableSet(d, l, start):
    pass

def intersect(set1, set2):
    pass


def isReachable(d, l, start, end):
    s1 = reachableSet(d, l/2, start)
    s2 = reachableSet(d, l/2, end)
    if len(intersect(s1, s2)) == 0:
        return False
    return True

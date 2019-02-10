def run():
    ways = []

    for i in reachableSet(1,2, (1,2,3,4)):
        print(i)

def combinations(n, k, res):
    if len(res) == k:
        yield res
    else:
        if len(res) == 0:
            last = -1
        else:
            last = res[-1]
        for i in range(last+1, n):
            res.append(i)
            for i in combinations(n, k, res):
                yield i
            res.pop(-1)



def generateSwitches(n, d):
    res = []
    for i in range(0, n):
        for j in range(i + d, min(i + n - d+1, n)):
            res.append((i,j))
    return res


def reachableSet(d, l, start):
    switces = generateSwitches(len(start), d)
    ways = []
    for i in combinations(len(switces), l, []):
        ways.append(i.copy())
    res = set()
    for way in  ways:
        final = list(start)
        for switch in [switces[i] for i in way]:
            a = switch[0]
            b = switch[1]
            temp = final[a]
            final[a] = final[b]
            final[b] = temp
        res.add(tuple(final))
    return res

def intersect(set1, set2):
    return set1.interstection(set2)


def isReachable(d, l, start, end):
    s1 = reachableSet(d, l/2, start)
    s2 = reachableSet(d, l/2, end)
    if len(intersect(s1, s2)) == 0:
        return False
    return True


run()
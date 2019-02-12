def run():
    results = [[] for i in range(0,4)]

    for d in range(1, 5):
        print(d)
        for l in range(1,10):
            print(l)
            results[d-1].append(isReachable(d,l, (1,2,3,4,5,6,7,8,9), (9,8,7,6,5,4,3,2,1)))


    for i in results:
        print(i)


def combinations(n, k, res):
    if len(res) == k:
        # print(res)
        yield res
    else:
        if len(res) == 0:
            last = -1
        else:
            last = res[-1]
        for i in range(last+1, n):
            res.append(i)
            for j in combinations(n, k, res):
                # print(i)
                yield j
            res.pop(-1)



def generateSwitches(n, d):
    res = []
    for i in range(0, n):
        for j in range(i + d, min(i + n - d+1, n)):
            # print((i,j))
            res.append((i,j))
    return res


def reachableSet(d, l, start):
    switces = generateSwitches(len(start), d)
    ways = []
    for i in combinations(len(switces), l, []):
        # print(i)
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
    for i in set1:
        if i in set2:
            return True
    return False


def isReachable(d, l, start, end):
    s1 = reachableSet(d, int(l/2), start)
    s2 = reachableSet(d, int(l/2), end)
    if intersect(s1, s2):
        return True
    return False


run()
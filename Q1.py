import copy
import itertools

deletedItems = []

arr = [
    {'A', 'B', 'D', 'G'},
    {'B', 'D', 'E'},
    {'A', 'B', 'C', 'E', 'F'},
    {'B', 'D', 'E', 'G'},
    {'A', 'B', 'C', 'E', 'F'},
    {'B', 'E', 'G'},
    {'A', 'C', 'D', 'E'},
    {'B', 'E'},
    {'A', 'B', 'E', 'F'},
    {'A', 'C', 'D', 'E'},
]

alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def support(item: set):
    s = 0
    for i in arr:
        if item.issubset(i):
            s += 1
    return s


def oneItemSet(allTerms: list, threshold):
    oneItems = []

    for item in allTerms:
        if support(item) >= threshold:
            oneItems.append(item)

    return oneItems


def buildItemSet(allTerms: list, setK, threshold):
    deletedItems = []
    twoItemSet = []

    for t in setK:
        for item in allTerms:
            if item not in t:
                twoItem: set = copy.copy(t)
                twoItem.add(item)
                if support(twoItem) < threshold:
                    deletedItems.append(twoItem)
                    continue
                for dele in deletedItems:
                    if twoItem.issuperset(dele):
                        break
                else:
                    if twoItem not in twoItemSet:
                        twoItemSet.append(twoItem)

    return twoItemSet


def generateKItemset(index, threshold):
    temp = []

    for item in alph:
        temp.append({item})

    tem = temp

    if (index == 1):
        oneItems = oneItemSet(tem, threshold)
        print(oneItems, len(oneItems))
    else:

        for i in range(index - 1):
            temp = (buildItemSet(alph, temp, threshold))
        print(temp, len(temp))


def generateAllItemset(threshold):
    temp = []
    all = []

    for item in alph:
        temp.append({item})

    tem = temp

    oneItems = oneItemSet(tem, threshold)
    all.append(oneItems)
    # print(oneItems, len(oneItems))

    for i in range(0, 7):
        temp = (buildItemSet(alph, temp, threshold))
        all.append(temp)

    for each in all:
        for e in each:
            if len(e) != 1:
                generateAssociationRull(e)


def generateAssociationRull(fi):
    fi_list = list(fi)
    fi_list_permutation = itertools.permutations(fi_list)

    sepration = list()

    for f in fi_list_permutation:

        f11 = list(f)

        for i in range(1, len(fi)):
            temp = copy.copy(f11)
            temp.insert(i, 0)
            if (temp not in sepration):
                sepration.append(temp)

    calConfidence(sepration)


def calConfidence(rule):
    # print("rule:",rule)

    finalrules = []
    rules = [1, 0, 2]

    # for ind in rule:

    for index, value in enumerate(rule):

        for ind, r in enumerate(value):
            if r == 0:
                setX = set(value[0:ind])
                setY = set(value[ind + 1:len(value)])
                if ([setX, 0, setY] not in finalrules):
                        finalrules.append([setX, 0, setY])

    for i,f in enumerate(finalrules):
        x = list(f[0])
        y = list(f[len(f) - 1])

        z = set(x + y)
        xp = set(x)
        yp = set(y)

        conf = support(z) / support(xp)

        if xp == {'B'} and yp == {'E'}:
            print("==============")
            q = set(x + y)
            confPartE = support(q) / support(xp)
            print("Soale 1 bakhshe (e) : ",confPartE)
            print("==============")

        if conf == 1:
            print("Soale 1 bakhshe d:")
            print(finalrules[i])

print("A:")
generateKItemset(1, 4)
#
print("B:")
generateKItemset(2, 4)
#
print("C:")
generateKItemset(2, 7)

# print("All frequnet itemSet:")
generateAllItemset(4)

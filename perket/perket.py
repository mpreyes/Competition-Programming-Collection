
import sys
import itertools

def main():
    n = int(sys.stdin.readline())
    resultSum = 0
    sourProd = 1
    bitterSum = 0
    smallestDiff =  1000000000
    ingredients = []
    for i in range(n):
        line = sys.stdin.readline().split() #split line
        ingredients.append((int(line[0]),int(line[1])))
    # for i in ingredients:
    #     print(i)
    combos = []
    for i in range(n+1):
        combos.append(itertools.combinations(ingredients,i))
    del combos[0]
    for i in combos: #gets each line of combination
        for j in i:
            #print("j " + str(j))
            for k in j:
                #print("k at 0 " + str(k[0]))
                sourProd *= k[0]
                bitterSum += k[1]
            #print("sour " + str(sourProd) + " bitter "+ str(bitterSum))
            lineDiff = abs(sourProd - bitterSum)
            #print("lineDiff "+ str(lineDiff))
            if(lineDiff < smallestDiff):
                smallestDiff = lineDiff
            sourProd = 1
            bitterSum = 0
    print(smallestDiff)






main()

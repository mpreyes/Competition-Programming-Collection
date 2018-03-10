

import sys
from collections import deque




def main():
    lines = sys.stdin.readlines()
    #d['mynewkey'] = 'mynewvalue'
    commandsDict = {}
    # for k, v in commandsDict.items():
    #     print(k, v)

    for line in lines:
        #print(line)
        splitL = line.strip('\n').split(" ") #must strip newline apparently
        #print("splitL " + str(splitL[0]))


        if splitL[0] == "def":
            #print("calculated function")

            commandsDict.update({ splitL[1]: splitL[2]})

        elif splitL[0] == "calc":
            numOps = 0
            holdD = deque()

            result = "empty"
            splitL.remove("calc") #removing the calc and = signs
            splitL.pop()
            Avar = 0
            resultH = 0
            #print("listy"  + str(splitL))
            #print("result b4" + str(result))
            for i in splitL:
                #print("list i " + str(i))
                if i in commandsDict:
                    holdD.append(commandsDict[i])
                    #print("its in the dictionary")
                elif i == '+' or i == '-':
                    numOps+= 1
                    holdD.append(i)
                    #print("its an op")
                else:
                    #print("not in dictionary and not an op")
                    result = "unknown"

            #print("result " + result)
            #print("len " + str(len(holdD)))
            if result == "empty":
                #print("no unknown variables found. now to check sum")
                for i in range(numOps):
                    #print("num Operations " + str(i))
                    Avar = holdD.popleft()
                    var = holdD.popleft()
                    Bvar = holdD.popleft()
                    if var == '+':
                        resultH = int(Avar) + int(Bvar)
                        holdD.appendleft(resultH)
                    if var == '-':
                        resultH = int(Avar) - int(Bvar)
                        holdD.appendleft(resultH)
                newD = dict((v, k) for k, v in commandsDict.items())
                #for i in newD:
                    #print("newD " + str(i))
                    #print("holdD " + str(holdD[0]))
                numHold = str(holdD[0])
                if numHold in newD:
                    result = newD[numHold]
                else:
                    result = "unknown"

            splitL.append("=")
            splitL.append(result)
            #print("calculated function is")
            result = ""
            for i in splitL:
                result += i + " "
            print(result.rstrip())
        elif splitL[0] == "clear":
            commandsDict.clear()







main()
    
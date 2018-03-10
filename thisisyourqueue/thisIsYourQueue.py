
from collections import deque
#import time
import sys

def main():
    caseCount = 1
    lines = " "
    #print("lines " + str(lines))
    #line = sys.stdin.readlines()

    #line = " "
    line = input()

    while line != "0 0":
        print("Case " + str(caseCount) + ": ")
        citizenQueue = deque() #append, pop left
        lineP = line.split()
        #print(lineP)
        P = int(lineP[0])
        #print("P " + str(P))
        C = int(lineP[1])
        #print("C " + str(C))
        for i in range(1,min(P,C)):
            citizenQueue.append(i)
        for d in range(C):
            command = input()
            #print("com " + str(command))
            if command == "N":
                processPatient = citizenQueue.popleft()
                citizenQueue.append(processPatient)
                print(processPatient)
            else:
                expedite = command.split(" ")
                #print("expedite " + str(expedite))
                urgent = int(expedite[1])
                citizenQueue.remove(urgent)
                citizenQueue.appendleft(urgent)
        caseCount += 1
        line = input()
    return 0


#start_time = time.time()
main()
#print("--- %s seconds ---" % (time.time() - start_time))

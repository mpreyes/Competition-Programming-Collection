

import sys


def main():
    line = sys.stdin.readline().split()
    N = int(line[0]) #N people
    T = int(line[1]) #time in minutes until Oliver closes the bank
    #print("N " + str(N))
    #print("T " + str(T))
    sortedPeople = []
    for i in range(N):
        s = sys.stdin.readline().split()
        sortedPeople.append((int(s[0]),int(s[1])))

    #sortedPeople.sort(key=lambda sl:(sl[0],-sl[1])) #sorts by first val, then second
    sortedPeople.sort(reverse = True)
    maxValue = 0
    timeElapsed = 0


    # for j in range(len(sortedPeople)):
    #     print(sortedPeople[j])
    peopleInQueue = [] #queue of 47


    hold = []
    for i in range(47): #gotta make sure we get them richies first
        hold.append(False)
    for j in range(len(sortedPeople)):
        timebeforeLeaving = sortedPeople[j][1]
        #print("time " + str(time))
        while(timebeforeLeaving >= 0): #making people go back as far as possible, before they leave
            if hold[timebeforeLeaving] == False:
                maxValue += sortedPeople[j][0]
                hold[timebeforeLeaving] = True
                break
            timebeforeLeaving -= 1

    print(maxValue)
















main()

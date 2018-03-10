
import sys
def main():
    n = int(sys.stdin.readline())
    cards = []
    holdList = []
    line =  sys.stdin.readline().split()
    for i in line:
        cards.append(int(i))
    if len(cards) > 2:
        holdList.append(cards[0])
        del cards[0]
        while len(cards) > 1:
            if(cards[0] + holdList[-1]) % 2 == 0:
                del cards[0]
                del holdList[-1]
                holdList.append(cards[0])
                del cards[0]
                print(holdList)
                print(cards)
            else:
                holdList.append(cards[0])
                del cards[0]
                print(holdList)
                print(cards)
        if(len(cards) == 1):
            if(cards[0] + holdList[-1]) % 2 ==0:
                del cards[0]
                del holdList[-1]
            else:
                holdList.append(cards[0])
        print(len(holdList))
    else:
        if n == 1:
            print(1)
        if n == 2:
            if(cards[0] + cards[1]) % 2 == 0:
                print(0)
            else:
                print(2)
main()

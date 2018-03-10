
   
def collatzC( N, hold = []):
    while(N != 1):
        if (N % 2 == 0):  #if it is even
            hold.append(N / 2);
            N /= 2;
        else:
            hold.append((3 *N) + 1);
            N = (3 *N) + 1;
    

def main():
    line = input();
    while line != "0 0":
         lines = line.split(" ");
         A = int(lines[0]);
         B = int(lines[1]);
         #print(str(A) + " " + str(B));
         stepsA = 0; 
         stepsB = 0;
         meetAt = 0;
         holdA = [];
         holdB = [];
         holdA.append(A);
         holdB.append(B);
         collatzC(A,holdA);
         collatzC(B,holdB);
         result = 0;
         for i in holdA:
             if i in holdB:
                 meetAt = i;
                 break;
         stepsA = holdA.index(meetAt);
         stepsB = holdB.index(meetAt);
                         
         print(lines[0] + " needs " + str(stepsA) + " steps, " + lines[1] + " needs " + str(stepsB) + " steps, they meet at " + str(int(meetAt)) );
         line= input();
main()
 

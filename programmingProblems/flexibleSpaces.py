





def main():
    line1 = input();
    line2 = input();
    lines1 = line1.split(" ");
    lines2 = line2.split(" ");
    lines2 = list(map(int, lines2)); #converting to ints

    width = int(lines1[0]);
    P = int(lines1[1]); #number of partitions
    masterList = [];
    holdNum = 0;
    masterList.append(width);
    #for i in lines2:
        #masterList.append(i);
        #masterList.append(width - i);

    for i in lines2: #running loop backwards
        if(i not in masterList):
            masterList.append(i); #adding the partitions
        if((width - i) not in masterList):
            masterList.append(width - i);

    for k in reversed(lines2):
        for j in reversed(lines2):
            if (abs(k-j) not in masterList):
                masterList.append(abs(k -j));


    masterList = sorted(masterList);

    masterList.remove(0);
    for d in masterList:
        print(d);
        
main()

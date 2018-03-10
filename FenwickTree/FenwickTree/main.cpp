//
//  main.cpp
//  FenwickTree
//
//  Created by Madelyn Reyes on 2/2/18.
//  Copyright © 2018 Madelyn Reyes. All rights reserved.
//

#include <iostream>
#include <stdio.h>


using namespace std;

//n elements in array

void incrementXbyY(long Fenwick[], long n, long x, long y){ //update the the arr[x] by y
   
    if(x == 0){
        Fenwick[0] += y;
    }
    else{
    
    for( ; x <= n; x +=(x & (-x))){
        Fenwick[x] += y;
    }
    }

}

 long querySum(long Fenwick[],long i) { //getSum of previous elements in array

    i--; //we want the sum of i -1 elements
     long answer = Fenwick[0];
     
     if( i == -1){
         return 0;
     }
  
    for (;i; i -=(i & (-i))) {
             
    answer += Fenwick[i];
        
     }
    
     return answer;

 }


int main() {
//    
    ios_base::sync_with_stdio(false); //optimizing for faster I/O
    cin.tie(NULL);
//
    long N, Q;
    cin >> N >> Q;
    //scanf("%lu",N
//    scanf("%ld" "%ld", &N, &Q);
    // scanf("%lu", &Q);
   
    long *FenwickTree = new long [N];
    FenwickTree[0] = 0;

    for(int i =0; i < Q; i++) {
        char symbol;// = getchar();
        cin >> symbol;
       //  scanf("%c", &symbol);
        
        if(symbol == '+'){ //increment x by y
            long x, y;
//            scanf("%ld" "%ld", &x, &y);
            cin >> x >> y;

            incrementXbyY(FenwickTree, N, x, y);
            
        }
        else{ // query for value

            long v;
            cin >> v;
            cout << querySum(FenwickTree, v) << "\n";
//            scanf("%ld", &v);
//            printf("%ld",querySum(FenwickTree, v));
            
        }
        
    }
    
 

    return 0;
}

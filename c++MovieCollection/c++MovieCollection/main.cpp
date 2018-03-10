//
//  main.cpp
//  c++MovieCollection
//
//  Created by Madelyn Reyes on 2/3/18.
//  Copyright © 2018 Madelyn Reyes. All rights reserved.
//

#include <iostream>

using namespace std;

//n elements in array

void incrementXbyY(long Fenwick[], long n, long x, long y){ //update the the arr[x] by y
    
        for( ; x <= n; x +=(x & (-x))){
            Fenwick[x] += y; //slight mod, make it equal to 0 instead
        }

}


long querySum(long Fenwick[],long i){ //getSum of previous elements in array
    
    long answer = 0;
    
    for (;i; i -=(i & (-i))) {
        
        answer += Fenwick[i];
        
    }
    
    return answer;
    
    
    
}

int main(void) {
    

    int testCases;
    cin >> testCases;
    int Arr[100005];
    
    for(int i =0; i < testCases; i++){
       // cout << "testCase " << i << endl;
        
        int numMovies, locateRequests;
        cin >> numMovies >> locateRequests;
        long *FenwickTree = new long [numMovies]; //there are still N items
        
        for(int j =1; j < numMovies; j++){ //might not need this
            incrementXbyY(FenwickTree, numMovies, FenwickTree[j], 1);
            Arr[i] = numMovies - j +1;

        }
        for(int d = 1; d < numMovies+1; d++){
            cout << "FWB4 " << d << ": " << FenwickTree[d] << " ";
        }

        for(int k = n +1 ; k < numMovies + locateRequests; k++){
            long request;
            cin >> request;

            
            incrementXbyY(FenwickTree,numMovies, request, 0);
            
        }
//        for(int d = 1; d < numMovies+1; d++){
//            cout << "FW " << d << ": " << FenwickTree[d] << " ";
//        }

        
    }
    
    return 0;
}

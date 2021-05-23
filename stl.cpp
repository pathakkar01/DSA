#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){

    vector<int> A = {11,2,4,15};

    cout << A[1] << endl;

    sort(A.begin(), A.end());  //o(Nlog(n))
    //search - o(log(n))
    bool present = binary_search(A.begin(),A.end(), 100);
    present = binary_search(A.begin(), A.end(), 4);


    //2,4,11,15ṇ

    A.push_back(100);
    A.push_back(100);
    A.push_back(100);
    A.push_back(100);

    A.push_back(123);

    //count trick

    vector<int>::iterator it = lower_bound(A.begin(),A.end(), 100); // >=
    vector<int>::iterator it2 = lower_bound(A.begin(),A.end(), 100); // >

    cout << *it << " " << *it2 << endl;
    
    cout << it2 - it << endl; //4

    return 0;



}

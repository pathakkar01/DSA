#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

void search(int A[],int i, vector<int> curr)
{
    //int n = sizeof(A) / sizeof(A[0]);
    sort(A,A+3);
    int size = 3;
    if (i == size || A[i] != A[i-1]){
    cout <<"(";
    for (int k : curr) 
    { 
        cout << k << "\t"; 
    } 
    cout<<")";
    cout << "\n";
    }
    else{

        curr.push_back(A[i]);
        search(A, i+1, curr);
        curr.pop_back();
        search(A, i+1, curr);
    }

}

int main(){
    int A[] = {1,2,3};
    //vector<vector<int>> subset;
    vector<int> curr; 
    //cout<<"xyz";
    search(A, 0 ,curr);
    return 0;
}
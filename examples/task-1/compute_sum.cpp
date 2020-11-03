#include<iostream>
using namespace std;


int compute_sum(int start, int end){

    if(start == end){
        return end
    }
    else return start + compute_sum((++start), end);
}

int main(){
    cout<<compute_sum(1,6)<<endl;
}
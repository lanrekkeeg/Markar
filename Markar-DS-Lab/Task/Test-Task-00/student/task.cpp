#include<iostream>
using namespace std;

class Sum{
    public:

        ///// YOUR CODE HERE //////
        long sum(long a, long b){
            return a+b;
        }
};

int main(){
    Sum s1;
    cout<<"Output:"<<s1.sum(1223,23232)<<endl;
}
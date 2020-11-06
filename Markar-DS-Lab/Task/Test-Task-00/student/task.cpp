#include<iostream>
using namespace std;

class Sum{
    public:

        ///// DO NOT CHANGE FUNCTION NAME OR PARAMETERS //////
        long sum(long a, long b){
            return a+b;
            // YOUR CODE //
            // RETURN THE OUTPUT OF a+b
        }
};

int main(){
    Sum s1;
    cout<<"Output:"<<s1.sum(1223,23232)<<endl;
}
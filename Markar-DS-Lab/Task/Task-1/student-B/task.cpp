#include<iostream>
#include<string>
using namespace std;

// ############# PART-A #######################
////////  DO NOT CHANGE FUNCTION NAME AND PARAMTERS ///////
string leave_2nd_print_reverse(string str, int leave, int index=0){
        // YOUR CODE HERE     aabdfb
        string s;
        if(index+leave>str.length())
        {
            return "";
        }
        index=index+leave;       
        s=s+leave_2nd_print_reverse(str, leave,index);
        return s+str[index];
}


////////  DO NOT CHANGE FUNCTION NAME AND PARAMTERS ///////
// ############# PART-B #######################
/*
    UNCOMMENT WHEN YOU DONE WITH PART A BECAUSE TEST CASES WILL SHOW YOU FAIL
int count_after_specific(string str, int num1,int num2, int index=0){
    // YOUR CODE HERE
}
*/
int main(){


 
    // PART A SAMPLE
    if (leave_2nd_print_reverse("aabdfb",2,0) == "fb"){
        cout<<"Match"<<endl;
    }
    else cout<<"MissMatch"<<endl;
    //cout<<"Output:"<<leave_2nd_print_reverse("aabdfb",2,0)<<endl;
/*  
    // PART B SAMPLE
    //cout<<"Output:"<<count_after_specific("111123112322311232000230",2,5,0)<<endl;

*/
}
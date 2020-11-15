#include<iostream>
#include<string>
using namespace std;

// ############# PART-A #######################
////////  DO NOT CHANGE FUNCTION NAME AND PARAMTERS ///////
// ############# PART-B #######################
   // UNCOMMENT WHEN YOU DONE WITH PART A BECAUSE TEST CASES WILL SHOW YOU FAIL
string leave_2nd_print_reverse(string str, int leave, int index=0)
{
    string x;
    string y;
        if(index < str.size())
        {
            index = index+leave;
           x=leave_2nd_print_reverse(str,leave,index);
           y=x+str[index];
           return y;
        }
        else
        {
            return y;
        }
        return y;
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
    //cout<<leave_2nd_print_reverse("aabdfb",2,0)<<endl;
   // if (leave_2nd_print_reverse("aabdfb",2,0) == "fb"){
   //     cout<<"Match"<<endl;
   // }
   // else cout<<"MissMatch"<<endl;
    //cout<<"Output:"<<leave_2nd_print_reverse("aabdfb",2,0)<<endl;
/*  
    // PART B SAMPLE
    //cout<<"Output:"<<count_after_specific("111123112322311232000230",2,5,0)<<endl;

*/
}
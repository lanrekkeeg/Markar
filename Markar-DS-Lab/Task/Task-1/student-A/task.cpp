#include<iostream>
#include<string>
using namespace std;


// ############# PART-A #######################
////////  DO NOT CHANGE FUNCTION NAME AND PARAMTERS ///////
//string  reverse_from_special_character(string str,char special, int index=0){
//    return "";
//}

string leave_2nd_print_reverse(string str, int leave, int index=0)
{
    string x;
    string y;
        if(index <= str.size())
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
    UNCOMMENT WHEN YOU DONE WITH PART A
int count_specific_number(string str, int num, int index=0){
    
}

*/
int main(){
        // SAMPLE
  
    //cout<<"Output:"<<reverse_from_special_character(".abcdef.sdssd",'.',0)<<endl;   
    //cout<<"Output:"<<count_specific_number("11112211119999912220000",1,0)<<endl;
    //return 0;
}
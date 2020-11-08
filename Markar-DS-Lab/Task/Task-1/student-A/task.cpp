#include<iostream>
#include<string>
using namespace std;


// ############# PART-A #######################
////////  DO NOT CHANGE FUNCTION NAME AND PARAMTERS ///////
//string  reverse_from_special_character(string str,char special, int index=0){
//    return "";
//}

string  reverse_from_special_character(string str,char special, int index=0){
  char cha = str[index];
    if(cha==special)
    {
        cout<<endl;
        return "";
    }
    else{
        cout<<cha;
        reverse_from_special_character(str,'/',index+1);
        cout<<cha;
    }
    return str;
}

int count_specific_number(string str, int num, int index=0){
   cout<< str[index];
   int x=0;
   if(str[index]==0)
   {
       return 0;
   }
   else{
       x=count_specific_number(str,num,index+1);
       char ch='0'+num;
       if(str[index]==ch)
       {
           x=x+1;
           return x;
       }
       else
       return x;
   }
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
   // cout<<"Output:"<<count_specific_number("11112211119999912220000",9,0)<<endl;
    //return 0;
}
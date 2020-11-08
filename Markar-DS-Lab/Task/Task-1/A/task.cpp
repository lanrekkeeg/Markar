#include<iostream>
#include<string>
using namespace std;
// #############PART-A#######################
////////  DO NOT CHANGE FUNCTION NAME AND PARAMTERS ///////
string reverse_from_special_character(string str,char special, int index=0){
    if (str[0] == special){
        return "";
        }
    if (str[index] == special)
        return "";
    else{
        return reverse_from_special_character(str, special, ++index)+str[index-1];
    }
}

int count_specific_number(string str, int num, int index=0){
    int c=0;
    if (str == "")
        return 0;
    if (index == str.length()){
        return 0;
        }
    if (str[index]-'0' == num){
            c = 1;
}
    return count_specific_number(str, num, ++index) + c;
}

int main(){

    // Section A
   if(reverse_from_special_character("sdssdsd..ds",'.',0)==""){
        cout<<"Empty"<<endl;
    }
    cout<<"Output:"<<reverse_from_special_character("Hello D$orothy",'$',0)<<endl;
    cout<<"Output:"<<reverse_from_special_character("abcdef.sds%sd",'%',0)<<endl;
    cout<<"Output:"<<reverse_from_special_character("abcde'fsdssd",'\'',0)<<endl;
    
    cout<<"Output:"<<reverse_from_special_character("abc-defsdssd",'-',0)<<endl;
    cout<<"Output:"<<reverse_from_special_character("abcd.ef.sdssd",'.',0)<<endl;
    cout<<"Output:"<<reverse_from_special_character("/abcdef.sdssd",'/',0)<<endl;
    cout<<"Output:"<<reverse_from_special_character("$abcdef.sdssd",'$',0)<<endl;
    cout<<"Output:"<<reverse_from_special_character("@abcdef.sdssd",'@',0)<<endl;
    cout<<"Output:"<<reverse_from_special_character("abcdef.sds@sd",'@',0)<<endl;
    cout<<"Output:"<<reverse_from_special_character("abc!def.sdssd",'!',0)<<endl;
    cout<<"Output:"<<reverse_from_special_character("!abcdef.sdssd",'!',0)<<endl;




    cout<<"Part B"<<endl;
    if(count_specific_number("1232",6,0)==0){
        cout<<"Empty"<<endl;
    }
    cout<<"Output:"<<count_specific_number("111122111112220000",2,0)<<endl;
    cout<<"Output:"<<count_specific_number("111122111112220000",9,0)<<endl;
    cout<<"Output:"<<count_specific_number("111.2323232",1,0)<<endl;
    cout<<"Output:"<<count_specific_number("11133333222255",5,0)<<endl;
    cout<<"Output:"<<count_specific_number("1111221111122333320000",3,0)<<endl;
    cout<<"Output:"<<count_specific_number("111122111112220000",0,0)<<endl;
    cout<<"Output:"<<count_specific_number("411112211111222000404",4,0)<<endl;
    cout<<"Output:"<<count_specific_number("55511155551221115551122200005",5,0)<<endl;
}
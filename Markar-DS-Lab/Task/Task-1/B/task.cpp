#include<iostream>
#include<string>
using namespace std;


string leave_2nd_print_reverse(string str, int leave, int index=0){
        if (leave >= str.length()){
            return "";
        }

        else if(index+leave >= str.length()){
            return "";
        }
        else return leave_2nd_print_reverse(str, leave, index+leave) + str[index+leave];

}

int count_after_specific(string str, int num1,int num2, int index=0){
    int c=0;
    if (str == "")
        return 0;
    if (index == str.length()){
        return 0;
    }
    if (str[index]-'0' == num1){
        if (index+1 <= str.length()){
            if (str[index+1] - '0' == num2)
                c = 1;
        }
    }
    return count_after_specific(str, num1, num2, ++index) + c;
}

int main(){


    cout<<"Output:"<<leave_2nd_print_reverse("axxx32sabdfb",2,0)<<endl;
    cout<<"Output:"<<leave_2nd_print_reverse("23242$@@#@#@",2,0)<<endl;
    cout<<"Output:"<<leave_2nd_print_reverse("23232323",2,0)<<endl;
    cout<<"Output:"<<leave_2nd_print_reverse("dfdwewe",2,0)<<endl;
    cout<<"Output:"<<leave_2nd_print_reverse("adsdsrsd",2,0)<<endl;
    cout<<"Output:"<<leave_2nd_print_reverse("aabdfbsds",2,0)<<endl;
    cout<<"Output:"<<leave_2nd_print_reverse("aabdfbwew",2,0)<<endl;
    cout<<"Output:"<<leave_2nd_print_reverse("",2,0)<<endl;


    cout<<"Output:"<<count_after_specific("111123112322311232000230",2,0,0)<<endl;
    cout<<"Output:"<<count_after_specific("1111231123223112320002309",9,9,0)<<endl;
    cout<<"Output:"<<count_after_specific("8111123112322311232000230",8,1,0)<<endl;
    cout<<"Output:"<<count_after_specific("111123112365566522311232000230",5,6,0)<<endl;
    cout<<"Output:"<<count_after_specific("111123112322311232000230",1,2,0)<<endl;
    cout<<"Output:"<<count_after_specific("1111231123223178787777781232000230",7,8,0)<<endl;
    cout<<"Output:"<<count_after_specific("111123112322311232000230",2,0,0)<<endl;
    cout<<"Output:"<<count_after_specific("111123112322311232000230099",0,9,0)<<endl;
    

}
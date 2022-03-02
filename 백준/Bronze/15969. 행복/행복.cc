#include<iostream>

int main(){
    int N, max, min, temp;
    max=0;
    min=1000;
    
    std::cin>>N;
    for(int i=0; i<N; i++){
        std::cin>>temp;
        if(temp>max) max=temp;
        if(temp<min) min=temp;
    }
    std::cout<<max-min;
}
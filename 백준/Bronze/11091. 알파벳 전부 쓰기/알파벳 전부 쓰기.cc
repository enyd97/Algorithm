#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

int main()
{
    string str[50];
    char check[50][26] = {0, };
    char nothing[50];
    int num;
    vector<char> buffer;
    cin >> num;
    cin.ignore();
    for (int i = 0; i < num; i++){
        int tag = 0;
        getline(cin, str[i]);
        for (int j = 0; j < str[i].size(); j++){
            int index;
            if (str[i][j] > 96 && str[i][j] < 123){
                index = str[i][j] - 97;
            }
            else if (str[i][j] > 64 && str[i][j] < 91){
                index = str[i][j] - 65;
            }
            else continue;
            check[i][index] = 1;
        }
    }
    for(int i = 0; i < num; i++){
        int tag = 0;
        for (int j = 0; j < 26; j++){
            if (!check[i][j]){
                buffer.push_back(j+97);
                check[i][j] = 0;
                tag = 1;
            }
        }
        if(!tag) cout<<"pangram"<<endl;
        else {
            cout<<"missing ";
            for(int j = 0; j<buffer.size(); j++){
                cout<<buffer[j];
            }
            buffer.resize(0);
            cout<<endl;
        }
    }
    cout<<endl;
}
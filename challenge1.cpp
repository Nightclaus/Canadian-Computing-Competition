#include <iostream>
#include <vector>
#include <string>

using namespace std;

string input() {
    string line;
    getline(cin, line);
    return line;
}

int main() {
    int maxInputs = stoi(input());
    int radius = maxInputs / 2;
    vector<string> array;

    for (int i = 0; i < maxInputs; i++) {
        array.push_back(input());
    }

    int results = 0;
    for (int i = 0; i < radius; i++) {
        if (array[i] == array[i+radius]) {
            results += 2;
        }
    }
    
    cout << results << endl;
    return 0;
}
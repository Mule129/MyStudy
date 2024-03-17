#include <iostream>

using namespace std;

void game(string, int);
string random(int);

int main() {
    string number = random(3);
    // cout << "Enter is  " << number << endl;
    int endGame = 5;
    
    game(number, endGame);

    return 0;
}
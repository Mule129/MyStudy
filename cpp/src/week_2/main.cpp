#include <iostream>

using namespace std;

void game(string);
string random(int);

int main() {
    string number = random(3);
    cout << "Enter is " << number << endl;

    game(number);

    return 0;
}
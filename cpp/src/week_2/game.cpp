#include <iostream>
#include <string>

using namespace std;


int game(string number) {
    string inputValue;
    int strikes = 0;
    int balls = 0;

    cout << "Enter a guess: ";
    cin >> inputValue;

    for (int i = 0; i < number.length(); i++) {
        for (int j = 0; j < number.length(); j++) {
            if (number[i] == inputValue[j] && i == j) {
                strikes ++;
            } else if (number[i] == inputValue[j]) {
                balls ++;
            }
        }
    }

    if (strikes != number.length()) {
        cout << "Strikes: " << strikes << ", Balls: " << balls << endl;
        strikes = 0;
        balls = 0;

        return game(number);
    } else {
        cout << "You win!";
    }

    return 0;
}
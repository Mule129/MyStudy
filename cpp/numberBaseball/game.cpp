#include <iostream>
#include <string>

using namespace std;


int game(string number, int endGame) {
    string inputValue;
    int strikes = 0;
    int balls = 0;

    cout << endGame << " Chances left." << endl;
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

        if (endGame > 1) {
            endGame--;
            return game(number, endGame);
        } else {
            cout << "You lost!";
            return 0;
        }
    } else {
        cout << "You win!";
    }

    return 0;
}
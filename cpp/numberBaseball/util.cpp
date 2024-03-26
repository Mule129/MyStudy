#include <string>
#include <iostream>
#include <random>
#include <time.h>

using namespace std;

string random(int len) {
    // random_device rd;

    mt19937 gen(time(NULL));
    uniform_int_distribution<int> dis(0, 9);

    int randomValueList[len];

    string value;

    for (int i = 0; i < len; i++) {
        randomValueList[i] = dis(gen);
        for (int j = 0; j < i; j++) {
            if (randomValueList[i] == randomValueList[j]) {
                i--;
            }
        }
    }

    for (int i = 0; i < len; i++) {
        value += to_string(randomValueList[i]);
    }

    return value;
}
#include <string>
#include <iostream>
#include <random>

using namespace std;

string random(int len) {
    // random_device rd;

    mt19937 gen(1);

    uniform_int_distribution<int> dis(0, 9);

    string value = "";

    for (int i = 0; i < len; i++) {
        value += to_string(dis(gen));
    }

    return value;
}
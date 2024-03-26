#include <string>
#include <random>
#include <time.h>

/**
 * calculate text angle (center)
*/
int angleText(std::string strValue, int integerValue = 0) {
    return strValue.length() + std::to_string(integerValue).length() / 2;    
}


/**
 * return random int value
*/
int randInt(int min, int max) {
    std::mt19937 gen(time(NULL));
    std::uniform_int_distribution<int> dis(min, max);

    return dis(gen);
}

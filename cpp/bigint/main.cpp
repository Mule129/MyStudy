#include <iostream>
#include <string>

using namespace std;

string reverse(string result) {
    int length = result.length();
    for (int i = 0; i < length / 2; ++i) {
        char temp = result[i];
        result[i] = result[length - i - 1];
        result[length - i - 1] = temp;
    }
    return result;
}

string bigIntegerSum(string num1, string num2) {
    string result = "";
    int carry = 0;

    int len1 = num1.size(), len2 = num2.size();
    int maxLength = max(len1, len2);
    num1 = string(maxLength - len1, '0') + num1;
    num2 = string(maxLength - len2, '0') + num2;

    for (int i = maxLength - 1; i >= 0; i--) {
        int digit1 = num1[i] - '0';
        int digit2 = num2[i] - '0';
        int sum = digit1 + digit2 + carry;
        carry = sum / 10;
        result = to_string(sum % 10) + result;
    }

    if (carry > 0)
        result = to_string(carry) + result;

    return result;
}

string bigIntegerSub(string num1, string num2) {
    string result;

    bool negativeResult = false;
    if (num1.length() < num2.length() || (num1.length() == num2.length() && num1 < num2)) {
        swap(num1, num2);
        negativeResult = true;
    }

    int len1 = num1.size(), len2 = num2.size();
    int maxLength = max(len1, len2);
    num1 = string(maxLength - len1, '0') + num1;
    num2 = string(maxLength - len2, '0') + num2;

    int borrow = 0;
    for (int i = maxLength - 1; i >= 0; --i) {
        int digit1 = num1[i] - '0';
        int digit2 = num2[i] - '0';

        int diff = digit1 - digit2 - borrow;
        if (diff < 0) {
            diff += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }

        result.push_back(diff + '0');
    }

    result = reverse(result);

    result.erase(0, min(result.find_first_not_of('0'), result.size() - 1));


    if (result.empty()) {
        result = "0";
    }

    if (negativeResult) {
        result.insert(0, "-");
    }

    return result;
}

int main() {
    string firstNumber;
    string secondNumber;
    
    cout << "First number\t>> ";
    cin >> firstNumber;

    cout << "Second number\t>> ";
    cin >> secondNumber;

    string resultSum = bigIntegerSum(firstNumber, secondNumber);
    string resultSub = bigIntegerSub(firstNumber, secondNumber);
    
    cout << "Sum\t\t>> " << resultSum << endl;
    cout << "Sub\t\t>> " << resultSub << endl;
}

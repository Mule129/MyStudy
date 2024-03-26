#include <iostream>
#include <string>

using namespace std;

string bigIntegerSum(string, string);
string bigIntegerSub(string, string);


int main() {
    string firstNumber;
    string secondNumber;
    
    cout << "First number\t>>";
    cin >> firstNumber;

    cout << "Second number\t>>";
    cin >> secondNumber;

    string resultSum = bigIntegerSum(firstNumber, secondNumber);
    string resultSub = bigIntegerSub(firstNumber, secondNumber);
    
    cout << "Sum\t\t>>" << resultSum << endl;
    cout << "Sum\t\t>>" << resultSub << endl;
}

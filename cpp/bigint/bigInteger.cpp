#include <string>
#include <cstring>

using namespace std;

string sum(string a, string b, string c) {
    int _a = stoi(a);
    int _b = stoi(b);
    int _c = stoi(c);

    int result = _a + _b + _c;

    return to_string(result);
}

string sub(string a, string b, string c) {
    int _a = stoi(a);
    int _b = stoi(b);
    int _c = stoi(c);

    int result = _a - _b - _c;

    return to_string(result);
}

string bigIntegerSum(string a, string b) {
    int loop;
    
    if (a.length() - b.length() > 0) {
        loop = a.length();
    } else {
        loop = b.length();
    }

    for (int i = loop; i >= 0; i--) {
        if (i > a.length() && i > b.length()) {
            continue;
        } else if (i > a.length() && i <= b.length()) {
            continue;
        } else if (i <= a.length() && i > b.length()) {
            continue;
        } else {
            continue;
        }
        
    }
    return ;
}

string bigIntegerSub(string a, string b) {
    return;
}

class Solution {
public:

    string encode(vector<string>& strs) {
        unsigned char separator = '|';
        unsigned char offset = 17;

        std:: string result;
        result.reserve(5000);

        for (const std:: string& str : strs) {
            for (const char& c : str) {
                unsigned char e = c + 17;
                result += e;
            }
            result += separator;
        }

        result = result.substr(0, result.size() - 1);

        return result;
    }

    vector<string> decode(string s) {
        char separator = '|';
        unsigned char offset = 17;

        std:: vector<std:: string> result;

        std:: stringstream ss (s);
        std:: string item;

        while (std:: getline(ss, item, separator)) {
            result.push_back(item);
        }

        for (std:: string& s : result) {
            for (char& c : s) {
                unsigned char d = c - 17;
                c = d;
            }
        }

        return result;
    }
};

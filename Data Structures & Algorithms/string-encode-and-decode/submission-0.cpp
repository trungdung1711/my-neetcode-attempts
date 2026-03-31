class Solution {
public:

    string encode(vector<string>& strs) {
        unsigned char separator = '|';
        unsigned char offset = "17";

        // 100 * 200 + 200 - 1
        std:: string result;
        result.reserve(5000);

        for (const std:: string& str : strs) {
            for (const char& c : str) {
                unsigned char e = ;
                result += e
            }
            result += separator;
        }
    }

    vector<string> decode(string s) {
        unsigned char separator = '|';
        unsigned char offset = "17";
    }
};

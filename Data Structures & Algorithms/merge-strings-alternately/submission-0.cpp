class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        // input: 2 strings
        // output: 1 string characters are chosen alternately from [1] and [2]
        // start with [1]

        // constraint
        // word.length >= 1, not empty string
        // lower English letters

        // edge case
        // a b -> ab
        // abc a -> aabc
        // a abc -> aabc
        // aa bb -> abab

        std:: size_t first = 0;
        std:: size_t second = 0;

        std:: string result{""};

        while (first < word1.size() && second < word2.size()) {
            // std:: max?
            result += word1[first];
            result += word2[second];

            first++;
            second++;
        }

        if (first < word1.size()) {
            result.append(word1.substr(first, std:: string:: npos));
        }

        if (second < word2.size()) {
            result.append(word2.substr(second, std:: string:: npos));
        }

        return result;
    }
};
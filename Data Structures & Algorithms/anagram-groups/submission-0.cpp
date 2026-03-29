class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std:: vector <std:: vector<std:: string>> results;

        std:: map<std:: map<char, int>, std:: vector<std:: string>> helper;

        std:: map<std:: string, std:: map<char, int>> charStructures;

        // const reference to the string
        // const auto& str = *it
        for (const string& str : strs) {
            std:: map<char, int> charMap;

            for (const auto& c : str) {
                charMap[c]++;
            }

            charStructures[str] = charMap;
        }

        for (const string& str : strs) {
            helper[charStructures[str]].push_back(str);
        }

        for (const auto& pair : helper) {
            results.push_back(pair.second);
        }

        return results;
    }
};
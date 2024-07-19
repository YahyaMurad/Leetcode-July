#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> luckyNums;

        for (int i = 0; i < matrix.size(); i++) {
            int minElement = matrix[i][0];
            int colIndex = 0;

            for (int j = 1; j < matrix[i].size(); j++) {
                if (matrix[i][j] < minElement) {
                    minElement = matrix[i][j];
                    colIndex = j;
                }
            }

            bool isLucky = true;
            for (int k = 0; k < matrix.size(); k++) {
                if (matrix[k][colIndex] > minElement) {
                    isLucky = false;
                    break;
                }
            }
            
            if (isLucky) {
                luckyNums.push_back(minElement);
            }
        }
        return luckyNums;
    }
};
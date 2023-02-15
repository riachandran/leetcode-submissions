#include <algorithm>
#include <string>

class Solution {
public:
    int smallestCommonElement(vector<vector<int>>& mat) {
        int curr_max = 0, idx=0;
        int possible_match = -1;
        int match = -1;
        for (int i=0; i<mat.size(); i++){
            if(mat[i][0] > curr_max){
                curr_max = mat[i][0];
                idx = i;
            }
        }
        vector<int> main_array =mat[idx];
        mat.erase(mat.begin()+idx);
        for (int i=0; i<main_array.size(); i++){
            int match = -1;
            for (int j=0; j<mat.size(); j++){
                if (std::find(mat[j].begin(), mat[j].end(), main_array[i]) != mat[j].end()){
                    match = main_array[i];
                    if ((j == mat.size()-1) && match > -1){
                        cout <<"Found match " << match << "\n";
                        return match;
                    }
                }
                else{
                    break;
                }
            }
        }
        return match;
    }
};

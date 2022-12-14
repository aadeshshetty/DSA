#include<bits/stdc++.h>
using namespace std;

void bubbleSort(vector<int>& arr) {
    /*
    * Time Complexity: O(N^2)
    * Space Complexity: O(1)
    */
    for (int i = 0; i < (int)arr.size(); i++) {
        for (int j = i + 1; j < (int)arr.size(); j++) {
            if (arr[i] > arr[j])
                swap(arr[i], arr[j]);
        }
    }
}


int main() {
    vector<int> arr = { 8, 5, 2, 10, 7, 4, -1,-6, 0 };

    bubbleSort(arr);

    for (int i = 0; i < (int)arr.size(); i++) {
        cout << arr[i] << ' ';
    }

    cout << '\n';

}
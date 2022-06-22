#include <iostream>

struct pair
{
    int left;
    int right;
};

void swap(int *a, int *b) {
    int c = *a;
    *a = *b;
    *b = c;
}

pair split(int *arr, int left, int right, int x) {
    pair p;
    p.left = left;
    p.right = left;
    for (int i = left; i < right; ++i) {
        if (arr[i] < x) {
            swap(arr + i, arr + p.left);
            if (p.right > p.left) {
                swap(arr + i, arr + p.right);
            }
            p.left++;
            p.right++;
        } else if (arr[i] == x) {
            swap(arr + i, arr + p.right);
            p.right++;
        }
    }
    return p;
}

int solve(int *arr, int left, int right, int k) {
    if (right - left <= 1) {
        return arr[left];
    }
    int x = arr[left + rand() % (right - left)];
    pair p = split(arr, left, right, x);
    if (k >= left and k < p.left) {
        return solve(arr, left, p.left, k);
    } else if (k >= p.left and k < p.right) {
        return arr[p.left];
    } else {
        return solve(arr, p.right, right, k);
    }
        
}

int main(int argc, const char * argv[]) {
    int n, m;
    std::cin >> n;
    int *arr = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    std::cin >> m;
    int left, right, k;
    for (int i = 0; i < m; ++i) {
        std::cin >> left >> right >> k;
        int *arr2 = (int *) malloc((right - left + 1) * sizeof(int));
        memcpy(arr2, arr + left - 1, (right - left + 1) * sizeof(int));
        std::cout << solve(arr2, 0, right - left + 1, k - 1) << "\n";
        free(arr2);
    }
    free(arr);
    return 0;
}

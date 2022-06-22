#include <iostream>
#include <cstdlib>

int compare(const void *a, const void *b) {
  return (*(int *)a - *(int *)b);
}

int lower_bound(int *arr, int n, int x) {
    int left = -1;
    int right = n;
    int middle;
    while (right - left > 1) {
        middle = (left + right) / 2;
        if (arr[middle] >= x) {
            right = middle;
        } else {
            left = middle;
        }
    }
    return right;
}

int main() {
    int n, k;
    int left, right;
    std::cin >> n;
    int *arr = (int *) malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    qsort(arr, n, sizeof(int), compare);
    std::cin >> k;
    for (int i = 0; i < k; ++i) {
        std::cin >> left >> right;
        std::cout << lower_bound(arr, n, right + 1) - lower_bound(arr, n, left) << " ";
    }
    free(arr);
    return 0;
}

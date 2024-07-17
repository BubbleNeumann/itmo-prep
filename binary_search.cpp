#include <cstddef>
#include <experimental/random>
#include <iostream>
#include <stdexcept>
#include <cassert>

int* generate_sorted_arr(size_t len)
{
    auto sorted_arr = new int[len];
    for (auto i = 0; i < len; ++i)
    {
        sorted_arr[i] = std::experimental::randint(i, i+10) + (i > 0 ? sorted_arr[i-1] : 0);
    }
    return sorted_arr;
}

void print_arr(int* arr, size_t arr_len)
{
    for (auto i = 0; i < arr_len; ++i)
    {
        std::cout << arr[i] << ' ';
    }
    std::cout << '\n';
}

size_t binary_search(int elem, int* arr, size_t arr_len)
{
    size_t lower_ind = 0;
    size_t upper_ind = arr_len;
    size_t cur_ind;

    while (upper_ind != lower_ind)
    {
        cur_ind = (upper_ind + lower_ind) / 2;
        if (arr[cur_ind] == elem) return cur_ind; // found

        if (arr[cur_ind] > elem) // then move the upper ind
        {
            upper_ind = cur_ind;
            continue;
        }
        lower_ind = cur_ind;
    }
    throw std::runtime_error("no elem found");
}


int main()
{
    const size_t arr_len = 10;
    auto arr = generate_sorted_arr(arr_len);
    assert(binary_search(arr[0], arr, arr_len) == 0);
    assert(binary_search(arr[2], arr, arr_len) == 2);
    assert(binary_search(arr[7], arr, arr_len) == 7);
    try {
        binary_search(-1, arr, arr_len);
        assert(false);
    } catch (std::runtime_error) {
        assert(true);
    }
    delete[] arr;
    return 0;
}

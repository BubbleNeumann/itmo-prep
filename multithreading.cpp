#include <iostream>
#include <thread>

void task1()
{
    for (auto i = 5; i; --i)
    {
        std::cout << "thread 1 : " << i << '\n' ;
        std::this_thread::sleep_for(std::chrono::milliseconds(6));
    }
}

void task2()
{
    for (auto i = 5; i; --i)
    {
        std::cout << "thread 2 : " << i << '\n' ;
        std::this_thread::sleep_for(std::chrono::milliseconds(10));
    }
}

int main()
{
    std::thread thread1(task1);
    std::thread thread2(task2);
    thread1.join();
    thread2.join();
    return 0;
}

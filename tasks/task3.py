def solve():
    # Ниже пишите решение задачи
    n = int(input())
    count = 0
    count += n // 100
    n = n % 100
    count += n // 20
    n = n % 20
    count += n // 10
    n = n % 10
    count += n // 5
    n = n % 5
    count += n
    print(count)

if __name__ == "__main__":
    solve()
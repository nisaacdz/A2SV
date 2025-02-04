if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    winner, runner_up = -101, -101
    for num in arr:
        if num > winner:
            runner_up = winner
            winner = num
        elif num == winner:
            pass
        elif num > runner_up:
            runner_up = num
    print(runner_up)

if __name__ == '__main__':
    N = int(input())
    items = []
    for _ in range(N):
        command = input()
        if command[:3] == "pop":
            items.pop()
        elif command[:4] == "sort":
            items.sort()
        elif command[:5] == "print":
            print(items)
        elif command[:6] == "remove":
            _, e = map(str, command.split())
            items.remove(int(e))
        elif command[:6] == "insert":
            _, i, e = map(str, command.split())
            items.insert(int(i), int(e))
        elif command[:6] == "append":
            _, e = map(str, command.split())
            items.append(int(e))
        elif command[:7] == "reverse":
            items.reverse()
        else:
            print(command)

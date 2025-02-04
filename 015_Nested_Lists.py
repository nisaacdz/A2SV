from itertools import dropwhile

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((score, name))
    students.sort()
    min_score = students[0][0]
    runner_up_score = None
    for score, name in dropwhile(lambda v: v[0] == min_score, students):
        if runner_up_score != None and runner_up_score != score:
            break
        runner_up_score = score
        print(name)

from collections import deque

count = int(input())
# process_list = [[i for i in input().split()] for j in range(count)]
# finished_list = []
finished_list = deque()

for i in range(count):
    process = input().split()

    if process[0] == 'insert':
        # finished_list.insert(0,process[1])
        finished_list.appendleft(process[1])
    elif process[0] == 'delete':
        if process[1] in finished_list:
            finished_list.remove(process[1])
    elif process[0] == 'deleteFirst':
        # finished_list.pop(0)
        finished_list.popleft()
    elif process[0] == 'deleteLast':
        # finished_list.pop(-1)
        finished_list.pop()

print(' '.join(map(str,finished_list)))

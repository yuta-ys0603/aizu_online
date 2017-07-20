count, qms = map(int, input().split())
# for 一度でいい
process_list = [[i for i in input().split()] for j in range(count)]
finished_list = []
time = 0


while len(process_list) != 0:
    # qmsよりもプロセスが長いとき
    if int(process_list[0][1]) - qms > 0:
        # qmsを引いて挿入し直す
        process_list[0][1] = int(process_list[0][1]) - qms
        process_list.append(process_list.pop(0))
        time = time + qms
    else:
        time = int(process_list[0][1]) + time
        process_list[0][1] = time
        finished_list.append(process_list.pop(0))

for i in range(count):
    print(' '.join(map(str,finished_list[i])))

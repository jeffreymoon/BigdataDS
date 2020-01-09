import sys
def selectionSort():
    num_list = [int(a) for a in sys.stdin.readline().split()]
    # num_list = [1, 5, 8, 0, 2, 4, 6, 5]

    length = len(num_list)
    for i, value in enumerate(num_list):
        if i+1 >= length:
            break
        minvalue = min(num_list[i+1:])
        minindex = (num_list[i+1:]).index(minvalue) + i + 1
        if value > minvalue:
            num_list[i], num_list[minindex] = minvalue, value
        print(num_list)
    return num_list

if __name__ == "__main__":
    selectionSort()
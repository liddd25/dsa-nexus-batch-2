if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    n_lst = list(set(arr))
    sorts = sorted(n_lst, reverse=True)
    print(sorts[1])

def main():
    t = int(input())
    for _ in range (t):
        n = int(input())
        arr = list(map(int,input().split()))
        ans = min(arr)
        print(ans)


if __name__ == '__main__':
    main()

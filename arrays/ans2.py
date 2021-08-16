######## max and min of an array ##########



def ans(arr):
    max, min = arr[0], arr[0]
    for i in arr:
        if i <= min:
            min = i
        else:
            max = i 
    print(max, min)
    # pass


if __name__ == "__main__":
    arr = [100, 2, 4, 7, 46, 32, 6, 5, 768, 86, 56, 456]
    ans(arr)
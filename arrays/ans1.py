######## Reverse an array ##########



def ans(arr):
    rev_arr = []
    for i in range(len(arr)):
        rev_arr.append(arr[len(arr)-i-1])
    
    print(rev_arr)
    
    
    # pass

if __name__ == "__main__":
    arr = [100, 2, 4, 7, 46, 32, 6, 5, 768, 86, 56, 456]
    ans(arr)
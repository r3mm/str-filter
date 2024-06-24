def str_filter(arr):
    result = []
    for string in arr:
        if len(string) <= 3:
            result.append(string)
    return result

if __name__ == '__main__':
    arr = ['Hello', '2', 'world', ':-D']
    print(str_filter(arr))
def binarySearchHelper(list, value):

    return binarySearch(list, 0, len(list) - 1, value)


def binarySearch(list, min, max, value):
    if max < min:
        return False
    mid = (max + min )//2
    if value == list[mid]:
        return True
    if value < list[mid]:
        return binarySearch(list, min, mid - 1, value)
    elif value > list[mid]:
        return binarySearch(list, mid + 1, max, value)


list = [1,2,3,4,5,6]
print(binarySearchHelper(list, 7))


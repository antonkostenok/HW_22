array = [int(x) for x in input("Введите целые числа через пробел: ").split()]

def merge_sort(arrey):
    if len(arrey) < 2:
        return arrey[:]
    else:
        middle = len(arrey) // 2
        left = merge_sort(arrey[:middle])
        right = merge_sort(arrey[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
print(merge_sort(array))
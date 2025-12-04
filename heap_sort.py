# i is the index of the array, starting from 0
# heap_size is the size of the heap, it's not
# necessarily the same as len(array),
# could be smaller but no bigger
def max_heapify(array, heap_size, i):
    if i >= heap_size:
        raise ValueError(f"index:{i} is out of bound of heap_size:{heap_size}")

    largest_i = i

    left_child = (i + 1) * 2 - 1
    right_child = left_child + 1
    if right_child >= heap_size:
        if left_child < heap_size:
            if array[left_child] > array[i]:
                largest_i = left_child
    else:
        if array[right_child] > array[left_child] >= array[i] or array[right_child] > array[i]>= array[left_child]:
            largest_i = right_child
        elif array[left_child] > array[right_child] >= array[i] or array[left_child] > array[i]>= array[right_child]:
            largest_i = left_child

    if largest_i != i:
        array[i], array[largest_i] = array[largest_i], array[i]
        max_heapify(array, heap_size, largest_i)

def build_max_heap(array):
    for i in range(len(array) // 2, -1, -1):
        max_heapify(array, len(array), i)

def heap_sort(array):
    build_max_heap(array)
    size = len(array)
    for i in range(size - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        size -= 1
        max_heapify(array, size, 0)

def test_heapify():
    array1 = [3, 6, 9]
    max_heapify(array1, 3, 2)
    assert array1 == [3, 6, 9], "op on leaf will have no effects, no error either"

    max_heapify(array1, 3, 0)
    assert array1 == [9, 6, 3], "it'll pick bigger of the children to swap"

    array2 = [3, 6, 9, 7, 8, 5, 4]
    max_heapify(array2, 7, 0)
    assert array2 == [9, 6, 5, 7, 8, 3, 4], "heapify will perform to the leaf level"

    array3 = [3, 9, 2, 7, 8, 6, 1]
    max_heapify(array3, 7, 0)
    assert array3 == [9, 8, 2, 7, 3, 6, 1], "just try the left side, notice rigt child is not heapified"

def test_build_max_heap():
    array = [3, 9, 2, 7, 8, 6, 1]
    build_max_heap(array)
    assert array == [9, 8, 6, 7, 3, 2, 1], "every sub tree is heapified"

def test_heap_sort():
    array = [3, 9, 2, 7, 8, 6, 1]
    heap_sort(array)
    assert array == [1, 2, 3, 6, 7, 8, 9], "sorted"

def test():
    test_heapify()
    test_heap_sort()

test()

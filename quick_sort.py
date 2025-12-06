# it splits A into 2 parts accoring
# to A[r], returning split point q
# where points on the left <= A[q] and right > A[q]
def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quick_sort_impl(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort_impl(A, p, q - 1)
        quick_sort_impl(A, q + 1, r)

def quick_sort(A):
    quick_sort_impl(A, 0, len(A) - 1)
 
def test():
    array1 = []
    quick_sort(array1)
    assert len(array1) == 0, "empty list can be sorted without error"

    array2 = [3, 4, 5, 6, 2]
    quick_sort(array2)
    assert array2 == [2, 3, 4, 5, 6], "odd number list can be sorted"

    array3 = [3, 1, 7, 9, 4, 5, 6, 2]
    quick_sort(array3)
    assert array3 == [1, 2, 3, 4, 5, 6, 7, 9], "even number list can be sorted"

test()

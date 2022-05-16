# int k: an integer
# int A[n]: an array of integers
# int B[n]: an array of integers
def twoArrays(k, A, B):
    # Write your code here
    a = [x for x in A]
    b = [x for x in B]
    a.sort()
    b.sort(reverse=True)
    for i in range(len(a)):
        if a[i] + b[i] < k:
            return "NO"
    return "YES"

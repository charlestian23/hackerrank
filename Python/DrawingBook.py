def pageCount(n, p):
    # Write your code here
    book_length = n
    if book_length % 2 == 0:
        book_length += 1
    front_flips = p // 2
    back_flips = (book_length - p) // 2
    return min(front_flips, back_flips)

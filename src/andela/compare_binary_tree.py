def compare(a, b):
    if a is None and b is None:
        return True
    elif a is not None and b is not None:
        return (a.val == b.val) and compare(a.left, b.left) and compare(a.right, b.right)
    else:
        return False

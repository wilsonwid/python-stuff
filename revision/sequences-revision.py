def reverse_i(seq):
    result = ()
    for i in range(len(seq)):
        result = (seq[i],) + result
    return result

def reverse_r(seq):
    if seq == ():
        return ()
    else:
        return reverse_r(seq[1:]) + (seq[0],)

def scale_seq_r(seq, factor):
    if seq == ():
        return ()
    else:
        return (seq[0] * factor, ) + scale_seq_r(seq[1:], factor)

def scale_seq_i(seq, factor):
    result = ()
    for item in seq:
        result += (item * factor)
    return result

def square_seq_r(seq):
    if seq == ():
        return ()
    else:
        return (seq[0] ** 2,) + square_seq_r(seq[1:])

def map(fn, seq):
    if seq == () or seq == []:
        return ()
    else:
        return (fn(seq[0]), ) + map(fn, seq[1:])


def scale_seq(seq, factor):
    return map(lambda x: x * factor, seq)

def count_leaves(tree):
    if tree == () or tree == []:
        return 0
    elif not isinstance(tree, tuple) and not isinstance(tree, list):
        return 1
    else:
        return count_leaves(tree[0]) + count_leaves(tree[1:])

def scale_tree(tree, factor):
    def scaler(subtree):
        if not isinstance(tree, tuple) and not isinstance(tree, list):
            return factor * subtree
        else:
            return scale_tree(subtree, factor)
    return map(scaler, tree)

print(count_leaves([3, 4, 5, [1, 2, 3]]))
import string

def get_statistics(data):
    res = {}
    for d in data.lower():
        if not d.isalpha():
            continue
        if d in res:
            res[d] += 1
        else:
            res[d] = 1
    return dict(sorted(res.items()))

def get_frequencies(data):
    dict_ = get_statistics(data)
    sorted_ = sorted(dict_.items(), key=lambda x: x[1], reverse=True)
    return sorted_


def get_words(data):
    words = data.split()
    return [x for x in words if len(x) != 0]


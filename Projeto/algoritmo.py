def contar_inversoes(arr):
    _, total = _merge_sort(arr)
    return total

def _merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    meio = len(arr) // 2
    esquerda, inv_esq = _merge_sort(arr[:meio])
    direita, inv_dir = _merge_sort(arr[meio:])
    intercalado, inv_merge = _merge(esquerda, direita)
    return intercalado, inv_esq + inv_dir + inv_merge

def _merge(e, d):
    res, inv = [], 0
    i = j = 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            res.append(e[i])
            i += 1
        else:
            res.append(d[j])
            inv += len(e) - i
            j += 1
    res.extend(e[i:])
    res.extend(d[j:])
    return res, inv
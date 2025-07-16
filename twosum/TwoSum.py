def two_sum_forca_bruta(numeros, alvo):
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] + numeros[j] == alvo:
                return [i, j]


def two_sum_hash(numeros, alvo):
    indice_por_valor = {}
    for i, valor_atual in enumerate(numeros):
        complemento = alvo - valor_atual
        if complemento in indice_por_valor:
            return [indice_por_valor[complemento], i]
        indice_por_valor[valor_atual] = i


def quicksort(arr):
    _quicksort(arr, 0, len(arr) - 1)

def _quicksort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        _quicksort(arr, left, pi - 1)
        _quicksort(arr, pi + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def two_sum_sorted(numeros, alvo):
    arr = [(num, idx) for idx, num in enumerate(numeros)]
    quicksort(arr)

    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left][0] + arr[right][0]
        if current_sum == alvo:
            return [arr[left][1], arr[right][1]]
        elif current_sum < alvo:
            left += 1
        else:
            right -= 1

    return []


if __name__ == "__main__":
    numeros = [2, 7, 11, 15]
    alvo = 9

    print("Força bruta:", two_sum_forca_bruta(numeros, alvo))  # [0, 1]
    print("Hash:", two_sum_hash(numeros, alvo))                # [0, 1]
    print("QuickSort:", two_sum_sorted(numeros, alvo))         # [0, 1]

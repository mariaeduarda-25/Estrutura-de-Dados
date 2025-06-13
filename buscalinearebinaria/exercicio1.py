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


def busca_linear(arr, alvo):
    for i in range(len(arr)):
        if arr[i] == alvo:
            return i
        if arr[i] > alvo:
            return i
    return len(arr)


def busca_binaria(arr, alvo):
    esquerda, direita = 0, len(arr) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if arr[meio] == alvo:
            return meio
        elif arr[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return esquerda

arr = [9, 4, 3, 8, 2, 7, 0, 1, 5]
alvo = 6
quicksort(arr)
print(" Vetor ordenado:", arr)
print("Busca linear:", busca_linear(arr, alvo))
print("Busca binária:", busca_binaria(arr, alvo))

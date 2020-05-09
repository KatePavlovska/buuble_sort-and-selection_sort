def bubble_sort(array, reverse=False, show_steps=False):
    """
    Сортировка пузырьком

    Parameters
    ----------
    array: массив который нужно отсортировать
    reverse: {True, False}, default 'False'
        * False:  от наименьшего до наибольшего
        * True:   от наибольшего до наименьшего
    show_steps: {True, False}, default 'False'
        * False:  не показывать сортировку пошагово
        * True:   показывать сортировку пошагово

    """

    for i in range(len(array) - 1):  # проходим по массиву N - 1 раз

        for j in range(len(array) - i - 1):  # внутренний цикл прохода

            if array[j] > array[j + 1] if not reverse else array[j] < array[j + 1]:
                # если значение текущего элемента больше(меньше) следующего, то
                # меняем эти элементы местами
                array[j], array[j + 1] = array[j + 1], array[j]

                # выводим на экран распакованый массив с таб-разделителем
                if show_steps:
                    print(*array, sep='\t', end='\n' * 2)


# Example
arr = [9, 3, 7, 5, 1]
print('Сортировка пузырьком от min до max:')
bubble_sort(arr, show_steps=True)

print('Сортировка пузырьком от max до min:')            # тут уже массив отсортирован по возрастанию
bubble_sort(arr, reverse=True, show_steps=True)

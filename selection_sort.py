def selection_sort(array, reverse=False, show_steps=False):
    """
    Сортировка выбором

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

    for i, _ in enumerate(array[:-1]):  # итерируемся по индексам до предпоследнего элемента массива
        # так как при последнем элементе массив уже будет отсортирован

        m = i  # инициализируем индекс минимального(максимального) (от i и до конца списка)
        # элемента массива

        for j in range(i + 1, len(array)):  # итерируемся по всех следующих индексах массива

            if array[j] < array[m] if not reverse else array[j] > array[m]:
                # если значение следующего элемента меньше(больше) текущего, то
                # индекс минимального(максимального) (от i и до конца списка)
                # элемента массива становится индексом этого элеманта

                m = j

        array[i], array[m] = array[m], array[i]  # меняем текущий элемент с минимальным(максимальным)
        # который мы нашли

        if show_steps:
            print(*array, sep='\t', end='\n' * 2)  # выводим на экран распакованый массив с таб-разделителем


# Example
arr = [9, 3, 7, 5, 1]
print('Сортировка выбором от min до max:')
selection_sort(arr, show_steps=True)

print('Сортировка выбором от max до min:')            # тут уже массив отсортирован по возрастанию
selection_sort(arr, reverse=True, show_steps=True)

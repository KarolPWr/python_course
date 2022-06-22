from random import randint


def print_elements(elements):
    print(f'List len: {len(elements)}')
    for e in elements:
        print(f'* {e}')


def sum_elements(elements):
    """Return 0 if list is empty"""
    sum=0
    for element in elements:
        sum = sum+element
    return sum


def min_element(elements):
    """Return None if list is empty"""
    if not elements:
        return None
    min = elements[0]
    for element in elements:
        if element < min:
            min = element
    return min



def avg_of_elements(elements):
    avg = sum(elements) / len(elements)
    return avg



if __name__ == '__main__':
    numbers = [randint(-5, 5) for _ in range(4)]
    print_elements(numbers)

    sum_val = sum_elements(numbers)
    print(f'SUM: {sum_val}')
    assert sum_val == sum(numbers)

    min_val = min_element(numbers)
    print(f'MIN: {min_val}')
    assert min_val == min(numbers)

    avg_val = avg_of_elements(numbers)
    print(f'AVG: {avg_val}')
    assert avg_val == sum(numbers) / len(numbers)

    # test empty sequences
    assert sum_elements([]) == 0
    assert min_element([]) is None

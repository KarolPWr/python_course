from typing import Generator


def identify_generator(elements) -> Generator:
    yield from elements
    # for e in elements: # equivalent to above statement
    #     yield e


def multiply_generator(elements, factor=1) -> Generator:
    """Return all values multiplied by factor"""
    # yield from elements*factor
    for e in elements:
        yield e*factor



def custom_chain(*lists) -> Generator:
    """Merge all lists form tuple to one long generator"""
    for list in lists:
        for element in list:
            yield element



def limit(l, *, n) -> Generator:
    """Return first n elements from l"""
    # works normally but next function in main passes generator here :(
    # for element in l[0:n]:
    #     yield element
    for el in l:
        yield el
        n-=1
        if n==0:
            break


def cycle(l) -> Generator:
    """Generate infinite series out of given list"""
    # for index, element in enumerate(l):
    #     yield l[index%len(l)]
    while True:
        for e in l:
            yield e


if __name__ == '__main__':
    short_list = [1, 2, 10]

    # id_gen = identify_generator(short_list)
    # assert list(id_gen) == short_list
    #
    # # Exercise1: make it works
    # multiplied_gen = multiply_generator(short_list, 10)
    # assert list(multiplied_gen) == [10, 20, 100]
    # assert type(multiplied_gen) is type(id_gen)  # make sure you've created generator, not just returned list
    #
    # # Exercise2: make it works
    # chained = custom_chain(short_list, [20], [30, 42])
    # assert list(chained) == [1, 2, 10, 20, 30, 42]
    # assert type(chained) is type(id_gen)  # make sure you've created generator, not just returned list
    #
    # # Exercise3: make it works
    # limited = limit(short_list, n=2)
    # assert list(limited) == [1, 2]
    # assert type(limited) is type(id_gen)  # make sure you've created generator, not just returned list

    # Exercise4: make it works
    c = cycle(short_list)
    list(c)
    # cycled = list(limit(cycle(short_list), n=900))
    # assert cycled[:3] == [1, 2, 10]
    # assert cycled[-3:] == [1, 2, 10]
    # assert len(cycled) == 900

import numpy as np 


def generate_random_data(size):
    # """""" Write docstring and return type for example:
    # def generate_random_data(size) -> np.array:
    return np.random.randint(1, 1000, size)


def generate_sorted_data(size):
    return np.sort(generate_random_data(size))


def generate_reverse_sorted_data(size):
    return np.sort(generate_random_data(size))[::-1]


# TODO: Learn about it
def generate_nearly_sorted_data(size):
    arr = np.sort(generate_random_data(size))
    
    # swap 5% elements
    nSwaps = max(1, size // 20)
    
    for _ in range (nSwaps):
        i = np.random.randint(0, size)
        j = np.random.randint(0, size)
        
        arr[i], arr[j] = arr[j], arr[i]
        
    return arr


def generate_all_inputs(size):
    return{
        "Random": generate_random_data(size),
        "Sorted": generate_sorted_data(size),
        "Reverse": generate_reverse_sorted_data(size),
        "Nearly Sorted": generate_nearly_sorted_data(size)
    }
from typing import Callable
from random import sample, randint, random

def verify_sort_func(func: Callable[[list], list],
                     generated_list_n: int=100,
                     min_size_of_list: int=3,
                     max_size_of_list: int=12,
                     min_n: int=-50,
                     max_n: int=50,
                     max_print_errors: int=3,
                     duplicate_probability: float=0.5,
                     max_duplicates_added: int=2,
                     ) -> None:
    """
    Args:
        func (function): A sorting function to test.
        generated_list_n (int, optional): Defaults to 5.
        min_size_of_list (int, optional): Defaults to 5.
        max_size_of_list (int, optional): Defaults to 12.
        min_n (int, optional): Defaults to -50.
        max_n (int, optional): Defaults to 50.
        max_print_errors (int, optional): Defaults to 3.
        duplicate_probability: (float, optional): Defaults to 0.5. So 50% of chance.
        The lower the number, the lower the probability is. 0.1 is only 10% of chance.
        max_duplicates_added (int, optional): Defaults to 3.
        

    Returns:
        None: Program prints a message  if there are no errors.
              Elsewhere it prints out what the errors are.
    """
    
    # Generate n lists and test them
    errors_n = 0
    for i in range(generated_list_n):
        arr = sample(range(min_n, max_n), randint(min_size_of_list, max_size_of_list))
        if random() < duplicate_probability: # Sometimes we want to add duplicated numbers
            for _ in range(randint(0, max_duplicates_added)): # But just a few
                arr.insert(randint(0, len(arr)-1), # Insert at any position
                           arr[randint(0, len(arr)-1)]) # Any other number of the list
        sorted_list = sorted(arr.copy())
        result_list = func(arr.copy())
        if sorted_list != result_list:
            errors_n += 1
            if errors_n <= max_print_errors:
                print(f"Error for loop n°{i}. The list: \n{arr} should output\n{sorted_list}, but instead outputs\n{result_list}\n")
    
    # Final message
    if not errors_n: print(f"""Number of successes: {generated_list_n}/{generated_list_n}
                           Job done! Congratulations! :)""")
    else: print(f"""Number of errors: {errors_n}/{generated_list_n}.
    \nNote : Only the first {max_print_errors} errors have been printed.""")
    
def wrong_selection_sort(arr: list) -> list:
    """This function is wrong about half the time.
       Useful to test the function "verify_sort_func".

    Args:
        arr (list): Input List.

    Returns:
        list: Output list
    """
    i = 0
    while i < len(arr):
        n_min_index = arr[i:].index(min(arr[i:]))
        if n_min_index != i:
            arr[i], arr[n_min_index + i] = arr[n_min_index + i], arr[i]
        i += 1
    return arr
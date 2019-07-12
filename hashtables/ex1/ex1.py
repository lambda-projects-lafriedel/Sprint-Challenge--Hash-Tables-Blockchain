#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length > 1:
        # insert each item to the hash table
        for i in range(length):
            hash_table_insert(ht, weights[i], i)
        
        for i in range(length):
            # subtract length - weights[i]
            diff = limit - weights[i]
            # attempt to retrieve item from hash_table with difference as key
            match_index = hash_table_retrieve(ht, diff)

            # if exists, the value is returned which is the list index
            if match_index is not None:
                # send indices to print_answer in correct order
                if match_index >= i:
                    return print_answer([str(match_index), str(i)])
                else:
                    return print_answer([str(i), str(match_index)])
    else:
        return print_answer(None)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
        return [int(answer[0]), int(answer[1])]
    else:
        print("None")
        return None

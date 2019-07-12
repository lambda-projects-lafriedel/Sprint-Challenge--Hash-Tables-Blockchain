#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    # Example input: get_indices_of_item_weights([4,6,10,15,16], 5, 21)
    # Example output: [3,1] (Indices of the weights 15 and 6 -- which equals limit of 21)
    # Find two items whose sum of weights equals the param 'limit' and return their indices

    # Higher valued index from weights list should be placed in index 0 and lower valued index from weights list placed in index 1
    # Return a call to print_answer with the two indices
    """

    # for each item in weights array, insert it into the hash table. key = value from array, value = its index from weights array
    if length > 1:

        for i in range(len(weights)):
            # (4, 0) (6,1) (10,2) (15,3) (16,4)
            hash_table_insert(ht, weights[i], i)
            # subtract length - weights[i] (21 - 4 = 17)
        
        for i in range(len(weights)):
            diff = limit - weights[i]
            # attempt to retrieve item from hash_table with key 17
            match_index = hash_table_retrieve(ht, diff)

            # if exists, the value is returned which is the list index
            if match_index is not None:
                print("COUPLE", weights[match_index], weights[i])
                if match_index >= i:
                    return print_answer([str(match_index), str(i)])
                else:
                    return print_answer([str(i), str(match_index)])
    else:
        return print_answer(None)


def print_answer(answer):
    print("ANSWER", answer)
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
        return [int(answer[0]), int(answer[1])]
    else:
        print("None inside print answer")

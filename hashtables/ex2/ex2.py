#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        # insert each ticket into the hash table
        hash_table_insert(ht, ticket.source, ticket.destination)

    # retrieve the starting ticket, where the key is NONE
    curr_ticket = hash_table_retrieve(ht, "NONE")
    print("CURR TICKET", curr_ticket)

    # add the starting ticket's "destination" (value) as the starting airport
    route[0] = curr_ticket
    i = 1
    # while current ticket destination is not None
    while route[-1] is not "NONE":
        next_ticket = hash_table_retrieve(ht, curr_ticket)
        print("NEXT TICKET", next_ticket)
        # next_ticket should be PDX, DCA
        route[i] = next_ticket
        print("ROUTE", route)
        # retrieve the next ticket that has the key of the current ticket as its value
        curr_ticket = next_ticket
        i += 1

    return route

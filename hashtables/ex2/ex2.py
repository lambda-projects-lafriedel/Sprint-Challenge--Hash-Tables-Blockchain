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

    for ticket in tickets:
        # insert each ticket into the hash table
        hash_table_insert(ht, ticket.source, ticket.destination)

    # retrieve the starting ticket
    curr_ticket = hash_table_retrieve(ht, "NONE")

    # add the starting ticket's destination as the starting airport
    route[0] = curr_ticket
    # set an index for the route list
    i = 1

    # while current ticket destination is not "NONE"
    while route[-1] is not "NONE":
        # retrieve the next ticket
        next_ticket = hash_table_retrieve(ht, curr_ticket)
        # set the next index of the route as the ticket's value
        route[i] = next_ticket
        print("ROUTE", route)
        # set current ticket as the ticket inside loop
        curr_ticket = next_ticket
        # increase the index by 1
        i += 1

    return route

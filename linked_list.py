#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" Import this module to create a linked list. """

from linked_list_errors import *


class Node:
    """ This class allows us to create a Node which contains any datas as any
    other Python collection to constitute the linked list. """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """ This class allows us to create a simple Linked list: datas refers only
    datas after them and not before. """

    def __init__(self):
        self.start_node = None
        self.count = 0

    def parse_list(self, nb=0):
        """ To parse the linked list and print all elements.
        If a linked list is nested in the parsing one it parse it
        of course. """
        space = '    ' * nb #+ '|'
        if self.start_node == None:
            raise ParsingError
        else:
            node = self.start_node
            while node != None:
                if type(node.data) != LinkedList:
                    print(space + str(node.data))
                else:
                    node.data.parse_list(nb=nb+1)
                node = node.next

    def len(self) -> (int):
        """ Return the number of elements in the list. """

        return self.count

    def is_in_list(self, data) -> (bool):
        """ To know if the element is in list.
        Return True or False. """

        node = self.start_node
        while node != None:
            if node.data == data:
                return True
            node = node.next
        return False

    def add(self, data):
        """ Insert the new data in the list (by default at the end). """

        new_node = Node(data)
        if self.start_node == None:
            self.start_node = new_node
        else:
            node = self.start_node
            while node.next != None:
                node = node.next
            node.next = new_node
        self.count += 1

    def add_at_start(self, data):
        """ Insert the new data at the begining of the linked list. """

        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node
        self.count += 1

    def add_after_x(self, x: Node, data):
        """ Insert the new data after data x. Return True in case of success
        or raise ParsingError if the list is empty or UnfoundElementError
        if the data is not found. """

        if self.start_node is None:
            raise ParsingError

        node = self.start_node
        while node != None:
            if node.data == x:
                break
            node = node.next

        if node == None:
            raise UnfoundElementError
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.count += 1
            return True

    def add_before_x(self, x: Node, data):
        """ Insert the new data before data x. Return True in case of success
        or raise ParsingError if the list is empty or UnfoundElementError
        if the data is not found. """

        if self.start_node is None:
            raise ParsingError

        if x == self.start_node.data:
            return self.add_at_start(data)

        node = self.start_node
        while node.next != None:
            if node.next.data == x:
                break
            node = node.next

        if node.next is None:
            raise UnfoundElementError
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.count += 1
            return True

    def add_at(self, at: int, data) -> (bool):
        """ Insert the new data at data's index x and return True
        in case of success or raise IndexError if the index is out of
        the list range. """

        if at == 0:
            return self.add_at_start(data)
        i = 1
        node = self.start_node
        while i < at and node != None:
            node = node.next
            i += 1
        if node == None:
            raise IndexError
        else:
            new_node = Node(data)
            new_node.next = node.next
            node.next = new_node
            self.count += 1
            return True

    def update_x(self, x, new_data) -> (bool):
        """ Update or replace data x and return True in case of success or
        raise UnfoundElementError if the element x wasn't found. """

        node = self.start_node
        while node != None:
            if node.data == x:
                break
            node = node.next

        if node == None:
            raise UnfoundElementError
        else:
            node.data = new_data
            return True

    def del_x(self, x: Node) -> (bool):
        """ Delete data x and return True in case of success
        or raise UnfoundElementError if the element x wasn't found. """

        if self.start_node.data == x:
            self.start_node = self.start_node.next
            self.count -= 1
            return True
        else:
            node = self.start_node
            while node != None:
                if node.data == x:
                    break
                node = node.next

            if node == None:
                raise UnfoundElementError
            else:
                previous_node = self.start_node
                while previous_node.next != node:
                    previous_node = previous_node.next
                previous_node.next = node.next
                self.count -= 1
                return True

    def pop(self, x: Node):
        """ Delete data x and return it in case of success or
        raise UnfoundElementError if the element x wasn't found. """

        if self.del_x(x):
            return x

    def del_first(self) -> (bool):
        """ This methode allows us to delete the first element of the list.
        It return True in case of success or raise ParsingError
        if the list is empty. """

        if self.start_node == None:
            raise ParsingError
        else:
            if self.start_node.next == None:
                self.start_node = None
            else:
                self.start_node = self.start_node.next
            self.count -= 1
            return True

    def del_last(self) -> (bool):
        """ This method allows us to delete the last element of the list.
        It return True in case of success or raise ParsingError
        if the list is empty. """

        if self.start_node == None:
            raise ParsingError
        else:
            if self.start_node.next == None:
                self.start_node = None
            else:
                previous_last_node = self.start_node
                last_node = self.start_node
                while last_node.next != None:
                    previous_last_node = last_node
                    last_node = last_node.next
                previous_last_node.next = None
                last_node = None
            self.count -= 1
            return True

def main():

    lklist = LinkedList()
    print("\n########## create the LinkedListed list and parse it")
    print(lklist.len())

    print("\n########## creation of the first element")
    first = {'first': True}
    print(first)
    print("\n########## add element at the start of the LinkedListed list and parse it")
    lklist.add(first)
    lklist.parse_list()
    print(lklist.len())

    print("\n########## creation of the second element")
    second = 'second'
    print(second)
    print("\n########## add element at end of the LinkedListed list and parse it")
    lklist.add(second)
    lklist.parse_list()
    print(lklist.len())

    print("\n########## creation of the third element")
    third = 3
    print(third)
    print("\n########## add element at the start of the LinkedListed list and parse it")
    lklist.add_at_start(third)
    lklist.parse_list()
    print(lklist.len())

    print("\n########## creation of the fourth")
    fourth = ['4', 4]
    print(fourth)
    print("\n########## insert fourth after the vaeiable 'third' and parse the list")
    lklist.add_after_x(third, fourth)
    lklist.parse_list()
    print(lklist.len())

    print("\n########## creation of the fifth element")
    fifth = 'This is a string!'
    print(fifth)
    print("\n########## insert fifth after the third element and parse the list")
    lklist.add_before_x(second, fifth)
    lklist.parse_list()
    print(lklist.len())

    print("\n########## delete this fifth element")
    lklist.del_x(3)
    lklist.parse_list()
    print(lklist.len())

    print("\n########## update the variable 'second'")
    lklist.update_x(second, "last one")
    lklist.parse_list()

    print("\n########## is element in list ?")
    print(lklist.is_in_list({'first': True}))

    print("\n########## del first element")
    lklist.del_first()
    lklist.parse_list()
    print(lklist.len())

    print("\n########## lets try to put a linked list in our linked list")
    lklist_2 = LinkedList()
    lklist_2.add('premier')
    lklist_2.add('deuxieme')
    lklist_3 = LinkedList()
    lklist_3.add('imbriquée')
    lklist_2.add(lklist_3)
    lklist_2.add('another data')
    lklist_2.add([1,2,3,])
    lklist.add(lklist_2)
    lklist.add({'hero': "Mc-Fly"})
    lklist.parse_list()

if __name__ == '__main__':
    print("\nModule Launch\n")
    main()
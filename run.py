from data_structure import Stack, LinkedList


if __name__ == '__main__':
    print('----------------------------------------')
    print('Stack')
    print('----------------------------------------')

    stack = Stack()

    print('is empty:' + str(stack.is_empty))
    print('stack size:' + str(stack.size))

    stack.push('a')
    stack.push('b')
    stack.push('c')

    print('stack pushed a, b, c')

    print('is empty:' + str(stack.is_empty))
    print('stack size:' + str(stack.size))

    print('Pop:', stack.pop())
    print('Pop:', stack.pop())
    print('Pop:', stack.pop())

    print('is empty:' + str(stack.is_empty))
    print('stack size:' + str(stack.size))

    print()
    print('----------------------------------------')
    print('Linked List')
    print('----------------------------------------')

    linked_list = LinkedList()

    print('size:' + str(linked_list.size))

    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.insert(30)

    print('size:' + str(linked_list.size))

    print(str(linked_list.search(30).get()))
    print(str(linked_list.search(30).get_next_node().get()))

    linked_list.delete(20)

    print('deleted: 20')
    print('size:' + str(linked_list.size))

    linked_list.insert('A')

    print('inserted: "A"')
    print('size:' + str(linked_list.size))

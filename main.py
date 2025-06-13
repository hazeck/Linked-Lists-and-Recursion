from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

   
    ll = LinkedList()


    ll.insert_at_front(10)
    ll.insert_at_front(20)
    ll.insert_at_end(5)
    ll.insert_at_end(1)


    print("Original list:")
    ll.display()


    total = ll.recursive_sum()
    print("Sum of all node data:", total)


    target = 5
    found = ll.recursive_search(target)
    print(f"Search for {target}:", found)

    print("Reversing list...")
    ll.recursive_reverse()
    ll.display()
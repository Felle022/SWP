import LinkedList as myLinkedList


#Erstellen der ersten Knoten
node1=myLinkedList.Node(1)
node2=myLinkedList.Node(2)
node3=myLinkedList.Node(3)
node1.next=node2
node2.next=node3
#Linkedlist initialisiern --> Head ist Anfangsknoten
linked_list=myLinkedList.LinkedList(node1)

node4=myLinkedList.Node(4)
linked_list.append_to_linkedList(node4)
print(linked_list.get_length())
linked_list.print_linkedList()


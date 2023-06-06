#include "lists.h"
/**
  * insert_node - Inserts a number into a sorted singly linked list
  * @head: The head of the sorted singly linked list
  * @number: The number to insert in the singly linked list
  *
  * Return: The singly linked list with the new number added
*/
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *curr, *tmp;
    listint_t *new_node = malloc(sizeof(listint_t));

    if (!new_node)
        return (NULL);
    new_node->n = number;

    if (!*head)
    {
        new_node->next = NULL;
        *head = new_node;
        return (new_node);
    }
    if ((*head)->n >= number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }
    curr = *head;
    while (curr->next)
    {
        if (curr->next->n >= number)
        {
            tmp = curr->next;
            curr->next = new_node;
            new_node->next = tmp;
            return (new_node);
        }
        curr = curr->next;
    }
    curr->next = new_node;
    new_node->next = NULL;
    return (new_node);
}

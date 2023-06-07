#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *node = *head;
    listint_t *new = malloc(sizeof(listint_t));

    if (new == NULL)
        return NULL;

    new->n = number;
    new->next = NULL;

    if (node == NULL || node->n >= number)
    {
        new->next = node;
        *head = new;
        return new;
    }

    while (node->next && node->next->n < number)
        node = node->next;

    new->next = node->next;
    node->next = new;

    return new;
}

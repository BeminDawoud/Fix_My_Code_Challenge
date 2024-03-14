#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 *
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *previous, *current;
	unsigned int count = 0;

	if (head == NULL || *head == NULL)
		return (-1);

	previous = *head;
	current = *head;

	if (index == 0)
	{
		*head = current->next;
		(*head)->prev = NULL;
		free(current);
		return (1);
	}
	while (current != NULL && count < index)
	{
		previous = current;
		current = current->next;
		count++;
	}

	if (current == NULL)
		return (-1);
	previous->next = current->next;
	if (current->next != NULL)
		current->next->prev = previous;
	free(current);
	return (1);
}

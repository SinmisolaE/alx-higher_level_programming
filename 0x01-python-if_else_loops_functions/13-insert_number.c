#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	curr = *head;
	new->n = number;

	if (*head == NULL || (number < (*head)->n))
	{
		new->next = *head;
		*head = new;
		return (*head);
	}

	while ((curr->next) && (number > curr->next->n))
	{
		curr = curr->next;
	}

	new->next = curr->next;
	curr->next = new;

	return (curr->next);
}

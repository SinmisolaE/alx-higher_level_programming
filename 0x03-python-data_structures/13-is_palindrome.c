#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if palindrome
 * @head: the list
 * Return: 1 if found else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *front = *head;
	listint_t *back = *head;
	listint_t *pal;
	listint_t *tmp = *head;

	if (!(*head) || !((*head)->next))
		return (1);
	while (1)
	{
		front = front->next->next;
		if (!front)
		{
			pal = back->next;
			break;
		}
		back = back->next;
	}
	reverse_list(&pal);
	while(tmp && pal)
	{
		if (tmp->n == pal->n)
		{
			tmp = tmp->next;
			pal = pal->next;
		}
		else
			return (0);
	}
	if (!tmp && !pal)
		return (1);
	return (0);
}

/**
 * reverse_list - reverses list
 * @head: the list
 * Return: nain
 */
void reverse_list(listint_t **head)
{
	listint_t *current = *head;
	listint_t *prev = NULL;
	listint_t *next;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

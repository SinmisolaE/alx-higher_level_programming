#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks for cycle in list
 * @list: the list
 * Return: 1 if cycle present. else o
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	fast = list;
	slow = list;

	while (fast && fast->next)
	{
		fast = (fast->next)->next;
		slow = slow->next;

		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);
}

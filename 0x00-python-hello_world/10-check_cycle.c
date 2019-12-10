#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: pointer of the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *bk, *fw;

	if (list == NULL)
		return (0);

	bk = list;
	fw = list;

	while (bk && fw && fw->next)
	{
		bk = bk->next;
		fw = fw->next->next;

		if (bk == fw)
			return (1);
	}

	return (0);
}

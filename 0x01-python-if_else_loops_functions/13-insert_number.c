#include "lists.h"

/**
 * insert_node - Adds a new node at the end of a listint_t list
 * @head: Pointer of the first node
 * @number: Number to insert
 * Return: The address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *tmp = NULL;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	tmp = *head;

	while (tmp->next)
	{
		if (number >= tmp->n && number < tmp->next->n)
		{
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	if (number >= tmp->n)
		tmp->next = new;
	else
	{
		new->next = *head;
		*head = new;
	}

	return (new);
}

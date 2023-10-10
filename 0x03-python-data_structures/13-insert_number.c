#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: A pointer to the address of the head of the list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - the address of the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp = *head, *prev = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (temp != NULL && temp->n < number)
	{
		prev = temp;
		temp = temp->next;
	}

	prev->next = new_node;
	new_node->next = temp;

	return (new_node);
}

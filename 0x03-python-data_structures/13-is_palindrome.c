#include "lists.h"
#include <stdlib.h>

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 * Return: pointer to the head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *current = *head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if not palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *rev;

	if (!*head || !(*head)->next)
		return (1);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast)
		slow = slow->next;

	rev = reverse_list(&slow);

	while (rev && temp)
	{
		if (rev->n != temp->n)
			return (0);
		rev = rev->next;
		temp = temp->next;
	}

	return (1);
}

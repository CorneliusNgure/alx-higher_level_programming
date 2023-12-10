#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int is_palindrome = 1;

	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL, *mid = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	mid = slow;
	prev_slow->next = NULL;
	reverse_list(&mid);

	while (*head != NULL && mid != NULL)
	{
		if ((*head)->n != mid->n)
		{
			is_palindrome = 0;
			break;
		}

		*head = (*head)->next;
		mid = mid->next;
	}

	reverse_list(&mid);
	prev_slow->next = mid;

	return (is_palindrome);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to pointer to the head of the list
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

#include "main.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/**
 * _strncpy - copies a string.
 * @dest: destination.
 * @src: source.
 * @n: int.
 *
 * Return: string.
 */

char *_strncpy(char *dest, char *src, int n)
{
	return (strncpy(dest, src, n));
}

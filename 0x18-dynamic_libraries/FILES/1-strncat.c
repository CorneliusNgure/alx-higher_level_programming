#include "main.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/**
 * _strncat - concatenates the string.
 * @dest: destination
 * @src: source.
 * @n: int.
 *
 * Return: the string.
 */

char *_strncat(char *dest, char *src, int n)
{
	return (strncat(dest, src, n));
}

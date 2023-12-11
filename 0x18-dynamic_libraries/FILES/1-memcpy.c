#include "main.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/**
 * _memcpy - copies memory.
 * @dest: destination.
 * @src: source.
 * @n: the int.
 *
 * Return: the memory
 */

char *_memcpy(char *dest, char *src, unsigned int n)
{
	return (memcpy(dest, src, n));
}

#include "main.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/**
 * _strchr - string char.
 * @s: the string
 * @c: the char
 *
 * Return: string char.
 */

char *_strchr(char *s, char c)
{
	return (strchr(s, c));
}

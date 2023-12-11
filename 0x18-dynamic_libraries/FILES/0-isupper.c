#include "main.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/**
 * _isupper - checks for uppercase letters.
 * @c: int
 *
 * Return: the string.
 */

int _isupper(int c)
{
	return (c >= 'A' && c <= 'Z');
}

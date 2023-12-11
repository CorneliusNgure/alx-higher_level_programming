#include "main.h"
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/**
 * _islower - checks for the lowercase chars.
 * @c: the char to be checked.
 *
 * Return: the char checked.
 */

int _islower(int c)
{
	return (c >= 'a' && c <= 'z');
}


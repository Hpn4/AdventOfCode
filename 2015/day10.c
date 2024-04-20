#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char inp[] = "1113122113";

	char *buff = malloc(1024 * 1024 * 20); // 20MB
	char *buff1 = malloc(1024 * 1025 * 20); // 20MB

	memmove(buff, inp, strlen(inp));

	char *src = buff;
	char *dst = buff1;
	for (int i = 0; i < 50; ++i)
	{
		char prev = src[0];
		int counter = 0;

		size_t src_i = 0;
		size_t dst_i = 0;
		while (src[src_i])
		{
			if (src[src_i] == prev)
				++counter;
			else
			{
				dst[dst_i] = counter + '0';
				dst[dst_i + 1] = prev;
				dst_i += 2;

				counter = 1;
				prev = src[src_i];
			}

			++src_i;
		}

		dst[dst_i] = counter + '0';
		dst[dst_i + 1] = prev;
		dst[dst_i + 2] = '\0';
		dst_i += 3;

		if (i == 39)
			printf("Part1: %lu\n", strlen(dst));
		else if (i == 49)
			printf("Part2: %lu\n", strlen(dst));

		// Swap
		char *tmp = dst;
		dst = src;
		src = tmp;
	}

	return 0;
}
/*
функция формирует "решето" простых чисел
*/
#include"calculate_primes.h"
#include <stdio.h>
#include <stdlib.h>
void calculate_primes(int primes[], int n)
{
    primes[0] = primes[1] = 0;

    // заполнение массива еденицамм
    for (int i = 2; i < n; i++)
		primes[i] = 1; 

    for (long i = 2; i < n; i++)             
		if (primes[i] != 0) // проверка: является ли число простым
			// находим числа, делителем которых является данное
	    	for (int j = i + 1; j < n; j++)
				if (j % i == 0)
		      		primes[j] = 0;
}


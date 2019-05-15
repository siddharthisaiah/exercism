<?php


function sumOfMultiples($limit, $numbers) {

    $sum = 0;

    for ($i = 1; $i < $limit; $i++)
    {
        $sum += divisible_by_any($i, $numbers);
    }
    return $sum;
}


function divisible_by_any($number, $divisors)
{
    foreach ($divisors as $n)
    {
        try
        {
            if ($number % $n == 0) {
                return $number;
            }
        }
        catch (DivisionByZeroError $e)
        {
            return 0;
        }
    }
}

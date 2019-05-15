<?php


/**
 * Check whether a year is leap or not.
 *
 * A year is a leapyear if it is 
 *
 * - evenly divisible by 400
 *
 * OR if it is 
 *
 * - evenly divisible by 4 
 * AND  
 * - not evenly divisible by 100
 * 
 * @param  int      $year
 * @return boolean  True if leap year, False otherwise
 */
function isLeap($year)
{
    if ($year % 400 == 0) {
        return true;
    } else {
        return ($year % 4 == 0) && ($year % 100 != 0);
    }
}

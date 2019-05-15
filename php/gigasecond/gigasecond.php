<?php


/**
 * Add 1 Gigasecond to a DateTime object
 * 1 Gigasecond = 10^9 seconds
 * 
 * @param  DateTime $given_date
 * @return DateTime             The date and time 1 gigasecond later
 */
function from($given_date) {
    $date = clone $given_date;
    
    $gigasecond = new DateInterval('PT1000000000S');
    $date->add($gigasecond);

    return $date;
}




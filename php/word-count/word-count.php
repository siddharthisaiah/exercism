<?php

function wordCount($string)
{
    $string = strtolower($string);
    $string = preg_replace("/[^a-z0-9]+/", " ", $string); // keep only letters and numbers
    $string = trim($string);

    $string_array = explode(" ", $string);

    return array_count_values($string_array);
}


// function wordCount($phrase)
// {
// 	$words = str_word_count(strtolower($phrase), 1, '0123456789');
// 	return array_count_values($words);
// }

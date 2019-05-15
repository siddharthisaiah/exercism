<?php

function detectAnagrams($needle, $haystack)
{
    $sublist = [];

    foreach ($haystack as $straw)
    {
        if (strtolower($needle) != strtolower($straw)) {
            $anagram = is_anagram($needle, $straw);

            if ($anagram)
            {
                if (!in_array(strtolower($straw), $sublist)) {
                    array_push($sublist, $straw);
                }
            }
        }
        
    }

    return $sublist;
}

function is_anagram($word, $test)
{
    $word_ar = str_split(strtolower($word));
    sort($word_ar);
    $test_ar = str_split(strtolower($test));

    sort($test_ar);

    return $word_ar == $test_ar;
}



// $find = 'ant';
// $sublist = ['tan', 'stand', 'at'];

// $ans = detectAnagrams($find, $sublist);

// print_r($ans);

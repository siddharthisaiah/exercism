<?php

function nucleotideCount($dna_strand)
{
    $dna_strand = str_split($dna_strand);
    $count = array_count_values($dna_strand);
    $a = array(
        'a' => (array_key_exists('A', $count) ? $count['A'] : 0 ), 
        'c' => (array_key_exists('C', $count) ? $count['C'] : 0 ),
        't' => (array_key_exists('T', $count) ? $count['T'] : 0 ),
        'g' => (array_key_exists('G', $count) ? $count['G'] : 0 )
    );

    return $a;
}


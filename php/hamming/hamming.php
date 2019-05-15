<?php


/**
 * Given an array with two nucleotides, check if they are different
 *
 * @param  array   $nucleodes an array containing 2 nucleotides
 * @return boolean            True if both nucleotides are different, False otherwise
 */
function are_different_nucleode($nucleodes) {
    return ($nucleodes[0] != $nucleodes[1]);
}

/**
 * Return the hamming distance of 2 DNA strands
 * Assume: the DNA strands are of equal length
 *
 * @param  String $a DNA strand
 * @param  String $b DNA strand
 * @return int       the hamming distance
 */
function distance($a, $b)
{
    if (strlen($a) != strlen($b)) {
        throw new InvalidArgumentException("DNA strands must be of equal length.");
    }

    $zipped_strands = array_map(null, str_split($a), str_split($b)); // https://stackoverflow.com/questions/2815162/is-there-a-php-function-like-pythons-zip
    $mutations = array_filter($zipped_strands, "are_different_nucleode");
    return count($mutations);
}

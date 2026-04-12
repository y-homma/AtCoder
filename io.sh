#!/bin/bash
input="in.txt"
output="out.txt"

while getopts "f:i:o" opt; do
    case $opt in
        f) file=$OPTARG ;;
        i) input=$OPTARG ;;
        o) output=$OPTARG ;;
    esac
done

$file < $input > $output

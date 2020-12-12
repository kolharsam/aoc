#!/bin/bash

# helper script to fetch Advent of Code input files
# this fetches the input and places it in the pwd

current_dir=$PWD
current_cookie=${AOC_COOKIE}

y_flag=''
d_flag=''

print_usage() {
    printf "Usage:\n\t-y YEAR\n\t-d DAY\n\n\tNOTE: Save the \"session\" cookie as AOC_COOKIE in your environment\n"
}

year=$(date +'%Y')
day=$(date +'%d')

while getopts 'y:d:' flag;do
    case "${flag}" in
        y) y_flag="${OPTARG}" ;;
        d) d_flag="${OPTARG}" ;;
        *) print_usage
           exit 1 ;;
    esac
done

# if the flags are empty then, I use today's datea and year
if [[ -z $y_flag ]]
then
    y_flag="$year"
fi

if [[ -z $d_flag ]]
then
    d_flag="$day"
fi

echo $y_flag
echo $d_flag

# make the curl request
curl -XGET -H "Cookie: session=${AOC_COOKIE}" "https://adventofcode.com/${y_flag}/day/${d_flag}/input" -o "${current_dir}/${d_flag}.in"

echo "Done! Fetched day ${d_flag} input."

# Read from the file words.txt and output the word frequency list to stdout.
grep -o '[^ ]*' words.txt | sort | uniq -c | sort -rn | awk '{print $2" "$1}'

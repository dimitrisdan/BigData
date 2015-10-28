# 1-1
tr -c '[:alnum:]' '[\n*]' < test.txt | sort | uniq -c | sort -nr | head  -10

# 1-2
grep -v '[0-9]\{5\}$' cars.txt >> filtered_cars.tx

# 1-3
tr -c '[:alnum:]' '[\n*]' < shakespeare.txt | sort | uniq >> tem
comm -23 <(tr 'a-z' 'A-Z' < temp|sort|uniq) <(tr 'a-z' 'A-Z'< dict|sort|uniq)| wc -l
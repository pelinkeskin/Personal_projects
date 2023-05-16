#! /bin/bash
database=$1
table=$2
tuple=$3
if [ $# -ne 3 ];then
echo "Error:parameters problem" >&2
exit 1
fi
if ! [ -d $database ]; then
echo "Database does not exist" >&2
exit 2
fi
if ! [ -e $database/$table ]; then
echo "Table does not exist" >&2
exit 2
fi
./p.sh $linkinpark
firstline=$(head -n 1  $database/$table)
IFS=' ' read -r -a columns <<<"$firstline"
numberofcolumns=${#columns[@]}
IFS=',' read -r -a entry <<<"$tuple"

numberoftuple=${#entry[@]}
if ! [ $numberofcolumns -eq $numberoftuple ];then
echo "Error: number of columns in tuple does not match schema"
else 
echo "${entry[@]}" >> $database/$table
echo "OK: tuple inserted"
fi
./v.sh $linkinpark

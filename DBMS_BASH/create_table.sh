#! /bin/bash
database=$1
table=$2
columns=$3
IFS=',' read -r -a array <<<"$columns"

if [ $# -ne 3 ];then
echo "Error:parameters problem" >&2
exit 1
fi
if ! [ -d $database ]; then
echo "Database does not exist" >&2
exit 2
fi
./p.sh $linkinpark
if  [ -e $database/$table ]; then
echo "The table already exists" >&2
exit 2
else
touch  $database/$table
echo "${array[@]}" >> $database/$table
echo "OK: table created"
fi
./v.sh $linkinpark


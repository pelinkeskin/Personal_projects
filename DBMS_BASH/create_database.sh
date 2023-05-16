#! /bin/bash
database=$1

if [ $# -ne 1 ]; then
echo "the number of parameters is wrong" >&2 
exit 1 
fi
if [ -d $database ]; then
echo "Error:DB already exist" >&2
else
./p.sh "$linkinpark"
mkdir  $database
echo "Database created" 
./v.sh "$linkinpark"
fi




#! /bin/bash
database=$1
table=$2
columnindexes=$3
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
lenghtcolumns=$((${#columns[@]} - 1))
IFS=',' read -r -a indexarray <<<"$columnindexes"
firstele=${indexarray[0]}
secondele=${indexarray[1]}
if [ $firstele -gt  $lenghtcolumns ]; then
echo "Error: column does not exist"
fi 
if [ $secondele -gt  $lenghtcolumns ];then
echo "Error: column does not exist"
else 
if [ -z  $columnindexes ]; then
echo $database/$table
else  
cut -d" " -f $firstele-$secondele  $database/$table
fi
./v.sh $linkinpark
fi 



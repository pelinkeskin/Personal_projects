#! /bin/bash
myid=$1
if [ $# -ne 1 ]; then
echo "the number of parameters is wrong" >&2 
exit 1 
fi
mkfifo "${myid}.pipe"
trap ctrl_c INT
function ctrl_c() {
rm "${myid}.pipe"
exit 1 
}
while true; do
read input
IFS=' ' read -r -a args <<<"$input"
command="${args[0]}"
case "$command" in
create_database)
echo "$myid" "$input" > server.pipe
read input < ${myid}.pipe 
echo "$input"
;;
create_table)
echo "$myid" "$input" > server.pipe
read input < ${myid}.pipe 
echo "$input"
;;
insert)
echo "$myid" "$input" > server.pipe 
read input < ${myid}.pipe 
echo "$input"
;;
select) 
echo "$myid" "$input" > server.pipe
while read input; do
echo "$input"
done < ${myid}.pipe
;;
shutdown)
echo "$myid" "$input" > server.pipe
rm "${myid}.pipe"
exit 0
;;
exit)
rm "${myid}.pipe"
exit 0
;;
*)
echo  "$myid" "$input" > server.pipe 
read input < ${myid}.pipe 
echo "$input"
rm "${myid}.pipe"
exit 1
;;
esac
done

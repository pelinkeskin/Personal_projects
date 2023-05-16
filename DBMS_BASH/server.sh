#! /bin/bash
mkfifo server.pipe
trap ctrl_c INT
function ctrl_c() {
rm "server.pipe"
exit 1 
}
while true; do
read input < server.pipe
IFS=' ' read -r -a args <<<"$input"
myid="${args[0]}"
command="${args[1]}"
database="${args[2]}"
table="${args[3]}"
tuple="${args[4]}"
case "$command" in
create_database)
./create_database.sh "$database" > "${myid}.pipe" 2>&1 &
;;
create_table)
./create_table.sh "$database" "$table" "$tuple" > "${myid}.pipe" 2>&1 &
;;
insert)
./insert.sh "$database" "$table" "$tuple" > "${myid}.pipe" 2>&1 &
;;
select)
./select.sh "$database" "$table" "$tuple" >> "${myid}.pipe" 2>&1 &
;;
shutdown)
rm "server.pipe" 
exit 0
;;
*)
echo "Error: bad request" > "${myid}.pipe" 2>&1 &
rm "server.pipe"
exit 1
;;
esac
done

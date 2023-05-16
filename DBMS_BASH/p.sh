#! /bin/bash
if [ -z "$1" ]; then
exit 1
#elif [ ! -e "$1" ]; then
#exit 2
else
while ! ln "$1" "$1-lock" 2>/dev/null; do
sleep 1
done
exit 0
fi

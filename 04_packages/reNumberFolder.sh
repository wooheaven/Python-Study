#! /bin/bash

if [ -f git-move.sh ]; then
rm git-move.sh
fi

ls -l \
| grep "^d" \
| awk 'BEGIN{FS=" ";OFS="\t"} {if(NF > 8) print $9,substr($9,4); next}' \
| sort -k2,2 \
| cat -n \
| sed -e 's/ //g' \
| awk 'BEGIN{FS=OFS="\t"} {if(length($1) < 2) print 0$1,$2,$3 ;else print $0}' \
| awk 'BEGIN{FS="\t"; OFS=" "} {print "git mv", $2"/", $1"_"$3"/" }' \
| awk 'BEGIN{FS=OFS=" "} {if($3 != $4) print $0; else print "# "$0}' \
> git-move.sh

chmod +x git-move.sh

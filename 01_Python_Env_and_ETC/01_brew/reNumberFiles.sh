#! /bin/bash

if [ -f git-move.sh ]; then
rm git-move.sh
fi

ls -l \
| grep -v "^d" \
| grep -v "reNumberFiles.sh" \
| grep -v "git-move.sh" \
| awk 'BEGIN{FS=" ";OFS="\t"} {if(NF > 8) print $9,substr($9,4); next}' | sort -k2,2 \
| cat -n \
| sed -e 's/ //g' \
| awk 'BEGIN{FS=OFS="\t"} {if(length($1) < 2) print $2,"0"$1"_"$3 ;else print $2,$1"_"$3}' \
| awk 'BEGIN{FS="\t"; OFS=" "} {if($1 != $2) print "git mv",$1,$2; else print "# git mv",$1,$2}' \
> git-move.sh

chmod +x git-move.sh

#!/bin/bash

echo "Getting URLs with a recursion depth of 1"
#urls=`wget -r -l1 --spider --force-html $1 2>&1  grep '^--' | awk '{ print $3 }' | grep -Eio "http.+html" | sort | uniq`

urls=`python just_get_urls.py "$1"`

numurls=`echo "$urls" | wc -l`
echo "Found $numurls URLs"

urloutput=""

counter=0
for url in $urls
do
	printf "$counter "
	if `wget -O - "$url" 2> /dev/null | grep -i -q "$2"`
	then
		printf "Hit "
		urloutput="$urloutput$url\n"
	fi
	let counter=counter+1
done
printf "\n"
printf "Done!\n\n"

printf "$urloutput"

#!/bin/bash
## Looks through all of the Markdown files in the folder,
## if they have been updated within the last hour, it generates
## a new HTML file.

MARKDOWN_EXEC=markdown

if [[ `uname -n` =~ 'linstat' ]] ; then
    MARKDOWN_EXEC='/home/a/ahanna/bin/Markdown.pl'
fi

#CURRTIME=`date +"%s"`
#OFFSET=`expr $CURRTIME - 3600`

for f in $HOME'/sandbox/political-sociology/notes/'*.text
do
## TK: fix this for OS X
#    LASTMOD=`stat -f "%Y" $f`

#    if [ "$LASTMOD" -gt "$OFFSET" ]
#        then
    OUT=`echo $f | sed 's/.text/.html/' | sed 's/\/notes/\/notes\/html/'`        
    echo "Processing $f"
    cat $HOME'/sandbox/political-sociology/notes/html/header.html' $f | $MARKDOWN_EXEC > $OUT 
#    fi
done

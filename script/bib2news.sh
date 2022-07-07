#!/bin/bash
#########################################################################
# Copyright (c) 2020-~ Beisi Xu && St Jude
# This source code is released for free distribution under the terms of the
# CreativeCommons BY-NC-SA 4.0 International License
#*Author:       Beisi Xu < xubeisi [at] gmail DOT com >
# File Name: bib2news.sh Created Time: Thu Jul  7 14:38:27 CDT 2022
#########################################################################

if [ $# -lt 1 ]
then
echo "Usage: bib2news.sh new.bib 2022"
exit
fi

echo $(basename $0) $* >> .run.log

suftmp=tmp.bib2news.sh.$(date +%Y%m%d-%H%M%S-%N).tmp

ff=$1
year=$2

cat $ff | grep @article | sed "s/@article{//;s/,//;s/_/ /g" | grep $year | while read l m n; do nn=$(echo $n | capital.sh); echo "[${nn} et al. $year; $m](/publications/#${l}_${m}_${n}){:target=\\\"_blank\\\"}"; done | tr "\n" "; "

#!/bin/bash
#########################################################################
# Copyright (c) 2020-~ Beisi Xu && St Jude
# This source code is released for free distribution under the terms of the
# CreativeCommons BY-NC-SA 4.0 International License
#*Author:       Beisi Xu < xubeisi [at] gmail DOT com >
# File Name: rename_bib_for_quicker_debug.sh Created Time: Thu May 13 16:49:09 CDT 2021
#########################################################################

if [ $# -lt 1 ]
then
    echo "Usage: rename_bib_for_quicker_debug.sh rename|recover"
    echo "#.bib took long time to build so move them for debug"
    exit
fi

mode=$1

if [[ $mode =~ rename ]]
then
    mkdir -p ../tmp_backup
    mv search.html ../tmp_backup
else
    mv ../tmp_backup/search.html ./
fi

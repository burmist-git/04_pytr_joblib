#!/bin/bash

# Date        : Sun Nov 22 13:35:05 CET 2020
# Autor       : Leonid Burmistrov
# Description : 

function clean_sh {
    rm -rf *~ __pycache__
}

function printHelp {
    echo " --> ERROR in input arguments "
    echo " -c  : clean"
    echo " -p2 : second parameter"
}

if [ $# -eq 0 ]; then
    printHelp
else
    if [ "$1" = "-c" ]; then
            clean_sh
    elif [ "$1" = "-p2" ]; then
	echo " $1 "
    else
        printHelp
    fi
fi

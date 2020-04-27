#!/bin/bash

function get_by_country() {
    COUNTRY=$1
    git submodule update --remote;
    cd covid-19/data;
    git pull;
    grep "$COUNTRY" countries-aggregated.csv  > ../../tmp/$COUNTRY.csv
    cd ../../
    python covgraph.py $1
}


function help() {
    echo "Show COVID-19 Graphs by CountryName"
    echo ""
    echo "Run: ./build.sh %CountryName%"
    echo "Example: ./build.sh Italy"
    echo ""
}


if [ -z $1 ]
then
    help
else
    get_by_country $1
fi;



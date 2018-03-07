#!/bin/bash

# this script controls all the feature

# tool part
Usage() {
    echo "Usage: $0 { deploy | insert | delete [NAME] | display | modify [NAME] }"
    exit 1
}

config_file="resume.json"

Sed_keyword() {
    keyword="$1" 
    read -p "$keyword:" value
    sed -i "s/$keyword/$value/g" $config_file 
}

Parameter_judge() {
    correct_num="$1"
    real_num="$2"
    if [ "$correct_num" != "$real_num" ];then
        Usage
    fi
}

# case part
Insert() {
    cp tamplate.json $config_file
    for keyword in NAME AGE SEX COMPANY
    do 
        Sed_keyword $keyword
    done
    ./insert.py
    rm resume.json
}

Delete() {
    name="$1"
    ./delete.py $name 
}

Display() {
    ./display.py
}

Modify() {
    name="$1"
    ./modify.py $name 
}

case "$1" in
    deploy)
        echo "deploy"
        ;;

    insert)
        Parameter_judge 1 $#
        Insert 
        ;;

    delete)
        Parameter_judge 2 $#
        Delete $2
        ;;

    display)
        Parameter_judge 1 $#
        Display
        ;;
    modify)
	    Parameter_judge 2 $#
	    Modify $2
	    ;;

    *)
        Usage
        ;;
esac



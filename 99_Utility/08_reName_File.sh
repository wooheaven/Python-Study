#!/bin/bash

var1=$1
var2=$(echo $1 | sed 's/\ /_/g' | sed 's/_/__/')

git mv "$var1" $var2

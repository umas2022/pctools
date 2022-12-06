#! /bin/bash

package="tshark"
# package="git"

if  type $package > /dev/null 2>&1;then
    echo "found"
else
    echo "not found"
fi
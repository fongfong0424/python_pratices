#!/bin/bash

#echo -e "\e[0m你好\e[0m"
echo -e "\033[31mDefault\033[0m"
for i in {30..37};do
  echo -e "\033[${i}m你好"

done



#! /bin/bash

# input

# read -p 'insert your name' NAME
# echo "hello $NAME"

#for loop

# NAMES="GILLI jeny annita caleb"

# for NAME in $NAMES
#     do
#         echo "hello $NAME"
# done

# if

# NAME='gillin'
# if [ "$NAME" == 'caleb' ]
# then
#     echo "yes"
# elif [ "$NAME" == 'gilli' ]
# then
#     echo "hello $NAME"
# else
#     echo 'no match'
# fi

# switch
# read -p 'should he have a beer? ' INPUT
# case "$INPUT" in
#     [Yy] | [Yy][eE][sS])
#         echo 'ypou deserve a beer'
#         ;;
#     [nN] | [nN][Oo])
#         echo " no beer for you"
#         ;;
#     *)
#         echo 'i dont know if you should have a beer'
#         ;;
# esac

# FILES
# file='lessonss'

# if [ -e "$file" ]
# then
#     echo "$file is a file"
# else
#     echo "$file is not a file"
# fi

# conditionals

# num1='y'
# num2=5

# if [ "$num1" -gt "$num2" ]
# then
#     echo "$num1 is greater than $num2"
# elif [ "$num1" -eq "$num2" ]
# then
#     echo "$num1 is equal to $num2"
# elif [ "$num1" -le "$num2" ]
# then 
#     echo "$num1 is less than or equal to $num2"
# else
#     echo 'no handle fpor this condition'
# fi

# FILES=$(ls *.txt)

# for FILE in $FILES
#     do
#         echo "renaming $FILE"
#         mv $FILE "new-$FILE"
# done

# read files

# LINE=1
# echo 'here'
# while read -r CURRENT_LINE
#     do
#         echo "$LINE: $CURRENT_LINE"
#         ((LINE++))
# done < "./write.txt"
# echo 'we are'
# function call (){
# echo " I love $1 and $2"
# }
# call "brad" "chioma"
# mkdir test
# cd test
# touch 'arm.txt'
# echo 'collected' >> 'arm.txt'
# echo 'done'
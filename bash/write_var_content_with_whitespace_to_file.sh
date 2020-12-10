var="\
a\n\
b
"
printf $var >> f
cat f
# OUTPUT
# a
# b

gpio mode 1 out
gpio mode 0 out
for (( c=0; c<=9; c++ ))
do  
   gpio write 1 1   
   gpio write 0 1
   sleep 1
   gpio write 1 0
   gpio write 0 0
   sleep 1
done

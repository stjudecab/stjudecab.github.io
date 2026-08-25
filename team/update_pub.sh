ff=$1

if [ $(grep "\-\-more\-\-" $ff | wc -l |awk '{printf $1}') -gt 0 ]
then
    nf=$(grep "\-\-more\-\-" $ff -n | sed "s/:.*//")
    cp $ff ${ff}.bk
    head -n $nf ${ff}.bk > ${ff}
    cat pub.txt >> ${ff}
fi

pref=$1
color=$2

#for i in _team.md
for i in _publications.md _research.md _team.md .md
do
    cat Epigenetics${i} | sed "s/Epigenetics/${pref}/;s/groupcolor:.*/groupcolor: \"#$color\"/" > ${pref}$i
done

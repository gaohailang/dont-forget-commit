# -*- coding: utf-8 -*-
# @Author: gaohailang
# @Date:   2016-03-30 09:06:49
# @Last Modified by:   gaohailang
# @Last Modified time: 2016-05-03 17:07:29

for i in {1..140}
do
  echo $i
  dateOpt="$i day ago"
  echo "$dateOpt"
  dateStr=`gdate --date "$dateOpt"`
  echo "$dateStr" >> daily-fake-commits.txt
  git commit --date="$dateStr" -am "chore: $dateStr"
  echo "$dateStr\n"
done

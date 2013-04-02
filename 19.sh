#!/usr/bin/zsh

for ((i = -2208409200; i < 978249600; i += 604800));
do
  echo `date -d @$i`
done

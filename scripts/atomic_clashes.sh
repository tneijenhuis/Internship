#!/bin/bash

/home/abonvin/haddock2.4/tools/contact-chainID $1 2.5 > contacts.temp

wc contacts.temp | awk '{print $1}'

rm -f contacts.temp 


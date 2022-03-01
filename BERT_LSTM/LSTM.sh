#!/bin/tcsh
##
##	Job Script for PC Cluster, JAIST
##		created by mkjob.pl
##	** Revise the script as necessary **
#
#PBS -N BERT_LSTM
#PBS -q GPU-S
#PBS -j oe 
#PBS -l select=2

#PBS -M s2020045@jaist.ac.jp -m be


setenv PATH /home/$USER/anaconda3/bin:${PATH}
setenv PYTHON_PATH /home/$USER/anaconda3/bin/python

cd ~/BERT/BERT_ABSA-X/BERT_LSTM/BERT_lstm/

sh train.sh

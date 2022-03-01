#!/bin/tcsh
##
##	Job Script for PC Cluster, JAIST
##		created by mkjob.pl
##	** Revise the script as necessary **
#
#PBS -N extractAll
#PBS -q SINGLE
#PBS -j oe 
#PBS -l select=4:ncpus=32:mpiprocs=32


setenv PATH /home/$USER/anaconda3/bin:${PATH}
setenv PYTHON_PATH /home/$USER/anaconda3/bin/python

cd ~/BERT/BERT_ABSA-X/

python extractAll.py

#!/usr/bin/env python

from os.path import isfile, join

from db.answered import answered_set
from db.unanswered import unanswered_set

import random
import sys

import time
import glob
import os

# algos
algos_dir_path = "algos"

# DBs
unanswered_file_path = 'unanswered.py'
answered_file_path = 'answered.py'
main_file_path = 'main'

# entrypoint
pracitce_environment_path = 'main.py'

path = os.getcwd()
files_all = set()

def seed():
    os.chdir(path+"/algos")
    for file in glob.glob("*.py"):
        if file not in answered_set:
            files_all.add(file)

    os.chdir(path+"/db")
    with open(unanswered_file_path, 'w') as f:
        print >> f, 'unanswered_set =', files_all

def reset():
	os.chdir(path+"/db")
	with open(answered_file_path, 'w') as f:
		print >> f, 'answered_set = set([])'

	os.chdir(path+"/algos")
	for file in glob.glob("*.py"):
		files_all.add(file)

	os.chdir(path+"/db")
	with open(unanswered_file_path, 'w') as f:
		print >> f, 'unanswered_set =', files_all

	seed()
	
def randomize():

    if not unanswered_set:
        print "no problems available, reset the database"
        return

    problem = random.sample(unanswered_set, 1)

    os.chdir(path+"/db")
    unanswered_set.remove(problem[0])
    with open(unanswered_file_path, 'w') as f:
        print >> f, 'unanswered_set =', unanswered_set

    answered_set.add(problem[0])
    with open(answered_file_path, 'w') as f:
        print >> f, 'answered_set =', answered_set

    with open(main_file_path, 'w') as f:
        print >> f, problem[0]

    problem_file_path = algos_dir_path + '/' + problem[0]

    os.chdir(path)
    with open(pracitce_environment_path, 'a+') as f:

        f.truncate(0)

        with open(problem_file_path) as fp:

            lines = fp.read().splitlines()

            for line in lines:

                if line == "# ----- end ------":
                    break

                f.write(line + '\n')


if __name__ == "__main__":

    if sys.argv[1] == "random":
        randomize()
    elif sys.argv[1] == "reset":
        reset()
    elif sys.argv[1] == "seed":
        seed()
    elif sys.argv[1] == "currfile":
    	os.chdir(path+"/db")
        with open('main', 'r') as f:
    		print(f.read())
    else:
        print "unknown arg"

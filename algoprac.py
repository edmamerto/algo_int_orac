#!/usr/bin/env python

from os import listdir
from os.path import isfile, join

from db.answered import answered_set
from db.unanswered import unanswered_set

import random

# algos
algos_dir_path = "algos"

# DBs
unanswered_file_path = 'db/unanswered.py'
answered_file_path = 'db/answered.py'
main_file_path = 'main'

# entrypoint
pracitce_environment_path = 'main.py'


def seed():
    files_all = {f for f in listdir(algos_dir_path) if f not in answered_set}
    with open(unanswered_file_path, 'w') as f:
        print >> f, 'unanswered_set =', files_all


def reset():
    with open(answered_file_path, 'w') as f:
        print >> f, 'answered_set = set([])'
    # for some reason this needs a double cll
    seed()
    seed()


def randomize():

    if not unanswered_set:
        print "no problems available, reset the database"
        return

    problem = random.sample(unanswered_set, 1)

    unanswered_set.remove(problem[0])
    with open(unanswered_file_path, 'w') as f:
        print >> f, 'unanswered_set =', unanswered_set

    answered_set.add(problem[0])
    with open(answered_file_path, 'w') as f:
        print >> f, 'answered_set =', answered_set

    with open(main_file_path, 'w') as f:
        print >> f, problem

    problem_file_path = algos_dir_path + '/' + problem[0]


    with open(pracitce_environment_path, 'a+') as f:
        
        f.truncate(0)

        with open(problem_file_path) as fp:

			lines = fp.read().splitlines()

			for line in lines:

				if line == "# ----- end ------":
					break

				f.write(line + '\n')


randomize()

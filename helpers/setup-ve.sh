#!/bin/bash
workon algo
cd -
alias ipython='frameworkpython -m IPython'
alias python='framworkpython'
alias nosetests="frameworkpython $(which nosetests)"
export PYTHONPATH=$PYTHONPATH:$(pwd)

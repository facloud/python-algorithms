#!/bin/bash
source ~/ve/algo/bin/activate
frameworkpython $(which nosetests) $@

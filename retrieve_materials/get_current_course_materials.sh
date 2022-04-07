#!/bin/bash

# script to retrieve current materials for 'Programming in Python SS2022'.
# The script creates a subdirectory with the current date and puts
# course materials within.

# NOTE:
# If you are familiar with git, you should use git-commands to obtain and
# administrate the materials.

# git-repo for the course:
GIT_REPO=https://github.com/terben/Programming_in_Python_BCGS_Summer_2022.git

DIR=python_course_$(date +'%F')

if [ ! -d ${DIR} ]; then
  mkdir -p ${DIR}
  cd ${DIR}
  git clone ${GIT_REPO}
  #
  echo ""
  echo "Please go to ${DIR} and run 'jupyter notebook' there."
else
  echo "You probably already retrieved the materials from GitHub!"
  echo "If you want to retrieve them again, then explicitely"
  echo "delete the directory ${DIR} before calling this script!"
  exit 1;
fi

exit 0;

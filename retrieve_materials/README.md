# How to download course materials

Those familiar with `git` and `github` should download and
administrate the course materials with `git`-commands. We will
introduce `git` and the concepts of *version control* at the end of
the term.

A way to obtain the materials easily without `git`-knowledge is:

1. Download the script [get_current_course_materials.sh](https://raw.githubusercontent.com/terben/Programming_in_Python_BCGS_Summer_2020/master/retrieve_materials/get_current_course_materials.sh).

2. Create a directory, where you want to store course materials. This
only needs to be done once for the whole course.

3. Go to that directory and execute:

   ```
   user$ bash get_current_course_materials.sh
   Cloning into 'Programming_in_Python_BCGS_Summer_2020'...
   .
   .
   user$ ls
   python_course_2018-04-10 ... # 2018-04-10 needs to be subtituted
                                # by the current date
   user$ cd python_course_2018-04-10
   user$ jupyter notebook       # to start working on the notebooks
   ```
4. Repeat step 3 whenever a new version of materials is available.



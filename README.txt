Files required to run testhomework.py:
testhomework.py
testracket.py
testocaml.py
suite-test.rkt
suite_test.ml
suite-test-results.rkt, which can be an empty file
<hwname>-suite-tests.rkt, which takes the form of (print-test (test as boolean statement) (info as string))
<hwname>_suite_tests.ml, which takes the form of print_test (Test (test as boolean statement), (info as string))

run testhomework.py as follows:
In a directory containing the above files, run
python testhomework.py <hwname>.{rkt, ml}

testhomework determines whether or not input file should run in racket or ocaml,
then creates a test suite file in the corresponding language (suite.{rkt, ml}, and scores the results,
printing any failed tests, and giving how many tests the student passed. This data is
archived in the file "<hwname>-archive.dat", which keeps track of a student's attempts to test their homework.

A few things to still work out:
1) The path in the CIT computers that will run racket and ocaml
2) Dealing with racket's teachpack stuff
3) Assigning the filenames that will be given in racket or ocaml
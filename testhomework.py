import io
import subprocess
import sys
import testracket
import testocaml

# Scores student based on how many tests passed, 
# as well as informing them of what tests failed.
def scoreAndPrint(cases):
	archive = io.open(hwname + "-archive.dat", 'a')
	score = 0
	possible = 0
	for case in cases:
		if(case == u'#test-passed\n'):
			score += 1
			possible += 1
		else:
			fail = u"Test failed: " + case[:-1]
			archive.write(fail + "\n")
			print fail
			possible += 1
	score_string = str(score) + " out of " + str(possible) + " tests passed."
	archive.write(score_string + u"\n*************\n")
	archive.close()
	print score_string

# files that will be written in racket
racketfiles = {'rightcode.rkt', 'wrongcode.rkt', 'hw01.rkt', 'hw02.rkt', 'hw03.rkt', 'hw04rkt', 'hw05.rkt'}
# files that will be written in ocaml
ocamlfiles = {'rightcode.ml', 'wrongcode.ml', 'hw06.ml', 'hw07.ml', 'hw08.ml', 'hw09.ml', 'hw10.ml'}

hwfile = sys.argv.pop(1) # the homework filename

if (hwfile in racketfiles):
	hwname = hwfile[:-4] # the homework name
	testracket.make_suite(hwname, hwfile) # makes suite code for student
	# runs suite in racket. ** the path may need to change depending on the machine.
	subprocess.check_output('/applications/"racket v5.3.6"/bin/racket suite.rkt', shell=True)
	
	with io.open("test-suite-results.dat") as answers:
		scoreAndPrint(answers.readlines()) # display and archive scores
		answers.close()

elif(hwfile in ocamlfiles):
	hwname = hwfile[:-3] # the homework name
	testocaml.make_suite(hwname, hwfile) # makes suite code for student
	# runs suite in ocaml. ** the path may need to change depending on the machine.
	subprocess.check_output("/usr/local/bin/ocaml suite.ml", shell=True)

	with io.open("test_suite_results.dat") as answers:
		scoreAndPrint(answers.readlines()) # display and archive scores
		answers.close()


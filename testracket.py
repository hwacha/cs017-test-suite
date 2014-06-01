import io

# initializes the current suite file to be run via racket
def make_suite(hwname, hwfile):
	suite = io.open("suite.rkt", 'w')
	suite.write(u"#lang racket\n(require \"suite-test.rkt\")\n")

	studentcode = io.open(hwfile) # the student's code
	suite.writelines(studentcode.readlines())
	studentcode.close()

	tests = io.open(hwname + "-suite-tests.rkt") # the test suite
	suite.writelines(tests.readlines())
	tests.close()

	suite.write(u"\n(close-output-port out)") # flushes racket writer's output stream
	suite.close()
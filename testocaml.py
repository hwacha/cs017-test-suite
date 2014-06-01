import io

# initializes the current suite file to be run via ocaml
def make_suite(hwname, hwfile):
	
	suite = io.open("suite.ml", 'w')

	studentcode = io.open(hwfile) # the student's code
	suite.writelines(studentcode.readlines())
	studentcode.close()

	suite.writelines(io.open("suite_test.ml").readlines()) # references the code which prints the test suite info

	tests = io.open(hwname + u"_suite_tests.ml") # the test suite
	suite.writelines(tests.readlines())
	tests.close()

	suite.write(u"close_out results;;") # flushes ocaml writer's output stream
	suite.close()

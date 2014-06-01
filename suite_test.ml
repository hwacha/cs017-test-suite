open Printf

(* provides a test case, and information about it, lest the student fail it *)
type suite_test = | Test of bool * string;;

(* prints test result to results file *)
let() = 
let results = open_out "test_suite_results.dat" in
let print_test (a_suite_test : suite_test) : unit =
	match a_suite_test with 
	| Test(pass, info) -> if pass then fprintf results "%s\n" "#test-passed" 
									else fprintf results "%s\n" info in

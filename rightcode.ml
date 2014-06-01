let rec factorial(n : int) : int =
	match n with
	| 0 -> 1
	| _ -> n * (factorial (n - 1));;
	
let rec factorial(n : int) : int =
	match n with
	| 0 -> 0
	| _ -> n * (factorial (n - 1));;
	
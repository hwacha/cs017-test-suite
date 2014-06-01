(define (factorial n)
	(cond
		[(= n 0) 0]
		[(> n 0) (* n (factorial (- n 1)))]))
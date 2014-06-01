#lang racket
(provide suite-test)
(provide out-1)
(provide out)
(provide print-test)

; provides a test case, and info about it, lest the student fail it
(struct suite-test (test info))
; truncates results file
(define out-1 (open-output-file "test-suite-results.dat" #:exists 'truncate))
(close-output-port out-1)
; writes test results to results file
(define out (open-output-file "test-suite-results.dat" #:exists 'append))
(define (print-test a-suite-test)
            (if (suite-test-test a-suite-test) 
                (begin
                 (display "#test-passed\n" out))
                (begin
                (display (string-append (suite-test-info a-suite-test) "\n") out))))
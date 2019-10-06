(define (assign_el array pos val)
	(newline)
	(display array)
	(
		if (= pos 0)
			(cons (cdr array) val)
			(cons (car array) (assign_el (cdr array) (- pos 1) val))
	)
)

(define (bubble_up array pos)
	(
		if (> (list-ref array pos) (list-ref array (+ pos 1))) 
			(list-ref array pos)
	)
)


(define (bubble_sort array)
	(define is_sorted #f)
)

(newline)
(define my_array (list 0 1 2 3 4 5 6 7 8 9))
(display my_array)
(assign_el my_array 4 123)
;(newline)
;(display my_array)

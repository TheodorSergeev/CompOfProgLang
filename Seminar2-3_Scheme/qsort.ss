(define (extract lst pred x)
	(filter (lambda (y) (pred y x)) lst)
)

(define (qsort lst)
	(if (null? lst) '()
		(let 
			(h (car lst))
			(t (cdr lst))
		)
		(append 
			(qsort (extract t <= h))
			(cons h [qsort (extract t > h)])
		)
	)
)
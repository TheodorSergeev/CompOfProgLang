; Task  : implement "len" function
; "len" function computes the length of the list via left fold (https://en.wikipedia.org/wiki/Fold_(higher-order_function))
; (+implement yourself foldl = fold-left)
; input : a list (can be empty)
; output: integer equal to the length of the list

; run: (load "len.ss")

(define (foldl f z l)
    (if (null? l)
        z
        (foldl f (f z (car l)) (cdr l))
    )
)

(define (len arr)
    (foldl (lambda (iter elem) (+ iter 1)) 0 arr)
)

(len '(1 2 3 4 5 6))
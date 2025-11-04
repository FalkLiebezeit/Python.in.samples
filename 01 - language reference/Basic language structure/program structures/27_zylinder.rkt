#lang racket
;zylinder.rkt
(define (volumen d l)
         (* 0.785 d d l))

(define (masse d l)
         (* 7.85 (volumen d l)))

(define (traegheitsmoment d l)
         (* 0.5 (masse d l) 2.5e-3 d d))

(define (beschleunigungsmoment d l alpha)
         (* alpha  0.5 (masse d l) 2.5e-3 d d))

(display "Volumen: ")(writeln (volumen 1 10))
(display "Masse:   ")(writeln (masse 1 10))
(display "Traegheitsmoment:      ")(writeln (traegheitsmoment 1 10))
(display "Beschleunigungsmoment: ")(writeln (beschleunigungsmoment 1 10 1.2))
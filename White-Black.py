"""
Domain
"""

(define (domain white_black_puzzle_domain)
  (:requirements :strips)
  (:types cell)
  (:predicates
    (adjacent ?c1 ?c2 - cell)
    (black_at ?c - cell)
    (white_at ?c - cell)
    (empty_at ?c - cell)
  )
  (:action slide_black
    :parameters (?empty ?black - cell)
    :precondition (and (empty_at ?empty) (adjacent ?empty ?black) (black_at ?black))
    :effect (and (not (empty_at ?empty)) (empty_at ?black) (not (black_at ?black)) (black_at ?empty))
  )
  (:action slide_white
    :parameters (?empty ?white - cell)
    :precondition (and (empty_at ?empty) (adjacent ?empty ?white) (white_at ?white))
    :effect (and (not (empty_at ?empty)) (empty_at ?white) (not (white_at ?white)) (white_at ?empty))
  )
)

"""
Problem
"""
(define (problem white_black_puzzle)
  (:domain white_black_puzzle_domain)
  (:requirements :strips)
  (:objects cell1 cell2 cell3 cell4 - cell)
  (:init
    (adjacent cell1 cell2) (adjacent cell2 cell1)
    (adjacent cell2 cell3) (adjacent cell3 cell2)
    (adjacent cell3 cell4) (adjacent cell4 cell3)
    (black_at cell1)
    (white_at cell2)
    (white_at cell3)
    (empty_at cell4)
  )
  (:goal
    (and (black_at cell3) (white_at cell2) (white_at cell1))
  )
)


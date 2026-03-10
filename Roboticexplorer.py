"""
Domain
"""
(define (domain robotic_explorer_domain)
  (:requirements :strips)
  (:types waypoint)
  (:predicates
    (at ?w - waypoint)
    (connected ?w1 ?w2 - waypoint)
    (rocks_at ?w - waypoint)
    (analysed ?w - waypoint)
    (transmitted ?w - waypoint)
  )
  (:action move
    :parameters (?from ?to - waypoint)
    :precondition (and (at ?from) (connected ?from ?to))
    :effect (and (not (at ?from)) (at ?to))
  )
  (:action analyse_rocks
    :parameters (?w - waypoint)
    :precondition (and (at ?w) (rocks_at ?w))
    :effect (analysed ?w)
  )
  (:action transmission
    :parameters (?w - waypoint)
    :precondition (and (at ?w) (analysed ?w))
    :effect (transmitted ?w)
  )
)

"""
Problem
"""
(define (problem robotic_explorer_problem)
  (:domain robotic_explorer_domain)
  (:requirements :strips)
  (:objects A B C D E F G - waypoint)
  (:init
    (at G)
    (connected A B) (connected B A)
    (connected B C) (connected C B)
    (connected C D) (connected D C)
    (connected D E) (connected E D)
    (connected E G) (connected G E)
    (connected B G) (connected G B)
    (connected G F) (connected F G)
    (connected F A) (connected A F)
    (rocks_at B) (rocks_at C) (rocks_at D) (rocks_at E)
  )
  (:goal
    (forall (?w - waypoint)
      (or (not (rocks_at ?w)) (transmitted ?w))
    )
  )
)


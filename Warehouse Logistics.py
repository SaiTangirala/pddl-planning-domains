"""
Domain
"""
(define (domain warehouse_domain)
  (:requirements :strips :typing)
  (:types truck item location)
  (:predicates
    (at-truck ?t - truck ?l - location)
    (empty ?t - truck)
    (carrying ?t - truck ?i - item)
    (at-item ?i - item ?l - location)
    (in-crate ?p - item ?c - item)
    (crate ?c - item)
    (package ?p - item)
    (connected ?l1 ?l2 - location)
  )
  (:action drive
    :parameters (?t - truck ?from ?to - location)
    :precondition (and (at-truck ?t ?from) (connected ?from ?to) (empty ?t))
    :effect (and (not (at-truck ?t ?from)) (at-truck ?t ?to))
  )
  (:action pickup
    :parameters (?t - truck ?i - item ?l - location)
    :precondition (and (at-truck ?t ?l) (at-item ?i ?l) (empty ?t))
    :effect (and (carrying ?t ?i) (not (empty ?t)) (not (at-item ?i ?l)))
  )
  (:action put-in-crate
    :parameters (?t - truck ?p ?c - item ?l - location)
    :precondition (and (at-truck ?t ?l) (carrying ?t ?p) (at-item ?c ?l) (crate ?c) (package ?p))
    :effect (and (in-crate ?p ?c) (empty ?t) (not (carrying ?t ?p)))
  )
)

"""
Problem
"""
(define (problem warehouse_problem)
  (:domain warehouse_domain)
  (:requirements :strips :typing)
  (:objects truck1 - truck crate package1 package2 - item w0 w1 w2 base - location)
  (:init
    (at-truck truck1 base)
    (empty truck1)
    (crate crate)
    (package package1) (package package2)
    (at-item crate w0)
    (at-item package1 w2)
    (at-item package2 w0)
    (connected base w0) (connected w0 base)
    (connected w0 w1) (connected w1 w0)
    (connected w1 w2) (connected w2 w1)
    (connected w2 base) (connected base w2)
  )
  (:goal
    (and (at-truck truck1 w0)
         (at-item crate w1)
         (in-crate package1 crate)
         (in-crate package2 crate))
  )
)



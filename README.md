# PDDL Planning Domains

This repository contains PDDL implementations for three classical planning problems.

The project demonstrates knowledge of:

- Automated Planning
- PDDL Domain Modeling
- Search Algorithms
- Heuristic Planning

---

# Domains Implemented

## 1 Robotic Explorer

### Problem Description

A robotic explorer navigates between waypoints on a planet to analyze rock samples and transmit results to Earth.

### Requirements

- Waypoints are connected
- The rover can navigate between connected waypoints
- Rocks exist at certain waypoints
- The rover must be at the waypoint to analyze rocks
- Transmission is only possible at special waypoints

### Files

```
robotic-explorer/
    domain.pddl
    problem.pddl
```

---

## 2 White Black Puzzle

### Problem Description

The puzzle contains four cells:

Initial configuration:

```
Black White White Empty
```

### Goal

Arrange the tiles so that:

```
White White Black _
```

### Actions

- Move tile to adjacent empty cell
- Jump over one tile

### Files

```
white-black-puzzle/
    domain.pddl
    problem.pddl
```

---

## 3 Warehouse Domain

### Problem Description

A warehouse contains trucks, crates, and packages.

Trucks can:

- Drive between locations
- Lift packages or crates
- Place packages into crates
- Secure crates inside trucks
- Drop crates at locations

### Files

```
warehouse-domain/
    domain.pddl
    problem.pddl
```

---

# Planner Used

Fast Downward Planner

Example command:

```
./fast-downward.py domain.pddl problem.pddl --search "astar(goalcount())"
```

---

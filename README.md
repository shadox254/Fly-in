*his project has been created as part of the 42 curriculum by rruiz*

## 📄 Description

Fly-in is a system capable of efficiently guiding a fleet of drones from a central base
(departure) to a target location (arrival), while navigating this dynamic network in accordance with
a set of strict constraints and optimization objectives.

## Project Structure
```
├── maps/                               # All maps sorted by difficulty level
├── src/                                # Core source code directory
│   ├── algo/                           # Pathfinding algorithms
│   │   └── pathfinding.py              # Time-expanded Dijkstra routing
│   ├── models/                         # Core data models and entities
│   │   ├── calendar.py                 # Space-time resource tracking
│   │   ├── drone.py                    # Drone entity representation
│   │   ├── enum.py                     # Zone types and color constants
│   │   ├── errors.py                   # Custom application exceptions
│   │   ├── hub.py                      # Hub zone properties and links
│   │   └── manager.py                  # Global state coordinator
│   ├── parsing/                        # Input map validation and processing
│   │   └── parsing.py                  # Line-by-line map configuration reader
│   ├── simulation/                     # Simulation execution logic
│   │   └── engine.py                   # Turn-based loop and terminal output
│   └── __main__.py                     # Application entrypoint
├── .gitignore                          # Git untracked files configuration
├── Makefile                            # Automation and build rules
├── pyproject.toml                      # Project metadata and configuration
├── README.md                           # Documentation and setup guide
└── uv.lock                             # Locked dependency versions
```

### All Makefile rules
| Command | Descrription |
|---------|--------------|
| make install | installs all project dependencies |
| make run | Runs the program with the selected map |
| make debug | Launches the simulation step-by-step using the native pdb debugger |
| make lint | Validates code style consistency and formatting conventions |
| make lint-strict | Executes rigorous and strict static type checking analysis |
| make clean | Removes generated cache, temporary files, and environment artifacts |
| make fclean | Deletes all cached artifacts and completely removes the virtual environment |

## 🛠️ Instructions

### Makefile instructions
```
    make & make install # Install all dependencies

    make run MAP=<PathToMap> # Runs the program with the selected map

    make debug MAP=<PathToMap> # Runs the program in debug mode with the selected map
```

### uv instructions
```
    uv run python -m src <PathToMap> # Runs the program with the selected map

    uv run python -m pdb -m src <PathToMap> # Runs the program in debug mode with the selected map
```

## Map rules

### Format
```
  nb_drones: 4

  start_hub: start 0 0 [color=green]
  hub: junction 1 0 [color=yellow max_drones=2]
  hub: path_a 2 1 [color=blue]
  hub: path_b 2 -1 [color=blue]
  end_hub: goal 3 0 [color=red max_drones=3]

  connection: start-junction [max_link_capacity=2]
  connection: junction-path_a
  connection: junction-path_b
  connection: path_a-goal
  connection: path_b-goal
```

### Zone Types

|Zone Type|Movement Cost|description|
|---------|-------------|-----------|
| **normal** | 1 turn | Standard zone |
| **restricted** | 2 turns | Area requiring 2 turns to navigate |
| **priority** | 1 turn | Preferred zone that the pathfinding algorithm always prioritizes |
| **blocked** | X | Inaccessible region that drones are strictly prohibited from entering |

### Metadata

| Element | Attribute | Default Value | Description |
|---------|-----------|---------------|-------------|
| **Hub** | `type` / `zone_type` | `normal` | Defines the zone category (`normal`, `restricted`, `priority`, `blocked`) affecting movement cost and routing priority. |
| **Hub** | `max_drones` | `1` | The maximum capacity of drones allowed simultaneously on this specific hub. |
| **Hub** | `color` | `lightgray` | The color used for the terminal visual representation. |
| **Connection** | `capacity` | *Required* | The total number of drones allowed to traverse the link simultaneously during the same turn. |

## Pathfinding & Algorithm

The core of the routing system relies on a **Time-Expanded Dijkstra Algorithm**. Instead of mapping paths solely based on static geographical locations, the state space is expanded to include time (measured in simulation turns).

### 1. State Representation
Each state explored by the algorithm is defined as a multi-dimensional token:
State = (Current Turn, Current Hub)

This allows drones to effectively "wait" at a hub if necessary (transitioning to `Current Turn + 1` at the same location) to resolve traffic bottlenecks or avoid collisions.

### 2. Resource Reservation & Collision Avoidance
To strictly enforce network constraints without relying on external graph libraries, a global `ReservationCalendar` tracks resource occupancy across space and time:
* **Hub Capacity:** A drone can only enter or wait at a hub if its maximum capacity (`max_drones`) is not exceeded at that specific turn.
* **Connection Capacity:** Links between hubs have a traversal capacity. The algorithm verifies link availability for every single turn during transit.

### 3. Native Priority Tie-Breaking
To prioritize `priority` zones without altering the true chronological cost of the path, the min-heap (`heapq`) leverages Python's native tuple comparison mechanics. Paths are pushed into the priority queue using the following structure:

(cost, priority_score, current_turn, current_hub, path)


When two distinct paths reach a state with identical movement costs, `heapq` automatically evaluates the second element (`priority_score`). By decrementing this score whenever a drone enters a priority zone, paths routing through preferred zones carry a lower negative score and are natively chosen first by the interpreter.

## 📚 Ressources

### Useful Links & References

* [Dijkstra Algorithm - Wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_Dijkstra)
* [Dijkstra Shortest Path - GeeksforGeeks](https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/)
* [Dijkstra Definition - Nexa](https://www.nexa.fr/blog/algorithme-de-dijkstra-definition)
* [Dijkstra in Python - DataCamp](https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python?)
* [Heap queue (heapq) - GeeksforGeeks](https://www.geeksforgeeks.org/python/heap-queue-or-heapq-in-python/)
* [Heapq Module - W3Schools](https://www.w3schools.com/python/ref_module_heapq.asp)
* [Fonction Frozenset - CommentCoder](https://www.commentcoder.com/python-fonction-frozenset/)
* [Frozenset Tutorial - DataCamp](https://www.datacamp.com/fr/tutorial/frozenset)

### AI Usage:

* **Compare with other algorithms to determine which one is most useful for the project**: Evaluated various pathfinding strategies (classic Dijkstra, A*, and Time-Expanded graphs) to select the architecture best suited for dynamic hub capacities and collision avoidance.
* **Find a solution for implementing Dijkstra's algorithm**: Guided the adaptation of Python's native `heapq` to support spatio-temporal states `(turn, hub)` and resolve routing constraints without external libraries.
* **Help me understand some of the problems I've encountered and suggest ways to solve them**: Assisted in diagnosing behavior issues with tuple comparison in min-heaps and designing an efficient tie-breaking mechanism for priority zones.
* **Help me with docstring**: Provided templates and standard formatting guidelines to ensure Google-style docstring compliance across all modules.
* **Help me with mypy**: Helped resolve strict static typing type-hints conflicts, particularly around complex nested queue structures.
* **Help me with Readme**: Structured the documentation layout, command summary tables, and algorithmic complexity analysis for clear presentation.

> ⚠️ **Important Note:** AI was used exclusively as a learning assistant and debugging tool. No code or documentation was blindly copied or pasted. Every concept was thoroughly analyzed, refactored, and implemented manually to ensure deep understanding and strict compliance with the project rules.

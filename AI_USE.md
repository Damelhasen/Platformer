# AI Use and Change Log

## Request

Fix moving platforms that appeared to reset to their original positions instead
of bouncing back at the ends of their paths. Do not modify `README.md`.

## Investigation

- Located the game implementation in `MAIN.py`.
- Found that every moving platform's coordinates were recalculated from its
  original spawn position and the system wall clock on every frame.
- Confirmed that this approach did not preserve a platform's current direction
  or position as movement state.

## Changes Made

- Added `platform_motion.py` with `advance_bouncing_axis()`.
- Changed moving platforms to store their current horizontal and vertical
  velocity plus their movement bounds.
- Updated `MAIN.py` to move platforms using Ursina's frame delta (`time.dt`).
- Platforms now reverse velocity at each bound and preserve overshoot, producing
  continuous back-and-forth movement without snapping to their spawn position.
- Kept stationary platform axes stationary.
- Added `test_platform_motion.py` with coverage for normal movement, both bound
  reflections, long-frame overshoot, and stationary axes.

## Files

- `MAIN.py`: uses stateful bounded platform movement.
- `platform_motion.py`: contains testable bounce calculations.
- `test_platform_motion.py`: verifies movement and reversal behavior.
- `AI_USE.md`: documents the agent's investigation and changes.

## Verification

Run the automated checks from the project directory:

```powershell
..\.venv\Scripts\python.exe -m unittest -v
```

- All 5 platform-motion unit tests passed.
- `MAIN.py`, `platform_motion.py`, and `test_platform_motion.py` passed Python
  bytecode compilation.
- `git diff --check` reported no patch formatting errors.
- `git diff -- README.md` produced no output.
- A short `MAIN.py` launch smoke test initialized without a traceback. The
  processes created for that timed test were stopped afterward.

`README.md` was intentionally not edited.

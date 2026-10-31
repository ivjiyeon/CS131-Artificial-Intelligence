# JumboProve

JumboProve is a Python resolution-based automated theorem prover for both propositional and first-order logic. It reads knowledge bases from JSON files, applies resolution rules with support for unification and variable binding, and searches for a proof by deriving the empty clause.

## Features

- Propositional logic resolution
- First-order logic resolution with unification
- Variable binding and substitution support
- Set-of-support proof search
- Example knowledge bases for logical reasoning tasks
- Test suite covering eight problem sets

## Project Structure

- `ResolutionProver.py` – main prover entry point and example execution
- `PropClauses.py` – propositional clause representation and resolution logic
- `FOLClauses.py` – first-order clause representation, unification, and bindings
- `prop_kbs/` – sample propositional knowledge bases
- `fol_kbs/` – sample first-order knowledge bases
- `tests/` – unit tests for each major prover component
- `test.py` – command-line runner for selected or all tests

## Running the Prover

Run the bundled example proofs:

```bash
python ResolutionProver.py
```

## Running the Tests

Run all test questions:

```bash
python test.py
```

Run a subset of tests:

```bash
python test.py -q q1 q2 q3
```

You can also run any combination of the available question groups:

```bash
python test.py -q q1 q2 q3 q4 q5 q6 q7 q8
```

## Notes

This project is intended as a logic programming and automated reasoning exercise focused on the resolution principle. It is useful for understanding how proof search, clause generation, and variable unification work in symbolic AI.

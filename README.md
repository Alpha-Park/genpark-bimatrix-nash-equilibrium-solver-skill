# genpark-bimatrix-nash-equilibrium-solver-skill

[![Stars](https://img.shields.io/github/stars/alphaparkinc/genpark-bimatrix-nash-equilibrium-solver-skill?style=social)](https://github.com/alphaparkinc/genpark-bimatrix-nash-equilibrium-solver-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pure Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20External-brightgreen.svg)]()

> Bimatrix strategic game solver detecting pure Nash equilibria and computing mixed Nash equilibria for 2x2 matrix games.

---

## Architectural Overview

```mermaid
graph TD
    A[Strategic Agents / Bidders] -->|Preferences / Valuations| B[Game Theory Engine]
    B --> C[Mechanism Design & Equilibrium Solver]
    C --> D[Payoff Allocation & Stable Allocation]
```

## Features
- **Pure Python Standard Library**: Zero third-party dependencies required.
- **Model Context Protocol (MCP)**: Native JSON-RPC server ready for LLM integration.
- **Deterministic Verification**: End-to-end sandbox tested with 100% pass rate.

## Quickstart

```bash
python example_usage.py
```

## Running the MCP Server

```bash
python mcp_server.py
```

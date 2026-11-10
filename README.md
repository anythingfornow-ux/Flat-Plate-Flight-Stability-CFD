# Flat-Plate-Flight-Stability-CFD
3D CFD study of a flat-plate wing for flight stability analysis.
# 3D CFD Analysis of a Diamond-Shaped Flat-Plate Wing

## Project Overview
This project presents a preliminary three-dimensional Computational Fluid Dynamics (CFD) analysis of a diamond-shaped flat-plate wing using SU2.

The simulation investigates the airflow around the wing at a single angle of attack of 0°.

## Geometry
- Wing configuration: Diamond-shaped flat plate
- Planform dimensions: 0.99 m × 0.99 m square, rotated by 45°
- Diagonal length: approximately 1.4001 m
- Thickness: 0.01 m

## Simulation Setup
| Parameter | Value |
|---|---|
| CFD solver | SU2 |
| Solver type | Inviscid Euler |
| Freestream velocity | 15 m/s |
| Angle of attack | 0° |
| Air density | 1.225 kg/m³ (approximately) |
| Mesh type | 3D tetrahedral |
| Mesh elements | 6,056 |

## Methodology
1. Created the diamond-shaped wing geometry using Python.
2. Generated the surrounding airflow domain using Gmsh.
3. Generated a three-dimensional tetrahedral mesh.
4. Defined inlet, outlet, farfield and wing boundary markers.
5. Configured the SU2 Euler solver.
6. Executed the CFD simulation and exported the flow-field and surface data.

## Repository Contents
- `notebooks/` – Google Colab simulation notebook.
- `scripts/` – Python geometry-generation script.
- `docs/` – Project documentation and validation checklist.
- `results/` – Mesh, solver configuration, history, surface data and flow visualisation.

## Tools Used
- Python
- Google Colab
- Gmsh
- SU2
- PyVista
- Plotly

## Limitations
This is a preliminary inviscid simulation at a single angle of attack. Viscous effects, boundary-layer behaviour and mesh independence have not been investigated. Solver completion does not by itself establish convergence or experimental validation.

## Project Status
Initial 3D CFD simulation completed. Further validation and aerodynamic analysis remain possible extensions.

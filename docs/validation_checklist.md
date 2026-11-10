# CFD validation checklist

- Confirm the real plate dimensions, thickness, chord/span axes and diamond orientation.
- Inspect STL bounds and verify the STL is watertight.
- Run checkMesh; resolve severe mesh-quality problems.
- Refine leading edge, trailing edge and tips; check near-wall resolution.
- Verify inlet velocity/angle, outlet pressure, far-field and no-slip plate conditions.
- Monitor residuals and integrated forces; residual reduction alone is not enough.
- Repeat coarse/medium/fine meshes and compare lift/drag coefficients.
- Compare angle-of-attack trends with safe glide-test observations.
- Recognise steady RANS may miss unsteady leading-edge vortices and stall.

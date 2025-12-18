# Simulation Parameters Worksheet

Use this worksheet to keep track of all your simulation parameters. Once you've determined all values, you can easily transfer them to main.tex.

## Student Information
- **Name**: _________________________
- **Student ID**: _________________________
- **Date**: _________________________

---

## Geometry Parameters

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Specimen Length | L | _______ | mm |
| Specimen Width | W | _______ | mm |
| Specimen Thickness | t | _______ | mm |
| Initial Crack Length | a₀ | _______ | mm |

---

## Bulk Material Properties

| Property | Symbol | Value | Unit |
|----------|--------|-------|------|
| Young's Modulus | E | _______ | GPa or MPa |
| Poisson's Ratio | ν | _______ | - |
| Density | ρ | _______ | kg/m³ or tonne/mm³ |
| Yield Strength (if applicable) | σy | _______ | MPa |

**Material Name**: _________________________

---

## Cohesive Zone Parameters

| Parameter | Symbol | Value | Unit | Notes |
|-----------|--------|-------|------|-------|
| Maximum Normal Traction | T_max or σ_max | _______ | MPa | Damage initiation |
| Fracture Energy | Gc | _______ | N/mm or kJ/m² | Critical energy release rate |
| Initial Stiffness | K | _______ | N/mm³ or MPa/mm | Penalty stiffness |
| Separation at Damage Init. | δ₀ | _______ | mm | δ₀ = T_max/K |
| Critical Separation | δc | _______ | mm | Complete failure |

**Traction-Separation Law Type**: 
- [ ] Bilinear
- [ ] Exponential
- [ ] Other: _________________________

---

## Mesh Parameters

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Element Size (Crack Region) | _______ | mm | Fine mesh |
| Element Size (Bulk Region) | _______ | mm | Coarse mesh |
| Number of Elements | _______ | - | Total |
| Number of Nodes | _______ | - | Total |
| Element Type (Bulk) | _______ | - | e.g., CPS4R, CPE4 |
| Element Type (Cohesive) | _______ | - | e.g., COH2D4 |

**Estimated Cohesive Zone Length**:
```
l_cz ≈ (9π/32) × (E × Gc) / (T_max²) = _______ mm
```

**Number of Elements in Cohesive Zone**: _______ (recommended: ≥ 3)

---

## Loading and Boundary Conditions

| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| Applied Displacement | Δ or u | _______ | mm | Maximum displacement |
| Loading Rate | _______ | mm/s | If time-dependent |
| Displacement Increment | _______ | mm | Per step |

**Boundary Conditions**:
- Bottom edge: 
  - [ ] Fixed in Y (uy = 0)
  - [ ] Fixed in X and Y
- Top edge:
  - [ ] Prescribed displacement in Y
  - [ ] Prescribed force
- Symmetry: 
  - [ ] No symmetry
  - [ ] X-symmetry
  - [ ] Y-symmetry

---

## Analysis Settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| Analysis Type | [ ] Static [ ] Dynamic | |
| Time Period | _______ | Total analysis time |
| Initial Increment | _______ | Starting time increment |
| Minimum Increment | _______ | Smallest allowed increment |
| Maximum Increment | _______ | Largest allowed increment |
| Nonlinear Geometry | [ ] ON [ ] OFF | Large deformations |

**Solver**: 
- [ ] Abaqus/Standard (Implicit)
- [ ] Abaqus/Explicit

---

## Key Results (Fill in after simulation)

### Force-Displacement Response

| Result | Value | Unit |
|--------|-------|------|
| Peak Load | F_max = _______ | N or kN |
| Displacement at Peak Load | Δ_max = _______ | mm |
| Final Failure Displacement | Δ_f = _______ | mm |
| Initial Stiffness (slope) | k = _______ | N/mm |

### Stress Analysis

| Result | Value | Unit | Location |
|--------|-------|------|----------|
| Maximum von Mises Stress | σ_VM,max = _______ | MPa | _________ |
| Maximum Principal Stress | σ₁,max = _______ | MPa | _________ |
| Stress at Crack Tip | σ_tip = _______ | MPa | _________ |

### Energy Balance

| Energy Component | Value | Unit |
|------------------|-------|------|
| External Work | W_ext = _______ | N·mm or J |
| Strain Energy | U = _______ | N·mm or J |
| Energy Dissipated in CZ | G_diss = _______ | N·mm or J |
| Total Energy | E_total = _______ | N·mm or J |

### Crack Propagation

| Parameter | Value | Unit |
|-----------|-------|------|
| Crack Extension | Δa = _______ | mm |
| Final Crack Length | a_f = _______ | mm |
| Crack Opening (COD) at peak | δ_peak = _______ | mm |

---

## Convergence Study (Optional)

If you perform a mesh convergence study, record results here:

| Mesh Density | # Elements | Peak Load (N) | Δ_max (mm) | Runtime |
|--------------|------------|---------------|------------|---------|
| Coarse | _______ | _______ | _______ | _______ |
| Medium | _______ | _______ | _______ | _______ |
| Fine | _______ | _______ | _______ | _______ |
| Very Fine | _______ | _______ | _______ | _______ |

**Converged Result**: _________________________

---

## Parametric Study (Optional)

If you vary cohesive parameters, record results here:

### Varying Maximum Traction (T_max)

| T_max (MPa) | Peak Load (N) | Δ_max (mm) | Notes |
|-------------|---------------|------------|-------|
| _______ | _______ | _______ | _______ |
| _______ | _______ | _______ | _______ |
| _______ | _______ | _______ | _______ |

### Varying Fracture Energy (Gc)

| Gc (N/mm) | Peak Load (N) | Δ_max (mm) | Notes |
|-----------|---------------|------------|-------|
| _______ | _______ | _______ | _______ |
| _______ | _______ | _______ | _______ |
| _______ | _______ | _______ | _______ |

---

## Notes and Observations

Use this space to record important observations, issues encountered, or insights:

```
_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
```

---

## Checklist Before Finalizing Report

- [ ] All geometry parameters confirmed
- [ ] Material properties verified from literature/datasheets
- [ ] Cohesive parameters justified/calibrated
- [ ] Mesh convergence checked
- [ ] Analysis completed without errors
- [ ] All results extracted and recorded
- [ ] Figures exported from Abaqus
- [ ] Values transferred to main.tex
- [ ] Units are consistent throughout
- [ ] Calculations verified

---

## References Used

List papers, textbooks, or datasheets used to determine parameters:

1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________
4. _________________________________________________________________
5. _________________________________________________________________

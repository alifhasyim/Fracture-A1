# Quick Start Guide - Cohesive Zone Modeling Assignment

This guide will help you complete your Computational Fracture Mechanics assignment using the provided templates.

## Step-by-Step Workflow

### Step 1: Understand the Assignment
Read through the main.tex file to understand what needs to be included in your report:
- Theory of cohesive zone modeling
- Abaqus simulation methodology
- Results and analysis
- Discussion of findings

### Step 2: Customize the Abaqus Script (Optional)

If you want to modify the simulation parameters, edit `cohesive_model.py`:

```python
# Geometry parameters (lines 14-18)
SPECIMEN_LENGTH = 100.0  # Change this to your desired length
SPECIMEN_WIDTH = 50.0    # Change this to your desired width
CRACK_LENGTH = 20.0      # Change this to your initial crack length

# Material properties (lines 20-22)
YOUNGS_MODULUS = 210000.0  # Change to match your material
POISSON_RATIO = 0.3        # Change to match your material

# Cohesive zone properties (lines 24-26)
MAX_TRACTION = 50.0      # Adjust based on material strength
FRACTURE_ENERGY = 0.5    # Adjust based on material toughness
```

### Step 3: Run the Abaqus Simulation

#### Option A: Interactive Mode
```bash
abaqus cae script=cohesive_model.py
```
This opens Abaqus CAE and creates the model. You can then:
1. Inspect the model visually
2. Make manual adjustments if needed
3. Submit the job from the GUI

#### Option B: Batch Mode
```bash
abaqus cae noGUI=cohesive_model.py
```
This creates the model without opening the GUI (faster).

#### Option C: Manual Creation
Follow the methodology section in main.tex to create the model manually in Abaqus CAE.

### Step 4: Run the Analysis

After creating the model:
1. In Abaqus CAE, go to **Job Manager**
2. Select the job (default name: `CohesiveZone_Job`)
3. Click **Submit**
4. Monitor the job progress
5. Once complete, click **Results** to open Abaqus/Viewer

### Step 5: Extract Results and Create Figures

#### 5.1 Mesh Visualization
1. In Abaqus/Viewer, go to **View → ODB Display Options**
2. Show undeformed model with mesh
3. **File → Print → Save As** → `figures/mesh.png`

#### 5.2 Force-Displacement Curve
1. **Tools → XY Data → Create**
2. Select **ODB history output**
3. Choose reaction force (RF2) vs displacement (U2)
4. **File → Print → Save As** → `figures/force_displacement.png`

#### 5.3 Stress Distribution
1. **Plot → Contours**
2. Select **S, Mises** (von Mises stress)
3. Choose an appropriate increment (e.g., at peak load)
4. **File → Print → Save As** → `figures/stress_distribution.png`

#### 5.4 Damage Evolution
1. **Plot → Contours**
2. Select **SDEG** (scalar stiffness degradation)
3. Choose increment showing significant damage
4. **File → Print → Save As** → `figures/damage_evolution.png`

#### 5.5 Crack Opening Displacement
1. **Tools → Path → Create**
2. Define path along crack line
3. **Tools → XY Data → Create** → **Path**
4. Plot opening displacement along path
5. **File → Print → Save As** → `figures/crack_opening.png`

### Step 6: Complete the LaTeX Report

#### 6.1 Add Your Information
Edit `main.tex` and update:
```latex
\author{Your Name \\              % Line ~32: Add your name
    \small Student ID: XXXXXXXX \\    % Add your student ID
```

#### 6.2 Fill in Numerical Values
Search for `[specify value]` in main.tex and replace with your actual values:
- Geometry dimensions
- Material properties
- Cohesive zone parameters
- Results (peak load, critical displacement, etc.)

#### 6.3 Uncomment Figure Includes
Find lines like:
```latex
% \includegraphics[width=0.8\textwidth]{figures/mesh.png}
```
Remove the `%` to uncomment:
```latex
\includegraphics[width=0.8\textwidth]{figures/mesh.png}
```

#### 6.4 Add Your Analysis
Complete the following sections with your specific findings:
- Results interpretation
- Discussion of cohesive parameter effects
- Mesh sensitivity analysis (if performed)
- Comparison with theory

### Step 7: Compile the LaTeX Document

#### On Windows (MiKTeX/TeX Live)
```cmd
pdflatex main.tex
pdflatex main.tex
```

#### On Linux/macOS
```bash
pdflatex main.tex
pdflatex main.tex
```

#### Using Overleaf
1. Create a new project on overleaf.com
2. Upload all files (main.tex, figures/*)
3. Click **Recompile**

### Step 8: Review Your Report

Open `main.pdf` and check:
- [ ] All figures appear correctly
- [ ] All values are filled in (no `[specify value]` remaining)
- [ ] Table of contents is complete
- [ ] References are formatted correctly
- [ ] Your name and information are correct
- [ ] Page numbers are present
- [ ] All sections are complete

### Step 9: Final Checks

Before submission:
1. Spell-check your additions
2. Verify all equations are formatted correctly
3. Ensure figure captions are descriptive
4. Check that units are consistent
5. Verify all references are cited in text

## Common Issues and Solutions

### LaTeX Compilation Errors

**Error: "File not found"**
- Make sure figures are in the `figures/` directory
- Check that filenames match exactly (case-sensitive)

**Error: "Undefined control sequence"**
- Check for typos in LaTeX commands
- Ensure all required packages are installed

**Error: "Missing $ inserted"**
- Check for unescaped special characters (_ # % & etc.)
- Ensure math mode is used correctly

### Abaqus Issues

**Script Error: "Part not found"**
- Check that all coordinate values are correct
- Verify part names match in script

**Analysis Error: "Too many attempts"**
- Reduce initial increment size
- Increase minimum increment size
- Check cohesive stiffness (try reducing if too high)

**Convergence Issues**
- Refine mesh near crack tip
- Adjust cohesive zone parameters
- Use automatic stabilization (carefully)

## Tips for Success

1. **Start Early**: Run the simulation early to identify any issues
2. **Save Often**: Save your Abaqus model (.cae) and LaTeX work frequently
3. **Document Everything**: Take notes while running simulations
4. **Multiple Figures**: Create more visualizations than required, then select the best
5. **Parametric Study**: Try different cohesive parameters to understand their effects
6. **Ask for Help**: If stuck, consult course materials or instructor

## Submission Checklist

- [ ] Abaqus model runs successfully
- [ ] All required figures generated
- [ ] LaTeX document compiles without errors
- [ ] All placeholder values filled in
- [ ] Figures properly labeled and referenced
- [ ] Analysis and discussion complete
- [ ] PDF generated and reviewed
- [ ] File size reasonable (<10 MB)

## Resources

- **Abaqus Documentation**: Help → Search → "Cohesive behavior"
- **LaTeX Help**: https://en.wikibooks.org/wiki/LaTeX
- **Fracture Mechanics**: Refer to course textbook and lectures
- **Repository Files**:
  - `COMPILE_INSTRUCTIONS.md` - Detailed LaTeX compilation guide
  - `figures/README.md` - Figure export instructions
  - `main.tex` - Complete report template with examples

Good luck with your assignment!

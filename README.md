# Fracture-A1: Computational Fracture Mechanics

This repository contains a comprehensive LaTeX report template and Abaqus Python script for the first assignment of Computational Fracture Mechanics. The project focuses on modeling crack propagation using cohesive zone modeling (CZM) in Abaqus under uniaxial tension.

## Repository Contents

- **main.tex** - Complete LaTeX report template with all sections for documenting your simulation
- **cohesive_model.py** - Abaqus Python script to automate model creation
- **COMPILE_INSTRUCTIONS.md** - Detailed instructions for compiling the LaTeX document
- **figures/** - Directory for storing simulation results and figures
- **.gitignore** - Git ignore file for LaTeX auxiliary files

## Quick Start

### 1. Run the Abaqus Simulation

```bash
# In Abaqus CAE
abaqus cae script=cohesive_model.py

# Or submit the job directly
abaqus cae noGUI=cohesive_model.py
```

### 2. Export Results

- Open the results file (.odb) in Abaqus/Viewer
- Export figures (mesh, stress contours, force-displacement curves, etc.)
- Save figures to the `figures/` directory

### 3. Complete the Report

- Edit `main.tex` to add your specific values and results
- Fill in the bracketed placeholders `[specify value]`
- Uncomment figure includes and update filenames
- Add your name, student ID, and course information

### 4. Compile the LaTeX Document

```bash
pdflatex main.tex
pdflatex main.tex  # Run twice for references
```

See `COMPILE_INSTRUCTIONS.md` for detailed compilation instructions.

## Report Features

The LaTeX template includes:
- Professional formatting with proper sections
- Comprehensive coverage of cohesive zone modeling theory
- Detailed methodology section for Abaqus implementation
- Placeholder sections for results and discussion
- References to key fracture mechanics literature
- Appendices with Abaqus input file examples and post-processing guidelines

## Abaqus Script Features

The Python script (`cohesive_model.py`) automatically creates:
- 2D plane stress specimen geometry
- Cohesive zone elements along crack path
- Appropriate material definitions (bulk and cohesive)
- Boundary conditions for uniaxial tension
- Mesh with refinement capabilities
- Analysis step with proper solver settings
- Output requests for post-processing

## Customization

Both the LaTeX template and Python script are designed to be easily customizable:
- Modify geometry parameters in the Python script
- Adjust material properties to match your study
- Update the report sections to reflect your specific analysis
- Add additional figures and results as needed

## Support

For detailed instructions, see:
- `COMPILE_INSTRUCTIONS.md` - LaTeX compilation guide
- `figures/README.md` - Figure export instructions
- Comments in `cohesive_model.py` - Script usage guide

## License

This template is provided for educational purposes for the Computational Fracture Mechanics course.

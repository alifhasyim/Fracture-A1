# Fracture-A1: Computational Fracture Mechanics

This repository contains a comprehensive LaTeX report template and Abaqus Python script for the first assignment of Computational Fracture Mechanics. The project focuses on modeling crack propagation using cohesive zone modeling (CZM) in Abaqus under uniaxial tension.

## Repository Contents

- **main.tex** - Complete LaTeX report template with all sections for documenting your simulation
- **cohesive_model.py** - Abaqus Python script template demonstrating model structure (Note: This is a learning template and does not include complete cohesive zone implementation)
- **COMPILE_INSTRUCTIONS.md** - Detailed instructions for compiling the LaTeX document
- **figures/** - Directory for storing simulation results and figures
- **.gitignore** - Git ignore file for LaTeX auxiliary files

## Important Note About the Python Script

The `cohesive_model.py` script provides a template structure for an Abaqus model but does **not** include a complete cohesive zone implementation. It demonstrates:
- Basic model structure and Python scripting in Abaqus
- Material definitions (bulk and cohesive properties)
- Boundary conditions and analysis setup
- Mesh generation basics

**For a complete cohesive zone model**, you should:
1. Create the model manually in Abaqus CAE following the methodology in `main.tex`, OR
2. Study Abaqus documentation and extend the Python script to include proper cohesive zone implementation

**Recommended approach**: Use surface-based cohesive behavior in Abaqus CAE (easier than cohesive elements).

## Quick Start

### 1. Create the Abaqus Model

**Recommended Approach: Manual Creation in Abaqus CAE**
- Open Abaqus CAE
- Follow the detailed methodology in `main.tex` to create the model
- Use surface-based cohesive behavior (see Abaqus documentation)
- Save your model

**Alternative: Use the Python Script as a Starting Point**
```bash
# This creates a basic model structure (NOT a complete cohesive zone model)
abaqus cae script=cohesive_model.py
# Then modify the model in Abaqus CAE to add cohesive zone behavior
```

### 2. Run the Simulation

- In Abaqus CAE, submit your analysis job
- Monitor the job progress
- Once complete, open the results file (.odb) in Abaqus/Viewer

### 3. Export Results

- In Abaqus/Viewer, create visualizations
- Export figures (mesh, stress contours, force-displacement curves, etc.)
- Save figures to the `figures/` directory

### 4. Complete the Report

- Edit `main.tex` to add your specific values and results
- Fill in the bracketed placeholders `[specify value]`
- Uncomment figure includes and update filenames
- Add your name, student ID, and course information

### 5. Compile the LaTeX Document

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

The Python script (`cohesive_model.py`) demonstrates:
- Basic 2D plane stress model structure in Abaqus Python
- Material property definitions (bulk and cohesive)
- Boundary conditions for uniaxial tension
- Analysis step configuration
- Output requests for post-processing

**Note**: This is a template for learning. A complete cohesive zone implementation requires additional work (see comments in the script).

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

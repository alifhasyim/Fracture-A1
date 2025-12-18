# Fracture-A1: Computational Fracture Mechanics Report

This repository contains a LaTeX report template for the first assignment of Computational Fracture Mechanics, focusing on cohesive zone modeling of crack propagation under uniaxial tension using Abaqus.

## Contents

- `main.tex` - Main LaTeX document containing the complete report structure
- `figures/` - Directory for storing simulation results and figures from Abaqus
- `.gitignore` - Git ignore file for LaTeX auxiliary files

## Report Structure

The report includes the following sections:

1. **Abstract** - Summary of the computational study
2. **Introduction** - Background on fracture mechanics and cohesive zone modeling
3. **Theoretical Background** - Cohesive zone model theory and traction-separation laws
4. **Methodology** - Problem description, FE model setup, and Abaqus implementation
5. **Results** - Force-displacement curves, stress distributions, crack opening profiles, and damage evolution
6. **Discussion** - Analysis of cohesive parameters, mesh sensitivity, and comparisons
7. **Conclusion** - Summary of findings and future work
8. **References** - Bibliography of relevant literature
9. **Appendices** - Abaqus input file examples and post-processing guidelines

## How to Compile

### Prerequisites

You need a LaTeX distribution installed on your system:
- **Windows**: MiKTeX or TeX Live
- **macOS**: MacTeX
- **Linux**: TeX Live

### Compilation Instructions

#### Method 1: Using pdflatex (Recommended)

```bash
pdflatex main.tex
pdflatex main.tex  # Run twice for references and table of contents
```

#### Method 2: Using latexmk (Automated)

```bash
latexmk -pdf main.tex
```

#### Method 3: Using Online LaTeX Editor

Upload the files to [Overleaf](https://www.overleaf.com) or another online LaTeX editor and compile there.

### Cleaning Auxiliary Files

To clean up auxiliary files generated during compilation:

```bash
latexmk -c main.tex
```

Or manually delete files matching patterns in `.gitignore`.

## Adding Your Simulation Results

1. **Export figures from Abaqus**:
   - In Abaqus/CAE or Abaqus/Viewer, use File → Print → Save As to export images
   - Recommended format: PNG (for raster images) or PDF/EPS (for vector graphics)
   - Save images to the `figures/` directory

2. **Update the LaTeX document**:
   - Uncomment the `\includegraphics` commands in `main.tex`
   - Replace placeholder filenames with your actual figure filenames
   - Example:
     ```latex
     \includegraphics[width=0.8\textwidth]{figures/mesh.png}
     ```

3. **Add your data**:
   - Fill in the bracketed placeholders `[specify value]` with your actual values
   - Update material properties, geometry dimensions, and simulation parameters
   - Add your name, student ID, and course information in the title section

## Recommended Figures to Include

Based on the report structure, you should generate and include the following figures from your Abaqus simulation:

1. **mesh.png** - Finite element mesh showing refinement near crack tip
2. **force_displacement.png** - Force-displacement curve
3. **stress_distribution.png** - Von Mises stress contour plot
4. **crack_opening.png** - Crack opening displacement profile
5. **damage_evolution.png** - Damage variable in cohesive elements
6. **energy_balance.png** - Energy components plot

## Customization Tips

- **Adjust geometry settings**: Modify the `\geometry` package parameters in the preamble
- **Change citation style**: Modify the bibliography style (currently using basic style)
- **Add more figures**: Use the provided figure templates as examples
- **Include code listings**: Use the `lstlisting` environment for Abaqus Python scripts or input files

## Package Dependencies

The template uses the following LaTeX packages:
- `amsmath`, `amsfonts`, `amssymb` - Mathematical symbols and equations
- `graphicx` - Including graphics
- `geometry` - Page layout
- `float`, `caption`, `subcaption` - Figure placement and captions
- `hyperref` - Hyperlinks and PDF metadata
- `cite` - Citation management
- `booktabs`, `multirow` - Table formatting
- `siunitx` - SI units
- `listings`, `xcolor` - Code listings

All packages should be included in standard LaTeX distributions.

## Support

For issues with:
- **LaTeX compilation**: Check the `.log` file for error messages
- **Abaqus simulation**: Refer to Abaqus documentation or course materials
- **Template structure**: Modify sections as needed for your specific assignment requirements

## License

This template is provided for educational purposes for the Computational Fracture Mechanics course.

## References

The template includes references to key papers in cohesive zone modeling:
- Barenblatt (1962) - Pioneering work on cohesive zones
- Dugdale (1960) - Cohesive zone model for yielding
- Hillerborg et al. (1976) - Fictitious crack model
- Park & Paulino (2011) - Critical review of cohesive zone models

Add additional references as needed for your specific study.

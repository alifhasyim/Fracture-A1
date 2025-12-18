# Figures Directory

This directory is for storing figures and images generated from your Abaqus simulation.

## Recommended Figures

Place the following figures from your Abaqus simulation here:

1. **mesh.png** - Finite element mesh with refinement near the crack tip
2. **force_displacement.png** - Force-displacement curve showing crack propagation
3. **stress_distribution.png** - Von Mises stress distribution contour plot
4. **crack_opening.png** - Crack opening displacement (COD) profile
5. **damage_evolution.png** - Damage variable evolution in cohesive elements
6. **energy_balance.png** - Plot of energy components during analysis

## Exporting Figures from Abaqus

### Method 1: From Abaqus/CAE or Abaqus/Viewer

1. Open your results file (.odb) in Abaqus/Viewer
2. Create the desired visualization (contour plot, XY plot, etc.)
3. Go to **File → Print → Save As**
4. Choose format (PNG recommended for reports)
5. Save to this directory

### Method 2: Using Python Scripts

You can automate figure export using Abaqus Python scripts:

```python
from odbAccess import *
import visualization

# Open ODB file
odb = openOdb('your_job.odb')
viewport = session.viewports['Viewport: 1']
viewport.setValues(displayedObject=odb)

# Create contour plot
viewport.odbDisplay.display.setValues(plotState=(CONTOURS_ON_DEF,))
viewport.odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT,
    refinement=(INVARIANT, 'Mises'))

# Save image
session.printOptions.setValues(vpBackground=OFF)
session.printToFile(fileName='figures/stress_distribution.png',
                    format=PNG, canvasObjects=(viewport,))
```

## Figure Format Recommendations

- **Resolution**: At least 300 DPI for publication quality
- **Format**: PNG for raster images, PDF/EPS for vector graphics
- **Size**: Images should be clear when included at 80% text width
- **Labels**: Ensure all axes are labeled and legible

## Including Figures in LaTeX

Once you've added figures to this directory, uncomment and update the corresponding `\includegraphics` commands in `main.tex`:

```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{figures/your_figure.png}
    \caption{Your figure caption}
    \label{fig:your_label}
\end{figure}
```

"""
Abaqus Python Script for Cohesive Zone Modeling - TEMPLATE
This script demonstrates the structure for creating a cohesive zone model
for crack propagation analysis under uniaxial tension.

IMPORTANT NOTES:
1. This is a SIMPLIFIED TEMPLATE. For a complete cohesive zone model, you will need to:
   - Create proper partitions for the crack path
   - Insert cohesive elements along the crack interface
   - Assign the cohesive section to cohesive elements
   
2. Two common approaches for implementing cohesive zones in Abaqus:
   a) Use surface-based cohesive behavior (easier - recommended for beginners)
   b) Use cohesive elements with partitioned geometry (shown here, but incomplete)
   c) Use XFEM for arbitrary crack paths (advanced)

3. This script creates the basic model structure. You should:
   - Study the Abaqus documentation on cohesive elements
   - Consider using surface-based cohesive behavior as an alternative
   - Modify the script based on your specific requirements
   - Test the model incrementally

4. For a working example, consider creating the model manually in Abaqus CAE first,
   then use this script as a reference for automation.

Usage: abaqus cae script=cohesive_model.py

RECOMMENDED ALTERNATIVE: Use surface-based cohesive behavior instead of
cohesive elements. This is simpler and more robust. See the Abaqus documentation
section "Modeling with cohesive elements" for details.
"""

from abaqus import *
from abaqusConstants import *
import regionToolset

# Model parameters
MODEL_NAME = 'CohesiveZoneModel'
SPECIMEN_LENGTH = 100.0  # mm
SPECIMEN_WIDTH = 50.0   # mm
CRACK_LENGTH = 20.0     # mm
THICKNESS = 1.0         # mm (for plane stress)

# Material properties - Bulk material
YOUNGS_MODULUS = 210000.0  # MPa
POISSON_RATIO = 0.3
DENSITY = 7.8e-9  # tonne/mm^3

# Cohesive zone properties
COHESIVE_STIFFNESS = 1e6  # N/mm^3
MAX_TRACTION = 50.0       # MPa
FRACTURE_ENERGY = 0.5     # N/mm

# Mesh parameters
ELEMENT_SIZE_CRACK = 0.5  # mm (fine mesh near crack)
ELEMENT_SIZE_BULK = 2.0   # mm (coarse mesh elsewhere)

# Analysis parameters
DISPLACEMENT = 1.0  # mm (applied displacement)
INITIAL_INCREMENT = 0.01
MIN_INCREMENT = 1e-8
MAX_INCREMENT = 0.1

# ============================================================================
# CREATE MODEL
# ============================================================================

print('Creating model...')
mdb.Model(name=MODEL_NAME)
myModel = mdb.models[MODEL_NAME]

# Delete default model
if 'Model-1' in mdb.models.keys():
    del mdb.models['Model-1']

# ============================================================================
# CREATE PARTS
# ============================================================================

print('Creating parts...')

# Create sketch for specimen
s = myModel.ConstrainedSketch(name='__profile__', sheetSize=200.0)

# Draw rectangle for specimen
s.rectangle(point1=(0.0, 0.0), point2=(SPECIMEN_LENGTH, SPECIMEN_WIDTH))

# Create part
part = myModel.Part(name='Specimen', dimensionality=TWO_D_PLANAR, 
                    type=DEFORMABLE_BODY)
part.BaseShell(sketch=s)
del myModel.sketches['__profile__']

# ============================================================================
# CREATE PARTITION FOR CRACK PATH
# ============================================================================

print('Creating crack path partition...')

# NOTE: This is a simplified example. For a complete cohesive zone implementation,
# you need to create proper partitions to insert cohesive elements.
# 
# RECOMMENDED APPROACH: Use surface-based cohesive behavior instead:
# 1. Create two separate parts (upper and lower halves)
# 2. Assemble them with a small gap or touching
# 3. Define surface-based cohesive behavior between them
#
# The code below is commented out as it's incomplete for cohesive elements.

# Example of what you might do for partitioning:
# 1. Partition the face to create the crack path
# 2. Create a datum plane along the crack
# 3. Use PartitionFaceByShortestPath or similar to split the geometry
# 
# For detailed examples, refer to Abaqus Example Problems Manual:
# "Crack propagation using cohesive elements"

# ============================================================================
# DEFINE MATERIALS
# ============================================================================

print('Defining materials...')

# Bulk material
bulkMaterial = myModel.Material(name='Steel')
bulkMaterial.Elastic(table=((YOUNGS_MODULUS, POISSON_RATIO), ))
bulkMaterial.Density(table=((DENSITY, ), ))

# Cohesive material
cohesiveMaterial = myModel.Material(name='CohesiveMaterial')
cohesiveMaterial.Elastic(type=TRACTION, table=(
    (COHESIVE_STIFFNESS, COHESIVE_STIFFNESS, COHESIVE_STIFFNESS), ))
cohesiveMaterial.MaxsDamageInitiation(table=((MAX_TRACTION, ), ))
cohesiveMaterial.DamageEvolution(type=ENERGY, table=((FRACTURE_ENERGY, ), ))

# ============================================================================
# CREATE SECTIONS
# ============================================================================

print('Creating sections...')

# Solid section for bulk material
myModel.HomogeneousSolidSection(name='BulkSection', 
                                material='Steel', 
                                thickness=THICKNESS)

# Cohesive section
myModel.CohesiveSection(name='CohesiveSection', 
                        material='CohesiveMaterial',
                        response=TRACTION_SEPARATION,
                        outOfPlaneThickness=THICKNESS)

# ============================================================================
# ASSIGN SECTIONS
# ============================================================================

print('Assigning sections...')

# Assign bulk section to part
region = (part.faces[:], )
part.SectionAssignment(region=region, sectionName='BulkSection')

# NOTE: For a complete cohesive zone model, you would need to:
# 1. Create cohesive elements along the crack interface (requires proper partitioning)
# 2. Create an element set containing those cohesive elements
# 3. Assign the cohesive section to that element set
#
# Example (after creating cohesive elements):
# cohesiveElements = part.elements.getByBoundingBox(...)
# cohesiveSet = part.Set(elements=cohesiveElements, name='CohesiveElements')
# part.SectionAssignment(region=cohesiveSet, sectionName='CohesiveSection')
#
# ALTERNATIVE: Use surface-based cohesive behavior in the assembly step instead

# ============================================================================
# CREATE ASSEMBLY
# ============================================================================

print('Creating assembly...')

myAssembly = myModel.rootAssembly
myAssembly.DatumCsysByDefault(CARTESIAN)
instance = myAssembly.Instance(name='Specimen-1', part=part, dependent=ON)

# ============================================================================
# CREATE SETS FOR BOUNDARY CONDITIONS
# ============================================================================

print('Creating sets...')

# Bottom edge (y = 0)
bottomEdges = instance.edges.findAt(((SPECIMEN_LENGTH/2, 0.0, 0.0),))
myAssembly.Set(edges=bottomEdges, name='BottomEdge')

# Top edge (y = WIDTH)
topEdges = instance.edges.findAt(((SPECIMEN_LENGTH/2, SPECIMEN_WIDTH, 0.0),))
myAssembly.Set(edges=topEdges, name='TopEdge')

# Reference point for reaction force
rp = myAssembly.ReferencePoint(point=(SPECIMEN_LENGTH/2, SPECIMEN_WIDTH, 0.0))
refPoints = (myAssembly.referencePoints[rp.id], )
myAssembly.Set(referencePoints=refPoints, name='RefPoint')

# ============================================================================
# CREATE STEP
# ============================================================================

print('Creating analysis step...')

myModel.StaticStep(name='Loading', 
                   previous='Initial',
                   description='Apply tensile displacement',
                   timePeriod=1.0,
                   initialInc=INITIAL_INCREMENT,
                   minInc=MIN_INCREMENT,
                   maxInc=MAX_INCREMENT,
                   nlgeom=ON)

# ============================================================================
# DEFINE BOUNDARY CONDITIONS
# ============================================================================

print('Defining boundary conditions...')

# Fix bottom edge in Y direction
myModel.DisplacementBC(name='FixBottom', 
                       createStepName='Initial',
                       region=myAssembly.sets['BottomEdge'],
                       u1=UNSET, u2=0.0, ur3=UNSET)

# Fix one point to prevent rigid body motion
vertices = instance.vertices.findAt(((0.0, 0.0, 0.0),))
fixPoint = myAssembly.Set(vertices=vertices, name='FixedPoint')
myModel.DisplacementBC(name='FixPoint',
                       createStepName='Initial',
                       region=fixPoint,
                       u1=0.0, u2=0.0, ur3=UNSET)

# Apply displacement to top edge
myModel.DisplacementBC(name='ApplyDisplacement',
                       createStepName='Loading',
                       region=myAssembly.sets['TopEdge'],
                       u1=UNSET, u2=DISPLACEMENT, ur3=UNSET)

# ============================================================================
# CREATE MESH
# ============================================================================

print('Creating mesh...')

# Seed part
part.seedPart(size=ELEMENT_SIZE_BULK, deviationFactor=0.1)

# NOTE: For mesh refinement near the crack, you would need to:
# 1. Identify edges along the crack path (requires proper partitioning)
# 2. Seed those edges with finer mesh
#
# Example (after creating crack partitions):
# crackEdges = part.edges.findAt(((CRACK_LENGTH/2, SPECIMEN_WIDTH/2, 0.0),))
# part.seedEdgeBySize(edges=crackEdges, size=ELEMENT_SIZE_CRACK)
#
# For now, using uniform mesh throughout

# Set element type
elemType1 = mesh.ElemType(elemCode=CPS4R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPS3, elemLibrary=STANDARD)
faces = part.faces[:]
pickedRegions = (faces, )
part.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))

# Generate mesh
part.generateMesh()

# ============================================================================
# OUTPUT REQUESTS
# ============================================================================

print('Setting up output requests...')

# Field output
myModel.fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'E', 'U', 'RF', 'STATUS', 'SDEG'))

# History output
regionDef = myAssembly.sets['TopEdge']
myModel.HistoryOutputRequest(name='H-Output-2',
                              createStepName='Loading',
                              variables=('U2', 'RF2'),
                              region=regionDef)

# ============================================================================
# CREATE JOB
# ============================================================================

print('Creating job...')

jobName = 'CohesiveZone_Job'
myJob = mdb.Job(name=jobName, 
                model=MODEL_NAME,
                description='Cohesive zone model - uniaxial tension')

# ============================================================================
# SAVE MODEL
# ============================================================================

print('Saving model...')
mdb.saveAs(pathName=MODEL_NAME + '.cae')

print('\n' + '='*70)
print('Model creation complete!')
print('='*70)
print('\nIMPORTANT: This script creates a basic model structure WITHOUT cohesive elements.')
print('The model created is suitable for:')
print('  1. Learning Abaqus Python scripting')
print('  2. Basic uniaxial tension simulation (without crack propagation)')
print('  3. Template for building more complex models')
print('\nTo implement cohesive zone modeling for crack propagation, you need to:')
print('  1. Create proper geometry partitions for the crack path')
print('  2. Insert cohesive elements along the crack interface, OR')
print('  3. Use surface-based cohesive behavior (recommended approach)')
print('\nFor surface-based cohesive behavior:')
print('  - Create two parts (upper and lower halves of specimen)')
print('  - Define contact interaction with cohesive behavior')
print('  - See Abaqus documentation: "Defining surface-based cohesive behavior"')
print('\nNext steps:')
print('  - Open the .cae file: abaqus cae database=' + MODEL_NAME + '.cae')
print('  - Modify the model to add cohesive zone implementation')
print('  - Refer to Abaqus Example Problems Manual for guidance')
print('='*70)
print('To submit the basic job, use: abaqus job=' + jobName)
print('(Note: This will run but will NOT simulate crack propagation)')
print('='*70 + '\n')

# Optional: Submit job automatically
# myJob.submit()
# myJob.waitForCompletion()
# print('Job completed!')

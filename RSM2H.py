#open 2HRS.txt in C:\Temp after simulation for viewing result
import random
b=1.0
phi=0.8
rho=12.00
Lp=rho*b
path_name='C:/Temp/2HRSAR12VF80'
path_odb1='C:/Temp/Q112HAR12VF80.odb'
path_odb2='C:/Temp/Q222HAR12VF80.odb'
job1_name='Q112HAR12VF80' 
job2_name='Q222HAR12VF80'

w=b/2.00
Lp=rho*b

Gm = 7
num = 0.49
Em = 2*Gm*(1+num)
Q11_1H=461.0268
Q12_1H=53.056
Q22_1H=1230.25
G12_1H=34.1
vg = b/phi - b
hg=0.25*vg
w=b/2.0
lb=hg/2

meshsize=vg/2##mesh size

Lrve=hg+Lp
Wrve=2*(vg+b)
Lrve=hg+Lp
Wrve=2*(vg+b)

from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=121.633964538574, 
    height=118.363288879395)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
Mdb()
s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=5000.0)
g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(lb, 0.0), point2=(lb+Lp, b/2))
s.rectangle(point1=(Lrve - Lp/2,  vg + b*0.5), point2=(Lrve,  vg + b*1.5))
s.rectangle(point1=(lb,  2*vg + b*1.5), point2=(Lrve-lb,  2*vg + b*2))
s.rectangle(point1=(Lp/2, vg + b*1.5), point2=(0, vg + b*.5))
session.viewports['Viewport: 1'].view.fitView()
p = mdb.models['Model-1'].Part(name='Platelet', dimensionality=TWO_D_PLANAR, 
    type=DEFORMABLE_BODY)
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=5000.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.Line(point1=(0.0, 0.0), point2=(lb, 0.0))
s1.Line(point1=(lb, 0.0), point2=(lb, b/2))
s1.Line(point1=(lb, b/2), point2=(lb+Lp, b/2))
s1.Line(point1=(lb+Lp, b/2), point2=(lb+Lp, 0.0))
s1.Line(point1=(lb+Lp, 0.0), point2=(Lrve, 0.0))
session.viewports['Viewport: 1'].view.fitView()
s1.Line(point1=(Lrve, 0.0), point2=(Lrve, vg + b*0.5))
s1.Line(point1=(Lrve, vg + b*0.5), point2=(Lrve- Lp/2,  vg + b*0.5))
s1.Line(point1=(Lrve - Lp/2,  vg + b*0.5), point2=(Lrve - Lp/2,  vg + b*1.5))
s1.Line(point1=(Lrve - Lp/2,  vg + b*1.5), point2=(Lrve,  vg + b*1.5))
s1.Line(point1=(Lrve,  vg + b*1.5), point2=(Lrve,  2*vg + b*2))
s1.Line(point1=(Lrve,  2*vg + b*2), point2=(Lrve-lb,  2*vg + b*2))
s1.Line(point1=(Lrve-lb,  2*vg + b*2), point2=(Lrve-lb,  2*vg + b*1.5))
s1.Line(point1=(Lrve-lb,  2*vg + b*1.5), point2=(lb,  2*vg + b*1.5))
s1.Line(point1=(lb,  2*vg + b*1.5), point2=(lb,  2*vg + b*2))
s1.Line(point1=(lb,  2*vg + b*2), point2=(0,  2*vg + b*2))
s1.Line(point1=(0,  2*vg + b*2), point2=(0,  1*vg + b*1.5))
s1.Line(point1=(0, vg + b*1.5), point2=(Lp/2,  1*vg + b*1.5))
s1.Line(point1=(Lp/2, vg + b*1.5), point2=(Lp/2,  1*vg + b*.5))
s1.Line(point1=(Lp/2, vg + b*.5), point2=(0,  1*vg + b*.5))
s1.Line(point1=(0, vg + b*.5), point2=(0, 0))
p = mdb.models['Model-1'].Part(name='Matrix', dimensionality=TWO_D_PLANAR,type=DEFORMABLE_BODY)
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', 
    sheetSize=5000.0)
g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
s1.setPrimaryObject(option=STANDALONE)
s1.Line(point1=(0.0, 0.0), point2=(lb, 0.0))
s1.Line(point1=(lb, 0.0), point2=(lb, b/2))
s1.Line(point1=(lb, b/2), point2=(0, vg + b/2))
s1.Line(point1=(0,vg + b/2), point2=(0, 0))
s1.Line(point1=(Lrve-lb, 0.0), point2=(Lrve, 0.0))
s1.Line(point1=(Lrve, 0.0), point2=(Lrve,vg + b/2))
s1.Line(point1=(Lrve,vg + b/2), point2=(Lrve-lb, b/2))
s1.Line(point1=(Lrve-lb, b/2), point2=(Lrve-lb, 0))
s1.Line(point1=(Lrve/2, b/2), point2=(Lrve - Lp/2, b/2 + vg))
s1.Line(point1=(Lrve - Lp/2, b/2 + vg), point2=(Lrve - Lp/2, 1.5*b + vg))
s1.Line(point1=(Lrve - Lp/2, 1.5*b + vg), point2=(Lrve/2, 1.5*b + 2*vg))
s1.Line(point1=(Lrve/2, 1.5*b + 2*vg), point2=(Lp/2, 1.5*b + vg))
s1.Line(point1=(Lp/2, 1.5*b + vg), point2=(Lp/2, b/2 + vg))
s1.Line(point1=(Lp/2, b/2 + vg), point2=(Lrve/2, b/2))
s1.Line(point1=(Lrve, 1.5*b + vg), point2=(Lrve, Wrve))
s1.Line(point1=(Lrve, Wrve), point2=(Lrve-lb, Wrve))
s1.Line(point1=(Lrve-lb, Wrve), point2=(Lrve-lb, Wrve- 0.5*b))
s1.Line(point1=(Lrve-lb, Wrve- 0.5*b), point2=(Lrve, 1.5*b + vg))
s1.Line(point1=(0, 1.5*b + vg), point2=(lb, Wrve - 0.5*b))
s1.Line(point1=(lb, Wrve- 0.5*b), point2=(lb, Wrve))
s1.Line(point1=(lb, Wrve), point2=(0, Wrve))
s1.Line(point1=(0, Wrve), point2=(0, 1.5*b + vg))
p = mdb.models['Model-1'].Part(name='EndMatrix', dimensionality=TWO_D_PLANAR,type=DEFORMABLE_BODY)
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()
mdb.models['Model-1'].Material(name='Platelet')
# mdb.models['Model-1'].materials['Platelet'].Elastic(type=LAMINA, table=((
    #Ep11, Ep22, nup12, G12p, G13p, G23p), )) #lamina material
mdb.models['Model-1'].Material(name='Platelet')
mdb.models['Model-1'].materials['Platelet'].Elastic(type=ORTHOTROPIC, table=((
        Q11_1H, Q12_1H, Q22_1H, 1e-10, 1e-10, 1e-10, G12_1H, 1e-10, 1e-10), )) #orthotropic

mdb.models['Model-1'].Material(name='Matrix')
mdb.models['Model-1'].materials['Matrix'].Elastic(table=((Em, num), ))
mdb.models['Model-1'].HomogeneousSolidSection(name='Platelet', 
    material='Platelet', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(name='Matrix', 
    material='Matrix', thickness=None)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Platelet']
a.Instance(name='Part-1-1', part=p, dependent=OFF)
p = mdb.models['Model-1'].parts['Matrix']
a.Instance(name='Part-2-1', part=p, dependent=OFF)
a = mdb.models['Model-1'].rootAssembly
a.InstanceFromBooleanMerge(name='Compositee', instances=(a.instances['Part-1-1'], 
    a.instances['Part-2-1'], ), keepIntersections=ON, 
    originalInstances=SUPPRESS, domain=GEOMETRY)
a = mdb.models['Model-1'].rootAssembly
a.makeIndependent(instances=(a.instances['Compositee-1'], ))
a = mdb.models['Model-1'].rootAssembly
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
p = mdb.models['Model-1'].parts['EndMatrix']
a.Instance(name='EndMatrix-1', part=p, dependent=ON)
a = mdb.models['Model-1'].rootAssembly
a.InstanceFromBooleanCut(name='Composite', 
    instanceToBeCut=mdb.models['Model-1'].rootAssembly.instances['Compositee-1'], 
    cuttingInstances=(a.instances['EndMatrix-1'], ), originalInstances=DELETE)
a.makeIndependent(instances=(a.instances['Composite-1'], ))
p = mdb.models['Model-1'].parts['Composite']
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
platelet_face_point_1 = (0.5*Lrve,b/4,0.0)
platelet_face_point_2 = ((Lp/4),(0.75*b + vg),0.0)
platelet_face_point_3 = ((Lrve- 0.25*Lp),(0.75*b + vg),0.0)
platelet_face_point_4 = (0.5*Lrve,1.75*b + 2*vg,0.0)
platelet_face_1 = p.faces.findAt((platelet_face_point_1,))
platelet_face_2 = p.faces.findAt((platelet_face_point_2,))
platelet_face_3 = p.faces.findAt((platelet_face_point_3,))
platelet_face_4 = p.faces.findAt((platelet_face_point_4,))
platelet_region=(platelet_face_1, platelet_face_2, platelet_face_3, platelet_face_4,)
p = mdb.models['Model-1'].parts['Composite']
p.SectionAssignment(region=platelet_region, sectionName='Platelet', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Composite']
f = p.faces
matrix_face_point_1 = (Lp/4, 0.5*(b+vg),0.0)
matrix_face_point_2 = (Lrve - Lp/4, 0.5*(b+vg),0.0)
matrix_face_point_3 = (Lp/4, 1.5*(b+vg),0.0)
matrix_face_point_4 = (Lrve - Lp/4,1.5*(b+vg),0.0)
matrix_face_1 = p.faces.findAt((matrix_face_point_1,))
matrix_face_2 = p.faces.findAt((matrix_face_point_2,))
matrix_face_3 = p.faces.findAt((matrix_face_point_3,))
matrix_face_4 = p.faces.findAt((matrix_face_point_4,))
matrix_region=(matrix_face_1,matrix_face_2,matrix_face_3,matrix_face_4,)
p = mdb.models['Model-1'].parts['Composite']
p.SectionAssignment(region=matrix_region, sectionName='Matrix', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p1 = mdb.models['Model-1'].parts['Composite']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['Composite']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#f0 ]', ), )
region = regionToolset.Region(faces=faces)
orientation=None
mdb.models['Model-1'].parts['Composite'].MaterialOrientation(region=region, 
    orientationType=GLOBAL, axis=AXIS_3, additionalRotationType=ROTATION_NONE, 
    localCsys=None, fieldName='', stackDirection=STACK_3)
#: Specified material orientation has been assigned to the selected regions.
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=ON)

a = mdb.models['Model-1'].rootAssembly.instances['Composite-1'].faces
rfm=[0]*len(a)
for i in range(0,len(a)):
    rfm[i]= a[i]
rfmr=tuple(rfm)                                         
a = mdb.models['Model-1'].rootAssembly
partInstances =(a.instances['Composite-1'], )

a.seedPartInstance(regions=partInstances, size=meshsize, deviationFactor=0.1, 
    minSizeFactor=0.1)
elemType1 = mesh.ElemType(elemCode=CPE4R, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, hourglassControl=DEFAULT, 
        distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
a.setMeshControls(regions=rfmr, elemShape=QUAD,technique=STRUCTURED)
a.setElementType(regions=rfmr, elemTypes=(elemType1, elemType2))#uncomment to activate plane strain element
a.generateMesh(regions=partInstances)
a = mdb.models['Model-1'].rootAssembly 
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
w1 = a.instances['Composite-1'].edges.findAt((((Lrve/2),Wrve,0.0,),),) 
w2= a.instances['Composite-1'].edges.findAt((((Lrve/2),0.0,0.0,),),) 
Top_edge=w1
Bottom_edge=w2
a.Set(edges=Top_edge, name='TopEdge')
a.Set(edges=Bottom_edge, name='BottomEdge')
w3 = a.instances['Composite-1'].edges.findAt(((0.0,(Wrve/2),0.0,),),)
w4 = a.instances['Composite-1'].edges.findAt(((Lrve,(Wrve/2),0.0,),),)
Left_edge=w3
Right_edge=w4 
a.Set(edges=Left_edge, name='LeftEdge')
a.Set(edges=Right_edge, name='RightEdge')
te=mdb.models['Model-1'].rootAssembly.sets['TopEdge'].nodes
a.Set(name='Top',nodes=te[0:len(te)])
be=mdb.models['Model-1'].rootAssembly.sets['BottomEdge'].nodes
a.Set(name='Bottom',nodes=be[0:len(be)])
le=mdb.models['Model-1'].rootAssembly.sets['LeftEdge'].nodes
re=mdb.models['Model-1'].rootAssembly.sets['RightEdge'].nodes
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
#: Warning: Cannot continue yet--complete the step or cancel the procedure.
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['BottomEdge']
mdb.models['Model-1'].YsymmBC(name='Bottom_Ysymm', createStepName='Step-1', 
    region=region, localCsys=None)
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['TopEdge']
mdb.models['Model-1'].YsymmBC(name='Top_Ysymm', createStepName='Step-1', 
    region=region, localCsys=None)
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['LeftEdge']
mdb.models['Model-1'].XsymmBC(name='Left_Xsymm', createStepName='Step-1', 
    region=region, localCsys=None)
a1 = mdb.models['Model-1'].rootAssembly
region = a1.sets['RightEdge']
mdb.models['Model-1'].DisplacementBC(name='Right_Disp', createStepName='Step-1', 
    region=region, u1=0.01, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
mdb.Job(name=job1_name, model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs[job1_name].submit(consistencyChecking=OFF)
mdb.jobs[job1_name].waitForCompletion()
mdb.models['Model-1'].boundaryConditions['Top_Ysymm'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
    meshTechnique=OFF)
mdb.models['Model-1'].boundaryConditions['Right_Disp'].suppress()
a = mdb.models['Model-1'].rootAssembly
region = a.sets['RightEdge']
mdb.models['Model-1'].XsymmBC(name='Right_Xsym', createStepName='Step-1', 
    region=region, localCsys=None)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['TopEdge']
mdb.models['Model-1'].DisplacementBC(name='Top_Disp', createStepName='Step-1', 
    region=region, u1=UNSET, u2=0.01, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name=job2_name, model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs[job2_name].submit(consistencyChecking=OFF)
mdb.jobs[job2_name].waitForCompletion()
mdb.saveAs(pathName=path_name)
#: The model database has been saved to "C:\Temp\ARVF1.cae".
o3 = session.openOdb(name=path_odb1)
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=0)
#defining the path using coordinates
session.Path(name='yy', type=POINT_LIST, expression=((3*Lp/8, Wrve, 0.0), (3*Lp/8,0, 0.0)))
session.Path(name='xx1', type=POINT_LIST, expression=((0, Wrve/2, 0.0), (Lp/2,Wrve/2, 0.0)))
session.Path(name='xx2', type=POINT_LIST, expression=((Lrve - Lp/2, Wrve/2, 0.0), (Lrve,Wrve/2, 0.0)))
#To take Von Mises Stress
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S11'))


#To find average stress in a path (integrating using trapezoidal rule and dividing by path length)
pth = session.paths['yy']
session.XYDataFromPath(name='Q11', path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
x0 = session.xyDataObjects['Q11']
total=0
for i in range(0,(len(x0)-1)):
    a1=list(x0[i])
    a2=list(x0[i+1])
    c=.5*(a2[0]-a1[0])*(a2[1]+a1[1])
    total=c+total
S11_avg= total/a2[0]
print('S11avg=', S11_avg)
exx=0.01/Lrve
Q11=S11_avg/exx
print('Q11=', Q11)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'))

#To find average stress in a path (integrating using trapezoidal rule and dividing by path length)
pth = session.paths['xx1']
session.XYDataFromPath(name='Q12_1', path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
x0 = session.xyDataObjects['Q12_1']
total=0
for i in range(0,(len(x0)-1)):
    a1=list(x0[i])
    a2=list(x0[i+1])
    c=.5*(a2[0]-a1[0])*(a2[1]+a1[1])
    total=c+total
S12_avg1= total/a2[0]
pth = session.paths['xx2']
session.XYDataFromPath(name='Q12_2', path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
x0 = session.xyDataObjects['Q12_2']
total=0
for i in range(0,(len(x0)-1)):
    a1=list(x0[i])
    a2=list(x0[i+1])
    c=.5*(a2[0]-a1[0])*(a2[1]+a1[1])
    total=c+total
S12_avg2= total/a2[0]

S12_avg=(S12_avg1+S12_avg2)/2

print('S12avg=', S12_avg)
exx=0.01/Lrve
Q12=S12_avg/exx
print('Q12=', Q12)
o3 = session.openOdb(name=path_odb2)
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    deformationScaling=UNIFORM, uniformScaleFactor=0)
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(COMPONENT, 
    'S22'))
#To find average stress in a path (integrating using trapezoidal rule and dividing by path length)
pth = session.paths['xx1']
session.XYDataFromPath(name='Q22_1', path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
x0 = session.xyDataObjects['Q22_1']
total=0
for i in range(0,(len(x0)-1)):
    a1=list(x0[i])
    a2=list(x0[i+1])
    c=.5*(a2[0]-a1[0])*(a2[1]+a1[1])
    total=c+total
S22_avg1= total/a2[0]
pth = session.paths['xx2']
session.XYDataFromPath(name='Q22_2', path=pth, includeIntersections=True, 
    projectOntoMesh=False, pathStyle=PATH_POINTS, numIntervals=10, 
    projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE)
x0 = session.xyDataObjects['Q22_2']
total=0
for i in range(0,(len(x0)-1)):
    a1=list(x0[i])
    a2=list(x0[i+1])
    c=.5*(a2[0]-a1[0])*(a2[1]+a1[1])
    total=c+total
S22_avg2= total/a2[0]
S22_avg=(S22_avg1+S22_avg2)/2
print('S22avg=', S22_avg)
eyy=0.01/Wrve
Q22=S22_avg/eyy
print('Q22=', Q22)
deno=Q11*Q22 - Q12*Q12
S11=Q22/deno
S12=-Q12/deno
S22=Q11/deno
E11=1/S11
with open("2HRS.txt","a") as outfile:
    outfile.write("----------------Start----------------------\n")
    outfile.write("E11=%2f\n" %(E11))
    outfile.write("----------------End----------------------\n")

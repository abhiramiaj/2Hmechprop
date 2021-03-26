#open sw.txt in C:\Temp after simulation for viewing result
import random
rho=12.00
b=1.
path_name='C:/Temp/SWAR30VF90'
path_odb1='C:/Temp/SWAR30VF90Q11.odb'
path_odb2='C:/Temp/SWAR30VF90Q22.odb'
job_name1='SWAR30VF90Q11'
job_name2='SWAR30VF90Q22' 
Lp=rho*b
n = 5
phi = 0.8
vg = b/phi - b
hg=0.25*vg#make small slits
w=b/2.0
lb=hg/2
ms=vg/2##mesh size
Ep=7000
EpGm=1000
Gm=Ep/EpGm
nup=0.22
num=0.49
Em=2*Gm*(1+num)
Wrve=n*(vg+b)
Lrve=hg+Lp
Lp11=(Lrve/n)-lb
Lp12=Lp-Lp11
Lp21=(2*Lrve/n)-lb
Lp22=Lp-Lp21
Lp31=Lp22
Lp32=Lp21
Lp41=Lp12
Lp42=Lp11
path_odb3='C:/Temp/SWARVFG12.odb'
job_name3='SWARVFG12' 
P=-10#load applied for finding out G12
flag=1
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
s.rectangle(point1=(Lrve-Lp42,  vg + b*0.5), point2=(Lrve,  vg + b*1.5))
s.rectangle(point1=(0,  vg + 0.5*b), point2=(Lp41,  vg + 1.5*b))
s.rectangle(point1=(Lrve-Lp32,  2*vg + b*1.5), point2=(Lrve,  2*vg + b*2.5))
s.rectangle(point1=(0,  2*vg + 1.5*b), point2=(Lp31,  2*vg + 2.5*b))
s.rectangle(point1=(Lrve-Lp22,  3*vg + b*2.5), point2=(Lrve,  3*vg + b*3.5))
s.rectangle(point1=(0,  3*vg + 2.5*b), point2=(Lp21,  3*vg + 3.5*b))
s.rectangle(point1=(Lrve-Lp12,  4*vg + b*3.5), point2=(Lrve,  4*vg + b*4.5))
s.rectangle(point1=(0,  4*vg + 3.5*b), point2=(Lp11,  4*vg + 4.5*b))
s.rectangle(point1=(lb,  5*vg + b*4.5), point2=(Lrve-lb,  5*vg + b*5))
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
s1.Line(point1=(Lrve, vg + b*0.5), point2=(Lrve-Lp42,  vg + b*0.5))
s1.Line(point1=(Lrve-Lp42,  vg + b*0.5), point2=(Lrve-Lp42,  vg + b*1.5))
s1.Line(point1=(Lrve-Lp42,  vg + b*1.5), point2=(Lrve,  vg + b*1.5))
s1.Line(point1=(Lrve,  vg + b*1.5), point2=(Lrve,  2*vg + b*1.5))
s1.Line(point1=(Lrve,  2*vg + b*1.5), point2=(Lrve-Lp32,  2*vg + b*1.5))
s1.Line(point1=(Lrve-Lp32,  2*vg + b*1.5), point2=(Lrve-Lp32,  2*vg + b*2.5))
s1.Line(point1=(Lrve-Lp32,  2*vg + b*2.5), point2=(Lrve,  2*vg + b*2.5))
s1.Line(point1=(Lrve,  2*vg + b*2.5), point2=(Lrve,  3*vg + b*2.5))
s1.Line(point1=(Lrve,  3*vg + b*2.5), point2=(Lrve-Lp22,  3*vg + b*2.5))
s1.Line(point1=(Lrve-Lp22,  3*vg + b*2.5), point2=(Lrve-Lp22,  3*vg + b*3.5))
s1.Line(point1=(Lrve-Lp22,  3*vg + b*3.5), point2=(Lrve,  3*vg + b*3.5))
s1.Line(point1=(Lrve,  3*vg + b*3.5), point2=(Lrve,  4*vg + b*3.5))
s1.Line(point1=(Lrve,  4*vg + b*3.5), point2=(Lrve-Lp12,  4*vg + b*3.5))
s1.Line(point1=(Lrve-Lp12,  4*vg + b*3.5), point2=(Lrve-Lp12,  4*vg + b*4.5))
s1.Line(point1=(Lrve-Lp12,  4*vg + b*4.5), point2=(Lrve,  4*vg + b*4.5))
s1.Line(point1=(Lrve,  4*vg + b*4.5), point2=(Lrve,  5*vg + b*5))
s1.Line(point1=(Lrve,  5*vg + b*5), point2=(Lrve-lb,  5*vg + b*5))
s1.Line(point1=(Lrve-lb,  5*vg + b*5), point2=(Lrve-lb,  5*vg + b*4.5))
s1.Line(point1=(Lrve-lb,  5*vg + b*4.5), point2=(lb,  5*vg + b*4.5))
s1.Line(point1=(lb,  5*vg + b*4.5), point2=(lb,  5*vg + b*5))
s1.Line(point1=(lb,  5*vg + b*5), point2=(0,  5*vg + b*5))
s1.Line(point1=(0,  5*vg + b*5), point2=(0,  4*vg + b*4.5))
s1.Line(point1=(0,  4*vg + 4.5*b), point2=(Lp11,  4*vg + b*4.5))
s1.Line(point1=(Lp11,  4*vg + 4.5*b), point2=(Lp11,  4*vg + b*3.5))
s1.Line(point1=(Lp11,  4*vg + 3.5*b), point2=(0,  4*vg + b*3.5))
s1.Line(point1=(0,  4*vg + 3.5*b), point2=(0,  3*vg + b*3.5))
s1.Line(point1=(0,  3*vg + 3.5*b), point2=(Lp21,  3*vg + b*3.5))
s1.Line(point1=(Lp21,  3*vg + 3.5*b), point2=(Lp21,  3*vg + b*2.5))
s1.Line(point1=(Lp21,  3*vg + 2.5*b), point2=(0,  3*vg + b*2.5))
s1.Line(point1=(0,  3*vg + 2.5*b), point2=(0,  2*vg + b*2.5))
s1.Line(point1=(0,  2*vg + 2.5*b), point2=(Lp31,  2*vg + b*2.5))
s1.Line(point1=(Lp31,  2*vg + 2.5*b), point2=(Lp31,  2*vg + b*1.5))
s1.Line(point1=(Lp31,  2*vg + 1.5*b), point2=(0,  2*vg + b*1.5))
s1.Line(point1=(0,  2*vg + 1.5*b), point2=(0,  vg + b*1.5))
s1.Line(point1=(0,  vg + 1.5*b), point2=(Lp41,  vg + b*1.5))
s1.Line(point1=(Lp41,  vg + 1.5*b), point2=(Lp41,  vg + b*0.5))
s1.Line(point1=(Lp41,  vg + 0.5*b), point2=(0,  vg + b*0.5))
s1.Line(point1=(0,  vg + 0.5*b), point2=(0,  0))
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


s1.Line(point1=(Lp11+0.5*hg, 3.5*b + 3*vg) , point2=(Lp11+hg, 3.5*b + 4*vg))
s1.Line(point1=(Lp11+hg, 3.5*b + 4*vg), point2=(Lp11+hg, 4.5*b + 4*vg))
s1.Line(point1=(Lp11+hg, 4.5*b + 4*vg), point2=(Lp11 + 0.5*hg, 4.5*b + 5*vg))
s1.Line(point1=(Lp11 + 0.5*hg, 4.5*b + 5*vg), point2=(Lp11, 4.5*b + 4*vg))
s1.Line(point1=(Lp11, 4.5*b + 4*vg), point2=(Lp11, 3.5*b + 4*vg))
s1.Line(point1=(Lp11, 3.5*b + 4*vg), point2=(Lp11+0.5*hg, 3.5*b + 3*vg))


s1.Line(point1=(Lp21+0.5*hg, 3.5*b + 4*vg) , point2=(Lp21+hg, 3.5*b + 3*vg))
s1.Line(point1=(Lp21+hg, 3.5*b + 3*vg), point2=(Lp21+hg, 2.5*b + 3*vg))
s1.Line(point1=(Lp21+hg, 2.5*b + 3*vg), point2=(Lp21 + 0.5*hg, 2.5*b + 2*vg))
s1.Line(point1=(Lp21 + 0.5*hg, 2.5*b + 2*vg), point2=(Lp21, 2.5*b + 3*vg))
s1.Line(point1=(Lp21, 2.5*b + 3*vg), point2=(Lp21, 3.5*b + 3*vg))
s1.Line(point1=(Lp21, 3.5*b + 3*vg), point2=(Lp21+0.5*hg, 3.5*b + 4*vg))


s1.Line(point1=(Lp31+0.5*hg, 2.5*b + 3*vg) , point2=(Lp31+hg, 2.5*b + 2*vg))
s1.Line(point1=(Lp31+hg, 2.5*b + 2*vg), point2=(Lp31+hg, 1.5*b + 2*vg))
s1.Line(point1=(Lp31+hg, 1.5*b + 2*vg), point2=(Lp31 + 0.5*hg, 1.5*b + vg))
s1.Line(point1=(Lp31 + 0.5*hg, 1.5*b + vg), point2=(Lp31, 1.5*b + 2*vg))
s1.Line(point1=(Lp31, 1.5*b + 2*vg), point2=(Lp31, 2.5*b + 2*vg))
s1.Line(point1=(Lp31, 2.5*b + 2*vg), point2=(Lp31+0.5*hg, 2.5*b + 3*vg))

s1.Line(point1=(Lp41+0.5*hg, 1.5*b + 2*vg) , point2=(Lp41+hg, 1.5*b + vg))
s1.Line(point1=(Lp41+hg, 1.5*b + vg), point2=(Lp41+hg, 0.5*b + vg))
s1.Line(point1=(Lp41+hg, 0.5*b + vg), point2=(Lp41 + 0.5*hg, 0.5*b ))
s1.Line(point1=(Lp41 + 0.5*hg, 0.5*b ), point2=(Lp41, 0.5*b + vg))
s1.Line(point1=(Lp41, 0.5*b + vg), point2=(Lp41, 1.5*b + vg))
s1.Line(point1=(Lp41, 1.5*b + vg), point2=(Lp41+0.5*hg, 1.5*b + 2*vg))


s1.Line(point1=(Lrve, Wrve-(0.5*b + vg)), point2=(Lrve, Wrve))
s1.Line(point1=(Lrve, Wrve), point2=(Lrve-lb, Wrve))
s1.Line(point1=(Lrve-lb, Wrve), point2=(Lrve-lb, Wrve- 0.5*b))
s1.Line(point1=(Lrve-lb, Wrve- 0.5*b), point2=(Lrve,  Wrve-(0.5*b + vg)))

s1.Line(point1=(0,  Wrve-(0.5*b + vg)), point2=(lb, Wrve - 0.5*b))
s1.Line(point1=(lb, Wrve- 0.5*b), point2=(lb, Wrve))
s1.Line(point1=(lb, Wrve), point2=(0, Wrve))
s1.Line(point1=(0, Wrve), point2=(0,  Wrve-(0.5*b + vg)))
p = mdb.models['Model-1'].Part(name='EndMatrix', dimensionality=TWO_D_PLANAR,type=DEFORMABLE_BODY)
p.BaseShell(sketch=s1)
s1.unsetPrimaryObject()


mdb.models['Model-1'].Material(name='Platelet')
mdb.models['Model-1'].materials['Platelet'].Elastic(table=((Ep, nup), ))
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


platelet_face_point_1 = ((Lrve/2),b/4,0.0)
platelet_face_point_2 = ((Lrve - Lp42*0.5),(b+vg),0.0)
platelet_face_point_3 = ((Lp41/2),(b+vg),0.0)
platelet_face_point_4 = ((Lrve - Lp32*0.5), 2*b + 2*vg,0.0)
platelet_face_point_5 = ((Lp31/2),(2*(b+vg)),0.0)
platelet_face_point_6= ((Lrve - Lp22*0.5), 3*b + 3*vg,0.0)
platelet_face_point_7 = ((Lp21/2),3*(b+vg),0.0)
platelet_face_point_8 = ((Lrve - Lp12*0.5), 4*b + 4*vg,0.0)
platelet_face_point_9 = ((Lp11/2),4*(b+vg),0.0)
platelet_face_point_10 = ((Lrve/2), 4.75*b + 5*vg,0.0)
platelet_face_1 = p.faces.findAt((platelet_face_point_1,))
platelet_face_2 = p.faces.findAt((platelet_face_point_2,))
platelet_face_3 = p.faces.findAt((platelet_face_point_3,))
platelet_face_4 = p.faces.findAt((platelet_face_point_4,))
platelet_face_5 = p.faces.findAt((platelet_face_point_5,))
platelet_face_6 = p.faces.findAt((platelet_face_point_6,))
platelet_face_7 = p.faces.findAt((platelet_face_point_7,))
platelet_face_8 = p.faces.findAt((platelet_face_point_8,))
platelet_face_9 = p.faces.findAt((platelet_face_point_9,))
platelet_face_10 = p.faces.findAt((platelet_face_point_10,))
platelet_region=(platelet_face_1, platelet_face_2, platelet_face_3, platelet_face_4,platelet_face_5,platelet_face_6,platelet_face_7,platelet_face_8,platelet_face_9,platelet_face_10,)
p = mdb.models['Model-1'].parts['Composite']
p.SectionAssignment(region=platelet_region, sectionName='Platelet', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)


p = mdb.models['Model-1'].parts['Composite']
f = p.faces

matrix_face_point_1 = (0.5*Lp11, Wrve- 0.5*(b+vg),0.0)
matrix_face_point_2 = (Lp11+hg+ 0.5*Lp12, Wrve- 0.5*(b+vg),0.0)
matrix_face_point_3 = (0.5*Lp21, 3.5*(b+vg),0.0)
matrix_face_point_4 = (Lp21+hg+ 0.5*Lp22, 3.5*(b+vg),0.0)
matrix_face_point_5 = (0.5*Lp31, 2.5*(b+vg),0.0)
matrix_face_point_6 = (Lp31+hg+ 0.5*Lp32, 2.5*(b+vg),0.0)
matrix_face_point_7 = (0.5*Lp41, 1.5*(b+vg),0.0)
matrix_face_point_8 = (Lp41+hg+ 0.5*Lp42, 1.5*(b+vg),0.0)
matrix_face_point_9 = (0.5*Lp41, 0.5*(b+vg),0.0)
matrix_face_point_10 = (Lp41+hg+ 0.5*Lp42, 0.5*(b+vg),0.0)
matrix_face_point_11 = (Lp11+hg, 3.5*(b+vg),0.0)
matrix_face_point_12 = (Lp21+hg, 2.5*(b+vg),0.0)
matrix_face_point_13 = (Lp31+hg, 1.5*(b+vg),0.0)
matrix_face_1 = p.faces.findAt((matrix_face_point_1,))
matrix_face_2 = p.faces.findAt((matrix_face_point_2,))
matrix_face_3 = p.faces.findAt((matrix_face_point_3,))
matrix_face_4 = p.faces.findAt((matrix_face_point_4,))
matrix_face_5 = p.faces.findAt((matrix_face_point_5,))
matrix_face_6 = p.faces.findAt((matrix_face_point_6,))
matrix_face_7 = p.faces.findAt((matrix_face_point_7,))
matrix_face_8 = p.faces.findAt((matrix_face_point_8,))
matrix_face_9 = p.faces.findAt((matrix_face_point_9,))
matrix_face_10 = p.faces.findAt((matrix_face_point_10,))
matrix_face_11 = p.faces.findAt((matrix_face_point_11,))
matrix_face_12 = p.faces.findAt((matrix_face_point_12,))
matrix_face_13 = p.faces.findAt((matrix_face_point_13,))
matrix_region=(matrix_face_1,matrix_face_2,matrix_face_3,matrix_face_4,matrix_face_5,matrix_face_6,matrix_face_7,matrix_face_8,matrix_face_9,matrix_face_10,matrix_face_11,matrix_face_12,matrix_face_13,)
p = mdb.models['Model-1'].parts['Composite']
p.SectionAssignment(region=matrix_region, sectionName='Matrix', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)


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
elemType1 = mesh.ElemType(elemCode=CPE4R, elemLibrary=STANDARD, 
        secondOrderAccuracy=OFF, hourglassControl=DEFAULT, 
        distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
a.setMeshControls(regions=rfmr, elemShape=QUAD,technique=STRUCTURED)
a.setElementType(regions=rfmr, elemTypes=(elemType1, elemType2))#uncomment to activate plane strain element
a.seedPartInstance(regions=partInstances, size=ms, deviationFactor=0.1, 
    minSizeFactor=0.1)
a.generateMesh(regions=partInstances)

session.viewports['Viewport: 1'].setValues(displayedObject=a)


#
mdb.models['Model-1'].StaticStep(name='Step-1', previous='Initial')
finalInstance=mdb.models['Model-1'].rootAssembly.instances['Composite-1']
finalPart= mdb.models['Model-1'].parts['Composite']

a.Set(edges=finalInstance.edges.findAt(((Lrve/2., Wrve, 0.0),), ), name="top")
a.Set(edges=finalInstance.edges.getByBoundingBox(xMin=Lrve-hg/5.), name="right")
a.Set(edges=finalInstance.edges.getByBoundingBox(xMax=hg/5.), name="left")
a.Set(edges=finalInstance.edges.getByBoundingBox(yMax=vg), name="bottom")


fixnode=mdb.models['Model-1'].rootAssembly.instances['Composite-1'].nodes.getClosest(coordinates=((Lrve/2., Wrve/2., 0.0),))[0].label
a.Set(nodes=mdb.models['Model-1'].rootAssembly.instances['Composite-1'].nodes[fixnode-1:fixnode], name="fixNode")


mdb.models['Model-1'].PinnedBC(createStepName='Step-1', localCsys=None, name='allfix',region=a.sets["fixNode"])
# generate the equations manually

nodesets = {}
for set,i in zip(["top","bottom","right","left"],[1,1,2,2]):
    nodesets[set]=[]
    for node in a.sets[set].nodes:
        nodesets[set].append((node.label,node.coordinates[0],node.coordinates[1]))
    nodesets[set].sort(key=lambda value: value[i])
mdb.models['Model-1'].keywordBlock.synchVersions(True)
keywordblock = mdb.models['Model-1'].keywordBlock
for i,kw in enumerate(keywordblock.sieBlocks):
    if kw.startswith("*End Part"):
        endpart = i
    elif kw.startswith("*End Instance"):
        endinstance = i
    elif kw.startswith("*Elset"):
        endassembly = i
    elif kw.startswith("*Static"):
        static = i
    elif kw.startswith("*Output, history"):
        history = i
        break


partstring="*Part, name=dummy-LR\n"
partstring+="*End Part\n"
partstring+="**\n"
partstring+="*Part, name=dummy-TB\n"
partstring+="*End Part\n"
partstring+="**\n"
keywordblock.insert(position=endpart+1,text=partstring)
endinstancestring="*Instance, name=dummy-LR-1, part=dummy-LR\n"
endinstancestring+="*Node\n"
endinstancestring+="100000, -10., 10., 0.\n"
endinstancestring+="**This dummy node can be arbitrary\n"
endinstancestring+="*Nset, nset=dummy-LR-1-RefPt_, internal\n"
endinstancestring+="100000,\n"
endinstancestring+="*End Instance\n"
endinstancestring+="*Instance, name=dummy-TB-1, part=dummy-TB\n"
endinstancestring+="*Node\n"
endinstancestring+="200000, 10., 0., 0.\n"
endinstancestring+="**This dummy node can be arbitrary\n"
endinstancestring+="*Nset, nset=dummy-TB-1-RefPt_, internal\n"
endinstancestring+="200000,\n"
endinstancestring+="*End Instance\n"
endinstancestring+="** Define nset Set-dummy-LR and Set-dummy-TB for the two dummy nodes\n"
endinstancestring+="**\n"
endinstancestring+="*Nset, nset=Set-dummy-LR, instance=dummy-LR-1\n"
endinstancestring+="100000,\n"
endinstancestring+="*Nset, nset=Set-dummy-TB, instance=dummy-TB-1\n"
endinstancestring+="200000,\n"
keywordblock.insert(position=endinstance+1,text=endinstancestring)

equationstring = "*Equation\n"
for ntop,nbot in zip(nodesets["top"],nodesets["bottom"]):
    equationstring += "3\n"
    equationstring += "Composite-1.%d, 1, 1.0, Composite-1.%d, 1, -1.0, %s, 1, -1.0\n" % (ntop[0],nbot[0],'Set-dummy-TB')
    equationstring += "3\n"
    equationstring += "Composite-1.%d, 2, 1.0, Composite-1.%d, 2, -1.0, %s, 2, -1.0\n" % (ntop[0],nbot[0],'Set-dummy-TB')
for nright,nleft in zip(nodesets["right"],nodesets["left"]):
    equationstring += "3\n"
    equationstring += "Composite-1.%d, 1, 1.0, Composite-1.%d, 1, -1.0, %s, 1, -1.0\n" % (nright[0],nleft[0],'Set-dummy-LR')
    equationstring += "3\n"
    equationstring += "Composite-1.%d, 2, 1.0, Composite-1.%d, 2, -1.0, %s, 2, -1.0\n" % (nright[0],nleft[0],'Set-dummy-LR')
keywordblock.insert(position=endassembly,text=equationstring)
bcstring = "**\n*Boundary\n"
bcstring += "Set-dummy-TB,1,1, 0.0\n" 
bcstring += "**\n*Boundary\n"
bcstring += "Set-dummy-LR,1,1, 0.01\n"
bcstring += "**\n*Boundary\n"
bcstring += "Set-dummy-LR,2,2, 0.0\n" 
bcstring += "**\n*Boundary\n"
bcstring += "Set-dummy-TB,2,2, 0.0\n"
keywordblock.insert(position=static+3,text=bcstring)
# ###################'Set-dummy-TB'##########################

job=mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name=job_name1, nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB,parallelizationMethodExplicit=DOMAIN, 
    numDomains=1,scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)

historystring = "*Output, history\n*Node Output, Nset=Set-dummy-LR\n RF\n" 
historystring += "*Node Output, Nset=Set-dummy-TB\n RF\n" 
keywordblock.replace(position=history+4,text=historystring)
mdb.jobs[job_name1].submit(consistencyChecking=OFF)
mdb.jobs[job_name1].waitForCompletion()


mdb.models['Model-1'].keywordBlock.setValues(edited = 0)


nodesets = {}
for set,i in zip(["top","bottom","right","left"],[1,1,2,2]):
    nodesets[set]=[]
    for node in a.sets[set].nodes:
        nodesets[set].append((node.label,node.coordinates[0],node.coordinates[1]))
    nodesets[set].sort(key=lambda value: value[i])
mdb.models['Model-1'].keywordBlock.synchVersions(True)
keywordblock = mdb.models['Model-1'].keywordBlock
for i,kw in enumerate(keywordblock.sieBlocks):
    if kw.startswith("*End Part"):
        endpart = i
    elif kw.startswith("*End Instance"):
        endinstance = i
    elif kw.startswith("*Elset"):
        endassembly = i
    elif kw.startswith("*Static"):
        static = i
    elif kw.startswith("*Output, history"):
        history = i
        break


partstring="*Part, name=dummy-LR\n"
partstring+="*End Part\n"
partstring+="**\n"
partstring+="*Part, name=dummy-TB\n"
partstring+="*End Part\n"
partstring+="**\n"
keywordblock.insert(position=endpart+1,text=partstring)
endinstancestring="*Instance, name=dummy-LR-1, part=dummy-LR\n"
endinstancestring+="*Node\n"
endinstancestring+="100000, -10., 10., 0.\n"
endinstancestring+="**This dummy node can be arbitrary\n"
endinstancestring+="*Nset, nset=dummy-LR-1-RefPt_, internal\n"
endinstancestring+="100000,\n"
endinstancestring+="*End Instance\n"
endinstancestring+="*Instance, name=dummy-TB-1, part=dummy-TB\n"
endinstancestring+="*Node\n"
endinstancestring+="200000, 10., 0., 0.\n"
endinstancestring+="**This dummy node can be arbitrary\n"
endinstancestring+="*Nset, nset=dummy-TB-1-RefPt_, internal\n"
endinstancestring+="200000,\n"
endinstancestring+="*End Instance\n"
endinstancestring+="** Define nset Set-dummy-LR and Set-dummy-TB for the two dummy nodes\n"
endinstancestring+="**\n"
endinstancestring+="*Nset, nset=Set-dummy-LR, instance=dummy-LR-1\n"
endinstancestring+="100000,\n"
endinstancestring+="*Nset, nset=Set-dummy-TB, instance=dummy-TB-1\n"
endinstancestring+="200000,\n"

keywordblock.insert(position=endinstance+1,text=endinstancestring)

equationstring = "*Equation\n"
for ntop,nbot in zip(nodesets["top"],nodesets["bottom"]):
    equationstring += "3\n"
    equationstring += "Composite-1.%d, 1, 1.0, Composite-1.%d, 1, -1.0, %s, 1, -1.0\n" % (ntop[0],nbot[0],'Set-dummy-TB')
    equationstring += "3\n"
    equationstring += "Composite-1.%d, 2, 1.0, Composite-1.%d, 2, -1.0, %s, 2, -1.0\n" % (ntop[0],nbot[0],'Set-dummy-TB')
for nright,nleft in zip(nodesets["right"],nodesets["left"]):
    equationstring += "3\n"
    equationstring += "Composite-1.%d, 1, 1.0, Composite-1.%d, 1, -1.0, %s, 1, -1.0\n" % (nright[0],nleft[0],'Set-dummy-LR')
    equationstring += "3\n"
    equationstring += "Composite-1.%d, 2, 1.0, Composite-1.%d, 2, -1.0, %s, 2, -1.0\n" % (nright[0],nleft[0],'Set-dummy-LR')
keywordblock.insert(position=endassembly,text=equationstring)
bcstring = "**\n*Boundary\n"
bcstring += "Set-dummy-TB,2,2, 0.01\n" 
bcstring += "**\n*Boundary\n"
bcstring += "Set-dummy-TB,1,1, 0.0\n"
bcstring += "**\n*Boundary\n"
bcstring += "Set-dummy-LR,2,2, 0.0\n" 
bcstring += "**\n*Boundary\n"
bcstring += "Set-dummy-LR,1,1, 0.0\n" 
keywordblock.insert(position=static+3,text=bcstring)


mdb.Job(name=job_name2, model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB,parallelizationMethodExplicit=DOMAIN, 
    numDomains=1,multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
historystring = "*Output, history\n*Node Output, Nset=Set-dummy-LR\n RF\n" 
historystring += "*Node Output, Nset=Set-dummy-TB\n RF\n"
keywordblock.replace(position=history+4,text=historystring)
mdb.jobs[job_name2].submit(consistencyChecking=OFF)
mdb.jobs[job_name2].waitForCompletion()


mesh_nodes=mdb.models['Model-1'].rootAssembly.instances['Composite-1'].nodes
a.Set(nodes=mesh_nodes.getByBoundingBox(xMin=Lrve-hg/2, yMin=vg/4, yMax=Wrve - vg/2.), name="BC")
a.Set(nodes=mesh_nodes.getByBoundingBox(xMax=hg,yMin=vg/4, yMax=Wrve - vg/2.), name="AD")
a.Set(nodes=mesh_nodes.getByBoundingBox(xMin=hg, xMax=Lrve - hg, yMax=vg/2.), name="AB")
a.Set(nodes=mesh_nodes.getByBoundingBox(yMin=Wrve - hg, xMin=hg, xMax=Lrve - hg), name="CD")

n1 = a.instances['Composite-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0 #1000 ]', ), )
a.Set(nodes=nodes1, name='A')
n1 = a.instances['Composite-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0 #2000 ]', ), )
a.Set(nodes=nodes1, name='B')
n1 = a.instances['Composite-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0 #4000 ]', ), )
a.Set(nodes=nodes1, name='C')
n1 = a.instances['Composite-1'].nodes
nodes1 = n1.getSequenceFromMask(mask=('[#0 #8000 ]', ), )
a.Set(nodes=nodes1, name='D')
n1 = a.instances['Composite-1'].nodes
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
mdb.models['Model-1'].boundaryConditions['allfix'].suppress()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF, loads=ON, 
    bcs=ON, predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
mdb.models['Model-1'].keywordBlock.setValues(edited = 0)
mdb.models['Model-1'].keywordBlock.synchVersions(storeNodesAndElements=False)
a = mdb.models['Model-1'].rootAssembly
region = a.sets['A']
mdb.models['Model-1'].DisplacementBC(name='Au2zer', createStepName='Step-1', 
    region=region, u1=UNSET, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
                distributionType=UNIFORM, fieldName='', localCsys=None)
region = a.sets['B']
mdb.models['Model-1'].DisplacementBC(name='Bu2zer', createStepName='Step-1', 
    region=region, u1=UNSET, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
region = a.sets['AB']
mdb.models['Model-1'].DisplacementBC(name='ABu1zer', createStepName='Step-1', 
    region=region, u1=0.0, u2=UNSET, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
region = a.sets['BC']
mdb.models['Model-1'].DisplacementBC(name='BCu2zer', createStepName='Step-1', 
    region=region, u1=UNSET, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
region = a.sets['AD']
mdb.models['Model-1'].DisplacementBC(name='ADu2zer', createStepName='Step-1', 
    region=region, u1=UNSET, u2=0.0, ur3=UNSET, amplitude=UNSET, fixed=OFF, 
    distributionType=UNIFORM, fieldName='', localCsys=None)
region = a.sets['C']
mdb.models['Model-1'].ConcentratedForce(name='C', createStepName='Step-1', 
    region=region, cf1=P, distributionType=UNIFORM, field='', 
    localCsys=None)
region = a.sets['D']
mdb.models['Model-1'].ConcentratedForce(name='D', createStepName='Step-1', 
    region=region, cf1=P, distributionType=UNIFORM, field='', 
    localCsys=None)

mdb.models['Model-1'].keywordBlock.setValues(edited = 0)


nodesets = {}
for set,i in zip(["top","bottom","right","left"],[1,1,2,2]):
    nodesets[set]=[]
    for node in a.sets[set].nodes:
        nodesets[set].append((node.label,node.coordinates[0],node.coordinates[1]))
    nodesets[set].sort(key=lambda value: value[i])
mdb.models['Model-1'].keywordBlock.synchVersions(True)
keywordblock = mdb.models['Model-1'].keywordBlock
for i,kw in enumerate(keywordblock.sieBlocks):
    if kw.startswith("*End Part"):
        endpart = i
    elif kw.startswith("*End Instance"):
        endinstance = i
    elif kw.startswith("*Elset"):
        endassembly = i
    elif kw.startswith("*Static"):
        static = i
    elif kw.startswith("*Output, history"):
        history = i
        break


equationstring = "*Equation\n"
for i in range(0,(len(nodesets["top"])-1)):
    equationstring += "2\n"
    equationstring += "Composite-1.%d, 1, 1.0, Composite-1.%d, 1, -1.0\n" % (nodesets["top"][i][0],nodesets["top"][i+1][0])
keywordblock.insert(position=endassembly,text=equationstring)



mdb.Job(name=job_name3, model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB,parallelizationMethodExplicit=DOMAIN, 
    numDomains=1,multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
historystring = "*Output, history\n" 
historystring += "*Node Output, Nset=D\n U\n"
keywordblock.replace(position=history,text=historystring)
mdb.jobs[job_name3].submit(consistencyChecking=OFF)
mdb.jobs[job_name3].waitForCompletion()


o3 = session.openOdb(name=path_odb1)
step = o3.steps["Step-1"]
horiRegion1 = step.historyRegions["Node DUMMY-LR-1.100000"]
vertRegion1 = step.historyRegions["Node DUMMY-TB-1.200000"]
fxx1 = horiRegion1.historyOutputs["RF1"].data[-1][1]
fxy1 = horiRegion1.historyOutputs["RF2"].data[-1][1]
fyx1 = vertRegion1.historyOutputs["RF1"].data[-1][1]
fyy1 = vertRegion1.historyOutputs["RF2"].data[-1][1]
exx=0.01/Lrve
Q11=fxx1/(Wrve*exx)
Q12=(fyy1)/(Lrve*exx)

with open("sw.txt","a") as outfile:
    outfile.write("------Simulation_using_RF,plane strain elements-----\n")
    outfile.write("n=%d, aspect=%d, vf=%.2f, Ep/Gm=%.1f\n" % (n,rho,phi, EpGm))
    outfile.write("---------------Horizontal displacement-----------------------\n")
    outfile.write("Q11=%2f\n" %(Q11))
    outfile.write("Q12=%2f\n" %(Q12))
    outfile.write("--------------------------------------\n")
o4 = session.openOdb(name=path_odb2)
step = o4.steps["Step-1"]
horiRegion2 = step.historyRegions["Node DUMMY-LR-1.100000"]
vertRegion2 = step.historyRegions["Node DUMMY-TB-1.200000"]
fxx2 = horiRegion2.historyOutputs["RF1"].data[-1][1]
fxy2 = horiRegion2.historyOutputs["RF2"].data[-1][1]
fyx2 = vertRegion2.historyOutputs["RF1"].data[-1][1]
fyy2 = vertRegion2.historyOutputs["RF2"].data[-1][1]
eyy=0.01/Wrve
Q12_vs=fxx2/(Wrve*eyy)
Q22=fyy2/(Lrve*eyy)
deno=(Q11*Q22) - (Q12*Q12)
S11=Q22/deno
S12=-Q12/deno
S22=Q11/deno
E11=1/S11



with open("sw.txt","a") as outfile:
    outfile.write("---------------Start-----------------------\n")
    outfile.write("Q12_1H=%2f\n" %(Q12))
    outfile.write("Q22_1H=%2f\n" %(Q22))
    outfile.write("E11=%2f\n" %(E11))
o3 = session.openOdb(name=path_odb3)
step = o3.steps["Step-1"]
U1reg = step.historyRegions["Node COMPOSITE-1.%d"%(nodesets["top"][0][0])]
delta = U1reg.historyOutputs["U1"].data[-1][1]
G12=2*P*Wrve/(Lrve*delta)

with open("sw.txt","a") as outfile:
    outfile.write("G12=%2f\n" %(2*P*Wrve/(Lrve*delta)))
        outfile.write("----------------End----------------------\n")







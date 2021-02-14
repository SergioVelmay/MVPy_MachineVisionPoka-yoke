# MVPy | Machine Vision Poka-yoke

Windows 10

Microsoft Visual Studio Community 2019

Microsoft Visual C++ 2015-2019 Redistributable x64

CMake 3.19.4

Python 3.6.5 x64

Intel Distribution of OpenVINO Toolkit 2020.3.1 LTS

Intel Neural Compute Stick 2 NCS2

```
py -m pip install --upgrade pip

pip install pillow

pip install numpy

pip install opencv-contrib-python
```

```
py

import cv2

cv2.__version__

'4.5.1'

exit()
```

```
cd C:\Program Files (x86)\IntelSWTools\openvino\bin\

setupvars.bat
```

```
py

import cv2

cv2.__version__

'4.3.0-openvino-2020.3.0'

exit()
```

```
cd C:\Program Files (x86)\IntelSWTools\openvino\deployment_tools\model_optimizer\install_prerequisites

install_prerequisites.bat
```

```
cd C:\"Program Files (x86)"\IntelSWTools\openvino\deployment_tools\demo

demo_squeezenet_download_convert_run.bat –d MYRIAD

[ ERROR ] Cannot create ShapeOf layer pool10/input_rank/shape_of id:145
```
```
cd C:\"Program Files (x86)"\IntelSWTools\openvino\deployment_tools\demo

demo_security_barrier_camera.bat -d MYRIAD
```

```
cd C:\Program Files (x86)\IntelSWTools\openvino\bin\

setupvars.bat
```

```
cd C:\Users\sergi\source\repos\MVPy_MachineVisionPoka-yoke

py MVPy.py
```

```
cd C:\Users\sergi\source\repos\MVPy_MachineVisionPoka-yoke

MVPy.bat
```

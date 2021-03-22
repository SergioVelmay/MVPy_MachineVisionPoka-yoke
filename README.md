# MVPy | Machine Vision Poka-yoke

## Project Setup

### Windows

- Windows 10 Pro

- Microsoft Visual Studio Community 2019

- Microsoft Visual C++ 2015-2019 Redistributable x64

- CMake 3.19.4

- Python 3.6.5 x64

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

Intel Distribution of OpenVINO Toolkit 2020.3.1 LTS

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

Intel Neural Compute Stick 2 NCS2

```
cd C:\"Program Files (x86)"\IntelSWTools\openvino\deployment_tools\demo

demo_squeezenet_download_convert_run.bat –d MYRIAD

[ INFO ] Loading network files

Top 10 results:

Image C:\Program Files (x86)\IntelSWTools\openvino\deployment_tools\demo\car.png

classid probability label
------- ----------- -----
817     0.6708984   sports car, sport car
479     0.1922607   car wheel
511     0.0936890   convertible
436     0.0216064   beach wagon, station wagon, wagon, estate car, beach waggon, station waggon, waggon
751     0.0075760   racer, race car, racing car
656     0.0049667   minivan
717     0.0027428   pickup, pickup truck
581     0.0019779   grille, radiator grille
468     0.0014219   cab, hack, taxi, taxicab
661     0.0008636   Model T

[ INFO ] Execution successful
```
```
cd C:\"Program Files (x86)"\IntelSWTools\openvino\deployment_tools\demo

demo_security_barrier_camera.bat -d MYRIAD

[ INFO ] Loading detection model to the MYRIAD plugin
[ INFO ] Loading Vehicle Attribs model to the MYRIAD plugin
[ INFO ] Loading Licence Plate Recognition (LPR) model to the MYRIAD plugin
[ INFO ] Number of InferRequests: 1 (detection), 3 (classification), 3 (recognition)
[ INFO ] Display resolution: 1920x1080
[ INFO ] Number of allocated frames: 3
[ INFO ] Resizable input with support of ROI crop and auto resize is disabled

0.1FPS for (1 / 1) frames

Detection InferRequests usage: 100.0%

[ INFO ] Execution successful
```

## Project Start

- Visual Studio Code 

- Git 2.30.1

- https://github.com/SergioVelmay/MVPy_MachineVisionPoka-yoke.git

- C:\Users\sergi\source\repos\

```
cd C:\Users\sergi\source\repos\MVPy_MachineVisionPoka-yoke

MVPy.bat
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
py MVPy.py -h

usage: MVPy | Machine Vision Poka-yoke 

[-h] [-d {CPU,GPU,HDDL,MYRIAD}] [-t {False,True,No,Yes,0,1}]

Edge computing application for manual assembly cells.

optional arguments:
  -h, --help        show this help message and exit
  -d, --device      device name for OpenVINO inference
  -t, --training    store image captures for training

example: $ py MVPy.py -d MYRIAD -t False
```

Videos .mp4 without audio track

```
Warning: libmmd.dll couldn't be found in %PATH%.
Please check if the redistributable package for Intel(R) C++ Compiler is installed and the library path is added to the PATH environment variable.
System reboot can be required to update the system environment.

C:\Program Files (x86)\Common Files\Intel\Shared Libraries\redist\intel64_win\compiler\

libmmd.dll

Edit the system environment variables / Environment Variables... / Path / Edit... / New / "C:\..." / Ok

https://software.intel.com/content/www/us/en/develop/articles/redistributable-libraries-for-intel-c-and-fortran-2020-compilers-for-windows.html
```

## Model Optimizer

### Windows

```
cd C:\Program Files (x86)\IntelSWTools\openvino\deployment_tools\model_optimizer\install_prerequisites

install_prerequisites_tf.bat
```

```
pip install tensorflow==1.2
```

```
cd C:\Program Files (x86)\IntelSWTools\openvino\deployment_tools\model_optimizer

py mo_tf.py --log_level=DEBUG --output_dir C:\Users\sergi\Desktop\MVPy\Models\Part4Detection\IR -b 1 --input_model C:\Users\sergi\Desktop\MVPy\Models\Part4Detection\GeneralCompact.TensorFlow\model.pb

[ SUCCESS ] Generated IR version 10 model.
[ SUCCESS ] XML file: C:\Users\sergi\Desktop\MVPy\Models\Part4Detection\IR\model.xml
[ SUCCESS ] BIN file: C:\Users\sergi\Desktop\MVPy\Models\Part4Detection\IR\model.bin
[ SUCCESS ] Total execution time: 24.51 seconds.
```
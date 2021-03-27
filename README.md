# MVPy | Machine Vision Poka-yoke <a id="top"></a>

- [Project Setup](#project-setup)
	- [Linux](#project-setup-linux)
		- [CPU](#project-setup-linux-cpu)
		- [GPU](#project-setup-linux-gpu)
		- [MYRIAD](#project-setup-linux-myriad)
		- [HDDL](#project-setup-linux-hddl)
	- [Windows](#project-setup-windows)
		- [NCS2](#project-setup-windows-ncs2)
- [Project Start](#project-start)
	- [Linux](#project-start-linux)
	- [Windows](#project-start-windows)
- [Model Optimizer](#model-optimizer)
	- [Windows](#model-optimizer-windows)
- [Vizi-AI GPIO MRAA](#vizi-ai-gpio-mraa)
	- [Linux](#vizi-ai-gpio-mraa-linux)

## Project Setup

### Linux <a id="project-setup-linux"></a>

- Ubuntu 18.04.5 LTS (Bionic Beaver)

- Intel Distribution of OpenVINO Toolkit 2020.3.1 LTS (latest)

```
cd ~/Downloads/

tar -xvzf l_openvino_toolkit_p_2020.3.341.tgz

cd l_openvino_toolkit_p_2020.3.341/

sudo ./install_GUI.sh
```

```
cd /opt/intel/openvino/install_dependencies

sudo -E ./install_openvino_dependencies.sh

source /opt/intel/openvino/bin/setupvars.sh

cd /opt/intel/openvino/deployment_tools/model_optimizer/install_prerequisites

sudo ./install_prerequisites.sh
```

[⇧](#top)

- CPU <a id="project-setup-linux-cpu"></a>

```
cd /opt/intel/openvino/deployment_tools/demo

./demo_squeezenet_download_convert_run.sh

Run Inference Engine classification sample

Run ./classification_sample_async -d CPU -i /opt/intel/openvino/deployment_tools/demo/car.png -m /home/sergio/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml

[ INFO ] InferenceEngine: 
	API version ............ 2.1
	Build .................. 2020.3.1-3500-68236d2e44c-releases/2020/3
	Description ....... API
[ INFO ] Parsing input parameters
[ INFO ] Parsing input parameters
[ INFO ] Files were added: 1
[ INFO ]     /opt/intel/openvino/deployment_tools/demo/car.png
[ INFO ] Creating Inference Engine
	CPU
	MKLDNNPlugin version ......... 2.1
	Build ........... 2020.3.1-3500-68236d2e44c-releases/2020/3

[ INFO ] Loading network files
[ INFO ] Preparing input blobs
[ WARNING ] Image is resized from (787, 259) to (227, 227)
[ INFO ] Batch size is 1
[ INFO ] Loading model to the device
[ INFO ] Create infer request
[ INFO ] Start inference (10 asynchronous executions)
[ INFO ] Completed 1 async request execution
[ INFO ] Completed 2 async request execution
[ INFO ] Completed 3 async request execution
[ INFO ] Completed 4 async request execution
[ INFO ] Completed 5 async request execution
[ INFO ] Completed 6 async request execution
[ INFO ] Completed 7 async request execution
[ INFO ] Completed 8 async request execution
[ INFO ] Completed 9 async request execution
[ INFO ] Completed 10 async request execution
[ INFO ] Processing output blobs

Top 10 results:

Image /opt/intel/openvino/deployment_tools/demo/car.png

classid probability label
------- ----------- -----
817     0.6853042   sports car, sport car
479     0.1835186   car wheel
511     0.0917199   convertible
436     0.0200693   beach wagon, station wagon, wagon, estate car, beach waggon, station waggon, waggon
751     0.0069604   racer, race car, racing car
656     0.0044177   minivan
717     0.0024739   pickup, pickup truck
581     0.0017788   grille, radiator grille
468     0.0013083   cab, hack, taxi, taxicab
661     0.0007443   Model T

[ INFO ] Execution successful
```

```
cd /opt/intel/openvino/deployment_tools/demo

./demo_security_barrier_camera.sh

Run Inference Engine security_barrier_camera demo

Run ./security_barrier_camera_demo -d CPU -d_va CPU -d_lpr CPU -i /opt/intel/openvino/deployment_tools/demo/car_1.bmp -m /home/sergio/openvino_models/ir/intel/vehicle-license-plate-detection-barrier-0106/FP16/vehicle-license-plate-detection-barrier-0106.xml -m_lpr /home/sergio/openvino_models/ir/intel/license-plate-recognition-barrier-0001/FP16/license-plate-recognition-barrier-0001.xml -m_va /home/sergio/openvino_models/ir/intel/vehicle-attributes-recognition-barrier-0039/FP16/vehicle-attributes-recognition-barrier-0039.xml

[ INFO ] InferenceEngine: 0x7fc2e79e3040
[ INFO ] Files were added: 1
[ INFO ]     /opt/intel/openvino/deployment_tools/demo/car_1.bmp
[ INFO ] Loading device CPU
	CPU
	MKLDNNPlugin version ......... 2.1
	Build ........... 2020.3.1-3500-68236d2e44c-releases/2020/3

[ INFO ] Loading detection model to the CPU plugin
[ INFO ] Loading Vehicle Attribs model to the CPU plugin
[ INFO ] Loading Licence Plate Recognition (LPR) model to the CPU plugin
[ INFO ] Number of InferRequests: 1 (detection), 3 (classification), 3 (recognition)
[ INFO ] 4 streams for CPU
[ INFO ] Display resolution: 1920x1080
[ INFO ] Number of allocated frames: 3
[ INFO ] Resizable input with support of ROI crop and auto resize is disabled
0.1FPS for (1 / 1) frames
Detection InferRequests usage: 100.0%

[ INFO ] Execution successful
```

```
source /opt/intel/openvino/bin/setupvars.sh

cd ~/inference_engine_samples_build/intel64/Release

./classification_sample_async -i /opt/intel/openvino/deployment_tools/demo/car.png -m ~/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml -d CPU

./classification_sample_async -i /opt/intel/openvino/deployment_tools/demo/car.png -m ~/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml -d CPU
[ INFO ] InferenceEngine: 
	API version ............ 2.1
	Build .................. 2020.3.1-3500-68236d2e44c-releases/2020/3
	Description ....... API
[ INFO ] Parsing input parameters
[ INFO ] Parsing input parameters
[ INFO ] Files were added: 1
[ INFO ]     /opt/intel/openvino/deployment_tools/demo/car.png
[ INFO ] Creating Inference Engine
	CPU
	MKLDNNPlugin version ......... 2.1
	Build ........... 2020.3.1-3500-68236d2e44c-releases/2020/3

[ INFO ] Loading network files
[ INFO ] Preparing input blobs
[ WARNING ] Image is resized from (787, 259) to (227, 227)
[ INFO ] Batch size is 1
[ INFO ] Loading model to the device
[ INFO ] Create infer request
[ INFO ] Start inference (10 asynchronous executions)
[ INFO ] Completed 1 async request execution
[ INFO ] Completed 2 async request execution
[ INFO ] Completed 3 async request execution
[ INFO ] Completed 4 async request execution
[ INFO ] Completed 5 async request execution
[ INFO ] Completed 6 async request execution
[ INFO ] Completed 7 async request execution
[ INFO ] Completed 8 async request execution
[ INFO ] Completed 9 async request execution
[ INFO ] Completed 10 async request execution
[ INFO ] Processing output blobs

Top 10 results:

Image /opt/intel/openvino/deployment_tools/demo/car.png

classid probability label
------- ----------- -----
817     0.6853042   sports car, sport car
479     0.1835186   car wheel
511     0.0917199   convertible
436     0.0200693   beach wagon, station wagon, wagon, estate car, beach waggon, station waggon, waggon
751     0.0069604   racer, race car, racing car
656     0.0044177   minivan
717     0.0024739   pickup, pickup truck
581     0.0017788   grille, radiator grille
468     0.0013083   cab, hack, taxi, taxicab
661     0.0007443   Model T

[ INFO ] Execution successful
```

[⇧](#top)

- GPU <a id="project-setup-linux-gpu"></a>

```
cd /opt/intel/openvino/install_dependencies/

sudo -E su

./install_NEO_OCL_driver.sh

exit
```

```
source /opt/intel/openvino/bin/setupvars.sh

cd ~/inference_engine_samples_build/intel64/Release

./classification_sample_async -i /opt/intel/openvino/deployment_tools/demo/car.png -m ~/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml -d GPU

./classification_sample_async -i /opt/intel/openvino/deployment_tools/demo/car.png -m ~/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml -d GPU
[ INFO ] InferenceEngine: 
	API version ............ 2.1
	Build .................. 2020.3.1-3500-68236d2e44c-releases/2020/3
	Description ....... API
[ INFO ] Parsing input parameters
[ INFO ] Parsing input parameters
[ INFO ] Files were added: 1
[ INFO ]     /opt/intel/openvino/deployment_tools/demo/car.png
[ INFO ] Creating Inference Engine
	GPU
	clDNNPlugin version ......... 2.1
	Build ........... 2020.3.1-3500-68236d2e44c-releases/2020/3

[ INFO ] Loading network files
[ INFO ] Preparing input blobs
[ WARNING ] Image is resized from (787, 259) to (227, 227)
[ INFO ] Batch size is 1
[ INFO ] Loading model to the device
[ INFO ] Create infer request
[ INFO ] Start inference (10 asynchronous executions)
[ INFO ] Completed 1 async request execution
[ INFO ] Completed 2 async request execution
[ INFO ] Completed 3 async request execution
[ INFO ] Completed 4 async request execution
[ INFO ] Completed 5 async request execution
[ INFO ] Completed 6 async request execution
[ INFO ] Completed 7 async request execution
[ INFO ] Completed 8 async request execution
[ INFO ] Completed 9 async request execution
[ INFO ] Completed 10 async request execution
[ INFO ] Processing output blobs

Top 10 results:

Image /opt/intel/openvino/deployment_tools/demo/car.png

classid probability label
------- ----------- -----
817     0.6679688   sports car, sport car
479     0.1914062   car wheel
511     0.1024170   convertible
436     0.0192413   beach wagon, station wagon, wagon, estate car, beach waggon, station waggon, waggon
751     0.0068817   racer, race car, racing car
656     0.0045090   minivan
717     0.0026093   pickup, pickup truck
581     0.0017672   grille, radiator grille
468     0.0013123   cab, hack, taxi, taxicab
661     0.0007715   Model T

[ INFO ] Execution successful
```

[⇧](#top)

- MYRIAD <a id="project-setup-linux-myriad"></a>

```
source /opt/intel/openvino/bin/setupvars.sh

cd /opt/intel/openvino/install_dependencies

./install_NCS_udev_rules.sh
```

```
sudo usermod -a -G users "$(whoami)"

*Log out and log in.
```

```
sudo cp /opt/intel/openvino/inference_engine/external/97-myriad-usbboot.rules /etc/udev/rules.d/

sudo udevadm control --reload-rules

sudo udevadm trigger

sudo ldconfig

*Reboot the machine.
```

```
cd /opt/intel/openvino/deployment_tools/demo

./demo_squeezenet_download_convert_run.sh -d MYRIAD

Run Inference Engine classification sample

Run ./classification_sample_async -d MYRIAD -i /opt/intel/openvino/deployment_tools/demo/car.png -m /home/sergio/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml

[ INFO ] InferenceEngine: 
	API version ............ 2.1
	Build .................. 2020.3.1-3500-68236d2e44c-releases/2020/3
	Description ....... API
[ INFO ] Parsing input parameters
[ INFO ] Parsing input parameters
[ INFO ] Files were added: 1
[ INFO ]     /opt/intel/openvino/deployment_tools/demo/car.png
[ INFO ] Creating Inference Engine
	MYRIAD
	myriadPlugin version ......... 2.1
	Build ........... 2020.3.1-3500-68236d2e44c-releases/2020/3

[ INFO ] Loading network files
[ INFO ] Preparing input blobs
[ WARNING ] Image is resized from (787, 259) to (227, 227)
[ INFO ] Batch size is 1
[ INFO ] Loading model to the device
[ INFO ] Create infer request
[ INFO ] Start inference (10 asynchronous executions)
[ INFO ] Completed 1 async request execution
[ INFO ] Completed 2 async request execution
[ INFO ] Completed 3 async request execution
[ INFO ] Completed 4 async request execution
[ INFO ] Completed 5 async request execution
[ INFO ] Completed 6 async request execution
[ INFO ] Completed 7 async request execution
[ INFO ] Completed 8 async request execution
[ INFO ] Completed 9 async request execution
[ INFO ] Completed 10 async request execution
[ INFO ] Processing output blobs

Top 10 results:

Image /opt/intel/openvino/deployment_tools/demo/car.png

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
cd /opt/intel/openvino/deployment_tools/demo

./demo_security_barrier_camera.sh -d MYRIAD

Run Inference Engine security_barrier_camera demo

Run ./security_barrier_camera_demo -d MYRIAD -d_va MYRIAD -d_lpr MYRIAD -i /opt/intel/openvino/deployment_tools/demo/car_1.bmp -m /home/sergio/openvino_models/ir/intel/vehicle-license-plate-detection-barrier-0106/FP16/vehicle-license-plate-detection-barrier-0106.xml -m_lpr /home/sergio/openvino_models/ir/intel/license-plate-recognition-barrier-0001/FP16/license-plate-recognition-barrier-0001.xml -m_va /home/sergio/openvino_models/ir/intel/vehicle-attributes-recognition-barrier-0039/FP16/vehicle-attributes-recognition-barrier-0039.xml

[ INFO ] InferenceEngine: 0x7fe6c7304040
[ INFO ] Files were added: 1
[ INFO ]     /opt/intel/openvino/deployment_tools/demo/car_1.bmp
[ INFO ] Loading device MYRIAD
	MYRIAD
	myriadPlugin version ......... 2.1
	Build ........... 2020.3.1-3500-68236d2e44c-releases/2020/3

[ INFO ] Loading detection model to the MYRIAD plugin
[ INFO ] Loading Vehicle Attribs model to the MYRIAD plugin
[ INFO ] Loading Licence Plate Recognition (LPR) model to the MYRIAD plugin
[ INFO ] Number of InferRequests: 1 (detection), 3 (classification), 3 (recognition)
[ INFO ] Display resolution: 1920x1080
[ INFO ] Number of allocated frames: 3
[ INFO ] Resizable input with support of ROI crop and auto resize is disabled
0.3FPS for (1 / 1) frames
Detection InferRequests usage: 100.0%

[ INFO ] Execution successful
```

```
source /opt/intel/openvino/bin/setupvars.sh

cd ~/inference_engine_samples_build/intel64/Release

./classification_sample_async -i /opt/intel/openvino/deployment_tools/demo/car.png -m ~/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml -d MYRIAD

./classification_sample_async -i /opt/intel/openvino/deployment_tools/demo/car.png -m ~/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml -d MYRIAD
[ INFO ] InferenceEngine: 
	API version ............ 2.1
	Build .................. 2020.3.1-3500-68236d2e44c-releases/2020/3
	Description ....... API
[ INFO ] Parsing input parameters
[ INFO ] Parsing input parameters
[ INFO ] Files were added: 1
[ INFO ]     /opt/intel/openvino/deployment_tools/demo/car.png
[ INFO ] Creating Inference Engine
	MYRIAD
	myriadPlugin version ......... 2.1
	Build ........... 2020.3.1-3500-68236d2e44c-releases/2020/3

[ INFO ] Loading network files
[ INFO ] Preparing input blobs
[ WARNING ] Image is resized from (787, 259) to (227, 227)
[ INFO ] Batch size is 1
[ INFO ] Loading model to the device
[ INFO ] Create infer request
[ INFO ] Start inference (10 asynchronous executions)
[ INFO ] Completed 1 async request execution
[ INFO ] Completed 2 async request execution
[ INFO ] Completed 3 async request execution
[ INFO ] Completed 4 async request execution
[ INFO ] Completed 5 async request execution
[ INFO ] Completed 6 async request execution
[ INFO ] Completed 7 async request execution
[ INFO ] Completed 8 async request execution
[ INFO ] Completed 9 async request execution
[ INFO ] Completed 10 async request execution
[ INFO ] Processing output blobs

Top 10 results:

Image /opt/intel/openvino/deployment_tools/demo/car.png

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

[⇧](#top)

- HDDL <a id="project-setup-linux-hddl"></a>

```
source /opt/intel/openvino/bin/setupvars.sh

${HDDL_INSTALL_DIR}/install_IVAD_VPU_dependencies.sh

========================================
Install HDDL depencdencies sucessful
Please reboot
```

```
cd ${HDDL_INSTALL_DIR}/drivers

sudo ./setup.sh install
```

```
source /opt/intel/openvino/bin/setupvars.sh

cd /opt/intel/openvino/deployment_tools/demo

./demo_squeezenet_download_convert_run.sh -d HDDL

Run Inference Engine classification sample

Run ./classification_sample_async -d HDDL -i /opt/intel/openvino/deployment_tools/demo/car.png -m /home/sergio/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml

[ INFO ] InferenceEngine: 
	API version ............ 2.1
	Build .................. 2020.3.1-3500-68236d2e44c-releases/2020/3
	Description ....... API
[ INFO ] Parsing input parameters
[ INFO ] Parsing input parameters
[ INFO ] Files were added: 1
[ INFO ]     /opt/intel/openvino/deployment_tools/demo/car.png
[ INFO ] Creating Inference Engine
	HDDL
	HDDLPlugin version ......... 2.1
	Build ........... 2020.3.1-3500-68236d2e44c-releases/2020/3

[ INFO ] Loading network files
[ INFO ] Preparing input blobs
[ WARNING ] Image is resized from (787, 259) to (227, 227)
[ INFO ] Batch size is 1
[ INFO ] Loading model to the device
[19:07:42.8180][2716]I[main.cpp:243] ## HDDL_INSTALL_DIR: /opt/intel/openvino_2020.3.341/deployment_tools/inference_engine/external/hddl
[19:07:42.8184][2716]I[main.cpp:245] Config file '/opt/intel/openvino_2020.3.341/deployment_tools/inference_engine/external/hddl/config/hddl_service.config' has been loaded
[19:07:42.8201][2716]I[FileHelper.cpp:272] Set file:/var/tmp/hddl_service_alive.mutex owner: user-'no_change', group-'users', mode-'0660'
[19:07:42.8203][2716]I[FileHelper.cpp:272] Set file:/var/tmp/hddl_service_ready.mutex owner: user-'no_change', group-'users', mode-'0660'
[19:07:42.8205][2716]I[FileHelper.cpp:272] Set file:/var/tmp/hddl_start_exit.mutex owner: user-'no_change', group-'users', mode-'0660'
[19:07:42.8262][2716]I[AutobootStarter.cpp:156] Info: No running autoboot process. Start autoboot daemon...
[19:07:42.8629][2718]I[FileHelper.cpp:272] Set file:/var/tmp/hddl_autoboot_alive.mutex owner: user-'no_change', group-'users', mode-'0660'
[19:07:42.8632][2718]I[FileHelper.cpp:272] Set file:/var/tmp/hddl_autoboot_ready.mutex owner: user-'no_change', group-'users', mode-'0660'
[19:07:42.8633][2718]I[FileHelper.cpp:272] Set file:/var/tmp/hddl_autoboot_start_exit.mutex owner: user-'no_change', group-'users', mode-'0660'
[19:07:42.8635][2718]I[FileHelper.cpp:272] Set file:/tmp/hddl_autoboot_device.map owner: user-'no_change', group-'users', mode-'0660'
[19:07:42.8643][2718]I[AutoBoot.cpp:308] [Firmware Config] deviceName=default deviceNum=0 firmwarePath=/opt/intel/openvino_2020.3.341/deployment_tools/inference_engine/external/hddl/lib/mvnc/usb-ma2x8x.mvcmd
[19:07:44.1740][2727]I[AutoBoot.cpp:197] Start boot device 1.8-ma2480
[19:07:44.4334][2727]I[AutoBoot.cpp:199] Device 1.8-ma2480 boot success, firmware=/opt/intel/openvino_2020.3.341/deployment_tools/inference_engine/external/hddl/lib/mvnc/usb-ma2x8x.mvcmd
[19:07:44.4335][2727]I[AutoBoot.cpp:197] Start boot device 1.4-ma2480
[19:07:44.6188][2727]I[AutoBoot.cpp:199] Device 1.4-ma2480 boot success, firmware=/opt/intel/openvino_2020.3.341/deployment_tools/inference_engine/external/hddl/lib/mvnc/usb-ma2x8x.mvcmd
[19:08:04.6232][2716]I[AutobootStarter.cpp:85] Info: Autoboot is running.
[19:08:04.6586][2716]W[ConfigParser.cpp:269] Warning: Cannot find key, path=scheduler_config.max_graph_per_device subclass=0, use default value: 1.
[19:08:04.6588][2716]W[ConfigParser.cpp:292] Warning: Cannot find key, path=scheduler_config.use_sgad_by_default subclass=0, use default value: false.
[19:08:04.6590][2716]I[DeviceSchedulerFactory.cpp:56] Info: ## DeviceSchedulerFacotry ## Created Squeeze Device-Scheduler2.
[19:08:04.6620][2716]I[DeviceManager.cpp:551] ## SqueezeScheduler created ##
[19:08:04.6620][2716]I[DeviceManager.cpp:649] times 0: try to create worker on device(2.6)
[19:08:06.6700][2716]I[DeviceManager.cpp:670] [SUCCESS] times 0: create worker on device(2.6)
[19:08:06.6702][2716]I[DeviceManager.cpp:719] worker(Wt2.6) created on device(2.6), type(0)
[19:08:06.6703][2716]I[DeviceManager.cpp:649] times 0: try to create worker on device(2.2)
[19:08:08.6752][2716]I[DeviceManager.cpp:670] [SUCCESS] times 0: create worker on device(2.2)
[19:08:08.6753][2716]I[DeviceManager.cpp:719] worker(Wt2.2) created on device(2.2), type(0)
[19:08:08.6754][2716]I[DeviceManager.cpp:145] DEVICE FOUND : 2
[19:08:08.6754][2716]I[DeviceManager.cpp:146] DEVICE OPENED : 2
[19:08:08.6757][2716]I[DeviceManagerCreator.cpp:81] New device manager(DeviceManager0) created with subclass(0), deviceCount(2)
[19:08:09.0120][2716]I[TaskSchedulerFactory.cpp:45] Info: ## TaskSchedulerFactory ## Created Polling Task-Scheduler.
[19:08:09.0676][2716]I[FileHelper.cpp:272] Set file:/var/tmp/hddl_snapshot.sock owner: user-'no_change', group-'users', mode-'0660'
[19:08:09.0685][2716]I[FileHelper.cpp:272] Set file:/var/tmp/hddl_service.sock owner: user-'no_change', group-'users', mode-'0660'
[19:08:09.0687][2716]I[MessageDispatcher.cpp:87] Message Dispatcher initialization finished
[19:08:09.0689][2716]I[main.cpp:103] SERVICE IS READY ...
[19:08:09.0882][2766]I[ClientManager.cpp:159] client(id:1) registered: clientName=HDDLPlugin socket=2
[19:08:09.4250][2767]I[GraphManager.cpp:491] Load graph success, graphId=1 graphName=squeezenet1.1
[ INFO ] Create infer request
[ INFO ] Start inference (10 asynchronous executions)
[ INFO ] Completed 1 async request execution
[ INFO ] Completed 2 async request execution
[ INFO ] Completed 3 async request execution
[ INFO ] Completed 4 async request execution
[ INFO ] Completed 5 async request execution
[ INFO ] Completed 6 async request execution
[ INFO ] Completed 7 async request execution
[ INFO ] Completed 8 async request execution
[ INFO ] Completed 9 async request execution
[ INFO ] Completed 10 async request execution
[ INFO ] Processing output blobs

Top 10 results:

Image /opt/intel/openvino/deployment_tools/demo/car.png

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

[19:08:09.5416][2766]I[ClientManager.cpp:189] client(id:1) unregistered: clientName=HDDLPlugin socket=2
[19:08:09.5501][2767]I[GraphManager.cpp:539] graph(1) destroyed
[ INFO ] Execution successful
```

```
source /opt/intel/openvino/bin/setupvars.sh

cd /opt/intel/openvino/deployment_tools/demo

./demo_security_barrier_camera.sh -d HDDL

Run Inference Engine security_barrier_camera demo

Run ./security_barrier_camera_demo -d HDDL -d_va HDDL -d_lpr HDDL -i /opt/intel/openvino/deployment_tools/demo/car_1.bmp -m /home/sergio/openvino_models/ir/intel/vehicle-license-plate-detection-barrier-0106/FP16/vehicle-license-plate-detection-barrier-0106.xml -m_lpr /home/sergio/openvino_models/ir/intel/license-plate-recognition-barrier-0001/FP16/license-plate-recognition-barrier-0001.xml -m_va /home/sergio/openvino_models/ir/intel/vehicle-attributes-recognition-barrier-0039/FP16/vehicle-attributes-recognition-barrier-0039.xml

[ INFO ] InferenceEngine: 0x7fe2896b9040
[ INFO ] Files were added: 1
[ INFO ]     /opt/intel/openvino/deployment_tools/demo/car_1.bmp
[ INFO ] Loading device HDDL
	HDDL
	HDDLPlugin version ......... 2.1
	Build ........... 2020.3.1-3500-68236d2e44c-releases/2020/3

[ INFO ] Loading detection model to the HDDL plugin
[19:10:08.9352][2766]I[ClientManager.cpp:159] client(id:2) registered: clientName=HDDLPlugin socket=2
[19:10:10.3769][2767]I[GraphManager.cpp:491] Load graph success, graphId=2 graphName=vehicle-license-plate-detection-barrier-0106
[ INFO ] Loading Vehicle Attribs model to the HDDL plugin
[19:10:10.4047][2766]I[ClientManager.cpp:159] client(id:3) registered: clientName=HDDLPlugin socket=3
[19:10:10.5231][2767]I[GraphManager.cpp:491] Load graph success, graphId=3 graphName=vehicle-attributes-recognition-barrier-0039
[ INFO ] Loading Licence Plate Recognition (LPR) model to the HDDL plugin
[19:10:10.5555][2766]I[ClientManager.cpp:159] client(id:4) registered: clientName=HDDLPlugin socket=4
[19:10:10.7742][2767]I[GraphManager.cpp:491] Load graph success, graphId=4 graphName=LPRNet
[ INFO ] Number of InferRequests: 1 (detection), 3 (classification), 3 (recognition)
[ INFO ] Display resolution: 1920x1080
[ INFO ] Number of allocated frames: 3
[ INFO ] Resizable input with support of ROI crop and auto resize is disabled
0.1FPS for (3 / 1) frames
Detection InferRequests usage: 0.0%

[19:10:58.6994][2766]I[ClientManager.cpp:189] client(id:4) unregistered: clientName=HDDLPlugin socket=4
[19:10:58.7059][2767]I[GraphManager.cpp:539] graph(4) destroyed
[19:10:58.8015][2766]I[ClientManager.cpp:189] client(id:3) unregistered: clientName=HDDLPlugin socket=3
[19:10:58.8075][2767]I[GraphManager.cpp:539] graph(3) destroyed
[19:10:58.9046][2766]I[ClientManager.cpp:189] client(id:2) unregistered: clientName=HDDLPlugin socket=2
[19:10:58.9201][2767]I[GraphManager.cpp:539] graph(2) destroyed
[ INFO ] Execution successful
```

```
source /opt/intel/openvino/bin/setupvars.sh

cd ~/inference_engine_samples_build/intel64/Release

./classification_sample_async -i /opt/intel/openvino/deployment_tools/demo/car.png -m ~/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml -d HDDL

./classification_sample_async -i /opt/intel/openvino/deployment_tools/demo/car.png -m ~/openvino_models/ir/public/squeezenet1.1/FP16/squeezenet1.1.xml -d HDDL
[ INFO ] InferenceEngine: 
	API version ............ 2.1
	Build .................. 2020.3.1-3500-68236d2e44c-releases/2020/3
	Description ....... API
[ INFO ] Parsing input parameters
[ INFO ] Parsing input parameters
[ INFO ] Files were added: 1
[ INFO ]     /opt/intel/openvino/deployment_tools/demo/car.png
[ INFO ] Creating Inference Engine
	HDDL
	HDDLPlugin version ......... 2.1
	Build ........... 2020.3.1-3500-68236d2e44c-releases/2020/3

[ INFO ] Loading network files
[ INFO ] Preparing input blobs
[ WARNING ] Image is resized from (787, 259) to (227, 227)
[ INFO ] Batch size is 1
[ INFO ] Loading model to the device
[19:12:00.9253][2766]I[ClientManager.cpp:159] client(id:5) registered: clientName=HDDLPlugin socket=2
[19:12:01.1912][2767]I[GraphManager.cpp:491] Load graph success, graphId=5 graphName=squeezenet1.1
[ INFO ] Create infer request
[ INFO ] Start inference (10 asynchronous executions)
[ INFO ] Completed 1 async request execution
[ INFO ] Completed 2 async request execution
[ INFO ] Completed 3 async request execution
[ INFO ] Completed 4 async request execution
[ INFO ] Completed 5 async request execution
[ INFO ] Completed 6 async request execution
[ INFO ] Completed 7 async request execution
[ INFO ] Completed 8 async request execution
[ INFO ] Completed 9 async request execution
[ INFO ] Completed 10 async request execution
[ INFO ] Processing output blobs

Top 10 results:

Image /opt/intel/openvino/deployment_tools/demo/car.png

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

[19:12:01.3033][2766]I[ClientManager.cpp:189] client(id:5) unregistered: clientName=HDDLPlugin socket=2
[19:12:01.3114][2767]I[GraphManager.cpp:539] graph(5) destroyed
[ INFO ] Execution successful
```

[⇧](#top)

### Windows <a id="project-setup-windows"></a>

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

- Intel Distribution of OpenVINO Toolkit 2020.3.1 LTS

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

[⇧](#top)

- NCS2 (Intel Neural Compute Stick 2) <a id="project-setup-windows-ncs2"></a>

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

[⇧](#top)

## Project Start

### Linux <a id="project-start-linux"></a>

- Pillow

```
sudo apt-get install python3-pil
```

- TkInter

```
sudo apt-get install python3-tk
```

- ImageTk

```
sudo apt-get install python3-pil.imagetk
```

- Visual Studio Code 

```
cd ~/Downloads/

sudo apt install ./code_1.54.3-1615806378_amd64.deb
```

- Git

```
sudo apt-get install git
```

- https://github.com/SergioVelmay/MVPy_MachineVisionPoka-yoke.git

```
cd ~/MVPy_MachineVisionPoka-yoke

MVPy.sh
```

```
source /opt/intel/openvino/bin/setupvars.sh
```

```
cd ~/MVPy_MachineVisionPoka-yoke

python3 MVPy.py
```

[⇧](#top)

### Windows <a id="project-start-windows"></a>

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

- Videos .mp4 without audio track

```
Warning: libmmd.dll couldn't be found in %PATH%.
Please check if the redistributable package for Intel(R) C++ Compiler is installed and the library path is added to the PATH environment variable.
System reboot can be required to update the system environment.

C:\Program Files (x86)\Common Files\Intel\Shared Libraries\redist\intel64_win\compiler\

libmmd.dll

Edit the system environment variables / Environment Variables... / Path / Edit... / New / "C:\..." / Ok

https://software.intel.com/content/www/us/en/develop/articles/redistributable-libraries-for-intel-c-and-fortran-2020-compilers-for-windows.html
```

[⇧](#top)

## Model Optimizer

### Windows <a id="model-optimizer-windows"></a>

- Prerequisites

```
cd C:\Program Files (x86)\IntelSWTools\openvino\deployment_tools\model_optimizer\install_prerequisites

install_prerequisites_tf.bat
```

- TensorFlow

```
pip install tensorflow==1.2
```

- Object Detection

```
cd C:\Program Files (x86)\IntelSWTools\openvino\deployment_tools\model_optimizer

py mo_tf.py --log_level=DEBUG --output_dir C:\Users\sergi\Desktop\MVPy\Models\Part4Detection\IR -b 1 --input_model C:\Users\sergi\Desktop\MVPy\Models\Part4Detection\GeneralCompact.TensorFlow\model.pb

[ SUCCESS ] Generated IR version 10 model.
[ SUCCESS ] XML file: C:\Users\sergi\Desktop\MVPy\Models\Part4Detection\IR\model.xml
[ SUCCESS ] BIN file: C:\Users\sergi\Desktop\MVPy\Models\Part4Detection\IR\model.bin
[ SUCCESS ] Total execution time: 24.51 seconds.
```

- Image Classification

```
cd C:\Program Files (x86)\IntelSWTools\openvino\deployment_tools\model_optimizer

py mo_tf.py --log_level=DEBUG --output_dir C:\Users\sergi\Desktop\MVPy\Models\ORingClassification\IR -b 1 --input_model C:\Users\sergi\Desktop\MVPy\Models\ORingClassification\GeneralCompact.TensorFlow\model.pb

[ SUCCESS ] Generated IR version 10 model.
[ SUCCESS ] XML file: C:\Users\sergi\Desktop\MVPy\Models\ORingClassification\IR\model.xml
[ SUCCESS ] BIN file: C:\Users\sergi\Desktop\MVPy\Models\ORingClassification\IR\model.bin
[ SUCCESS ] Total execution time: 54.47 seconds.
```

[⇧](#top)

## Vizi-AI GPIO MRAA

### Linux <a id="vizi-ai-gpio-mraa-linux"></a>

[⇧](#top)
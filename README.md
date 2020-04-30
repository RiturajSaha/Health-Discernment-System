# Health-Discernment-System
Diseases like Malaria, Pneumonia, Breast cancer and Skin cancer are very common and suffering patients are increasing every day. So our team has created a Helath Discernment System which will detect if a patient is suffering from Malaria, Pneumonia, Breast cancer or Skin cancer by taking an essential input image. The frontend of this product is created using Python Tkinter module and for backend, four different custom CNN models are developed for detecting the diseases.

Below are diseases and their accuracy of detecting it in a patient: 
| Model(Disease)  | Accuracy |
| ------------- | ------------- |
| Malaria  | 95.21%  |
| Pneumonia  | 90.47%  |
| Breast Cancer  | 86.88%  |
| Skin Cancer  | 83.58%  |

### Product Scope
This system will help to predict the medical results efficiently. In this predicting system, we will provide an user friendly interface that can be used by the users to detect whether their medical test results are positive or normal, i.e. it will detect the disease. This will ultimately help the patients to save time as they won’t have to run to the doctor just to know what their medical
reports say. In case the test results are negative, it will greatly help the patient to save money, as there won’t be any requirement to visit the doctor again. Decisions are often made based on the doctor’s intuition and experience and sometimes
that may not be completely correct. In this interface the predictions will be free of unwanted biases and errors- so it will be completely trust worthy. The doctors can also use this system to predict the results better. The lab technicians and the other health-care professionals can also use this predicting system to guide the people.

### Technical Process
Following are the technologies that are used to develop the project:
-**Front-end development:** Deep Learning, Transfer Learning
-**Back-end development:** Tkinter

### Performance Requirements
- The product performance will be based on a local system.
- The image prediction will take some time.
- The evaluation performance will depend on some software and hardware components.

### Product Perspective
The Health Discernment System helps not only the patients but also the health-care professionals to predict the medical test results more effectively and in a bias-free manner by computerizing the prediction process. Predictions or results will be generated from the medical test images which will help the patients to take appropriate decisions regarding the course of their treatment. For example, if the patient fails to get the doctor’s appointment, they can still know the results of their medical tests by simply using this interface and this in term saves time and money.

### Product Functionality
System will read the image uploaded by the user, augment it and will use the
saved custom model to detect whether the disease is present or not in the patient
and thus display the result in a user-friendly language.
##### Below are the step:
- **Upload Image**
The user can upload the medical test image through a workstation running on Windows OS. The image should be in jpeg, png or jpg format.
- **Read Image**
The image will be scanned before augmentation takes place.
- **Transform Image**
The scanned image is then transformed into a format that is needed by the
saved custom model.
- **Evaluate image using saved model**
The saved custom model creates a feature map of the uploaded medical test
image and predicts the output.
- **Determine and Analyze the Output**
The predicted output is then analyzed (0 means normal; 1means positive)
and converted to a user friendly language.
- **Display the Output**
The analyzed result is then displayed to the user.

### Users and Characteristics
The Health Discernment System has one active actor(patients along with healthcare professionals) and one cooperating system at the back end. The patients and health-care professionals like doctors and interns can access the system through a desktop for predicting diseases.

### Operating Environment
**Operating System:*** Minimum Windows XP or Windows VISTA. Better environment Windows 7, 8, 8.1, 10.
**Language:** Python
A workstation which will run on any Windows OS is needed to predict the
diseases using this system.

### Assumptions and Dependencies
If the user has a workstation that works on Windows OS then that person can easily use the predicting interface. The user also has to have the medical test images in JPEG, JPG or PNG format for prediction purpose.

###External Interface Requirements
There are many types of interfaces that are supported by this system. Namely-
User Interface and Software Interface.
#####User Interfaces: The user interface will be implemented using any desktop running on Windows OS. This interface will be very user friendly, so that people from different strata can use it to detect their disease without any difficulty by just uploading their
medical test image. 
#####Software Interfaces: A software interface running on Windows OS. It should have Python
compiler(3.6).



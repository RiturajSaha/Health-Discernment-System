# Health-Discernment-System

### Product Link: [**[***DOWNLOAD*]](https://drive.google.com/open?id=1CcUnRM_3RQC34I1HZBy4ggGEnSNUf_Km)

### Product Description
Diseases like Malaria, Pneumonia, Breast cancer and Skin cancer are very common and suffering patients are increasing every day. So our team has created a Helath Discernment System which will detect if a patient is suffering from Malaria, Pneumonia, Breast cancer or Skin cancer by taking an essential input image. The frontend of this product is created using Python Tkinter module and for backend, four different custom CNN models are developed for detecting the diseases.

**Below are diseases and their accuracy of detecting it in a patient:** 
| Model(Disease)  | Accuracy |
| ------------- | ------------- |
| Malaria  | 95.21%  |
| Pneumonia  | 90.47%  |
| Breast Cancer  | 86.88%  |
| Skin Cancer  | 83.58%  |


### Product Scope
This system will help to predict the medical results efficiently. In this predicting system, we will provide an user friendly interface that can be used by the users to detect whether their medical test results are positive or normal, i.e. it will detect the disease. This will ultimately help the patients to save time as they won’t have to run to the doctor just to know what their medical
reports say. In case the test results are negative, it will greatly help the patient to save money, as there won’t be any requirement to visit the doctor again. Decisions are often made based on the doctor’s intuition and experience and sometimes that may not be completely correct. In this interface the predictions will be free of unwanted biases and errors- so it will be completely trust worthy. The doctors can also use this system to predict the results better. The lab technicians and the other health-care professionals can also use this predicting system to guide the people.


### Technical Process
Following are the technologies that are used to develop the project:
- **Front-end development:** Deep Learning, Transfer Learning
- **Back-end development:** Tkinter


### Product Functionality
System will read the image uploaded by the user, augment it and will use the
saved custom model to detect whether the disease is present or not in the patient
and thus display the result in a user-friendly language.
##### Below are the steps:
- **Upload Image:**<br/>
The user can upload the medical test image through a workstation running on Windows OS. The image should be in jpeg, png or jpg format.
- **Read Image:**<br/>
The image will be scanned before augmentation takes place.
- **Transform Image:**<br/>
The scanned image is then transformed into a format that is needed by the
saved custom model.
- **Evaluate image using saved model:**<br/>
The saved custom model creates a feature map of the uploaded medical test
image and predicts the output.
- **Determine and Analyze the Output:**<br/>
The predicted output is then analyzed and converted to a user friendly language.
- **Display the Output:**<br/>
The analyzed result is then displayed to the user.


### Users and Characteristics
The Health Discernment System has one active actor(patients along with healthcare professionals) and one cooperating system at the back end. The patients and health-care professionals like doctors and interns can access the system through a desktop for predicting diseases.


### Assumptions and Dependencies
If the user has a workstation that works on Windows OS then that person can easily use the predicting interface. The user also has to have the medical test images in JPEG, JPG or PNG format for prediction purpose.


### Product Requirements
##### Operating Environment
- **Operating System:** Minimum Windows XP or Windows VISTA. Better environment Windows 7, 8, 8.1, 10.
- **Language:** Python 3.6
- A workstation which will run on any Windows OS is needed to predict the diseases using this system.

##### Performance Requirements
- The product performance will be based on a local system.
- The image prediction will take some time.
- The evaluation performance will depend on some software and hardware components.

##### Other Requirements
- **Licensing Requirements:**<br/>
Not Applicable.
- **Legal, Copyright, and Other Notices:**<br/>
All right reserved by our team.
- **Applicable Standards:**<br/>
It should be as per the medical standard.

### References
- [www.kaggle.com](https://www.kaggle.com) - the world’s largest data science community
- [www.tensorflow.org](https://www.tensorflow.org) - open source machine-learning platform
- [www.superdatascience.com/deep-learning](https://www.superdatascience.com/deep-learning) - online educational platform
- [www.udemy.com](https://www.udemy.com) - online learning platform
### Product Developers
[**Rituraj Saha**](https://www.linkedin.com/in/rituraj-saha/)</br>
[**Ritam Barik**](https://www.linkedin.com/in/ritam-barik-557905195/)</br>
[**Pranav Jain**](https://www.linkedin.com/in/pranav-jain-0516ba195/)</br>
[**Anish Kumar**](https://www.linkedin.com/in/anish-kumar-6a5b60169/)</br>

**Note:** The custom CNN disease models are not uploaded in the repository.

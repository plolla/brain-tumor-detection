# Brain-Tumor-Detection

Built an image classifier that looks at brain MRI scans and classifies brains with tumors and brains without tumors. Utilized transfer learning and fine tuned pretrained models (MobileNetV2, VGG16, and ResNet50). Used TensorFlow and Keras, as well as NumPy, Matplotlib, OpenCV, and Scikit-Learn. 

Using Flask to host the application. Used HTML/CSS for frontend

Currently working on deploying app publicly

## Screenshots
This is the main page where users can upload their scans to the site: 

![Home Page](https://user-images.githubusercontent.com/19865455/177800654-e208371e-17af-4443-9ce0-fa878ecf1bac.png)

After uploading the scan, a POST request is made to send the image data to the API which will return the prediction

This is the response the user will see if their scan doesn't indicate any sign of a tumor
![Result Page (NO)](https://user-images.githubusercontent.com/19865455/177805481-f1f21f60-e150-497d-b8bd-cc070ff80528.png)
Users can always chose to go back and upload another scan

This is the response the user will see if their scan does show a tumor
![Result Page (YES)](https://user-images.githubusercontent.com/19865455/177806594-84306d0a-b9a0-41d2-9bc6-0622408bc4aa.png)

## Tech/framework used

<b>Built with</b>
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [TensorFlow](https://www.tensorflow.org)
- [Numpy](https://numpy.org)
- Python
- JavaScript
- HTML/CSS

# Brain-Tumor-Detection

## Summary

Built an image classifier that looks at brain MRI scans and classifies brains with tumors and brains without tumors. Utilized transfer learning and fine tuned pretrained models (MobileNetV2, VGG16, and ResNet50)

Currently working on deploying app publicly

## Screenshots

This is the main page where users can upload their scans to the site: 
![Home Page](https://user-images.githubusercontent.com/19865455/177800654-e208371e-17af-4443-9ce0-fa878ecf1bac.png)

After uploading the scan, a POST request is made to send the image data to the API which will return the prediction

This is the response the user will see if their scan doesn't indicate any sign of a tumor
![Result Page (NO)](https://user-images.githubusercontent.com/19865455/177808026-714ceb9a-ee2c-4070-a479-616922847ef2.png")
Users can always chose to go back and upload another scan

This is the response the user will see if their scan does show a tumor
![Result Page (YES)](https://user-images.githubusercontent.com/19865455/177809155-a5e1cae8-a81b-46e0-9c65-ec5885eb5179.png)

## Tech/framework used

<b>Built with</b>
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [TensorFlow](https://www.tensorflow.org)
- [Numpy](https://numpy.org)
- [Matplotlib](https://matplotlib.org)
- [OpenCV](https://opencv.org)
- Python
- JavaScript
- HTML/CSS

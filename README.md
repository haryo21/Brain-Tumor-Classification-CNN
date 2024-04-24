Brain Tumor Classification using CNN
This project involves the development of a Convolutional Neural Network (CNN) model to classify brain tumors based on MRI scans. The trained model is deployed as a web application using Flask, enabling users to upload MRI scans and receive predicted tumor classifications.

## Project Overview
The project comprises the following main components:

- **Data Preprocessing**: MRI scan images undergo preprocessing to prepare them for training the CNN model.
- **Model Training**: Various CNN architectures, including VGG16 and Inception, are explored to train the brain tumor classification model.
- **Model Deployment**: The trained CNN model is deployed as a web application using Flask, allowing users to upload MRI scans and obtain predicted tumor classifications.

## Getting Started
To begin with the project, follow these steps:

1. Clone the repository:
bash
git clone https://github.com/haryo21/Brain-Tumor-Classification-CNN.git

2. Install the required dependencies:

bash
pip install -r requirements.txt

3. Generate the pre-trained model files (.h5 files) by running the respective CNN architecture scripts in the `Program CNN/` folder.
4. Deploy the Flask application by running the `app.py` file:
bash
python app.py

5. Upload an MRI scan image through the web interface, and the deployed model will predict the tumor classification.

## Repository Structure
- **Program CNN/**: Contains scripts for training different CNN architectures (e.g., VGG16, Inception) and generating the pre-trained model files (.h5 files).
- **app.py**: The Flask application script for deploying the brain tumor classification model.
- **static/**: Directory for storing static files (e.g., CSS, JavaScript).
- **templates/**: Directory for storing HTML templates.
- **README.md**: This file, providing an overview and instructions for the project.

## Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Flask for the web application framework.
- TensorFlow and Keras for building and training the CNN models.

Feel free to customize and enhance this README.md file according to your project's specific details and requirements.


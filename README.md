# OpticalApp

## Introduction
OpticalApp is an AI-powered tool designed to assist opticians by recognizing lens engravings and helping them manage their workflow more efficiently. This project was initiated in collaboration with a certified optician, and its purpose is to streamline the process of identifying lens engravings using machine learning techniques.

The project involves scraping data from France Optique, fine-tuning YOLOv8 for recognizing lens engravings, and building a user-friendly interface for tactile engraving recognition on mobile devices.

## Project Structure
The project has been restructured to maintain a professional approach and includes the following directories:

**config/:** Contains the configuration files for the training data.<br>
**data/:** Holds the datasets (e.g., test, train, valid) used for training the YOLOv8 model.<br>
**formulaire/:** Includes the analysis notebooks and questionnaires used to verify the project requirements.<br>
**models/:** Stores the trained weights and models generated during training.<br>
**notebooks/:** Jupyter notebooks used for prototyping and analysis.<br>
**outputs/:** The results, logs, and artifacts generated during training and evaluation.<br>
**src/:** Main source code for the OpticalApp project.<br>
**opticalapp/spiders:** Contains the spiders used for scraping engraving data from the France Optique website.<br>

## Setup Instructions
To run OpticalApp on your local machine:

## Prerequisites
Python 3.12 or newer
Pip
CUDA-compatible GPU (for model training)
Git
Installation
Clone the repository:

```bash
git clone git@github.com:AntoineMLD/opticalApp.git
cd opticalApp
Create a virtual environment and activate it:
```
```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\\Scripts\\activate`
```
Install the dependencies:

```bash
pip install -r requirements.txt
```
Running the Application
To train the model:

```bash
python src/train_model.py
```
To run the web scraping spider:

```bash
scrapy crawl opticalspider
```
## Directory Details
**config:** Config files for YOLOv8.<br>
**data:** Contains the training, validation, and test datasets, along with data configuration files.<br>
**formulaire:** Contains all analysis notebooks and related files, including surveys conducted.
models: Trained YOLOv8 weights are saved here.<br>
**notebooks:** For experimental analysis and prototyping.<br>
**outputs:** Stores all the training results, such as metrics and logs.<br>
**src:** Main source code, including the scraping spider and scripts for model training and evaluation.<br>

## Model Training
The model is trained using YOLOv8 on custom data scraped from France Optique. The training process was iterated over 100 epochs, and results were logged and analyzed. The model was further fine-tuned using images drawn by users to mimic tactile engravings.

## Usage Instructions
OpticalApp has the following primary features:

**Lens Engraving Detection:** The trained model can detect specific engravings on lenses, which can help opticians reduce manual workload.
**Tactile Engraving Recognition:** Users can draw engravings on a mobile interface, which the model can recognize and identify.


## Acknowledgments
Special thanks to Simplon for the training opportunity and the opticians who provided valuable insights during the initial phases of the project. ​

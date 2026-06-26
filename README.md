# Galaxy-Classifier-CNN Model
A CNN Model to Classify Galaxies Based On Features--1500 predictions made on uncertain galaxy classification

## About the Project
* It is a machine learning CNN model used to classify galaxies based on its dinstinct features
* Achieved **87.64%** accuracy on test set 
* Trained, validated, and tested on 21,000+ images
* Used to classify 1500+ glaxies that had uncertain classifications

## Why I built this
* The Galaxy Zoo team is seeking volunteers to classify numerous galaxies that were collected from the James Webb Space Telescome
* I love astronomy, and wanted to do a mini research project
   * I decided to code a way to help the Galaxy Zoo Team

## Pipeline/Procedure 
* I built a CNN that was trained on 21,000 images from the Galaxy10 SDSS dataset
* I used the 2016 Galaxy Zoo excel dataset that has the classifications for over 240,000 galaxies
* I created two .py scripts (in the Data Scripts folder)
  * **UncertainClassification.py**: Looks through all 240,000 galaxies, finds the galaxies that had uncertain classifications (i.e., between .4 and .6 probability), and then downloads 1,500 images of those uncertain galaxy classification
       * This script found over 20,000 uncertain galaxies
   * **ImageProcessing.py**: This script ensures that the 1,500 image found are compatibale with my model by resizing them to 69 by 69, removing corrupted files, etc
 * The 1500 images collected was then put through my model for classification
 * The **output** folder contains the csv file of the classifications collected 

## HOW TO RUN:
* Download the 2016 Galaxy Zoo excel dataset: **https://gz2hart.s3.amazonaws.com/gz2_hart16.csv.gz** --> Link to download
* Run UncertainClassification.py
* Run ImageProcessing.py
* Upload the folder containing all the images that were processed into a google drive folder named "galaxyZoo2ImagesCleaned"
* Run each cell of the .ipynb file (in the notebook folder)
  
 
## Developmental Timeline
* Built over 3 months (April to June)
   * It was an on and off project between school and personal life

# Key Milestones
* Month 1: Researching CNNs, computer visions, and building the first few iterations of my model
* Month 2: Optimizing/finetuning the CNN and collecting 1500+ images for inference set
* Month 3: Further refinement to CNN, processing the 1500+ images collected, and running the model on inference set

## Technology Used
* Python 3.13.2
* VS Code
* Google Colab

## Future Roadmap
>> Note: This project is considered complete, but feel free to fork the repository and further develop it.

* Expand the uncertain galaxy images: I used 1,500 to minimize strain on my laptop, but there is over 20,000 galaxies that still need better classifications
* **Ensemble Method**: Combining my model with a pre-trained models like EfficientNet to get a more robust and accurate model 




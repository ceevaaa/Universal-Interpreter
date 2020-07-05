## EDIT- 19th May 2020
Winner of Unisys Cloud 2020

# Universal Interpreter  
A solution to help the differently-abled people, i.e. deaf, dumb, blind or combination of any, by using Image
Recognition and AI/ML.  

## **Inspiration**  

The present world we live in, a world dominated by visual and audio peripherals, can prove to be
a tough place to live in for differently abled people. Hence, our aim was inspired by the need to
use the very same dominating technologies to help the differently abled overcome their challenges.  

## **Requirements**  
* Python 
* Tensorflow  
* OpenCV  
* Web development/Android tools for UI/Testing  

## **Project Flow**  

### **Phase 1 - Input Phase**    
Collect Data such as Gestures (Sign language), taps (for Morse Code) or direct speech (Voice)
from any client device.  

### **Phase 2 - Conversation and Transmission Phase**    
Convert the input data into some fundamental form (such as Morse/Digital), transmit and process
the data.  

### **Phase 3 - Output Phase**    
Take the output data and represent it either visually, via vibrations or via speech, depending on the following:  
1. Voice/Morse for the Blind
2. Sign-language/Text for the Deaf
3. Sign-language/Voice for the Dumb
4. Morse codes wherever these are not possible  

## **Project Flow - Flowchart**  
![Project Flow - Flowchart](./Abstract_Flowchart.jpg)

## **Android App Implementation**
[Universal Interpreter Android App GitHub Link](https://github.com/allanakshay12/Universal-Interpreter-Android-App.git)

## **Instructions to use the Project**

### Data Set Training and Usage
1. Install all the dependencies from the requirements.txt file.
2. Prepare the image data sets - In order to start the transfer learning process, a folder named dataset needs to be created in the root of the project folder. This folder will contain the image data sets for all the subjects, for which the classification is to be performed.
3. Create the dataset folder and add the images for all the data sets in the following manner:
>|
---- /dataset
|    |
|    |
|    ---- /A
|    |    A1.jpg
|    |    A2.jpg
|    |    ...
|    |
|    |
|    ---- /B
|         B1.jpg
|         B2.jpg
|         ...
|`
This enables classification of images between the A and B data sets.
4. Initiate transfer learning - Go to the project directory and run:
`python train.py \
  --bottleneck_dir=logs/bottlenecks \
  --how_many_training_steps=2000 \
  --model_dir=inception \
  --summaries_dir=logs/training_summaries/basic \
  --output_graph=logs/trained_graph.pb \
  --output_labels=logs/trained_labels.txt \
  --image_dir=./dataset`
5. The training summaries, trained graphs and trained labels will be saved in a folder named logs.
6. To run prediction on the images use " python classify.py _example.png_ ".
7. To run prediction using a webcam use " python classify_webcam.py ".

### Android App Usage

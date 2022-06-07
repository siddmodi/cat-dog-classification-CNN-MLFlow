# Dog-Cat classifier Ml-Flow 
Dog-Cat classifier Ml-Flow app

## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 05 - Create conda.yaml file -
```bash
conda env export > conda.yaml
```

### STEP 06- commit and push the changes to the remote repository

## MLFlow commands

### Command to run MLproject file
```bash
mlflow run . --no-conda
```
### run any specific entry point in MLproject file
```bash
mlflow run . -e get_data --no-conda
```

### run any specific entry point in MLproject file
```bash
mlflow run . -e get_data -P config=configs/your_config.yaml --no-conda
```
=================== **Explaination** ===============================

**Flask** app asking to upload picture and it'll predict whether it is a cat or dog.
We use **MLops** pipeline for this project to smoothen the process and seprate each stage from each other 

This project we divided in 5 stages. we use **tensorlow** to define our architecture

1) This stage download data from online source as zip file, extract that data and store in their respective directory automatically 

2) This stage will define a base **CNN** model architecture , create a base cnn model and save it in a dirrectory

3) Here we defined **early-stopping callback** in case the model is not improving much from last few iterations and checkpoint callbacks in case any 
   failure like powercut etc  
   
4) Here we **train** our base model with the data of cats and dogs run multiple epochs and dump that model in respective directory

5) Stage for prediction 

We also consider the situation if we stuck anywhere by creating **log** files for each and every steps for each stage

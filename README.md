# ML based Crop Recommendation Appliccation

---

## Technical Description

This app uses a Dataset with 2200 Datapoins for Training and for Generating predictions.</br>
Model used: Gaussian Naive Bayes</br>
Accuracy: 99.54%

---

## Run it on your Browser now! (New)

- Just click on this [link]https://github.com/Satyanaryana-Merla/Crop-Recommendation-system

- Enjoy!

---

## How to run on Local Machine

- Download the Github Package from this repo and Unzip it anywhere.

- Download and install Anaconda for Windows from this [link](https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe) or Jupyter for Windows from this [link](https://jupyter.org/install).

- Open Jupyter Notebook and navigate to the Crop-Recommendation folder.

- Launch a new Jupyter Terminal and type these commands</br>
```
 pip install streamlit
 pip install pandas
 pip install scikit-learn
```

- Now navigate to *Crop-Recommendation* folder using ```cd``` command in the terminal.

- Type this command
```
    streamlit run app.py
```

- Enjoy!

---

### Inspiration

Many farmers are confused when making the choice before the sowing season. This app will help them with their choice and save them a lot of time and money.

### What it does

It takes input about the Farmer's soil and tells them which Crop would be best for their soil type using ML prediction.

### How we built it

We have used a dataset of 2200 entries and trained an ML model on it for making the predictions. We have then used Streamlit library to create a user-friendly and simple UI for anyone to use. It uses Jupyter environment to run.

### Challenges we ran into

Finding the right dataset, Training the model for high accuracy, Hosting the model as a web-app. 

### Accomplishments that we're proud of

High Accuracy of our ML model (99.54% during validation). Custom UI elements on Streamlit web-app.

### What we learned

Machine Learning, Using Streamlit for Hosting, Creating custom environment on Jupyter.

---

# Algerian Forest Fire Weather Prediction (FWI)


**🌳 Project Overview**

This project implements a machine learning model to predict the Forest Fire Weather Index (FWI) based on various meteorological and forest fire activity metrics derived from the Algerian Forest Fire Dataset.

The solution involves a full data science pipeline: Data Cleaning, Exploratory Data Analysis (EDA), Regression Modeling using Ridge Regression, and deployment via a Flask web application. Users can input nine key parameters on the web page to receive a real-time FWI prediction.


**🛠️ Technology Stack**
---

Language: Python, HTML

Web Framework: Flask

Data Analysis: Pandas, NumPy, Matplotlib, Seaborn

Machine Learning: Scikit-learn (Ridge Regression, StandardScaler)

Model Persistence: pickle


**📊 Dataset and Methodology**
---

Data Source:

- The project utilizes the Algerian Forest Fire Dataset, which provides daily weather data and fire-related indices across two regions in Algeria.


Pipeline:

- Data Cleaning: Handled missing values, standardized column names, and converted necessary features to numeric types.

- Exploratory Data Analysis (EDA): Performed visualization and statistical analysis to understand feature distributions, correlations, and the relationship between weather factors and the FWI target variable.

- Feature Engineering: Categorical features (like Region and Classes) were prepared for model consumption.

- Modeling: A Ridge Regression model was trained to predict the FWI.

- Scaling: A StandardScaler was fitted to the training data and saved to ensure new inputs from the web application are scaled correctly before prediction.


**🚀 Getting Started**
---

Follow these instructions to set up and run the Flask application locally.

Prerequisites:

- Python (3.8+)

- pip (Python package installer)

1. Clone the Repository
```
git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
cd your-repo-name
```

2. Set Up the Environment

It is highly recommended to use a virtual environment to manage dependencies.
```
# Create the virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows (Command Prompt):
# venv\Scripts\activate.bat
```

3. Install Dependencies

Install all necessary libraries using the provided requirements.txt file:
```
pip install -r requirements.txt
```

4. Run the Application

The application requires the saved model files (ridge.pickle and scaler.pickle) to be present in the ./models directory.
```
# Ensure you are in the project's root directory and the venv is active
python application.py
```

The application will start, and you will see output similar to:
```
* Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
```

5. Access the Web App

Open your web browser and navigate to:

https://www.google.com/search?q=http://127.0.0.1:5000/predictdata

You can now input the nine required weather parameters and click "Predict" to see the calculated Forest Fire Weather Index (FWI).

**📁 Project Structure**
---

```
├── application.py          # Main Flask application file
├── requirements.txt        # Python package dependencies
├── models/
│   ├── ridge.pickle        # Trained Ridge Regression model
│   └── scaler.pickle       # Fitted StandardScaler object
├── templates/
│   ├── home.html           # Prediction form and result display
│   └── index.html          # Simple welcome page
└── README.md               # This file
```

**⚠️ Note on Model Versions**
---

If you encounter InconsistentVersionWarning from scikit-learn, it means the models were saved using a different version than the one currently installed. While predictions may still work, for best practice, you should use the same version of scikit-learn that was used for training.

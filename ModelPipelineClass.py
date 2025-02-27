import pandas as pd 
import numpy as np
import joblib

class ModelPipeline:
    def __init__(self, model, tracker):
        """
        Initialize the ModelPipeline with a model and tracker.

        Parameters:
        - model: The pre-trained machine learning model for making predictions.
        - tracker: Dictionary used for encoding categorical variables.
        
        """
        self.model = model
        
        self.tracker = tracker

    def predict_anxiety_level(self,input_data):
        # Convert the input data to a NumPy array
        input_data_as_numpy_array = np.asarray(input_data)
        print(input_data_as_numpy_array)

        # Reshape the array to ensure it has one row and multiple columns (required for model input)
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
        print(input_data_reshaped)
        
        # Create a DataFrame from the reshaped array with specified column names
        df_input_data = pd.DataFrame(input_data_reshaped, columns=['GAD1', 'GAD2', 'GAD3', 'GAD4',
        'GAD5', 'GAD6', 'GAD7', 'GADE', 'SWL1',
        'SWL2', 'SWL3', 'SWL4', 'SWL5', 'SPIN1', 'SPIN2', 'SPIN3', 'SPIN4',
        'SPIN5', 'SPIN6', 'SPIN7', 'SPIN8', 'SPIN9', 'SPIN10', 'SPIN11',
        'SPIN12', 'SPIN13', 'SPIN14', 'SPIN15', 'SPIN16', 'SPIN17',
        'Narcissism', 'Gender', 'Age', 'Work', 'Degree'])
        print(df_input_data)
        
        # List of columns that require encoding
        columns_need_encoding = ['GADE','Gender', 'Work', 'Degree']

        # Encode categorical columns using the provided tracker
        for column in columns_need_encoding:
            if column in self.tracker:
                df_input_data[column] = df_input_data[column].apply(
                    lambda x: self.tracker[column].get(x, x)  # Map values using tracker or keep unchanged
                )
        
        print(df_input_data)

        # Make prediction using the pre-trained classifier
        prediction = self.model.predict(df_input_data)
        print(f"Predicted anxiety level: {prediction[0]}")
        
        # Reverse mapping for decoding the predicted numeric value to its original category
        anxiety_level = {v: k for k, v in self.tracker['Anxiety_Level'].items()}

        # Get the result by decoding the prediction
        result = anxiety_level[prediction[0]]

        return result

    def save(self, filename):
        """
        Save the ModelPipeline instance to a file.

        Parameters:
        - filename: The name of the file where the pipeline will be saved.
        """
        with open(filename, 'wb') as file:
            joblib.dump(self, file)

    def load(filename):
        """
        Load a ModelPipeline instance from a file.

        Parameters:
        - filename: The name of the file from which the pipeline will be loaded.

        Returns:
        - An instance of the ModelPipeline class.
        """
        with open(filename, 'rb') as file:
            return joblib.load(file)

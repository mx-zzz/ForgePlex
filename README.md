# ForgePlex - Neural Network Development Application (Beta Version)


**ForgePlex** is a lightweight application for training, evaluating, testing, and deploying predictive neural networks. Designed with simplicity in mind, it provides an intuitive interface for both beginners and developers working on the early stages of neural network development.

## Note (Important)

**This is a beta version, so there may be bugs, and the testing features are only partially implemented.**

---

## README: Neural Network Management Application

### Overview

This application is designed to simplify the development and evaluation of neural networks tailored for time-series data. It provides a graphical user interface for creating, training, testing, and visualizing models, while automating complex data preprocessing tasks such as binning time-series data and generating categorical change outputs. The program supports flexible data input formats, making it ideal for domains such as financial analysis, signal processing, and other sequential data applications.

---

### Purpose

The primary purpose of this application is to process and analyze time-series data by:

1. **Binning Time-Series Data:** Segmenting input data into manageable windows for feature extraction.
2. **Generating Categorical Change Outputs:** Transforming numerical changes into predefined categorical labels (e.g., "Increase", "Decrease").
3. **Flexible Data Input Formats:**
   - **Single-Level Directory:** A folder containing multiple CSV files, each representing a time-series dataset.
   - **Hierarchical Directory:** A folder with subfolders, each containing multiple CSV files. This ensures that data is equally extracted from each subfolder, allowing balanced representation across categories or sources.

---

### Key Features

#### Data Preparation
- Automates preprocessing of time-series data, including sliding window segmentation, feature extraction, and balanced data extraction.
- Computes percentage changes and bins them into categorical outputs for classification.

#### Neural Network Management
- Create, load, and save models.
- Design custom architectures with convolutional and dense layers, activation functions, and regularization options.

#### Training
- Train models using k-fold cross-validation.
- Log metrics such as accuracy and loss for each epoch.
- Save trained models for future use.

#### Testing and Evaluation
- Evaluate trained models using test datasets.
- Generate detailed evaluation metrics, including confusion matrices, classification reports, and ROC curves.

#### Graphical Interface
- User-friendly interface for managing workflows without coding.
- Interactive tools to design networks, configure training, and visualize performance.

---

### Installation

#### Prerequisites
- Python 3.8 or higher.
- Required libraries: `tensorflow`, `keras`, `numpy`, `pandas`, `PyQt6`/`PySide6`, `scikit-learn`, `matplotlib`, `seaborn`.

#### Installation Steps
1. Install the required Python libraries listed in the `requirements.txt` file.
2. Run the main Python file (`main.py`) to launch the application.

---

### How It Works

#### Data Input Formats
1. **Single-Level Directory:** Place time-series CSV files in a single folder.
2. **Hierarchical Directory:** Place CSV files within subfolders under a parent directory. The program ensures equal data extraction from each subfolder to maintain balance in the dataset.

#### Data Preprocessing
- Segments input data into sliding windows of specified length.
- Calculates percentage changes and bins these values into categorical outputs for predictive modeling.

#### Model Training
- Data is split into training and testing sets or processed directly from separate directories.
- Neural networks are trained to predict categorical outputs using the prepared features.

#### Model Evaluation
- Testing datasets are used to evaluate the trained model.
- Generates metrics such as accuracy, precision, recall, confusion matrices, and ROC curves.

---

### Modules

#### Core Modules
- **Menu.py:** Main entry point to load and navigate between views.
- **Data_Handler.py:** Handles data preprocessing, including binning, sliding window extraction, and category labeling.

#### Model Operations
- **Neural_Network_Menu.py:** Manages model creation and architecture configuration.
- **Training_Menu.py:** Configures and executes training workflows.
- **Testing_Menu.py:** Conducts testing and generates evaluation metrics.

#### Graphical User Interface
- **Menu_View.py:** Main menu interface for navigation.
- **Neural_Network_View.py:** Interface for defining network architectures.
- **Training_View.py:** Interface for managing training workflows.
- **Testing_View.py:** Interface for visualizing evaluation metrics.

---

### Folder Structure


├── Saved Models/            # Stores trained neural network models
├── Icons/                   # Icons for the graphical interface
├── Utility/                 # Helper scripts for logging and model information
├── Views/                   # UI components for different tasks
├── main.py                  # Application entry point
├── requirements.txt         # List of dependencies


### Usage

#### Main Menu
- Select options to create, train, or test models.

#### Data Preparation
- Ensure input time-series data is in one of the supported formats:
  - A folder with CSV files.
  - A folder with subfolders containing CSV files.

#### Neural Network Creation
- Define network architecture by setting layer types and parameters.

#### Training
- Configure settings like epochs, learning rates, and validation splits.
- Train the model on the prepared data.

#### Testing
- Load test datasets and evaluate the model's performance.
- Visualize results through confusion matrices and ROC curves.

---

### Customization

1. **Modify Binning Logic:** Update `Data_Handler.py` to customize the sliding window size or output binning scheme.
2. **Enhance Model Options:** Add new layer types or architectures in `Neural_Network_Menu.py`.
3. **Extend Evaluation Metrics:** Incorporate additional metrics or visualizations in `Testing_Menu.py`.

---

### Contributing

We welcome contributions! Fork the repository, make changes, and submit a pull request.

---
### License

© Max Medina-Ducros. All rights reserved.

This project is licensed under a custom license. 

- **You are welcome to contribute** by submitting pull requests or suggestions.
- **Reproduction or redistribution** of this code, in part or whole, is prohibited without explicit written permission.
- **Commercial use of this code** or its derivatives is strictly prohibited.

For more details, please refer to the `LICENSE` file included in the repository or contact [Max.Medina-Ducros@gmail.com] for inquiries.

---

If you're open to licensing discussions or want a custom license file written for this, feel free to ask!


# **Preswald Tutorial App**

Welcome to the **Preswald Tutorial App**, a hands-on example for getting started with the **Preswald SDK**. This repository demonstrates how to build an end-to-end lightweight data workflow using the Preswald SDK.

## **✨ Key Features**

- **Data Ingestion**: Learn how to connect to common data sources like CSV files and load data into pipelines.
- **Data Transformation**: Explore Python and SQL-based transformation techniques to clean and process data.
- **Data Orchestration**: Understand how to chain ingestion, transformation, and visualization steps into a unified pipeline.
- **Data Visualization**: Build interactive dashboards to visualize data insights with minimal code.

## **🚀 Why Use This Tutorial?**

- **Quick Start**: Provides a fully functional app to run locally and explore.
- **Learn by Example**: Gain hands-on experience with Preswald’s features.
- **Extensible**: Adapt and extend the example app to suit your own data needs.
- **Open Source**: Clone, modify, and contribute to the tutorial app as needed.

---

## **📖 Table of Contents**

- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [How It Works](#-how-it-works)
- [Usage Instructions](#-usage-instructions)
- [Contributing](#-contributing)
- [License](#-license)

---

## **📥 Getting Started**

Follow these steps to set up and run the Preswald Tutorial App.

### **Prerequisites**

- Python 3.8 or later
- `pip` (Python package installer)

---

### **Installation**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/preswald-tutorial.git
   cd preswald-tutorial
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## **📂 Project Structure**

Here's an overview of the repository's directory structure:

```plaintext
preswald-tutorial/
├── ingestion/                # Scripts for data ingestion
│   ├── sample_data.csv       # Example dataset
│   └── load_csv.py           # Load data from CSV
├── transformations/          # Scripts for data transformations
│   ├── clean_data.py         # Basic data cleaning
│   └── aggregate_data.sql    # SQL transformation example
├── orchestration/            # Pipeline orchestration scripts
│   └── pipeline.py           # End-to-end pipeline script
├── visualization/            # Scripts for visualization
│   └── create_dashboard.py   # Visualization example
├── requirements.txt          # Dependencies for the project
├── README.md                 # Documentation
├── app.py                    # Main entry point
└── LICENSE                   # Apache 2.0 License
```

---

## **⚙️ How It Works**

### **Workflow Overview**

1. **Ingest Data**:

   - The app starts by loading sample data from a CSV file (`ingestion/sample_data.csv`) using Preswald's ingestion utilities.

2. **Transform Data**:

   - The ingested data is cleaned and processed using both Python (`transformations/clean_data.py`) and SQL transformations (`transformations/aggregate_data.sql`).

3. **Visualize Data**:
   - Finally, the processed data is visualized in an interactive dashboard using the `visualization/create_dashboard.py` module.

---

## **🖥️ Usage Instructions**

### **Running the App**

1. **Start the App**:

   ```bash
   python app.py
   ```

2. **Expected Output**:
   - The app will:
     1. Load the data from `ingestion/sample_data.csv`.
     2. Clean the data to remove null values.
     3. Create and display a bar chart visualization of the processed data.

---

### **Customizing the App**

This app is designed to be **modular and extensible**. Here's how you can customize different components:

#### **1. Data Ingestion**

To use a different data source:

- Modify or replace `ingestion/load_csv.py` to connect to your preferred source (e.g., an API or database).

#### **2. Data Transformation**

To apply additional transformations:

- Create new transformation scripts in the `transformations` folder.
- Add the new scripts to the pipeline in `orchestration/pipeline.py`.

#### **3. Data Visualization**

To add new visualizations:

- Modify or extend `visualization/create_dashboard.py` to include additional charts or visual components.

---

## **🔬 Example Workflow**

### **Input Data**

Sample data is provided in `ingestion/sample_data.csv`:

```csv
Category,Value
A,10
B,20
C,30
```

### **Pipeline Output**

1. **Console Output**:

   ```plaintext
   Starting pipeline...
   Data loaded successfully:
     Category  Value
   0        A     10
   1        B     20
   2        C     30
   Cleaned data:
     Category  Value
   0        A     10
   1        B     20
   2        C     30
   Pipeline completed successfully!
   ```

2. **Visualization**:
   A bar chart displaying the `Category` and `Value` columns is generated using Plotly.

---

## **🤝 Contributing**

We welcome contributions to make this tutorial app even better! Here’s how you can contribute:

1. **Fork the Repository**:
   Click the **Fork** button on the top-right corner of this repository.

2. **Clone Your Fork**:

   ```bash
   git clone https://github.com/your-username/preswald-tutorial.git
   cd preswald-tutorial
   ```

3. **Create a Branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**.

5. **Commit Your Changes**:

   ```bash
   git commit -m "Add your feature description"
   ```

6. **Push to Your Branch**:

   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**:
   Go to the repository on GitHub and click **New Pull Request**.

---

## **📝 License**

This project is licensed under the [Apache 2.0 License](LICENSE).

---

## **📣 Acknowledgments**

- **Preswald SDK**: The powerful framework enabling this tutorial app.
- The open-source community for inspiration and support.

Thank you for exploring the Preswald Tutorial App! If you have any questions or feedback, please open an issue or start a discussion on GitHub.

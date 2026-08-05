# HealthMate - Daily Health Dashboard

HealthMate is a professional, data-driven health dashboard built with Streamlit, Pandas, and Matplotlib. It enables users to evaluate key health parameters, compute metabolic metrics, analyze lifestyle habits, and review actionable recommendations through clean data visualizations.

🚀 **Live Application:** [https://healthmate-uza.streamlit.app/](https://healthmate-uza.streamlit.app/)  
📁 **GitHub Repository:** [https://github.com/ukashazarar/HealthMate](https://github.com/ukashazarar/HealthMate)

---

## Key Features

- **Physiological Calculations**: Computes Body Mass Index (BMI), Basal Metabolic Rate (BMR using Mifflin-St Jeor equation), and Total Daily Energy Expenditure (TDEE).
- **Ideal Weight Range Analysis**: Evaluates healthy body weight thresholds based on height medical reference standards.
- **Lifestyle Metric Tracking**: Tracks hydration status, sleep duration quality, exercise volume, and daily step count.
- **Health Index Assessment**: Aggregates key health parameters into a normalized cumulative health score (0–100).
- **Data Visualizations**: Includes Matplotlib charts illustrating BMI threshold positions and normalized lifestyle metrics.
- **Structured Metrics Summary**: Generates a clean tabular summary dataframe of all evaluated input and calculated metrics.

---

## Tech Stack

- **Framework**: [Streamlit](https://streamlit.io/)
- **Data Processing**: [Pandas](https://pandas.pydata.org/)
- **Data Visualization**: [Matplotlib](https://matplotlib.org/)
- **Language**: Python 3.9+

---

## Local Setup & Installation

Follow these steps to set up and run the application locally on your machine:

### 
```bash
1. git clone [https://github.com/ukashazarar/HealthMate.git](https://github.com/ukashazarar/HealthMate.git)
cd HealthMate

2. Create & Activate a Virtual Environment

On macOS/Linux:
python3 -m venv venv
source venv/bin/activate


On Windows:
python -m venv venv
venv\Scripts\activate


3. Install Required Dependencies
pip install -r requirements.txt


4. Run the Streamlit Application
streamlit run app.py


The application will launch automatically in your web browser at http://localhost:8501.

Repository Structure
Plaintext
├── app.py              # Main Streamlit application logic
├── requirements.txt    # Required Python dependencies with compatible versions
├── .gitignore          # Files ignored by Git (venv, pycache)
└── README.md           # Project documentation
Disclaimer
This dashboard provides analytical estimates based on standardized mathematical formulas (BMI, Harris-Benedict/Mifflin-St Jeor BMR). It is designed for educational and informational purposes only and does not substitute professional medical advice, diagnosis, or treatment.

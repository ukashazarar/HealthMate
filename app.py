import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="HealthMate - Health Dashboard",
    layout="wide"
)

# ---------------------------------------
# Header
# ---------------------------------------
st.title("HealthMate - Daily Health Dashboard")
st.write(
    "Monitor key health indicators, analyze daily activity, and receive data-driven lifestyle insights."
)

st.markdown("---")

# ---------------------------------------
# Sidebar Inputs
# ---------------------------------------
st.sidebar.title("Personal Information")

name = st.sidebar.text_input("Name", "User")

age = st.sidebar.number_input("Age", min_value=1, max_value=100, value=22)

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

height_cm = st.sidebar.number_input(
    "Height (cm)", min_value=50.0, max_value=250.0, value=170.0
)

weight_kg = st.sidebar.number_input(
    "Weight (kg)", min_value=10.0, max_value=250.0, value=65.0
)

st.sidebar.markdown("---")

st.sidebar.title("Daily Lifestyle Metrics")

water_intake = st.sidebar.slider(
    "Water Intake (Liters)", 0.0, 6.0, 2.0, 0.1
)

sleep_hours = st.sidebar.slider("Sleep Duration (Hours)", 0.0, 12.0, 7.0, 0.5)

exercise_min = st.sidebar.slider("Exercise (Minutes)", 0, 180, 30, 5)

daily_steps = st.sidebar.number_input(
    "Daily Steps", min_value=0, max_value=50000, value=5000, step=500
)

activity_level = st.sidebar.selectbox(
    "Activity Level",
    [
        "Sedentary (little or no exercise)",
        "Light (1-3 days/week)",
        "Moderate (3-5 days/week)",
        "Active (6-7 days/week)",
        "Very Active (athlete)",
    ],
)

st.sidebar.markdown("---")

calculate = st.sidebar.button("Generate Health Report")


# ---------------------------------------
# Health Calculation Functions
# ---------------------------------------

def calculate_bmi(weight, height):
    """Calculate Body Mass Index"""
    height_m = height / 100
    bmi = weight / (height_m**2)
    return round(bmi, 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return round(bmr)


def calorie_requirement(bmr, activity):
    activity_factor = {
        "Sedentary (little or no exercise)": 1.2,
        "Light (1-3 days/week)": 1.375,
        "Moderate (3-5 days/week)": 1.55,
        "Active (6-7 days/week)": 1.725,
        "Very Active (athlete)": 1.9,
    }
    calories = bmr * activity_factor[activity]
    return round(calories)


def ideal_weight(height):
    height_m = height / 100
    minimum = 18.5 * (height_m**2)
    maximum = 24.9 * (height_m**2)
    return round(minimum, 1), round(maximum, 1)


def hydration_status(water):
    if water < 1.5:
        return "Low Intake", 0.30
    elif water < 2.5:
        return "Adequate Intake", 0.70
    else:
        return "Optimal Intake", 1.0


def sleep_status(hours):
    if hours < 6:
        return "Suboptimal Duration", 0.40
    elif hours <= 9:
        return "Optimal Duration", 1.0
    else:
        return "Excessive Duration", 0.75


def activity_status(steps):
    if steps < 5000:
        return "Sedentary Level", 0.30
    elif steps < 8000:
        return "Low Activity", 0.60
    elif steps < 12000:
        return "Active Level", 0.85
    else:
        return "Highly Active", 1.0


def health_score(bmi, water, sleep, steps, exercise):
    score = 0

    # BMI Scoring
    if 18.5 <= bmi < 25:
        score += 25
    elif bmi < 18.5 or (25 <= bmi < 30):
        score += 15
    else:
        score += 8

    # Water Scoring
    if water >= 2:
        score += 20
    elif water >= 1.5:
        score += 15
    else:
        score += 8

    # Sleep Scoring
    if 7 <= sleep <= 9:
        score += 20
    elif 6 <= sleep < 7:
        score += 15
    else:
        score += 8

    # Steps Scoring
    if steps >= 10000:
        score += 20
    elif steps >= 7000:
        score += 15
    else:
        score += 8

    # Exercise Scoring
    if exercise >= 30:
        score += 15
    elif exercise >= 15:
        score += 10
    else:
        score += 5

    return score


def overall_status(score):
    if score >= 90:
        return "Optimal Health Score"
    elif score >= 75:
        return "Good Health Score"
    elif score >= 60:
        return "Moderate Health Score"
    else:
        return "Requires Improvement"


def recommendations(category, water, sleep, steps, exercise):
    tips = []
    if category == "Underweight":
        tips.append("Caloric Intake: Increase daily calorie intake using nutrient-dense foods.")
    elif category == "Overweight":
        tips.append("Caloric Management: Maintain a caloric deficit paired with regular exercise.")
    elif category == "Obese":
        tips.append("Clinical Consultation: Consult a clinical specialist for a custom intervention plan.")
    else:
        tips.append("Weight Maintenance: Current BMI is within normal bounds. Maintain routine.")

    if water < 2:
        tips.append("Hydration: Increase daily fluid intake to a minimum of 2.0 - 2.5 liters.")
    if sleep < 7:
        tips.append("Sleep Cycle: Target 7 - 9 hours of uninterrupted sleep for adequate recovery.")
    if steps < 8000:
        tips.append("Physical Activity: Increase daily walking volume to at least 8,000 steps.")
    if exercise < 30:
        tips.append("Cardiovascular Training: Aim for at least 30 minutes of moderate activity daily.")

    return tips


# ---------------------------------------
# Main Dashboard Logic
# ---------------------------------------

if calculate:
    bmi = calculate_bmi(weight_kg, height_cm)
    bmi_text = bmi_category(bmi)
    bmr = calculate_bmr(weight_kg, height_cm, age, gender)
    calories = calorie_requirement(bmr, activity_level)

    health = health_score(
        bmi, water_intake, sleep_hours, daily_steps, exercise_min
    )
    status = overall_status(health)

    water_text, water_progress = hydration_status(water_intake)
    sleep_text, sleep_progress = sleep_status(sleep_hours)
    activity_text, activity_progress = activity_status(daily_steps)
    ideal_min, ideal_max = ideal_weight(height_cm)

    # Report Heading
    st.info(f"User: **{name}** | Report Generated")
    st.subheader("Personalized Health Analysis")
    st.markdown("---")

    # KPI Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Body Mass Index (BMI)", bmi, bmi_text)
    with c2:
        st.metric("Basal Metabolic Rate (BMR)", f"{bmr} kcal")
    with c3:
        st.metric("Est. Caloric Requirement", f"{calories} kcal")
    with c4:
        st.metric("Overall Health Index", f"{health}/100")

    st.markdown("---")

    # Overall Health Status
    st.subheader("Health Index Assessment")
    st.write(f"**Classification:** {status}")
    st.progress(health / 100)

    st.markdown("---")

    # Specific Health Indicators
    left, middle, right = st.columns(3)
    with left:
        st.markdown("#### Hydration")
        st.write(water_text)
        st.progress(water_progress)
        st.caption(f"Current Intake: {water_intake} Liters")

    with middle:
        st.markdown("#### Sleep")
        st.write(sleep_text)
        st.progress(sleep_progress)
        st.caption(f"Sleep Duration: {sleep_hours} Hours")

    with right:
        st.markdown("#### Daily Movement")
        st.write(activity_text)
        st.progress(activity_progress)
        st.caption(f"Total Steps: {daily_steps}")

    st.markdown("---")

    # Weight Analysis
    st.subheader("Weight Category Analysis")
    colA, colB = st.columns(2)

    with colA:
        st.info(f"Reference Ideal Weight Range\n\n**{ideal_min} kg - {ideal_max} kg**")

    with colB:
        difference = round(weight_kg - ideal_max, 1)
        if weight_kg < ideal_min:
            st.warning("Current body weight is below the standard medical reference range.")
        elif weight_kg > ideal_max:
            st.warning(
                f"Current body weight is approximately **{difference} kg** above the ideal range."
            )
        else:
            st.success("Current weight is within normal physiological range.")

    st.markdown("---")

    # Visual Analytics
    st.subheader("Data Visualizations")
    chart1, chart2 = st.columns(2)

    with chart1:
        fig1, ax = plt.subplots(figsize=(6, 4))
        bmi_labels = ["Underweight", "Normal", "Overweight", "Obese"]
        bmi_values = [18.5, 25, 30, 35]
        colors = ["#2C3E50", "#16A085", "#D35400", "#C0392B"]

        ax.bar(bmi_labels, bmi_values, color=colors, width=0.5)
        ax.axhline(
            bmi,
            color="#2980B9",
            linestyle="--",
            linewidth=2,
            label=f"User BMI = {bmi}",
        )
        ax.set_ylabel("BMI Value")
        ax.set_title("BMI Reference Thresholds")
        ax.legend(loc="upper left")
        ax.grid(axis="y", linestyle=":", alpha=0.6)
        st.pyplot(fig1, clear_figure=True)

    with chart2:
        fig2, ax = plt.subplots(figsize=(6, 4))
        labels = ["Water (L)", "Sleep (h)", "Exercise (x10m)", "Steps (x1k)"]
        values = [
            water_intake,
            sleep_hours,
            exercise_min / 10,
            daily_steps / 1000,
        ]
        colors = ["#2980B9", "#8E44AD", "#27AE60", "#F39C12"]

        bars = ax.bar(labels, values, color=colors, width=0.5)
        ax.bar_label(bars, fmt="%.1f", padding=3)
        ax.set_title("Normalized Lifestyle Metrics")
        ax.grid(axis="y", linestyle=":", alpha=0.6)
        st.pyplot(fig2, clear_figure=True)

    st.markdown("---")

    # Recommendations
    st.subheader("Targeted Action Plan")
    tips = recommendations(
        bmi_text, water_intake, sleep_hours, daily_steps, exercise_min
    )
    for tip in tips:
        st.write(f"- {tip}")

    st.markdown("---")

    # Summary Table
    st.subheader("Parameter Metrics Summary")
    summary = pd.DataFrame(
        {
            "Parameter": [
                "User Name",
                "Age",
                "Gender",
                "Height (cm)",
                "Weight (kg)",
                "Body Mass Index (BMI)",
                "BMI Classification",
                "Reference Weight Range",
                "Basal Metabolic Rate",
                "Est. Caloric Requirement",
                "Water Intake",
                "Sleep Duration",
                "Exercise Duration",
                "Daily Step Count",
                "Health Score Index",
            ],
            "Value": [
                name,
                f"{age} years",
                gender,
                f"{height_cm} cm",
                f"{weight_kg} kg",
                bmi,
                bmi_text,
                f"{ideal_min} - {ideal_max} kg",
                f"{bmr} kcal",
                f"{calories} kcal",
                f"{water_intake} L",
                f"{sleep_hours} hrs",
                f"{exercise_min} mins",
                f"{daily_steps} steps",
                f"{health} / 100",
            ],
        }
    )

    st.dataframe(summary, use_container_width=True, hide_index=True)

    st.markdown("---")
    st.caption(
        "HealthMate Operational Intelligence Dashboard | Analytical Reference Only | "
        "Values presented are clinical estimates and do not replace formal diagnosis."
    )

else:
    # Initial Welcome Screen
    st.info(
        "Complete the personal parameters in the left sidebar and click **'Generate Health Report'** to view analytical metrics."
    )

    # Unsplash image retained with fixed Streamlit parameter
    try:
        st.image(
            "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b",
            use_container_width=True,
        )
    except Exception:
        pass

    st.markdown("---")
    st.subheader("Core System Features")

    feature1, feature2, feature3 = st.columns(3)
    with feature1:
        st.markdown("### Physiological Metrics")
        st.markdown("- Body Mass Index (BMI)\n- Basal Metabolic Rate (BMR)\n- Total Energy Expenditure\n- Ideal Weight Calculation")
    with feature2:
        st.markdown("### Interactive Visual Analytics")
        st.markdown("- Normalized Metrics Bar Charts\n- Cumulative Health Scoring Index\n- Threshold Target Indicators\n- Tabular Parameter Summary")
    with feature3:
        st.markdown("### Actionable Recommendations")
        st.markdown("- Targeted Caloric Guidance\n- Activity Volume Thresholds\n- Hydration Monitoring\n- Behavioral Optimization")

    st.markdown("---")
    st.caption("Engineered with Streamlit, Pandas, and Matplotlib.")
# IDAI104-2505204-Phreya_Shethwala
Rocket Launch Path Visualization is an interactive Streamlit web app that analyzes real rocket mission data and simulates rocket motion using physics-based equations. It helps users understand how thrust, payload, fuel, and drag affect launch performance through visual graphs and dynamic controls.

# Project Overview 

The Rocket Launch Path Visualization project is an interactive Streamlit web application that analyzes real-world rocket mission data and combines it with a physics-based rocket launch simulation.

The purpose of this project is to apply mathematical concepts such as Newton’s Laws, acceleration formulas, and force balance equations to real aerospace scenarios. At the same time, the project demonstrates data cleaning, visualization, and interactive dashboard development.

This application allows users to:

Explore real mission data

Understand relationships between payload, fuel, cost, and mission success

Simulate rocket launches using adjustable parameters

Compare simulation behavior with real-world trends

This project connects mathematics, physics, programming, and data science in one complete system.


# STAGE 1 – Problem Understanding & Research

Before starting coding, I studied how rockets work in real life.

Rocket motion follows Newton’s Second Law of Motion:

Force = Mass × Acceleration

This means acceleration depends on the net force acting on the rocket and its mass.

The formula used in simulation is:

Acceleration = (Thrust − Gravity − Drag) / Mass

Three main forces act on a rocket:

1️⃣ Thrust

The upward force produced by rocket engines.
This force must be greater than gravity for the rocket to lift off.

2️⃣ Gravity

The downward force pulling the rocket toward Earth (9.81 m/s²).

3️⃣ Drag

Air resistance that opposes upward motion.
Drag is highest near the ground and reduces as altitude increases because air becomes thinner.

Another important factor is fuel consumption.

As the rocket burns fuel:

Its total mass decreases

Acceleration increases

Speed increases

This explains why rockets move faster after launch.

# Research Questions Answered

1) How does adding more payload affect altitude?
When payload increases, rocket mass increases. More thrust and more fuel are required to reach high altitude.

2) How does increasing thrust affect launch success?
Higher thrust increases acceleration. This helps the rocket overcome gravity faster and improves the chances of successful launch.

3) Does lower drag at higher altitude improve speed?
Yes. Because air density decreases at high altitude, drag becomes smaller and the rocket moves more efficiently.

4) Can simulation results be compared to real mission data?
Yes. For example, if simulation shows that heavier payload requires more fuel, the dataset also shows a positive relationship between payload weight and fuel consumption.

# Real-World Importance

Understanding rocket dynamics helps:

Aerospace engineers design efficient rockets

Plan fuel requirements accurately

Reduce mission cost

Increase mission success rate

This stage connects mathematics with real-world aerospace applications.

# STAGE 2 – Data Preprocessing & Cleaning

The dataset contains real mission information such as:

Mission ID

Mission Name

Launch Date

Payload Weight

Fuel Consumption

Mission Cost

Distance from Earth

Mission Duration

Crew Size

Mission Success

🔹 Data Cleaning Steps Performed

Loaded dataset using pandas.

Explored dataset using head(), info(), and describe().

Converted Launch Date into proper datetime format.

Converted numeric columns (payload, fuel, cost, duration, distance, crew size).

Removed duplicate rows.

Handled missing values using dropna() or replacement methods.

Reset index and verified data consistency.

🔹 Why This Stage Is Important

If the data is not cleaned properly:

Graphs may show incorrect patterns

Calculations may produce errors

Simulation comparisons become unreliable

Clean data ensures accuracy, reliability, and meaningful insights.

# STAGE 3 – Rocket Launch Simulation

A simplified physics-based rocket simulation was created.

The simulation works step-by-step:

Calculate acceleration using force formula

Update velocity

Update altitude

Reduce fuel mass

Repeat for multiple time steps

🔹 User Controls (Interactive Sliders)

The app allows users to adjust:

Payload Weight

Thrust

Initial Fuel

Drag Factor

This makes the simulation interactive and allows experimentation.

🔹 Simulation Visualizations
📈 Altitude vs Time

Shows how rocket height increases during launch.

📈 Velocity vs Time

Shows how rocket speed changes as fuel burns.

🔹 Purpose of Simulation

Demonstrates practical application of mathematics

Shows how physical variables affect rocket performance

Allows comparison with real mission data

# STAGE 4 – Data Visualization & Analysis

Five compulsory graphs were created to analyze mission data.

1️⃣ Scatter Plot

Payload Weight vs Fuel Consumption

Purpose: To analyze relationship between two continuous variables.
Why Used: Scatter plots clearly show correlation patterns.
Insight: Heavier payload generally requires more fuel.

2️⃣ Bar Chart

Mission Cost: Success vs Failure

Purpose: Compare average cost between categories.
Why Used: Bar charts are best for comparing groups.
Insight: Higher cost does not always guarantee mission success.

3️⃣ Line Chart

Mission Duration vs Distance from Earth

Purpose: Show trend between distance and duration.
Insight: Longer distance missions take more time.

4️⃣ Box Plot

Crew Size vs Mission Success

Purpose: Show distribution and detect outliers.
Insight: Crew size variation may influence mission complexity.

5️⃣ Correlation Heatmap

Purpose: Show relationships between all numeric variables.
Insight: Payload, fuel, and cost often show strong positive relationships.

# Interactivity Features

Dropdown filters for Mission Type

Launch Vehicle selection

Year filter

Distance range slider

This makes the dashboard dynamic and user-friendly.


# Benefits of This Project

Improves understanding of rocket physics

Enhances data analysis skills

Strengthens programming knowledge

Connects theory with real-world application

Builds experience in web app deployment

# Advantages

• Combines real data and simulation in one platform

• Easy to use interface

• Interactive controls for experimentation

• Suitable for learning and demonstration

• Accessible online via Streamlit Cloud

# Limitations

• Simulation is simplified and does not include full orbital mechanics

• Does not model weather conditions

• Assumes constant thrust

• Real rocket systems are more complex

# Conclusion

This project successfully integrates mathematics, physics, and data analysis into a complete interactive web application. By combining rocket simulation with real mission data, it demonstrates how mathematical models can be used to understand complex aerospace systems. The project shows the importance of proper data cleaning, visualization, and simulation in making informed decisions. It highlights how AI and mathematical modeling can be applied to real-world engineering problems. Overall, this project demonstrates strong problem understanding, proper data handling, effective visualization, and successful deployment, meeting all the objectives of the Mathematics for AI course.

Streamlit App: https://idai104-2505204-phreyashethwala-ncuwbutseqxpsawuy7ykjd.streamlit.app/

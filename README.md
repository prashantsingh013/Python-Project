Poshan Tracker Data Analysis & Visualization Project
👶 Project Overview
This project presents a comprehensive analysis and interactive data visualizations based on the Poshan Tracker dataset – a vital tool under the Indian Government's Integrated Child Development Services (ICDS) scheme. It monitors health, nutrition, and service delivery for children, pregnant/lactating women, and adolescent girls through Anganwadi Centers (AWCs).

The goal is to extract insights, identify disparities, and communicate them effectively using engaging and clean Python visualizations.

🔧 Technologies Used
Python

Pandas – for data manipulation

NumPy – for numerical operations

Matplotlib & Seaborn – for data visualization

🎯 Key Objectives
Infrastructure Analysis

Examined the availability of drinking water, functional toilets, and own building status in AWCs across states.

Used bar plots and subplots to highlight gaps.

Beneficiary Participation

Analyzed participation of pregnant women, lactating mothers, adolescent girls, and children across regions.

Visualized with grouped bar charts and boxplots.

Program Coverage & Efficiency

Evaluated how consistently AWCs remain operational (1 day vs. 21 days).

Compared these metrics with child participation to assess effectiveness.

Health Check-up Monitoring (HCM)

Assessed the frequency of health checkups (1–6, 7–14, 15–30 days, etc.).

Used a bar chart to show regularity and service delivery adequacy.

Aadhaar & Health ID Coverage

Investigated Aadhaar verification and digital health ID creation among beneficiaries.

Created a comparative bar chart grouped by state.

📈 Visualizations Created
✅ Bar Plots – State-wise comparisons (infra, health, participation)

✅ Histograms – Skewness and distribution of numeric variables

✅ Box Plots – Outlier and range detection for beneficiaries

✅ Scatter Plots – AWC operational days vs. child participation

✅ Line Plots – Aadhaar & Health ID coverage trends

✅ Correlation Heatmaps – Relationship between key indicators

📁 Dataset
mapped_poshan_tracker_updated.csv

Data includes:

Infrastructure indicators

Beneficiary counts

Health checkup frequencies

Aadhaar & Health ID data

AWC operational metrics

📌 Notable Insights
Wide state-wise disparities in AWC infrastructure.

High variability in frequency of health check-ups.

Some states have very high Aadhaar coverage but low Health ID penetration.

Functional infrastructure often correlates with higher beneficiary participation.

🧠 Learnings
Data preprocessing using fillna(), feature engineering, and aggregation.

Handling large categorical axes in plots (e.g., state names).

Choosing the right plot type for impact.

Converting data into actionable public health insights.


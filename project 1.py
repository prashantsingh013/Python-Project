import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import textwrap


sns.set(style="whitegrid")


# Load dataset
df = pd.read_csv(r"C:\Users\prash\Downloads\mapped_poshan_tracker_updated.csv")

# 🔍 1. Check for missing values
print("Missing values:\n", df.isnull().sum())

# 📊 2. Summary statistics
print("\nSummary statistics:\n", df.describe())

# 🧹 3. Fill missing values with mean for selected numeric columns
fill_cols = [
    "awc_infra_dws", "awc_infra_fun_toilets", "awc_infra_own_buil",
    "pregnant_women", "lact_mothers", "adolescent_girls",
    "children_0_6_months", "children_6months_3years", "children_3_6_years",
    "awc_open_1day", "awc_open_21day", "hcm_1_6days", "hcm_7_14days", 
    "hcm_15_20days", "hcm_atleast_21days", "aadhar_verf_benf", "health_id_created"
]

for col in fill_cols:
    df[col] = df[col].fillna(df[col].mean())

# 🆕 4. Create new column: Children Coverage Ratio
df["children_coverage_ratio"] = df["children_3_6_years"] / (df["children_0_6_months"] + 1)

# 📈 5. Bar Plot: Avg Infrastructure by State
# Group and sort data
infra_avg = df.groupby("state_name")[["awc_infra_dws", "awc_infra_fun_toilets", "awc_infra_own_buil"]].mean().reset_index()
infra_avg = infra_avg.sort_values("awc_infra_dws", ascending=False)

# Plot as horizontal bar chart
plt.figure(figsize=(12, 10))
sns.barplot(data=infra_avg, y="state_name", x="awc_infra_dws", hue="state_name", palette="viridis", legend=False)

plt.title("Average Drinking Water Supply by State", fontsize=16)
plt.ylabel("State", fontsize=12)
plt.xlabel("Avg AWC Drinking Water Facilities", fontsize=12)
plt.tight_layout()
plt.show()

# 📉 6. Histogram: Children (3-6 years) Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["children_3_6_years"], bins=20, color="teal", edgecolor="black")
plt.title("Distribution of Children (3-6 Years)")
plt.xlabel("Number of Children")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 📦 7. Boxplot: Beneficiary Participation
plt.figure(figsize=(8, 5))
sns.boxplot(data=df[["pregnant_women", "lact_mothers", "adolescent_girls"]])
plt.title("Boxplot of Beneficiary Counts")
plt.grid()
plt.tight_layout()
plt.show()

# 🔄 8. Scatter Plot: AWC Open Days vs Children 3-6 Years

plt.figure(figsize=(12, 6))

sns.scatterplot(
    data=df,
    x="awc_open_21day",
    y="children_3_6_years",
    hue="state_name",
    palette="Set2",
    alpha=0.7,
    edgecolor="black"
)

plt.title("AWC Open Days vs Children Participation")
plt.xlabel("AWC Open (21 Days)")
plt.ylabel("Children (3-6 Years)")

# Move legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.tight_layout()

plt.grid()
plt.show()
# 🔥 9. Correlation Heatmap
plt.figure(figsize=(12, 8))
corr_matrix = df[fill_cols + ["children_coverage_ratio"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 🚨 10. Outlier Detection: Aadhar Verified Beneficiaries
plt.figure(figsize=(8, 5))
sns.boxplot(x=df["aadhar_verf_benf"], color="coral")
plt.title("Outlier Detection in Aadhar Verified Beneficiaries")
plt.grid()
plt.tight_layout()
plt.show()

# 11 . Line Plot :
# Filter relevant columns and remove missing values
columns = ['state_name', 'aadhar_verf_benf', 'health_id_created']
df_filtered = df[columns].dropna()

# Calculate average for each state
line_avg = df_filtered.groupby('state_name')[['aadhar_verf_benf', 'health_id_created']].mean().reset_index()

# Melt the dataframe to long format for line plotting
line_melted = pd.melt(line_avg, id_vars='state_name', var_name='Metric', value_name='Average Value')

# Plot the line chart
plt.figure(figsize=(14, 6))
sns.lineplot(data=line_melted, x='state_name', y='Average Value', hue='Metric', marker='o')
plt.title("Line Plot: Aadhaar & Health ID Coverage by State")
plt.xlabel("State")
plt.ylabel("Average Percentage")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Metric")
plt.tight_layout()
plt.show()

# 12 . Plot Histogram to visualize Skewness :


# Print column names to verify
print("Available columns:", df.columns.tolist())

# Use the correct column names based on your dataset
numeric_cols = ['aadhar_verf_benf', 'health_id_created', 
                'awc_open_less_than_1_day', 'awc_open_exactly_21_days']

# Plot histograms
plt.figure(figsize=(14, 10))
for i, col in enumerate(numeric_cols, 1):
    if col in df.columns:
        plt.subplot(2, 2, i)
        sns.histplot(df[col].dropna(), kde=True, bins=30, color='skyblue')
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
    else:
        print(f"Column not found: {col}")

plt.tight_layout()
plt.show()

# Objective (1):Infrastructure Analysis by District/State

# Group and average
infra_avg = df.groupby("state_name")[["awc_infra_dws", "awc_infra_fun_toilets", "awc_infra_own_buil"]].mean().reset_index()
infra_avg_sorted = infra_avg.sort_values(by="awc_infra_dws", ascending=False)

# Set style
sns.set(style="whitegrid")

# Subplots
fig, axes = plt.subplots(3, 1, figsize=(16, 16), sharex=True)

# Drinking Water
sns.barplot(data=infra_avg_sorted, x="state_name", y="awc_infra_dws", hue="state_name",
            ax=axes[0], palette="Blues_d", legend=False)
axes[0].set_title("Average Drinking Water Facilities by State")
axes[0].set_ylabel("AWC Infra - DWS")

# Functional Toilets
sns.barplot(data=infra_avg_sorted, x="state_name", y="awc_infra_fun_toilets", hue="state_name",
            ax=axes[1], palette="Greens_d", legend=False)
axes[1].set_title("Average Functional Toilets by State")
axes[1].set_ylabel("AWC Infra - Functional Toilets")

# Own Buildings
sns.barplot(data=infra_avg_sorted, x="state_name", y="awc_infra_own_buil", hue="state_name",
            ax=axes[2], palette="Purples_d", legend=False)
axes[2].set_title("Average Own Building Facilities by State")
axes[2].set_ylabel("AWC Infra - Own Building")

# Rotate labels for readability
for ax in axes:
    ax.set_xlabel("")
    ax.tick_params(axis='x', rotation=60)

plt.tight_layout()
plt.show()

#Objective (2) :Beneficiary Participation Analysis

# Find all relevant columns using keywords
beneficiary_keywords = ["pregnant", "lactating", "adolescent", "children"]
beneficiary_cols = [col for col in df.columns if any(key in col.lower() for key in beneficiary_keywords)]

# Optional: Print matched columns to verify
print("Matched beneficiary columns:", beneficiary_cols)

# Group by state and get average
beneficiary_avg = df.groupby("state_name")[beneficiary_cols].mean().reset_index()

# Plotting
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
fig.suptitle("Beneficiary Participation Across States", fontsize=16)

# Plot only available columns (in case fewer than 6 matched)
for i, col in enumerate(beneficiary_cols[:6]):
    ax = axes[i // 3, i % 3]
    sns.barplot(
        data=beneficiary_avg.sort_values(by=col, ascending=False),
        y="state_name", x=col, ax=ax, hue="state_name", palette="viridis", legend=False
    )
    ax.set_title(col.replace("_", " ").title())
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.set_yticklabels([])  # Hide state names for clean plot

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

#Objective (3):Program Coverage and Efficiency

# Group by state and calculate mean of relevant columns
coverage_efficiency = df.groupby("state_name")[["awc_open_1day", "awc_open_21day", "children_awc_21days"]].mean().reset_index()

# Sort by awc_open_21day for better visualization
coverage_efficiency = coverage_efficiency.sort_values(by="awc_open_21day", ascending=False)

# Plot
plt.figure(figsize=(16, 6))
sns.set_style("whitegrid")

# Bar plot for AWC open 1 day
plt.bar(coverage_efficiency["state_name"], coverage_efficiency["awc_open_1day"], label="AWC Open ≥1 Day", color="skyblue")

# Bar plot for AWC open 21 days (stacked on top)
plt.bar(coverage_efficiency["state_name"], coverage_efficiency["awc_open_21day"], label="AWC Open ≥21 Days", color="navy")

# Line plot for child participation
plt.plot(coverage_efficiency["state_name"], coverage_efficiency["children_awc_21days"], color="red", marker='o', label="Children in AWC (21 days)")

plt.title("Program Coverage & Efficiency Across States")
plt.xlabel("State")
plt.ylabel("Count (Average)")
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()

#Objective (4) :Health Check-up Monitoring (HCM) Frequency


# Define HCM-related columns based on available names
hcm_columns = [
    "hcm_1_6days",
    "hcm_7_14days",
    "hcm_15_30_days",
    "hcm_30_plus_days",
    "hcm_not_done"
]

# Filter only if those columns exist in your dataset
existing_hcm_columns = [col for col in hcm_columns if col in df.columns]

# Group by state and get average values
hcm_avg = df.groupby("state_name")[existing_hcm_columns].mean().reset_index()

# Melt into long format
hcm_melted = hcm_avg.melt(id_vars="state_name", var_name="HCM_Frequency", value_name="Average_Count")

# Plot
plt.figure(figsize=(14, 6))
sns.barplot(data=hcm_melted, x="HCM_Frequency", y="Average_Count", hue="HCM_Frequency", dodge=True, palette="Set2")
plt.title("Average Health Check-Up Frequency Across States")
plt.xlabel("Health Check-Up Frequency Band")
plt.ylabel("Average Number of Beneficiaries")
plt.xticks(rotation=45)
##plt.legend(title="Frequency")
plt.tight_layout()
plt.show()


#Objective (5) :Aadhaar and Health ID Coverage

# Check available column names to avoid KeyError
print("Columns in the dataset:", df.columns.tolist())

# Filter for necessary columns
columns = ['state_name', 'aadhar_verf_benf', 'health_id_created']

# Drop rows where either column is missing
df_filtered = df[columns].dropna()

# Group by state and calculate average coverage
coverage_avg = df_filtered.groupby('state_name')[['aadhar_verf_benf', 'health_id_created']].mean().reset_index()

# Melt the dataframe for visualization
coverage_melted = coverage_avg.melt(id_vars='state_name', 
                                     value_vars=['aadhar_verf_benf', 'health_id_created'],
                                     var_name='Coverage_Type', 
                                     value_name='Average_Percentage')

# Plot
plt.figure(figsize=(14, 6))
sns.barplot(data=coverage_melted, x='state_name', y='Average_Percentage', hue='Coverage_Type', palette='Set2')
plt.title("Aadhaar Verification & Health ID Creation Coverage by State")
plt.xlabel("State")
plt.ylabel("Average Coverage (%)")
plt.xticks(rotation=45, ha='right')
plt.legend(title="Type of Coverage")
plt.tight_layout()
plt.show()

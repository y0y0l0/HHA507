# Healthcare Claims Data Analysis Assignment

## Real-World Context

This assignment simulates the type of analysis performed daily by healthcare data analysts, medical billing specialists, and health informaticians. Understanding claims data is essential for:
- Revenue cycle management
- Coding accuracy audits
- Payer contract analysis
- Clinical quality reporting
- Healthcare operations optimization

The skills you'll develop:
- Working with relational healthcare data
- Understanding claims data structure (HEADER, LINE, CODE files)
- Performing multi-table joins and aggregations
- Analyzing provider billing patterns
- Identifying common diagnosis-procedure combinations

## Scenario

You are a data analyst at Stony Brook University Hospital. The compliance and revenue cycle teams have provided you with a sample of prospective claims data from May 2024. They need your help analyzing billing patterns, identifying the most common diagnoses and procedures, and understanding payer mix to support operational decision-making.

## Assignment Overview

You will analyze three interconnected claims files to answer key questions about provider billing patterns, common diagnoses, procedures, and payer relationships. This assignment focuses on relational data analysis using Python and pandas.

## Dataset Description

The claims data consists of three CSV files that form a relational database structure:

### 1. HEADER File (`STONYBRK_20240531_HEADER.csv`)
Contains one row per claim with high-level information:
- **ProspectiveClaimId**: Unique claim identifier
- **Provider NPIs**: Billing, Attending, Rendering, Referring, Operating providers
- **ServiceFromDate/ServiceToDate**: Service dates
- **PrimaryPayerName/PrimaryPayerCode**: Primary insurance payer
- **PlaceOfService**: Where services were rendered
- **WorkQueName**: Audit/review queue assignment

### 2. LINE File (`STONYBRK_20240531_LINE.csv`)
Contains one row per service line (procedures/services):
- **ProspectiveClaimId**: Links to HEADER file
- **LinePos**: Line number on the claim
- **HCPCS**: CPT/HCPCS procedure code
- **Modifier1-4**: Procedure modifiers
- **DxMapDelim**: Shows which diagnosis codes justify this procedure
- **Charges**: Dollar amount billed for this line
- **Units**: Quantity of service

### 3. CODE File (`STONYBRK_20240531_CODE.csv`)
Contains diagnosis codes (ICD-10):
- **ProspectiveClaimId**: Links to HEADER file
- **CodePos**: Position/order of diagnosis on claim
- **CodeValue**: ICD-10 diagnosis code
- **CodeQualifier**: Code type (ABF, ABK, etc.)


1. Create a **public** GitHub repository named `claims-analysis`
2. Structure your repository:
   ```
   claims-analysis/
   ├── content/
   │   ├── STONYBRK_20240531_HEADER.csv
   │   ├── STONYBRK_20240531_LINE.csv
   │   ├── STONYBRK_20240531_CODE.csv
   ├── notebooks/
   │   └── claims_analysis.ipynb
   ├── .gitignore
   ├── about.md
   ├── requirements.txt
   └── README.md
   ```

2. **How to run the notebook** in your GitHub repository with:
   - Brief project description
   - Data source information
   - How to run the notebook
      - Prerequisites (Python version, libraries)
      - Instructions to install dependencies from `requirements.txt`
      ```
      pip install -r .\requirements.txt
      ```
   ***Summary of key findings and visualizations***
   - The most frequent billing providers is Dr. YuehJien Gu.
      with total of 660 claims billed by this provider, mostly with procedure code 99291 (Acute respiratory failure and hypoxia).
   - The primary payer with the highest number of claims is Medicare, accounting for 450 claims (62.4% of total claims).
   - The most common diagnosis code is J96.01 Acute respiratory failure with hypoxia, appearing in 62 claims.
   - The majority of claims (63.6%) were billed for services provided in an INPATIENT setting (PlaceOfService code 21) with 231 claims.
   - Visualizations:
      - Bar chart of top 5 billing providers by number of claims are Dr. YuehJien Gu, Reema Ochanley NP, Dr. Iesha Arfeen, Dr. Zahra Naseer MBBS, and Dr. Mashal Salehi.
      - Pie chart showing distribution of primary payers are Medicare, Healthfirst, Fidelis, HIP Medicaid and Healthfirst Capitated.
      - Pie chart of top 10 diagnosis codes by frequency are the following :
      ``` |CodeValue  |code_count  |                                     CodeName                                                   |
          |J96.01     |    62      |                                                 Acute respiratory failure with hypoxia (J96.01)|
          |E78.5      |    49      |                                                             Hyperlipidemia, unspecified (E78.5)|
          |I10        |    49      |                                                          Essential (primary) hypertension (I10)|
          |G93.5      |    34      |                                                                    Compression of brain (G93.5)|
          |D64.9      |    29      |                                                                     Anemia, unspecified (D64.9)|
          |I25.10     |    27      |        Atherosclerotic heart disease of native coronary artery without angina pectoris (I25.10)|
          |I61.9      |    26      |                                      Nontraumatic intracerebral hemorrhage, unspecified (I61.9)|
          |I48.91     |    24      |                                                        Unspecified atrial fibrillation (I48.91)|
          |I60.8      |    24      |                                              Other nontraumatic intracranial hemorrhage (I60.8)|
          |I50.9      |    22      |                                                              Heart failure, unspecified (I50.9)|
         ```
   ### How to Run the Notebook
To run the `claims_analysis.ipynb` notebook, follow these steps:
      - Git installed on your machine
      - Python 3.8 or higher installed
      - Required libraries listed on requirements.txt
      - Then click on the RunAll button to execute all cells in the notebook.(all paths are updated to relative paths)

3. **requirements.txt** with necessary Python packages:
   ```
   pandas>=1.3.0
   matplotlib>=3.4.0
   base64>=1.0.0
   seaborn>=0.11.0
   ```
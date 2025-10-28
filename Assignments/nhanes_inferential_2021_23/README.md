# Objective

In this assignment, you will use NHANES data to perform basic inferential statistics using Python in Google Colab. You will explore relationships and differences in health metrics and demographic variables, utilizing the skills learned in class to answer key questions about the dataset. Your final analysis should be saved as a Google Colab notebook and uploaded to a GitHub repository
- NHANES Data: [NHANES 2021-2023](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023)

# Data Preparation
## - NHANES Data: [NHANES 2021-2023](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2021-2023)
- **Marital Status** (`DMDMARTZ`) - created categorical DMDMARTZ_group, recoding (married or not married). - ***DEMO_L.xpt***
- **Education Level** (`DMDEDUC2`) - created categorical DMDEDUC2_group,recoding (bachelor’s or higher vs. less than bachelor’s). - ***DEMO_L.xpt***
- **Age in Years** (`RIDAGEYR`) - continuous.- ***DEMO_L.xpt***
- **Systolic Blood Pressure** (`BPXOSY3`) - continuous. - ***BPXO_L_Doc.xpt***
- **Diastolic Blood Pressure** (`BPXODI3`) - continuous. - ***BPXO_L_Doc.xpt***
- **Vitamin D Lab Interpretation** (`LBDVD2LC`) - categorical, two levels (remove values with null).- ***VID_L.xpt***
- **Hepatitis B Lab Antibodies** (`LBXHBS`) - categorical, needs recoding to two levels.- ***HEPB_S_L.xpt***
- **Weak/Failing Kidneys** (`KIQ022`) - categorical, can be treated as two levels (remove values `7`, `9`, and null). - ***KIQ_U_L.xpt***
- **Minutes of Sedentary Behavior** (`PAD680`) - continuous, needs cleaning (remove values `7777`, `9999`, and null).- ***PAQ_L.xpt***
- **Current Self-Reported Weight** (`WHD020`) - continuous, needs cleaning (remove values `7777`, `9999`, and null).- ***WHQ_L.xpt***
## Instructions

1. **Create Your GitHub Repository**
   - Create a new GitHub repository titled `nhanes_inferential_2021_23`.
   - Include a `README.md` file that briefly describes the project and the analyses you are performing for each of the questions.

2. **Complete the Analysis in Google Colab**
   - Use Google Colab to conduct your analysis. Your notebook should be well-documented with explanations of each step just as like we have done in the class notebooks.

3. **Questions for Analysis**

   Use the questions below to guide your analysis. Remember to transform or recode variables where needed as specified, and determine the appropriate statistical tests that should be performed based on the question and variables.

   - **Question 1**: "Is there an association between marital status (married or not married) and education level (bachelor’s degree or higher vs. less than a bachelor’s degree)?"  
     - Variables: `DMDMARTZ` (marital status) and `DMDEDUC2` (education level). Recode as specified.

   - **Question 2**: "Is there a difference in the mean sedentary behavior time between those who are married and those who are not married?"  
     - Variables: `DMDMARTZ` (marital status, recoded) and `PAD680` (sedentary behavior time, cleaned).

   - **Question 3**: "How do age and marital status affect systolic blood pressure?"  
     - Variables: `RIDAGEYR` (age), `DMDMARTZ` (marital status, recoded), and `BPXOSY3` (systolic blood pressure).

   - **Question 4**: "Is there a correlation between self-reported weight and minutes of sedentary behavior?"  
     - Variables: `WHD020` (self-reported weight, cleaned) and `PAD680` (sedentary behavior time, cleaned).
.
  - **Question 5 (Creative Analysis)**: Develop your own unique question using at least one of the variables listed above. Ensure that your question can be answered using one of the following tests: chi-square, t-test, ANOVA, or correlation. Clearly state your question, explain why you chose the test, and document your findings.
      - **Does vitamin D levels and high diastolic pressure affect Kidney failure?**
        - Variables: `DMDMARTZ` martial status, `BPXODIE` diastolic - 3rd oscillometric reading, `LBDVD2LC` vitamin D, and `KIQ022` kindey failure.
        - The selection of this question is related to the following articles that discuss the relationship between vitamin D levels, blood pressure, and kidney health:
         - https://pmc.ncbi.nlm.nih.gov/articles/PMC4101586/
         - https://pubmed.ncbi.nlm.nih.gov/39906471/

4. **Deliverables**

   - A completed Google Colab notebook (`.ipynb` file) with:
     - Data loading and preparation steps
     - Analysis and any transformations
     - Visualizations of descriptives/results (if relevant)
     - Brief summaries of your findings for each question
   - Submit the link to your GitHub repository titled `nhanes_inferential_2023`.

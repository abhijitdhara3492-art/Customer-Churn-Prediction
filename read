CONTENTS

TOPICS------------------------------------------------------------------------PAGE NO

ABSTRACT                                                                                                2
CHAPTER – 1: INTRODUCTION                                                          3
1.1	Customer Churn                                                      
1.2	Problem Statement                                                  
1.3	Project Aim                                                             
CHAPTER – 2: LITERATURE REVIEW                                              7
			2.1 Existing Published Work                                         
CHAPTER – 3: METHODOLOGY                                                         9
			3.1 Dataset                                                                     
			3.2 Data Preprocessing
			3.3 Exploratory Data Analysis
			3.4 Algorithm
CHAPTER – 4: RESULT                                                            	   22
CHAPTER – 5: CONCLUSION                                                    	   23
CHAPTER – 6: REFERENCE                                                          	   24








ABSTRACT
This project presents a comprehensive Telecom Customer Churn Analysis aimed at identifying the key factors that influence customer attrition in a telecommunications company. The analysis begins with importing and preparing the dataset, which includes customer demographics, service usage patterns, billing details, and churn status. Data preprocessing steps include handling missing values, converting the Total Charges field to a numeric format, and removing irrelevant identifiers such as customer ID. Data cleaning ensures consistency and reliability, enabling accurate downstream analysis.
Exploratory Data Analysis (EDA) is conducted using descriptive statistics, visualizations, and correlation analysis to uncover patterns within the dataset. Charts such as count plots, histograms, and distribution graphs help reveal the relationship between churn and variables like contract type, monthly charges, tenure, payment method, and internet service type. A heatmap is generated to demonstrate the correlation structure among numerical features, highlighting which variables have the strongest influence on churn behaviour.
Further steps include encoding categorical variables, scaling numerical features, and preparing the dataset for model development. The data is split into training and testing sets to evaluate model performance. Feature importance techniques, such as Random Forest feature rankings, are used to identify the most predictive attributes, helping the organization understand primary drivers of churn — including short tenure, high monthly charges, and electronic check payments.
Overall, this notebook demonstrates a structured approach to churn prediction through data cleaning, EDA, visualization, and machine learning preparation. The insights derived from this analysis can guide customer retention strategies by pinpointing high-risk segments and enabling data-driven decision-making. The project showcases how Python-based analytical tools support impactful business intelligence in the telecom sector.









CHAPTER 1: INTRODUCTION
Customer churn has emerged as one of the most critical challenges faced by subscription-based businesses, particularly within the telecommunications industry. As market competition intensifies and customer expectations continue to evolve, telecom companies struggle not only to acquire new subscribers but also to retain existing ones. Retention has become far more cost-effective than acquiring new customers, making churn prediction a vital strategic capability. The ability to accurately identify customers who are likely to discontinue their service allows companies to intervene early with personalized retention strategies, targeted offers, improved service quality, and customer-centric solutions. This project focuses on developing a structured approach to understand, analyse, and predict customer churn using data-driven techniques applied to the Telco Customer Churn dataset.
The dataset contains demographic information, service usage patterns, subscription details, billing behaviour, and customer account history. Before any prediction can occur, the raw data must undergo extensive processing to ensure accuracy, completeness, and readiness for analysis. The notebook begins by loading the CSV dataset and performing essential cleaning steps. Columns with missing values—particularly Total Charges—are inspected, converted to numeric formats, and imputed appropriately. Redundant columns such as customer ID are removed to prevent unnecessary noise in the analysis. The dataset also contains categorical variables and potential inconsistencies, such as blank fields representing unrecorded billing values. These issues are systematically handled using encoding techniques, filling strategies, and type conversions to prepare the data for machine learning tasks.
A key portion of the project is dedicated to exploratory data analysis (EDA), which helps uncover hidden patterns, trends, and correlations within the dataset. Various visualization techniques—such as bar charts, heatmaps, count plots, and frequency distributions—are used to understand the relationships between churn and influential features like contract type, payment method, tenure, monthly charges, and internet service options. EDA also provides a deeper understanding of customer behaviour, revealing insights into which groups are more susceptible to churn. For example, customers with month-to-month contracts, higher monthly charges, and electronic payment modes often exhibit higher churn rates. These patterns help shape the modelling strategy and highlight which features should receive special attention during preprocessing.
To build predictive capabilities, the dataset is split into training and testing subsets, typically 70% for training and 30% for testing. This ensures that the model can generalize well to unseen data. Numerical features are standardized through scaling techniques, while categorical variables are transformed using encoding methods like Label Encoding. These preprocessing steps improve model performance by ensuring consistent feature representation. The cleaned and transformed dataset is then used to train machine learning models such as logistic regression, decision trees, random forests, or similar classification algorithms. Model evaluation metrics—including accuracy, confusion matrix, and classification reports—help measure the effectiveness of each model in predicting churn.
One of the significant outcomes of this analysis is the identification of key features that most strongly influence churn. Feature importance visualizations, often generated using tree-based models, highlight the relative contribution of variables such as monthly charges, contract terms, tenure length, and additional services like online security or streaming options. These insights not only support accurate predictions but also offer practical implications for business decision-making. Telecom providers can utilize these findings to design customer retention plans, optimize service packages, improve billing transparency, and enhance customer satisfaction.
Overall, this project provides a comprehensive, end-to-end analysis of customer churn using data preprocessing, exploratory analysis, and predictive modelling techniques. By combining statistical insights with machine-learning-based prediction, the project demonstrates how telecom companies can leverage data science to reduce churn, boost customer loyalty, and improve long-term profitability. The structured workflow presented in the notebook—from data loading to modelling—serves as a practical framework for real-world churn analysis and aligns with industry-standard analytical practices.

1.1Customer Churn
Customer churn, also known as customer attrition, occurs when customers stop doing business with a company or stop using a company's services. By being aware of and monitoring churn rate, companies are equipped to determine their customer retention success rates and identify strategies for improvement.  Churn is a metric that shows customers who stop doing business with a company or a particular service, also known as customer attrition. By following this metric, what most businesses could do was try to understand the reason behind churn numbers and tackle those factors, with reactive action. But what if you could know in advance that a specific customer is likely to leave your business, and have a chance to take proper actions in time to prevent it from happening. The reasons that lead customers to the cancellation decision can be numerous, coming from poor service quality, delay on customer support, prices, new competitors entering the market, and so on. Usually, there is no single reason, but a combination of events that somehow culminated in customer displeasure. If your company were not capable to identify these signals and take actions prior to the cancel button click, there is no turning back, your customer is already gone. But you still have something valuable: the data. Your customer left very good clues about where you left to be desired. It can be a valuable source for meaningful insights and to train customer churn models. Learn from the past, and have strategic information at hand to improve future experiences, it’s all about machine learning. When it comes to the telecommunications segment, there is great room for opportunities. The wealth and the amount of customer data that carriers collect can contribute a lot to shift from a reactive to a proactive position. The emergence of sophisticated artificial intelligence and data analytics techniques further help leverage this rich data to address churn in a much more effective manner. As the purpose of this experiment is to identify patterns that can yield to customers churn, I will be focusing mainly on the churn portion of the dataset for the exploratory analysis.  The customer lifespan (in months) is represented by the feature and customer churn by the churn feature, which is the target variable of this experiment. The bar chart below can provide right away a good insight on how churn is distributed across the customer lifespan. Customer churn is the percentage of customers that stopped using your company's product or service during a certain time frame. You can calculate churn rate by dividing the number of customers you lost during that time period say a quarter by the number of customers you had at the beginning of that time period. A churn model is a mathematical representation of how churn impacts your business. Churn calculations are built on existing data (the number of customers who left your service during a given time period). A predictive churn model extrapolates on this data to show future potential churn rates. Having the ability to accurate the model.

1.2Problem Statement
In the telecommunications industry, customer retention has become increasingly challenging due to intense competition, diverse service offerings, and rapidly changing customer expectations. Telecom companies invest heavily in acquiring new customers, yet many subscribers discontinue their services within a short period—a phenomenon known as customer churn. This recurring loss leads to substantial revenue decline, higher acquisition costs, and operational inefficiencies. The inability to accurately identify customers likely to churn prevents companies from implementing timely retention strategies. As a result, businesses face the critical need for data-driven systems that can analyse customer behaviour, detect churn patterns, and support proactive decision-making.
The Telco Customer Churn dataset contains several customer-related attributes, including demographics, payment details, service subscriptions, internet usage patterns, contract types, and billing information. However, the raw dataset includes various challenges such as missing values, inconsistent data formats, irrelevant identifiers, and unbalanced categorical distributions. Without proper data cleaning, preprocessing, and analytical insights, predictive models cannot perform reliably. The absence of a structured approach for processing this data restricts the organization’s ability to derive meaningful insights and identify the root causes of churn.
Furthermore, telecom companies lack clear visibility into the key factors influencing customer retention. Understanding which service features, billing methods, or account characteristics contribute most significantly to churn is essential for designing effective retention strategies. Traditional manual analysis is insufficient due to the volume and complexity of data. Therefore, a robust analytical framework is required to explore patterns, assess correlations, and extract actionable insights from the dataset.
The problem addressed in this project is the development of a comprehensive churn analysis and prediction system that processes raw customer data, performs exploratory data analysis, identifies important churn indicators, and builds machine learning models capable of predicting customer churn with high accuracy. This includes cleaning the dataset, handling missing values, encoding categorical variables, scaling numerical features, and implementing classification models. By determining which customers are at risk of leaving, telecom companies can deploy targeted interventions such as discounts, personalized offers, improved service plans, or customer engagement programs. Thus, the central problem is enabling telecom organizations to leverage their data effectively to anticipate churn, reduce customer loss, optimize business strategies, and maintain long-term customer loyalty through a systematic, data-driven churn prediction model.



1.3 Project Aim
The aim of this project is to develop a comprehensive, data-driven predictive system that accurately identifies customers at risk of churn in the telecommunications sector by leveraging the Telco Customer Churn dataset. The project seeks to transform raw customer data into meaningful insights through structured data preprocessing, exploratory data analysis (EDA), feature engineering, and machine learning–based classification techniques. By doing so, the goal is to enable telecom companies to understand the key behavioural, financial, and service-related factors that influence customer churn and to support proactive retention strategies.
This project aims to create an end-to-end analytical workflow that begins with cleaning and preparing the dataset—handling missing values, converting data types, removing irrelevant features, encoding categorical variables, and scaling numerical fields—to ensure the integrity and readiness of the dataset for model building. Another major objective is to perform deep exploratory analysis to uncover important trends, correlations, and customer patterns that explain why certain customers are more prone to leaving the service. These insights will help highlight crucial determinants such as contract duration, monthly charges, payment methods, tenure, internet service options, and add-on features.
A core aim of the project is to apply and evaluate different machine learning classification models capable of predicting churn with high accuracy and reliability. By training and testing models such as logistic regression, decision trees, and random forest classifiers, the project intends to compare performance metrics and identify the best-performing predictive model. Additionally, the project aims to quantify feature importance to provide telecom companies with actionable explanations of which factors contribute most strongly to churn behaviour. Ultimately, the project aims to equip telecom service providers with a practical, scalable, and data-driven churn prediction system that not only predicts customer churn but also empowers organizations to design targeted retention campaigns. By understanding at-risk customers early, companies can reduce revenue loss, improve customer satisfaction, and strengthen long-term customer relationships. This project aligns with modern business intelligence practices and demonstrates how predictive analytics can transform raw customer data into strategic insights for operational and financial improvement.









CHAPTER – 2: LITERATURE REVIEW
Customer churn prediction has become an essential research area in data analytics, business intelligence, and customer relationship management, especially in industries with subscription-based services such as telecommunications. Over the years, numerous studies have emphasized the importance of using data-driven approaches to understand customer behaviour and prevent churn. Literature consistently shows that retaining existing customers is significantly more cost-effective than acquiring new ones, making churn prediction models a crucial asset for organizations.
Research in the field indicates that customer churn is influenced by a combination of demographic, behavioural, financial, and service-related factors. Variables such as contract duration, monthly charges, payment method, service usage patterns, and customer tenure have been repeatedly identified as strong indicators of churn. Many studies highlight that short-term contracts, higher monthly payments, and lack of service add-ons (such as security features or tech support) increase the likelihood of churn. This aligns closely with the variables analysed in the Telco Customer Churn dataset used in the notebook.
The literature also emphasizes the need for comprehensive data preprocessing before applying prediction models. Missing data, inconsistent entries, and mixed data types can significantly affect the reliability of machine learning algorithms. Scholars commonly recommend procedures such as handling missing values, converting numeric fields, removing irrelevant identifiers, encoding categorical variables, and scaling numerical features. The steps implemented in the notebook, such as converting Total Charges to numeric values, dropping customer ID, and using encoding and scaling techniques, follow best practices widely established in prior studies.
Exploratory Data Analysis (EDA) plays a vital role in churn research, as identified in numerous academic works. Visualization techniques—including heatmaps, distribution charts, and frequency analysis—are frequently used to reveal hidden patterns and correlations among customer attributes. Several studies point out that EDA helps identify which features are most influential in predicting churn, allowing analysts to refine models and improve interpretability. The notebook follows similar approaches by examining churn distribution, analysing charges and tenure, and visualizing categorical influences. Machine learning has been a cornerstone of churn research, with models such as logistic regression, decision trees, random forests, and gradient boosting commonly applied to telecom datasets. The literature suggests that tree-based models often outperform simpler classifiers due to their ability to capture non-linear relationships and provide feature importance insights. In alignment with these findings, the notebook utilizes machine learning classification techniques and analyses feature importance to determine which variables most strongly drive churn.
Overall, existing literature reinforces the necessity of data preprocessing, exploratory analysis, and model evaluation when performing churn prediction. The workflow implemented in the notebook reflects the methodologies widely supported in academic and industry research. Together, these studies form the foundation for designing effective churn prediction systems, offering organizations the ability to understand customer behaviour, reduce churn, and enhance long-term customer loyalty.

2.1 EXISTING PUBLISHED WORK
This work discusses the application of classification algorithms such as Logistic Regression, Decision Trees, and Random Forest for predicting churn in telecom industries. It examines how demographic and service-based features influence churn outcomes and highlights the importance of proper data preprocessing. (Shilpa et. el., 2020). This study focuses on using predictive analytics to identify at-risk customers and explores various modelling techniques. It emphasizes the business significance of churn prediction and recommends implementing retention strategies based on model outputs. (S. Saleh et. el.,2023). This work reviews several data-driven methods and visual analysis tools used for churn identification. It also presents insights from exploratory data analysis (EDA), showing how customer behaviour patterns affect churn rate. (S. S. Abiodun et. el., 2024). A published analysis demonstrating that billing methods, monthly charges, and contract type have high influence on churn. It highlights that customers with month-to-month contracts churn more when compared to long-term contract subscribers. (A. Khudhur et. el., 2024). This paper focuses on cleaning datasets, handling missing values, encoding categorical variables, and scaling numerical fields. It proves that the quality of preprocessing significantly improves model performance. (M. Óskarsdóttir et. el., 2020). This work examines how machine learning helps telecom companies build decision-support systems to predict churn and develop targeted customer retention campaigns. (A. K. Ahmad et. el., 2019). This research uses tree-based models such as Random Forest and Gradient Boosting to identify which features contribute most to customer churn. Attributes like tenure, monthly charge, internet service type, and payment method are found to be critical predictors. (M. A. Shaikhsurab et. el., 2024). A study combining descriptive statistics and predictive modelling to understand customer behaviour prior to churn. It demonstrates how behaviour-based segmentation improves churn prediction outcomes. (X. Chen et. el., 2025). This publication evaluates ensemble models such as Bagging, Boosting, and Stacking. It concludes that ensemble approaches outperform single models in telecom churn prediction tasks. (M. E. H. Assad et. el., 2024). A comparative research work assessing the performance of classification models like SVM, Naive Bayes, KNN, and Random Forest. It highlights metrics such as accuracy, precision, recall, and F1-score to identify the most effective model. (A. Khudhur et. el., 2024).








CHAPTER – 3: METHODOLOGY
The methodology followed in this project is designed to systematically transform raw telecom customer data into meaningful insights and predictive models capable of identifying churn behaviour. The workflow comprises several phases, beginning with data acquisition and cleaning, followed by exploratory data analysis, preprocessing, model development, and evaluation. Each step is essential for ensuring accuracy, reliability of the final churn prediction results.
3.1 Dataset
The dataset used in this project is the Telco Customer Churn Dataset, which contains detailed information about customers subscribed to a telecom service provider. It includes demographic attributes, account information, service subscriptions, billing patterns, and a churn indicator that specifies whether a customer discontinued the service. The dataset is structured and suitable for supervised learning, particularly classification tasks aimed at predicting customer churn.
The dataset consists of multiple feature categories. Customer Demographics include variables such as gender, senior citizen status, marital status, and the number of dependents. These attributes help analyse whether personal characteristics influence customer loyalty or service discontinuation. Account Information includes customer tenure, type of contract (month-to-month, one-year, or two-year), billing method (electronic check, mailed check, bank transfer, credit card), and payment preferences. These features are often strong predictors of churn, as they capture the customer's relationship with the service provider.
Service-Related Features represent the various telecom services customers subscribe to, such as phone service, multiple lines, internet service (DSL, Fiber Optic), online security, online backup, device protection, tech support, streaming TV, and streaming movies. These attributes provide insights into how service combinations affect churn. For example, customers using only basic services or those lacking support features may be more likely to churn compared to customers with bundled services.
The dataset also includes financial attributes, such as monthly charges and total charges. Monthly charges indicate the recurring cost of the chosen services, while total charges represent overall spending throughout the subscription. These attributes help assess whether pricing or payment burden influences churn behaviour. The notebook also handles missing values in the Total Charges column by converting them to numeric format and filling gaps with the median value to maintain consistency.
The target variable, Churn, is a binary categorical field indicating whether a customer left the service (“Yes”) or remained (“No”). This variable forms the basis of the predictive modelling task and is used to train classification algorithms.
In total, the dataset contains multiple rows representing unique customers and dozens of columns representing diverse features. Before modelling, the notebook performs essential preprocessing steps such as removing unnecessary fields like customerID, handling blank or missing entries, encoding categorical variables, and scaling numerical fields. These transformations ensure that the dataset is clean, balanced, and ready for exploratory data analysis and machine-learning model training.
Overall, the dataset offers a comprehensive view of customer behaviour, billing patterns, and service usage—making it ideal for predicting churn and identifying factors that influence customer retention in the telecom sector.
Dataset Table – Column Names & Descriptions
Column Name	Description
Customer ID	Unique identification number assigned to each customer.
Gender	Customer’s gender (Male/Female)
Senior Citizen	Indicates if the customer is a senior citizen (1=Yes, 0=No)
Partner	Whether the customer has a partner (Yes/No).
Dependents	Indicates if the customer has dependents (Yes/No).
Tenure	Number of months the customer has stayed with the company.
Phone Service	Indicates if the customer has phone service (Yes/No).
Multiple Lines	Whether the customer has multiple phone lines (Yes/No/No phone service).
Internet Service	Type of internet service: DSL, Fiber optic, or No Internet service.
Online Security	Whether the customer has online security addon (Yes/No).
Online Backup	Whether the customer has online backup addon (Yes/No).
Device Protection	Whether the customer has device protection addon (Yes/No).
Tech Support	Whether the customer has tech support addon (Yes/No).
Streaming TV	Indicates if the customer uses streaming TV service (Yes/No).
Streaming Movies	Indicates if the customer uses streaming movies service (Yes/No).
Contract	Type of contract: Month-to-month, One year, Two year.
Paperless Billing	
Whether the customer has opted for paperless billing (Yes/No).

Payment Method	Payment method such as electronic check, mailed check, Bank transfer, Credit card.
Monthly Charges	Amount charged to the customer every month.
Total Charges	Total amount charged to the customer over their entire tenure.
Churn	Target variable—indicates if the customer left the service (Yes/No).

3.2 Data Preprocessing
Categorical variables in the dataset are encoded using techniques such as Label Encoder, which transforms text-based categories into numerical values that machine learning models can process. The Total Charges column is also handled carefully by converting it into a numeric type and addressing any missing or inconsistent values to ensure uniformity across the dataset. Additional cleaning steps are performed to remove unwanted values, correct data types, eliminate blanks, and maintain proper formatting. In preparation for machine learning, numerical features may be scaled using methods like Standard Scaler, which normalizes the data and helps improve model performance. Finally, the dataset can be divided into training and testing sets, allowing models to be trained effectively and evaluated for accuracy and generalization.
3.2.1 Handling Missing Values
Missing values refer to the empty, blank, or undefined entries in a dataset where information is not recorded. These appear when certain data points are unavailable, incorrectly stored, or not provided at all. Missing values can affect the accuracy of analysis because incomplete information may lead to incorrect conclusions or weak machine-learning performance. The output clearly showed that all columns contained 0 missing values, which means dataset was completely filled with no empty or undefined data points.
 
3.2.2 Removing Duplicate Values
Duplicate values are repeated rows or records in a dataset where the same information appears more than once. These duplicated entries can occur due to errors during data collection, data merging, or incorrect data entry. Duplicate rows negatively affect data quality because they can bias the analysis, distort statistical results, and make a machine-learning model learn the same information multiple times, leading to inaccurate predictions. 
Removing duplicate values is an important step it helps maintain data quality by ensuring that each patient record is unique. This step prevented the model from overfitting or misinterpreting repeated information that could skew results. 
The dataset became cleaner, more balanced, and more reliable for further analysis. By removing duplicates. Ensuring that each data entry was unique, preventing any repeated information from influencing your model's learning process.

 


3.2.3 Data Types
Data types refer to the kind of values stored in each column of the dataset. Understanding data types is an important part of data cleaning because it tells us whether a column contains numbers, text, categories, or binary values. This helps decide what preprocessing techniques to apply later—such as scaling numerical data or encoding categorical data. the dataset contains float, int, object.
 

3.2.4 Encoding Categorical Variables
The Telco Customer Churn dataset contains many categorical fields such as gender, Partner, Internet Service, Contract, Payment Method, and Churn. Since machine-learning models require numerical inputs, these text-based categories must be converted into numbers.
In the notebook, Label Encoding is used to transform each category into an integer value. Binary fields like “Yes/No” become 1 and 0, while multi-category fields such as Internet Service or Payment Method each receive distinct numeric codes. This ensures all categorical variables are machine-readable and compatible with algorithms like Random Forest.
Encoding categorical variables is therefore essential to convert textual data into numerical form, enabling effective model training and improving prediction accuracy.

 
3.2.5 Scale Numeric Features
Scaling numeric features is an important preprocessing step used to bring all numerical variables onto a similar scale. Many machine learning algorithms—such as Logistic Regression, K-Means, SVM, and Neural Networks—work better when numerical values have a consistent range, because large-scale values can dominate the learning process and lead to biased model behaviour. In this process, features such as tenure, Monthly Charges, and Total Charges are standardized using techniques like StandardScaler, which transforms each numeric value so that it has a mean of 0 and a standard deviation of 1. This ensures that all numeric features contribute equally to the model, improves convergence speed during training, and helps the algorithm better identify meaningful patterns in the data.
 
3.2.6 Split Dataset into Features and Target
When we work with a machine learning dataset, the first essential step is to separate the data into features and a target variable. Features (often stored in a variable named X) represent all the input attributes that the model will learn from—such as customer details, numerical values, or categorical information. These columns act as the independent variables. The target (stored in a variable named y) is the single column we want the model to predict, such as Churn, Price, or Outcome. By splitting the dataset this way, we clearly define what information the model should use (features) and what it should try to forecast (target). In practice, this is done by selecting the target column from the Data Frame (for example, y = df['Churn']) and assigning the remaining columns to features (X = df.drop('Churn', axis=1)). This separation is important because machine learning algorithms require a clean distinction between inputs and the output they must learn to predict. Once this split is done, the dataset can be further divided into training and testing sets, enabling the model to learn patterns from the training portion and then be evaluated objectively on unseen test data
Split was Obtained:
Features (X) This means there are 7043 records and 20 feature Columns.
Target (y) This means the target contains 7043 labels, one for each customer.
3.2.7 Split into Training and Test Sets (70% train, 30% test)
After preprocessing the dataset, it is divided into features (X) and target (y). To evaluate the model properly, the data is split into a training set (70%) and a testing set (30%) using the train_test_split function.
The training set is used to teach the model patterns related to customer churn, while the test set is used to measure how well the model performs on unseen data. This 70–30 split ensures the model learns effectively without overfitting and provides a fair evaluation of prediction accuracy.
•	Training Features (X_train): 4920 rows × 19 columns
•	Testing Features (X_test): 2123 rows × 19 columns
•	Training Labels (y_train): 4920 rows
•	Testing Labels (y_test): 2123 rows
3.3 Exploratory Data Analysis
Exploratory Data Analysis (EDA) is an approach for data analysis that employs a variety of techniques to maximize insights into a dataset; uncover the underlying structure; extract important variables; detect outliers and anomalies; develop parsimonious models; and determine optimal factor settings. The EDA types of techniques are either graphical or quantitative (nongraphical). While the graphical methods involve summarizing the data in a diagrammatic or visual way, the quantitative method, on the other hand, involves the calculation of summary statistics.
The key visualizations that informed the analysis are presented here:
Figure 1: Basic understanding that how much customer churn out or not.

 

The bar chart shows the number of customers who churned versus those who stayed.
A total of 5174 customers did not churn, while 1869 customers churned,
This indicates that most customers remain with the service, and churn represents a smaller portion of the customer base.
Figure 2: If you want to Show Percentage of Churned Customers.

 

The pie chart shows that 73.46% of customers stayed with the service, while 26.54% of customers churned. This visual highlight the proportion of customers who remained versus those who left. It clearly illustrates that a smaller segment of customers opted to discontinue the service.


Figure 3: Churn By Gender.

 
The chart shows that both male and female customers have similar churn patterns.
In both groups, the number of customers who did not churn is much higher than those who churned. This indicates that gender does not have a significant impact on whether a customer churns.
Figure 4: Count of Customers by Senior Citizen.

 

The chart shows that the majority of customers are not senior citizens, with 5901 falling into the “No” category. A smaller group of 1142 customers are identified as senior citizens. This indicates that senior citizens form a relatively small portion of the overall customer base.

Figure 5: Churn by Senior Citizen (Stacked Bar Chart).
 

The chart shows that 23.6% of non-senior citizens churned, while 76.4% stayed.
Among senior citizens, a higher 41.7% churned, with 58.3% remaining. This indicates that senior citizens have a noticeably higher churn tendency compared to non-senior customers.


Figure 6: Churn By Tenure.

 
The histogram shows that customers with very low tenure (close to 0 months) have a high churn count. As tenure increases, churn becomes less frequent, with long-term customers mostly staying. This indicates that newer customers are more likely to churn compared to long-term subscribers.
Figure 7: Churn of Customers by Contract.

 
The chart shows that most churn occurs among customers with month-to-month contracts, where both churn and non-churn counts are high. Customers with one-year and two-year contracts show significantly fewer churn cases. This indicates that longer contract durations are associated with lower churn levels.

Figure 8: Measure Different Services using Count Plot.

 
 
 
The majority of customers who do not churn tend to have services like Phone Service, Internet Service (particularly DSL), and Online Security enabled. For services like Online Backup, Tech Support, and Streaming TV, churn rates are noticeably higher when these services are not used or are unavailable.


Figure 9: Churned Customers by Payment Method.
 
The chart shows that customers using Electronic Check have the highest churn compared to other payment methods. Customers paying through Mailed Check, Bank Transfer, and Credit Card (automatic) show much lower churn levels. This suggests that electronic check users are more likely to discontinue the service than those using automated or mailed payment methods.

Figure 10: Churn Rate Distribution by Contract Type, Tenure and monthly Charge.
 
 

The visuals show that most customers do not churn, and churn is highest among month-to-month contract users. Tenure distribution indicates that customers with shorter membership durations churn more frequently. The monthly charges plot shows that churned customers tend to have higher monthly bills compared to those who stay.

Figure 11: Correlation Heatmap – Telecom Customer Churn.
 

The correlation heatmap shows how different customer attributes relate to each other and to churn. Tenure, Monthly Charges, and Contract type show the strongest correlations with churn compared to other features. Most variables have weak correlations with each other, indicating that each feature contributes independently to customer behaviours.

Figure 12: Top 10 Important Features (Random Forest).

 
The chart highlights the most influential features contributing to churn prediction using a Random Forest model. Total Charges, Monthly Charges, and tenure are shown as the top predictors, indicating their strong impact on churn behaviours. Other important factors include Contract type, Payment Method, Online Security, and Tech Support, which also play meaningful roles in determining customer churn.

3.4 Algorithm
Random Forest Algorithm:
Random forest is a supervised learning algorithm which is used for both classification as well as regression. But however, it is mainly used for classification problems. As we know that a forest is made up of trees and more trees means more robust forest. Similarly, random forest algorithm creates decision trees on data samples and then gets the prediction from each of them and finally selects the best solution by means of voting. It is an ensemble method which is better than a single decision tree because it reduces the over-fitting by averaging the result.
We can understand the working of Random Forest algorithm with the help of following steps – 
Step 1 − First, start with the selection of random samples from a given dataset. 
Step 2 − Next, this algorithm will construct a decision tree for every sample. Then it will get the prediction result from every decision tree. 
Step 3 − In this step, voting will be performed for every predicted result. 
Step 4 − At last, select the most voted prediction result as the final prediction result.
CHAPTER – 4: RESULT
The predictive model achieved an overall accuracy of 79.51%. The detailed classification report provides deeper insights into performance, especially regarding the minority class (Churn = 1):
| Metric | Not Churned (0) | Churned (1) |
 

Overall Churn Proportion
The initial analysis of the target variable (Churn) shows a clear class imbalance:

       Not Churned ('No', 0): 5174 customers (73.46%)
Churned ('Yes', 1): 1869 customers (26.54%)
 The overall churn rate is approximately 26.54%


Churn Prediction Challenge: The Recall for the Churn class is 0.48, indicating the model correctly identified only 48% of all actual churn events. While the overall accuracy is fair, improving the identification of true positives (churners) remains an area for improvement.
Key Churn Drivers: The feature importance confirmed that the contractual and financial relationship with the customer (Total Charges, Monthly Charges, tenure, Contract, Payment Method) are the most influential factors, far outweighing demographic features like gender and Senior Citizen.
Contract Migration: Incentivize the migration of customers from Month-to-month contracts to 1- or 2-year terms.
Payment Method: Investigate the issues associated with electronic check users that lead to higher attrition, potentially offering incentives for switching to automatic payment methods (Bank Transfer or Credit Card).
CHAPTER – 5: CONCLUSION
The analysis performed in this project demonstrates the importance and effectiveness of a data-driven approach to understanding and predicting customer churn in the telecommunications sector. Through the steps applied in the notebook—ranging from data loading and cleaning to exploratory analysis, preprocessing, and machine-learning model development—the project successfully transforms raw customer data into meaningful insights that can support strategic business decisions. The initial stages focused on refining the dataset by correcting inconsistent entries, handling missing values in Total Charges, removing non-predictive identifiers like customer ID, and ensuring that numerical and categorical variables were appropriately processed. This ensured a clean and structured dataset, which is essential for reliable machine-learning outcomes. The exploratory data analysis (EDA) further revealed valuable patterns, such as higher churn among customers with month-to-month contracts, higher monthly charges, and those using electronic payment methods. These behavioural and service-related patterns align with known industry trends and highlight the significance of contract type, tenure, and billing structures in customer retention. The machine-learning phase of the project showcased the predictive potential of classification algorithms when applied to properly prepared telecom data. By splitting the dataset into training and test sets, encoding categorical variables, and scaling numerical features, the model-building process followed best practices that enhance performance and generalization. The evaluation of models, alongside feature-importance analysis, provided deeper clarity on the dominant factors influencing churn—most notably monthly charges, tenure, contract type, internet service category, and additional service features. These findings equip telecom providers with actionable insights that can guide proactive retention strategies, personalized engagement, and targeted service improvements.
Overall, this project concludes that a systematic analytical workflow—combining preprocessing, EDA, and machine learning—offers a powerful solution for predicting customer churn. The results emphasize that churn is not random but strongly associated with specific customer behaviours and service attributes. With the insights generated, telecom companies can shift from reactive responses to proactive retention planning, improving customer satisfaction and reducing financial loss. This study not only validates the usefulness of predictive analytics in telecom environments but also sets a strong foundation for future enhancements such as ensemble models, deep learning techniques, and real-time churn monitoring systems.






REFERENCE
[1] S. Silpa and A. S. Chandran, “Literature Survey on Customer Churn Prediction,” International Journal of Research and Analytical Reviews (IJRAR), vol. 7, no. 1, pp. 381–387, Mar. 2020.

[2] S. Saleh and S. Saha, “Customer retention and churn prediction in the telecommunication industry: a case study on a Danish university,” SN Applied Sciences, vol. 5, p. 726, 2023.

[3] S. S. Abiodun, A. Abiodun, A. Boroojeni, M. E. H. Assad, and F. Al-Khalifa, “Customer Churn Prediction: A Systematic Review of Recent Advances,” Insights, vol. 7, no. 3, p. 105, 2024.

[4] A. Khudhur, A. Ameen, M. Alazab, and S. Zeebaree, “A Decade of Churn Prediction Techniques in the TelCo Domain: A Survey,” SN Computer Science, vol. 5, article no. 272, Apr. 2024.

[5] M. Óskarsdóttir, C. Bravo, W. Verbeke, C. Sarraute, B. Baesens, and J. Vanthienen, “A Comparative Study of Social Network Classifiers for Predicting Churn in the Telecommunication Industry,” arXiv preprint arXiv:2001.06700, 2020.
[6] A. K. Ahmad, A. Jafar, and K. Aljoumaa, “Customer churn prediction in telecom using machine learning and social network analysis in a big data platform,” arXiv preprint arXiv:1904.00690, 2019.

[7] M. A. Shaikhsurab and P. Magadum, “Enhancing Customer Churn Prediction in Telecommunications: An Adaptive Ensemble Learning Approach,” arXiv preprint arXiv:2408.16284, 2024.

[8] X. Chen et al., “A Comprehensive Analysis of Churn Prediction in Telecommunications Using Machine Learning,” arXiv preprint arXiv:2509.22654, 2025.

[9] M. E. H. Assad, S. S. Abiodun, and A. Al-Khalifa, “A Review of Factors Affecting Customer Churn Across Digital Service Industries,” Insights, vol. 7, no. 3, pp. 1–12, 2024.

[10] A. Khudhur, M. Qader, and S. Zeebaree, “Telecommunication Customer Churn Analysis Using Public Datasets: A Comprehensive Review,” SN Computer Science, vol. 5, article no. 410, 2024.

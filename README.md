# Phone Sale Price Recommender

# Background:
Phone resellers often have to manually compare price listings across various resale platforms to determine a competitive and optimal price for their phone. This process is time-consuming and prone to errors, leading to suboptimal pricing decisions that result in missed revenue and profit opportunities.
 

# Project Objectives:
Resale websites like Carousell often lead to sellers being lowballed as they may not have an accurate understanding of the true value of their phones. This results in sellers losing money as they may not have the necessary pricing and negotiating strategies to maximize their revenue and profit. Therefore, the objective of this project is to develop a predictive model that can help sellers identify the optimal price for their phones on Carousell. By analyzing various factors such as phone specifications,  the model will provide sellers with a recommended price range for phone sale listing, enabling them to sell their phone effectively and efficiently.


# Problem statement:
The business problem in this project is that many sellers on resale websites are losing money due to suboptimal pricing and negotiating strategies. So, what is the best sale price to set?

 
# Potential Audiences:
Anyone want to sell their phone on Carousell
  

# Data used:
Data used in the analysis consists of phone listing details and seller reviews scrapped from Carousell, the largest second-hand platform widely used in Singapore. Please refer to the data dictionary for more information on the columns extracted.
 

# Data Dictionary:
- Dataset name: carousell.csv
This dataset contains all the scrapped data of phone listing on Carousell.
 
Feature  	Type Dataset  	Description
Title		object		listing title
Price		int64		Listing price
Model		object		Phone model
Capacity	int64		Phone built in storage capacity
Condition	object		physical condition rating
Battery		int64		battery health of the phone
Warranty	object		manufacturing warranty validity
Reviews	int64		number of seller reviews
Time_posted	int64		listing time stamp
Color		object		phone color 
Description	object		listing description 
Username	object		seller username


- Dataset name: data382.csv
This dataset contains all the cleaned data of carousell.csv for modeling prediction.
 
Feature  		Type Dataset  	Description
Price			int64		Listing price
Os			object		Operating system of the phone
Brand			object		Phone brand
Series			object		Phone series
Model			object		Phone model
Phone 			object		Phone series & model
Capacity		int64		Phone built in storage capacity
Condition		object		physical condition rating
Battery			int64		battery health of the phone
Warranty		int64		manufacturing warranty validity
Reviews		int64		number of seller reviews
 
- Dataset name: data_to_map.csv
This dataset contains all the cleaned data of data382.csv with encoded columns as a reference to user input for model prediction.
 
Feature  		Type Dataset  	Description
Price			int64		Listing price
Os			object		Operating system of the phone
Brand			object		Phone brand
Series			object		Phone series
Model			object		Phone model
Phone 			object		Phone series & model
Capacity		int64		Phone built in storage capacity
Condition		object		physical condition rating
Battery			int64		battery health of the phone
Warranty		int64		manufacturing warranty validity
Reviews		int64		number of seller reviews
Os_num		int64		Operating system of the phone numeric data
Phone_num 		int64		Phone series & model numeric data
Condition_num	int64		physical condition rating numeric data
Warranty_num	object		manufacturing warranty validity numeric data

# Key takeaways from the project:
Recommender deployed successfully on streamlit.io(link).

The recommender is a fuss free way to determine the recommended sale price by selecting the phone features on the app. The recommender uses a XGBoost Model with a model accuracy of 84%.
With the recommended price, users are enabled to come out with pricing and negotiating strategies to maximize their revenue and profit.
 

# Limitations and Future Enhancements
Analysis is only limited to all the phone models that have been successfully scrapped. Suggest extracting data from other sites as well to have a more decent comparison geographically.
Recommender could be scaled to include more data across the year to know when is the best time to sell.


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
Dataset name: carousell.csv
- This dataset contains all the scrapped data of phone listing on Carousell.
 
<img width="489" alt="image" src="https://user-images.githubusercontent.com/125956661/229686211-d748b985-21e0-46c0-9b90-8199c5a54161.png">

Dataset name: data382.csv
- This dataset contains all the cleaned data of carousell.csv for modeling prediction.
 
<img width="491" alt="image" src="https://user-images.githubusercontent.com/125956661/229686071-0ed84a0e-4ebf-4505-a8dd-1e47d0be6ff9.png">

 
Dataset name: data_to_map.csv
- This dataset contains all the cleaned data of data382.csv with encoded columns as a reference to user input for model prediction.
 
<img width="487" alt="image" src="https://user-images.githubusercontent.com/125956661/229686118-18183f22-1e02-49f2-b549-57fd7c1bf80d.png">


# Key takeaways from the project:
Recommender deployed successfully on streamlit.io.
- url:   https://angieyhq-phone-price-prediction-app-w02apw.streamlit.app

The recommender is a fuss free way to determine the recommended sale price by selecting the phone features on the app. The recommender uses a XGBoost Model with a model accuracy of 84%.
With the recommended price, users are enabled to come out with pricing and negotiating strategies to maximize their revenue and profit.
 

# Limitations and Future Enhancements
Analysis is only limited to all the phone models that have been successfully scrapped. Suggest extracting data from other sites as well to have a more decent comparison geographically.
Recommender could be scaled to include more data across the year to know when is the best time to sell.


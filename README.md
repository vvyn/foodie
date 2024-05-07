# Foodie
How much time do you spend deciding on what would you like to eat? Save time by using foodie! An NLP model the provides food recommendations based on user inputted ingredients

# Input
Please format your entry by seperating each ingrediant and keyword by comma

![image](https://github.com/vvyn/foodie/assets/62407356/d68bc49e-5235-44d6-b5ef-825d00064761)

# Output
Top 5 recommendations based on input

![image](https://github.com/vvyn/foodie/assets/62407356/46dd1289-1e37-419f-82f8-7dabdf8e838d)

# Project Overview
- Data
  - The first step was to find a good data source. I tried to query WikiData for food related data, but later I ended up using Food.com's Recipe dataset from Kaggle.
  - I used the recipe name, ingrediant, and description columns of the dataset.
- Preprocessing
  - Included checking for null and unique values.
  - Removing special characters such as commas, brackets, and spaces.
  - Correct tokenzation of both the recipe data and the user's input. 
- Word2Vec
- Cosine Similarity
- Testing
- Keyword Extraction

# Code
- model: src/foodie.ipynb
- model+chatbot: chatbot.py
- chatbot: chatbot2.py

# Discord Commands
- prompt with "$foodie"
- end chat with "thank you!"
![image](https://github.com/vvyn/foodie/assets/62407356/0bb01d54-2a01-40ac-984d-ffdb5337a3c1)

# Bot Start Up
- install all dependancies
- cd nlp-project
- chatbot-env/Scripts/activate.bat
- python chatbot.py

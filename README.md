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
  - I trained a Word2Vec model on the recipe dataset, resulting the model's wordlist including all the ingrediants in the dataset. 
  - Afterwards, I took every recipe token array, checked whether each token was in the Word2Vec wordlist, then took the averages of the vectors of the tokens that were in the wordlist. This created an array of all of the recipe vectors that could be compared against to fidn the most similar recipes.
- Cosine Similarity
  - To find the most similar recipe based on the user input, I cleaned, tokenized, and vectoried the user input in a similar way to the dataset. Then, I compared the similarities of the user input vector with that of all of the recipe vectors using cosine similarity. I sorted by the percentage of similarity to get the top 5 most similar recipes that were outputted to the user. 
- Testing
  - To see how accurate the model is, I looked at how similar the cosine similarity percentages were along with whether the results matched something I would want to be outputted as a potential user. 
- Keyword Extraction
  - I then extracted keywords, by self defining a list based on 'salty' and 'sweet', along with other terms, comparing the list with the description column using name entity recognition, and then creating a new column named keywords that label each recipe with the extracted keywords found in the description.

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

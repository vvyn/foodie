# foodie
- get food recommendations based on ingredients and keywords

# dataset
- Food.com Recipes (https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv)
- 230186 rows

# preprocessing
- remove null values
- fill in NaN values with "" for descriptions
- unique names
  
# name entitry recognition
- keywords from descriptions (salty, sweet, spicy)

# recommendations
- cosine similarity based on ingredient list

# model
- kmeans
- randomForestClassifier

# commands
- prompt with "$foodie"
- end chat with "thank you!"

# bot start up
- cd nlp-project
- chatbot-env/Scripts/activate.bat
- python chatbot.py

# previous versions
- to see previous commits with code reference this link: https://github.com/vvyn/nlp-project
- there were issues pushing commits due to accidentally uploading multiple datasets

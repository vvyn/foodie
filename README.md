# STILL IN PROGRESS!!

# foodie
- get food recommendations based on ingredients and keywords

# dataset
- Food.com Recipes (https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?select=RAW_recipes.csv)
- 230186 rows

# preprocessing
- remove null values
- fill in NaN values with "" for descriptions
- unique names

# model
## cosine similarity + word2vec based on ingrediant list
![image](https://github.com/vvyn/foodie/assets/62407356/ee2e7df2-886b-4c3d-9cc0-e96741160ca4)
![image](https://github.com/vvyn/foodie/assets/62407356/e403408d-0b5d-4ccc-8b9d-5b37b43f03f7)

# name entitry recognition
- keywords from descriptions (salty, sweet, spicy)
![image](https://github.com/vvyn/foodie/assets/62407356/c1d452ab-1c68-489a-a5fb-c097e3231124)
![image](https://github.com/vvyn/foodie/assets/62407356/c3e475d7-a82a-4073-bb8c-08e9f2162331)

# commands
- prompt with "$foodie"
- end chat with "thank you!"

# bot start up
- cd nlp-project
- chatbot-env/Scripts/activate.bat
- python chatbot.py

# version timeline
## if statements
![image](https://github.com/vvyn/foodie/assets/62407356/0bb01d54-2a01-40ac-984d-ffdb5337a3c1)
## general search based
![image](https://github.com/vvyn/foodie/assets/62407356/2a41c026-4f82-4e97-8a73-b3a5d01e149b)
## finding specific category based on the word
![image](https://github.com/vvyn/foodie/assets/62407356/46803a7a-bf3d-4583-a964-e6d0b15112af)
## detailed search results
![image](https://github.com/vvyn/foodie/assets/62407356/eb1655fc-4df0-4fad-a0fc-3fc19c3bfd4f)

# previous code versions
- to see previous commits with code reference this link: https://github.com/vvyn/nlp-project
- there were issues pushing commits due to accidentally uploading multiple datasets

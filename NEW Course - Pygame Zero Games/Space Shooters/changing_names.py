import os

for filename in os.listdir("./images"):
    new_name = filename.lower()
    os.rename("./images/" + filename, "./images/" + new_name)
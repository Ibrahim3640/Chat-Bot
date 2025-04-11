# Project 1: Chatbot

import json
import random

def load_data_from_json(file_path):
 with open (file_path, 'r') as file:
    return json.load(file)

keywords_json = load_data_from_json('keywords.json')

Agent_Name = ["Jack", "Ayesha", "Maryam", "Harrison", "Mohammad", "Kai", "Robert", "Felix", "Julius", "Adam"]

Random_Name = random.choice(Agent_Name)

print("Welcome to the University of Poppleton, my name is", Random_Name)
print("")

Name = str(input("Enter your name: "))
print("")
print("Hey, hope you are doing well", Name)
print("")

def log_chatbot_session(name, question, response):
    with open("log_chatbot_session.txt", "a") as log_file:
        log_file.write(f"{name}: {question}\n{Random_Name}: {response}\n")

def response_from_keywords_json(question, keywords):
    question_lower = question.lower()

    for keyword, response in keywords.items():
        if keyword.lower() in question_lower:
         return response

    return"Sorry, we don't have any information on that question you have asked"

exit_command = ['exit', 'bye', 'quit']

def chatbot():
    while True:
        question = input("What questions would you like to ask: ")

        if any(command in question.lower() for command in exit_command):
            print("Bye, hope you have a great day")
            break

        response = response_from_keywords_json(question, keywords_json)
        print(f"{Random_Name}: {response}")

        (log_chatbot_session(Name, question, response))

if __name__ == "__main__":
    chatbot()

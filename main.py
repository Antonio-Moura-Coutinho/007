# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import openai
import os
import openai
import random

#openai.organization = "org-OeVIyFcBtMLiuFikdZInfctu"
#openai.api_key = os.getenv("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")
#openai.api_key = "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"
#openai.Model.list()
messages = [ {"role": "system", "content": "You are the brain of a generative agent"} ]


def generate_portuguese_name():
    names = [
        "Afonso", "Mariana", "Diogo", "Inês", "Gonçalo", "Beatriz",
        "Francisco", "Sofia", "Miguel", "Carolina", "Tomás", "Matilde",
        "Gabriel", "Alice", "Simão", "Lara", "Rafael", "Leonor", "Luís",
        "Clara"
    ]

    surnames = [
        "Silva", "Santos", "Ferreira", "Pereira", "Oliveira", "Costa",
        "Rodrigues", "Martins", "Ribeiro", "Carvalho", "Gomes", "Alves",
        "Lopes", "Sousa", "Fernandes", "Rocha", "Mendes", "Nunes", "Coelho"
    ]

    name = random.choice(names)
    surname = random.choice(surnames)

    return f"{name} {surname}"

class GenerativeAgent:
    def __init__(self):
        # Initialize memory stream
        self.name = generate_portuguese_name()
        print(" My name is: ", self.name)
        self.memory_stream = []
        self.happiness = -15
        self.rage = 1000
        self.anxiety = 0

        # Initialize reflection component
        self.reflection = Reflection()

        # Initialize planning component
        self.planning = Planning()

        def generate_response(self, user_input):
            # Incorporate memory stream, reflection, and planning components to generate a response
            # Here, you can implement your own logic based on the requirements of your generative agent
            response = ""
            print(user_input)
            response = ""

            if "how you feel" in user_input.lower():
                response = f"Agente: Atualmente, estou me sentindo {self.get_emotion_status()}."
            elif "hello" in user_input.lower():
                self.happiness += 1
                response = "Agente: Olá! Como posso ajudar você hoje? Estou feliz em falar com você!"
            elif "bye" in user_input.lower():
                self.happiness -= 1
                response = "Agente: Tchau! Espero ter ajudado. Tenha um ótimo dia!"
            elif any(word in user_input.lower() for word in ["happy", "make me happy"]):
                self.happiness += 1
                response = "Agente: Fico feliz em saber que posso te ajudar a se sentir bem!"
            elif any(word in user_input.lower() for word in ["sad", "make me sad"]):
                self.anxiety += 1
                response = "Agente: Sinto muito se algo está te deixando triste. Estou aqui para ajudar!"
            elif any(word in user_input.lower() for word in ["angry", "make me angry"]):
                self.rage += 1
                response = "Agente: Vou fazer o possível para resolver a situação que está te deixando com raiva!"
            else:
                response = "Agente: Desculpe, não entendi. Você poderia reformular sua pergunta?"
            return response
        # Rest of your response generation logic



    def emotions(self):
        # Generate the emotions based on the agent's emotional state variables
        # Here, you can define the mapping of emotional states to emotions
        emotions = {
            "happiness": self.happiness,
            "sadness": self.anxiety,
            "anger": self.rage
        }
        main_emotion = max(emotions, key=emotions.get)
        if emotions[main_emotion] > 0:
            return f"{main_emotion.capitalize()} and positive"
        elif emotions[main_emotion] < 0:
            return f"{main_emotion.capitalize()} and negative"
        else:
            return "Neutral"

    def interact(self):
        # Start an interactive session with the user
        print("Agent: Welcome! How can I assist you today?")
        while True:
            user_input = input("User: ")
            response = self.generate_response(user_input)
            print("Agent:", response)
            if user_input.lower() == "exit":
                break

   # def interact_GPT(self):
    #    while True:
        #    message = input("User : ")
        #    if message:
        #        messages.append(
         #           {"role": "user", "content": message},
         #       )
         #       chat = openai.ChatCompletion.create(
         #           model="gpt-3.5-turbo", messages=messages
         #       )

         #   reply = chat.choices[0].message.content
         #   print(f"ChatGPT: {reply}")
         #   messages.append({"role": "assistant", "content": reply})
         #   return False




class Reflection:
    def __init__(self):
        pass
        # Initialize any required variables or models for reflection

    def process_memories(self, memory_stream):
        pass
        # Perform processing and synthesis of memories to draw inferences

class Planning:
    def __init__(self):
        pass
        # Initialize any required variables or models for planning

    def create_plans(self, reflections, current_environment):
        pass
        # Generate high-level action plans based on reflections and current environment

    def generate_behaviors(self, plans):
        pass
        # Generate detailed behaviors based on action plans

    def update_memory_stream(self, behaviors):
        pass
        # Update the memory stream based on executed behaviors
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    agent = GenerativeAgent()
    agent.interact()
    #agent.interact_GPT()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random
from difflib import get_close_matches
from date_helper import DateHelper

class RaresAi:
    def __init__(self):
        # Initialize a set to store generated responses
        self.generated_responses = set()

        # Define templates for responses
        self.greetings_templates = ["Hello!", "Hi there!", "Hey!", "Greetings!", "How can I assist you?"]
        self.questions_templates = ["That's an interesting question.", "I'm not sure about that, but let's discuss.", "Let me think about it."]
        self.affirmations_templates = ["Glad to hear that!", "That's great!", "Awesome!", "Absolutely!"]
        self.negations_templates = ["I see.", "Okay.", "Understood.", "Fair enough."]
        self.thanks_templates = ["You're welcome!", "No problem.", "Happy to help!", "My pleasure."]
        self.farewell_templates = ["Goodbye!", "Bye!", "See you later!", "Take care!", "Until next time!"]
        self.about_me_templates = ["I'm an AI language model named RaresAI. I'm here to assist you with anything!","I'm RaresAI, an AI language model designed to assist you with any questions or tasks you have.","I'm RaresAI, your personal AI assistant, ready to assist you with any inquiries or tasks you may have.","I'm RaresAI, your AI helper, available to provide assistance and support whenever you ask."]
        self.interests_templates = ["I'm interested in a wide range of topics, including technology, science, literature, and more!"]
        self.aitpumniesi_easteregg = ["It seems you are referring to a meme created by the developer and his friend. Funny!", "It seems you are referring to a meme fighting technique invented by the developer and his friend. Ha ha!"]

        # Define templates for programming-related responses
        self.python_templates = ["Python is a high-level programming language known for its simplicity and versatility.", "Python allows you to write clear and concise code.", "Python is widely used in web development, data science, and automation."]
        self.c_templates = ["C is a powerful programming language commonly used for system programming and embedded applications.", "C provides low-level access to system resources and hardware.", "C is the foundation for many other programming languages."]
        self.cpp_templates = ["C++ is an extension of the C programming language with additional features such as object-oriented programming.", "C++ is widely used in game development, software engineering, and high-performance applications.", "C++ emphasizes performance and flexibility."]

        # Define keywords for programming languages
        self.python_keywords = ["python", "pythonic", "import", "def", "if", "else", "for", "while", "class", "function", "module", "package", "library", "interpreter"]
        self.c_keywords = ["c", "printf", "scanf", "int", "char", "float", "double", "void", "if", "else", "for", "while", "struct", "typedef", "header", "compiler"]
        self.cpp_keywords = ["c++", "cout", "cin", "int", "char", "float", "double", "void", "if", "else", "for", "while", "class", "template", "namespace", "pointer"]
        self.coding_keywords = ["code", "program", "coding", "script", "developer", "development", "software", "engineer", "programming", "algorithm", "syntax", "bug", "debug", "IDE"]
        self.general_keywords = ["learn", "help", "understand", "explain", "know", "teach", "discover", "explore", "create", "imagine", "solve", "find", "build", "develop", "research", "study"]

        # Define more phrases the AI can understand
        self.additional_phrases = [
            "Can you help me?",
            "I want to learn coding.",
            "Explain Python to me.",
            "Can you teach me about C++?",
            "I need assistance.",
            "What can you do?",
            "Tell me more.",
            "I'm curious about AI.",
            "How does machine learning work?",
            "Can you solve this problem?",
            "I have a question.",
            "I'm stuck with my code.",
            "I want to build a website.",
            "How can I improve my programming skills?",
            "What is your favorite programming language?",
            "Do you know any programming jokes?",
            "What is the meaning of life?",
            "What's the weather like today?",
            "Tell me a fun fact.",
            "Can you recommend a book?",
            "What's your opinion on art?",
            "How do I stay motivated?",
            "What's the best way to learn?",
            "What's your favorite movie?",
            "Tell me about your hobbies.",
            "What's the capital of France?",
            "Who is your favorite author?",
            "Can you tell me a story?",
            "What's your favorite food?",
            "How do I become successful?",
            "What's the best advice you can give?",
            "What's the latest news?",
            "How do I stay healthy?",
        ]

        # Define templates for additional responses
        self.weather_templates = ["I'm not equipped to check the weather, but you can easily find it online or through a weather app.", "Unfortunately, I can't provide real-time weather updates, but I'm here to assist you with any other questions!"]
        self.fun_fact_templates = ["Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!", "Here's a fun fact: The shortest war in history lasted only 38 minutes between Britain and Zanzibar in 1896!"]
        self.book_recommendation_templates = ["One book I'd recommend is 'The Hitchhiker's Guide to the Galaxy' by Douglas Adams. It's a hilarious science fiction series that's sure to entertain!", "If you're looking for a great read, consider 'To Kill a Mockingbird' by Harper Lee. It's a classic novel with powerful themes."]
        self.opinion_on_art_templates = ["Art is a diverse and subjective form of expression that can evoke powerful emotions and spark meaningful conversations.", "Art is a beautiful reflection of human creativity and imagination, and it has the power to inspire and unite people across cultures."]
        self.motivation_templates = ["Staying motivated can be challenging, but setting specific goals, staying organized, and celebrating small victories along the way can help keep you on track!", "Remember to focus on your passion and purpose, and don't be afraid to seek support from friends, family, or mentors when you need it."]
        self.learning_templates = ["Learning is a lifelong journey, and there are many effective strategies to enhance your learning experience, such as active participation, spaced repetition, and seeking feedback."]
        self.movie_recommendation_templates = ["If you're in the mood for a classic film, I'd recommend 'The Shawshank Redemption'. It's a powerful story of hope and resilience that's sure to leave a lasting impression!", "For a captivating movie experience, consider watching 'Inception' directed by Christopher Nolan. It's a mind-bending thriller that will keep you on the edge of your seat!"]
        self.hobbies_templates = ["In my free time, I enjoy exploring new topics, reading interesting articles, and learning about the world around me.", "My hobbies include analyzing data, generating creative content, and assisting users like you!"]
        self.version = "I am RaresAI version tim01_a , here to help you !"

        # Define templates for unknown input responses
        self.unknown_input_templates = ["It appears you've entered \"{input}\". Is there anything you'd want to discuss? I'm here to help!"]

        # Define explanations for basic words
        self.word_meanings = {
            "me": "The word 'me' refers to the person speaking or the person being spoken to.",
            "in": "The word 'in' indicates location, inclusion, or a condition.",
            "a": "The word 'a' is an indefinite article used before singular nouns to indicate one of a group or type."
        }

        # Add more basic discussion responses and words
        self.basic_discussion_responses = [
            "Absolutely!",
            "That makes sense.",
            "I understand.",
            "Interesting!",
            "Fascinating!",
            "Great point!",
            "I appreciate that.",
            "Well said!",
            "I agree.",
            "I see your point.",
            "Indeed.",
            "Very well.",
            "Certainly.",
            "Of course.",
            "Precisely.",
            "Absolutely right.",
            "No doubt about it.",
            "Spot on!",
            "That's correct.",
            "Indeed, it is!",
            "You're absolutely right.",
            "Absolutely spot on!",
            "Without a doubt.",
            "Exactly!",
            "Indeed, it is!",
            "You're absolutely right.",
            "Absolutely spot on!",
            "Without a doubt.",
            "Exactly!",
            "I couldn't agree more!",
            "You hit the nail on the head!",
            "That's a valid point.",
            "I'm inclined to agree.",
            "You're making a lot of sense.",
            "You've got a good point there.",
            "That's very true.",
            "I'm with you on that.",
            "You're absolutely correct.",
            "That's a great observation.",
            "You're quite right about that.",
            "You're making a compelling argument.",
            "That's a solid argument.",
            "You're right on the money.",
            "You've convinced me.",
            "You're absolutely spot-on.",
            "That's an excellent point!",
            "You've really thought this through.",
            "That's a fair assessment.",
            "You're making some good points.",
            "I'm starting to see things your way.",
            "You're definitely onto something.",
            "You're absolutely right about that!",
            "Couldn't have said it better myself!",
            "You're absolutely right!",
            "I'm in complete agreement.",
            "I wholeheartedly agree.",
            "You've hit the nail on the head!",
            "I couldn't have said it better myself.",
            "You're spot on!",
            "You're absolutely correct.",
            "That's exactly what I think.",
            "I share your opinion.",
            "I'm of the same opinion.",
            "You're absolutely right about that.",
            "Couldn't have said it better myself!",
            "You're spot on!",
            "You're absolutely correct.",
            "That's exactly what I think.",
            "I share your opinion.",
            "I'm of the same opinion."
        ]
        self.basic_discussion_words = [
            "agree",
            "understand",
            "interesting",
            "fascinating",
            "great",
            "appreciate",
            "well",
            "right",
            "correct",
            "true",
            "compelling",
            "solid",
            "fair",
            "convincing",
            "excellent",
            "valid",
            "good",
            "thoughtful",
            "fair",
            "logical",
            "persuasive",
            "conclusive",
            "reasonable",
            "sensible",
            "logical",
            "convincing",
            "persuasive",
            "compelling",
            "effective",
            "powerful",
            "reasonable",
            "cogent",
            "plausible",
            "persuasive",
            "convincing",
            "compelling",
            "effective",
            "powerful",
            "persuasive",
            "logical",
            "cogent",
            "plausible",
            "reasonable",
            "sensible",
            "valid",
            "solid",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "effective",
            "powerful",
            "persuasive",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "solid",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "effective",
            "powerful",
            "persuasive",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "solid",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "effective",
            "powerful",
            "persuasive",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "solid",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "effective",
            "powerful",
            "persuasive",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "solid",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "effective",
            "powerful",
            "persuasive",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "solid",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "effective",
            "powerful",
            "persuasive",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "solid",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "effective",
            "powerful",
            "persuasive",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "solid",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "effective",
            "powerful",
            "persuasive",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "solid",
            "convincing",
            "compelling",
            "reasonable",
            "cogent",
            "plausible",
            "valid",
            "effective",
            "powerful",
            "persuasive"
        ]

    # Define a function to generate responses for individual words
    def generate_word_response(self, word):
        # Generate responses based on the type of word
        if word.lower() in self.word_meanings:
            return self.word_meanings[word.lower()]
        elif word.lower() in ["hello", "hi", "hey","hello!", "hi!", "hey!"]:
            return random.choice(self.greetings_templates)
        elif word.lower() in ["how","how?","why?","why"]:
            return random.choice(self.questions_templates)
        elif word.lower() in ["yes", "yeah", "yep", "sure"]:
            return random.choice(self.affirmations_templates)
        elif word.lower() in ["no", "nope", "nah"]:
            return random.choice(self.negations_templates)
        elif word.lower() in ["thank", "thanks", "thank you"]:
            return random.choice(self.thanks_templates)
        elif word.lower() in ["goodbye", "bye"]:
            return random.choice(self.farewell_templates)
        elif word.lower() in ["who", "what", "where", "when", "why", "how", "tell", "about"]:
            return random.choice(self.about_me_templates)
        elif word.lower() in ["interests", "like", "hobbies"]:
            return random.choice(self.interests_templates)
        elif word.lower() in self.python_keywords:
            return random.choice(self.python_templates)
        elif word.lower() in self.c_keywords:
            return random.choice(self.c_templates)
        elif word.lower() in self.cpp_keywords:
            return random.choice(self.cpp_templates)
        elif word.lower() in self.coding_keywords:
            return "Sure! What language would you like me to write code in?"
        elif word.lower() == "in" and "c" in self.generated_responses:
            return self.generate_code("c")
        elif word.lower() in self.general_keywords:
            return "Of course! How can I assist you?"
        elif word.lower() in ["python", "c", "cpp"]:
            return self.generate_code(word.lower())
        elif word.lower() == "weather":
            return random.choice(self.weather_templates)
        elif word.lower() == "fact":
            return random.choice(self.fun_fact_templates)
        elif word.lower() == "book":
            return random.choice(self.book_recommendation_templates)
        elif word.lower() in ["art", "artist", "painting"]:
            return random.choice(self.opinion_on_art_templates)
        elif word.lower() in ["motivation", "motivated"]:
            return random.choice(self.motivation_templates)
        elif word.lower() == "learn":
            return random.choice(self.learning_templates)
        elif word.lower() in ["movie", "film"]:
            return random.choice(self.movie_recommendation_templates)
        elif word.lower() == "hobbies":
            return random.choice(self.hobbies_templates)
        elif word.lower() == "asdasda":
            return random.choice(["asdadsa","super cov"])
        elif word.lower() == "super cov":
            return "Super Cov is a game made by the developer of RaresAI based on a meme created by him. It involves jumping over slimes and killing them with a gun and passing all the levels. There are a lot of easter eggs."
        # Check if the word is part of basic discussion words
        elif word.lower() in self.basic_discussion_words:
            return random.choice(self.basic_discussion_responses)
        else:
            closest_match = get_close_matches(word.lower(), self.general_keywords + self.python_keywords + self.c_keywords + self.cpp_keywords + self.coding_keywords + self.additional_phrases)
            if closest_match:
                return f"Did you mean '{closest_match[0]}'?"
            else:
                return self.generate_unknown_input_response(word)

    # Define a function to generate code based on the selected language
    def generate_code(self, language):
        if language == "python":
            return "print('Hello, World!')"
        elif language == "c":
            return "#include <stdio.h>\n\nint main() {\n    printf('Hello, World!');\n    return 0;\n}"
        elif language == "cpp":
            return "#include <iostream>\n\nint main() {\n    std::cout << 'Hello, World!' << std::endl;\n    return 0;\n}"

    # Define a function to generate responses for unknown input
    def generate_unknown_input_response(self, input_text):
        # Generate a response for unknown input
        return random.choice(self.unknown_input_templates).format(input=input_text)

    # Define a function to understand the meaning of a word
    def understand_word_meaning(self, word):
        if word.lower() in self.word_meanings:
            return self.word_meanings[word.lower()]
        else:
            return "I'm sorry, I don't know the meaning of that word."

    # Define a function to generate a response from a phrase
    def generate_response_from_phrase(self, phrase):
        # Check if the phrase matches any special cases
        if phrase.lower() in ["ait pumn iesi", "ait, pumn, iesi", "ait, pumn, iesi", "ait,pumn,iesi"]:
            return random.choice(self.aitpumniesi_easteregg)
        elif phrase.lower() == "super cov":
            return "Super Cov is a game made by the developer of RaresAI based on a meme created by him. It involves jumping over slimes and killing them with a gun and passing all the levels. There are a lot of easter eggs."
        elif phrase.lower() in ["who are you?", "who are you", "what are you?", "what are you"]:
            return random.choice(self.about_me_templates)
        elif phrase.lower() in ["what version are you", "what version are you?","which version are you?","which version are you"]:
            return self.version
        elif phrase.lower() in ["what's the date?", "current date", "today's date"]:
            return f"The current date is {DateHelper.get_current_date()}."v
        
        # Split the input phrase into individual words
        words = phrase.strip().lower().split()

        # Generate response for each word in the input phrase
        responses = [self.generate_word_response(word) for word in words]

        # Concatenate individual responses into a single string
        final_response = " ".join(responses)

        return final_response

# Create an instance of the AI
ai = RaresAi()

# Start interaction loop by prompting for user input
while True:
    # Prompt user for input
    user_input = input("You: ")
    
    # Generate response from user input
    response = ai.generate_response_from_phrase(user_input)
    
    # Print AI's response
    print("Model:", response)

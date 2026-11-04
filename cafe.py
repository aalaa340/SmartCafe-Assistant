import re
import json

class research_agent:
    def __init__(self, data_file): #to initialize data_file and load JSON.
      self.data_file = data_file
      self.data = self.load_data()

    def load_data(self):
        with open(self.data_file, 'r') as f:
         return json.load(f)
        
        
    def search(self, result, user_input):
       if result == "ingredients":
          match = re.search(r"(?:in|of)\s+(.*)", user_input, re.IGNORECASE)
          item_name = match.group(1).strip() if match else ""
          item_name_case_insensetive=item_name.title()
          menu_data=self.data.get("menu", {})
          item_data=menu_data.get(item_name_case_insensetive, {})
          ingrediant_data=item_data.get("ingredients", "❌ Item not found.")
          return ingrediant_data
       
       elif result == "calories":
          match = re.search(r"(?:calories.*(?:in|on)?\s+)(.*)", user_input, re.IGNORECASE)
          item_name = match.group(1).strip() if match else ""
          item_name_case_insensetive=item_name.title()
          menu_data=self.data.get("menu", {})
          item_data=menu_data.get(item_name_case_insensetive, {})
          calories_data=item_data.get("nutrition", "❌ Calorie info not found.")
          return calories_data
       
       elif result=="drinks":
          drinks_data=self.data.get("drinks", {})
          return drinks_data
          

       elif result == "hours":
         match = re.search(r"(monday|tuesday|wednesday|thursday|friday|saturday|sunday)", user_input, re.IGNORECASE)
        
         day = match.group(1).strip() if match else ""
      
         item_name_case_insensetive=day.capitalize()
         try:
            opening_data=self.data.get("opening_hours", {})
        
            item_data=opening_data.get(item_name_case_insensetive, {})
        
            user_opening_data=item_data
            return user_opening_data
         except:
           print("opening hour not found!")
    

       else:
        return " Intent not recognized."

    

        


class chat_bot:
    def __init__(self, research_agent):
        self.research_agent = research_agent
    
    def great (self):
        print ('''welcome to our smart cafe 
               
   i wish you to have a great time with us 

               ''')
    def get_user_request(self):
        user_request=input('''how can i help you 
        you can ask for the drinks that we have also the ingredients and calories in each drink or our works time
        example of how to ask :
                           what drinks do you have ?
                           how much calories in (drink's name)? 
                           what's in (drink's name) ?
                           when do you open on (name of the day) ?
                           NOW : ask your question here  ''')
        return user_request
    
    def parse_intent(self, user_input):
        # Ingredients
        if re.search(r"what.*in\s+(.*)", user_input, re.IGNORECASE):
            return "ingredients"
        # Calories
        elif re.search(r"how.*calories.*\s+(.*)", user_input, re.IGNORECASE):
            return "calories"
        # Opening hours
        elif re.search(r"(when|what time).*open.*(monday|tuesday|wednesday|thursday|friday|saturday|sunday)", user_input, re.IGNORECASE):
            return "hours"
        elif re.search(r"drink", user_input, re.IGNORECASE):
           return"drinks"
        else :
           return "unknown"

    def handle_query(self, result, user_input):
        response = self.research_agent.search(result, user_input)
        return response
    
    def display_response(self, response):
       print(f" {response}\n")
    
    def run(self):
       self.great()
       
       while True:
         user_input = self.get_user_request()
         if user_input.lower()in ["exit","quit"]:
            print(" Goodbye! Have a lovely day!")
            break
       
         result = self.parse_intent(user_input)
         response =self.handle_query(result, user_input)
         self.display_response(response)





search=research_agent("cafe_data.json")
chat=chat_bot(search)
chat.run()


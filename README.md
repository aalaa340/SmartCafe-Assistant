# SmartCafe-Assistant
this project is  OOP Based Console Application   help the user to know what's the drink that we have in the cafe , the calories of each and opening time of the cafe  based on regex feature the app search in cafe_data.json file about what user asked for .
class research_agent:
 this class is linked with cafe_data file and search on it about what user ask 

    def __init__(self, data_file):
    to initialize data_file and load JSON.

    def load_data(self):
        open json file 
        
        
    def search(self, result, user_input):
        result pass to it , then compare result value with what in json file and return output 
        the output is what user asked for 
        the comparision process is done by compare  what the regex pattren find in the user input with what in the json file
         
class chat_bot:
this class contact with user , get user request , analyse the question of the user , use the search agent class and display the output 
    def __init__(self, research_agent):
      constructor use  self.research_agent to pass search agent to use it in handle query function 
    
    def great (self):
        to great user
    def get_user_request(self):
        get user input 
    def parse_intent(self, user_input):
        use regexto know what user intent , output it as keywords like ingredians to pass it to search function later 

    def handle_query(self, result, user_input):
    use search function to get the final result
        
    
    def display_response(self, response):
       display final result 
    
    def run(self):
       call the functions and run the program until user type exit 




  

#survey
class AnonymousSurvey():
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.response =[]
    
    def show_question(self):
        print(self.question)

    def store_respond(self,new_respond):
        self.response.append(new_respond)
    
    def show_result(self):
        print("Survey result:")
        for response in self.response:
            print('--' + response)
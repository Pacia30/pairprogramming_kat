class DiaryEntry(): #one entry
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def todo(self):
    # adds todo to todo list
    #returns todo list
        if "to do" in self.title:
            return self.content
    
    
    def contact(self):
    # add number to contact list
    #returns contact list
            if self.content.isnumeric() and (len(str(self.content)) == 12):
                return (f"{self.title}:{self.content}")
            


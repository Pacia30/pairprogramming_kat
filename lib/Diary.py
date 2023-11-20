class Diary(): #multiple entries
    def __init__(self):
        self.diaryentry = []
    # Parameters: 
    #   diaryentry, list containing entries
    #   contacts, list of mobile phone numbers in diary entries
        
    def add_entry(self, entry):
    # Parameters: 
    #   title: a string containing title of diary entry
    #   content: a string with content of diary entry
    # Side effect:
    #   adds a diary entry to the list
    # Returns:
    #   nothing
        self.diaryentry.append(entry)

    def todolist(self):
         return [entry.todo() for entry in self.diaryentry
                if entry.todo()        
             ]
    
    def contactlist(self):
         return [entry.contact() for entry in self.diaryentry
                if entry.contact()]
    
    
    def diaryentries(self):
    # Parameters: 
    #   no parameters
    # Side effect:
    #   nothing
    # Returns:
    #   list of all diary entries
        return  self.diaryentry

    def read_entry_busyday(self, available_time, wpm):
    # Parameters: 
    # Side effect:
    #   we go back to DiaryEntry.read_entry_busyday and if true
    #   adds to readable_entries
    # Returns:
    #   diary entries that are readable with wpm and time given
        readable_entries = []
        for entry in self.diaryentry:
            count_words = len(entry.content.split())
            entry_reading_time = count_words / wpm
        
            if entry_reading_time <= available_time:
                readable_entries.append(entry)

        if readable_entries == []:
            return None
        return readable_entries
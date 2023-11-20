## 1. Describe the Problem

'''
As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries
'''

## 2. Design the Class System
```python

class Diary(): #multiple entries
    def __init__(self)
    # Parameters: 
    #   diaryentry, list containing entries
    #   contacts, list of mobile phone numbers in diary entries
    
    def add_entry(self, entry)
    # Parameters: 
    #   title: a string containing title of diary entry
    #   content: a string with content of diary entry
    # Side effect:
    #   adds a diary entry to the list
    # Returns:
    #   nothing
    
    def diaryentries(self)
    # Parameters: 
    #   no parameters
    # Side effect:
    #   nothing
    # Returns:
    #   list of all diary entries

    def read_entry_busyday(self)
    # readable_entries = []
    # Parameters: 
    #   wpm: int representing readable words per minute
    #   time: int representing how long we have to read
    # Side effect:
    #   we go back to DiaryEntry.read_entry_busyday and if true
    #   adds to readable_entries
    # Returns:
    #   diary entries that are readable with wpm and time given
    three entries and only 1 and 3 are readable
        [entry1, entry3]


class DiaryEntry(): #one entry
    def __init__(self, title, content)
    #   todo list = []
    #   contact list = []
    #   readable list = []
    def todo
    # adds todo to todo list
    #returns todo list
    def contact
    # add number to contact list
    #returns contact list 
    def read_entry_busyday(self, wpm, time)
    # Parameters: 
    #   wpm: int representing readable words per minute
    #   time: int representing how long we have to read
    # Side effect:
    #   wordreadable = calculation to know how many words we can read with wpm and time
    #   compare wordreadable <= len of words in content

    # Returns:
    #   diary contents that are readable with wpm and time given
    
```
## 3. Create Examples as Integration Tests
```python
def test_add_entry()
    diaryentry = Diary()
    entry1 = DiaryEntry("title1", "content1")
    diaryentry.add_entry(entry1)
    assert diaryentry.diaryentries() == [entry1]

```


## 4. Create Examples as Unit Tests


## 5. Implement the Behaviour



diaryentries => []
    [entry1, entry2]
eg  [monday, tuesday]


class(self, title, content) 
    entry1:  (title1, content1)
eg  "monday": (todo, eafyeasf hihfisueh)
    entry2:  (title2, content2)
eg  "tuesday": (today, today was hard)


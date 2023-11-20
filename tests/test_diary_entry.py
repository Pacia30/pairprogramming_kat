from lib.diary_entry import *

def test_todo():
    diaryentry = DiaryEntry("monday to do", "walk the dog")
    assert diaryentry.todo() == "walk the dog"

# def test_busyday_twoentries():
#     diaryentry = Diary()
#     entry1 = DiaryEntry("title1", "content1")
#     Monday = DiaryEntry("Today", "today was very hard")
#     diaryentry.add_entry(entry1)
#     diaryentry.add_entry(Monday)
#     assert diaryentry.read_entry_busyday(5, 1) == [entry1, Monday]
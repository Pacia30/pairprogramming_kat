from lib.Diary import *
from lib.diary_entry import *

def test_add_entry():
    diaryentry = Diary()
    entry1 = DiaryEntry("title1", "content1")
    diaryentry.add_entry(entry1)
    assert diaryentry.diaryentries() == [entry1]

def test_add_two_entry():
    diaryentry = Diary()
    entry1 = DiaryEntry("title1", "content1")
    Monday = DiaryEntry("Today", "today was very hard")
    diaryentry.add_entry(entry1)
    diaryentry.add_entry(Monday)
    assert diaryentry.diaryentries() == [entry1, Monday]

def test_busyday_entry():
    diaryentry = Diary()
    entry1 = DiaryEntry("title1", "content1")
    Monday = DiaryEntry("Today", "today was very hard")
    diaryentry.add_entry(entry1)
    diaryentry.add_entry(Monday)
    assert diaryentry.read_entry_busyday(2, 1) == [entry1]

def test_busyday_twoentries():
    diaryentry = Diary()
    entry1 = DiaryEntry("title1", "content1")
    Monday = DiaryEntry("Today", "today was very hard")
    diaryentry.add_entry(entry1)
    diaryentry.add_entry(Monday)
    assert diaryentry.read_entry_busyday(5, 1) == [entry1, Monday]

def test_busyday_none():
    diaryentry = Diary()
    entry1 = DiaryEntry("title1", "content today is hard")
    Monday = DiaryEntry("Today", "today was very hard")
    diaryentry.add_entry(entry1)
    diaryentry.add_entry(Monday)
    assert diaryentry.read_entry_busyday(2, 1) == None

def test_todd_list_for_multiple_entries():
    diaryentry = Diary()
    week1 = DiaryEntry("monday to do","today was a good day")
    week2 = DiaryEntry("tuesday to do","today was not a good day")
    diaryentry.add_entry(week1)
    diaryentry.add_entry(week2)
    assert diaryentry.todolist() == ["today was a good day", "today was not a good day"]

def test_onetodo_list_for_multiple_entries():
    diaryentry = Diary()
    week1 = DiaryEntry("monday","today was a good day")
    week2 = DiaryEntry("tuesday to do","today was not a good day")
    diaryentry.add_entry(week1)
    diaryentry.add_entry(week2)
    assert diaryentry.todolist() == ["today was not a good day"]

def test_nonetodo_list_for_multiple_entries():
    diaryentry = Diary()
    week1 = DiaryEntry("monday","today was a good day")
    week2 = DiaryEntry("tuesday","today was not a good day")
    diaryentry.add_entry(week1)
    diaryentry.add_entry(week2)
    assert diaryentry.todolist() == []

def test_contact_list():
    diaryentry = Diary()
    week1 = DiaryEntry("kat","447777777777")
    week2 = DiaryEntry("emir","447888888888")
    diaryentry.add_entry(week1)
    diaryentry.add_entry(week2)
    assert diaryentry.contactlist() == ["kat:447777777777", "emir:447888888888" ]

def test_contact_onecontact_not_number_list():
    diaryentry = Diary()
    week1 = DiaryEntry("kat","447777777777")
    week2 = DiaryEntry("emir","emailaddress")
    diaryentry.add_entry(week1)
    diaryentry.add_entry(week2)
    assert diaryentry.contactlist() == ["kat:447777777777"]

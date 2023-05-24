# Your unit tests implementation goes here.
import dbmodels
from decimal import Decimal  #Needed for decimal results

#1 Command
command_1 = '/number-of-users-borrowed NewAge SelfHelp'
output_1 = [{
  'Book Title': 'You are the universe'
}, {
  'Book Title': 'Atomic Habits'
}, {
  'Book Title': 'Atomic Habits'
}]


def unit_test_num_books_genre(command_1, output_1):
  split_command = command_1.split()
  arguments = split_command[1:]
  if len(arguments) == 2:
    genre_1 = arguments[0]
    genre_2 = arguments[1]
    result = dbmodels.BorrowedGenres(genre_1, genre_2).entity
    if result == output_1:
      return True
    else:
      return False
  else:
    return False


#-------------------------------------------------

#2 Command
command_2 = '/number-of-books-by Chopra 1'
output_2 = [{'Title': 'You are the universe'}]


def unit_test_num_books_borrowed_by_at(command_2, output_2):
  split_command = command_2.split()
  arguments = split_command[1:]
  if len(arguments) == 2:
    author = arguments[0]
    branch = arguments[1]
    result = dbmodels.BorrowedBookBranch(author, branch).entity
    if result == output_2:
      return True
    else:
      return False
  else:
    return False


#-------------------------------------------------

#3
command_3 = '/payments-by 2023 20000801'
output_3 = [{'amount': Decimal('2.31'), 'name': 'Chaewon'}]


def unit_test_payment_by_user(command_3, output_3):
  split_command = command_3.split()
  arguments = split_command[1:]
  if len(arguments) == 2:
    year = arguments[0]
    user_id = arguments[1]
    result = dbmodels.PaymentByUser(year, user_id).entity
    if result == output_3:
      return True
    else:
      return False
  else:
    return False


#-------------------------------------------------

#4
command_4 = '/books-ebooks NewAge Chopra'
output_4 = [{'title': 'You are the universe'}]


def unit_test_book_ebook_genre_author(command_4, output_4):
  split_command = command_4.split()
  arguments = split_command[1:]
  if len(arguments) == 2:
    genre = arguments[0]
    author = arguments[1]
    result = dbmodels.BookEbookGenreAuthor(genre, author).entity
    if result == output_4:
      return True
    else:
      return False
  else:
    return False


#-------------------------------------------------

#5
command_5 = '/borrow-book 20010309 1250326753 3'
output_5 = "Successfully added"


def unit_test_borrow_book(command_5, output_5):
  split_command = command_5.split()
  arguments = split_command[1:]
  if len(arguments) == 3:
    user_id = arguments[0]
    book = arguments[1]
    branch = arguments[2]
    result = dbmodels.Borrow(user_id, book, branch).entity
    if result == output_5:
      return True
    else:
      return False
  else:
    return False


#-------------------------------------------------

#6
command_6 = '/borrowed-expires 735211299 2030'
output_6 = [{'Title': 'Atomic Habits', 'Borrowed By': 'Chaewon'}]


def unit_test_borrow_expires(command_6, output_6):
  split_command = command_6.split()
  arguments = split_command[1:]
  if len(arguments) == 2:
    book = arguments[0]
    year = arguments[1]
    result = dbmodels.BorrowExpires(book, year).entity
    if result == output_6:
      return True
    else:
      return False
  else:
    return False


#-------------------------------------------------
#7
command_7 = '/find-payment-average 2023'
output_7 = [{'Average': Decimal('7.01')}]


def unit_test_average_payment(command_7, output_7):
  split_command = command_7.split()
  arguments = split_command[1:]
  if len(arguments) == 1:
    year = arguments[0]
    result = dbmodels.AveragePayment(year).entity
    if result == output_7:
      return True
    else:
      return False
  else:
    return False


#-------------------------------------------------
#8
command_8 = '/find-borrowed-book SelfHelp Yunjin'
output_8 = [{
  'Book Title': 'You are the universe'
}, {
  'Book Title': 'Atomic Habits'
}]


def unit_test_find_book_borrowed(command_8, output_8):
  split_command = command_8.split()
  arguments = split_command[1:]
  if len(arguments) == 2:
    genre = arguments[0]
    user = arguments[1]
    result = dbmodels.BorrowedUserGenre(genre, user).entity
    if result == output_8:
      return True
    else:
      return False
  else:
    return False

#-------------------------------------------------
#9
command_9 = '/find-total-users-watched-video-with SOMU'
output_9 = [{'name': 'Yunjin', 'title': 'Unforgiven'}, {'name': 'Yeji', 'title': 'Unforgiven'}, {'name': 'Yunjin', 'title': 'Unforgiven'}]
def unit_test_watched_credits(command_9, output_9):
  split_command = command_9.split()
  arguments = split_command[1:]
  if len(arguments) == 1:
    credits = arguments[0]
    result = dbmodels.VideosWatched(credits).entity
    if result == output_9:
      return True
    else:
      return False
  else:
    return False

#-------------------------------------------------

#10
command_10 = '/find-books-ebooks-by Yunjin 2023'
output_10 = [{'title': 'love you twice'}, {'title': 'I != Doll'}, {'title': 'Love you twice ebook'}, {'title': 'I != Doll ebook'}]
def unit_test_find_book_ebook(command_10, output_10):
  split_command = command_10.split()
  arguments = split_command[1:]
  if len(arguments) == 2:
    author = arguments[0]
    year = arguments[1]
    result = dbmodels.BookEbookYearAuthor(author, year).entity
    if result == output_10:
      return True
    else:
      return False
  else:
    return False

#-------------------------------------------------

#11
command_11 = '/hold 20010417 735211299'
output_11 = "Successfully added"
def unit_test_hold(command_11, output_11):
  split_command = command_11.split()
  arguments = split_command[1:]
  if len(arguments) == 2:
    user_id = arguments[0]
    book = arguments[1]
    result = dbmodels.ReserveBook(user_id, book).entity
    if result == output_11:
      return True
    else:
      return False
  else:
    return False

#-------------------------------------------------
    
#12
command_12 = '/find-totalbooks-has-researchpaper'
output_12 = [{'title': 'love you twice'}, {'title': 'I != Doll'}]
def unit_book_research_paper(command_12, output_12):
  split_command = command_12.split()
  arguments = split_command[1:]
  if len(arguments) == 0:
    result = dbmodels.AuthorResearchPaper().entity
    if result == output_12:
      return True
    else:
      return False
  else:
    return False

#-------------------------------------------------

#13
command_13 = '/find-total-managers-at 1'
output_13 = [{'Employee Name:': 'Mina'}]
def unit_test_manager(command_13, output_13):
  split_command = command_13.split()
  arguments = split_command[1:]
  if len(arguments) == 1:
    branch = arguments[0]
    result = dbmodels.TotalManagersAtBranch(branch).entity
    if result == output_13:
      return True
    else:
      return False
  else:
    return False

#-------------------------------------------------

#14
command_14 = '/find-most-borrowed-book-by-students-with SelfHelp'
output_14 = [{'title': 'I != Doll', 'COUNT(*)': 2}]
def unit_test_borrowed_students(command_14, output_14):
  split_command = command_14.split()
  arguments = split_command[1:]
  if len(arguments) == 1:
    genre = arguments[0]
    result = dbmodels.BorrowedByStudents(genre).entity
    if result == output_14:
      return True
    else:
      return False
  else:
    return False

#-------------------------------------------------
#15
command_15 = '/find-totalfacultystaff-who-has-researchpaper'
output_15 = [{'name': 'Lia', 'title': 'Coffee and its consumption: benefits and risks'}]
def unit_faculty_research_paper(command_15, output_15):
  split_command = command_15.split()
  arguments = split_command[1:]
  if len(arguments) == 0:
    result = dbmodels.FacultyResearchPaper().entity
    if result == output_15:
      return True
    else:
      return False
  else:
    return False

#-------------------------------------------------
#16
command_16 = '/find-publisher-with-most-registered-catalog'
output_16 = [{'publisherName': 'SOMU', 'COUNT(*)': 6}]
def unit_faculty_publisher_catalog(command_16, output_16):
  split_command = command_16.split()
  arguments = split_command[1:]
  if len(arguments) == 0:
    result = dbmodels.PublisherCatalog().entity
    if result == output_16:
      return True
    else:
      return False
  else:
    return False
#-------------------------------------------------
#17
command_17 = '/find-total-students-credited-in-researchpapers'
output_17 = [{'name': 'Somi', 'title': 'Sleep and human cognitive development'}]
def unit_faculty_research_student(command_17, output_17):
  split_command = command_17.split()
  arguments = split_command[1:]
  if len(arguments) == 0:
    result = dbmodels.StudentResearchPaper().entity
    if result == output_17:
      return True
    else:
      return False
  else:
    return False
#-------------------------------------------------
#18
command_18 = '/filter-catalog-author Chopra'
output_18 = [{'title': 'You are the universe'}]
def unit_test_filter_author(command_18, output_18):
  split_command = command_18.split()
  arguments = split_command[1:]
  if len(arguments) == 1:
    author = arguments[0]
    result = dbmodels.FilterAuthor(author).entity
    if result == output_18:
      return True
    else:
      return False
  else:
    return False

#-------------------------------------------------
#19
command_19 = '/sort-catalog-by-callnumber'
output_19 = [{'catalogID': 1, 'title': 'BTS V Vogue Korea Magazine 2022'}, {'catalogID': 2, 'title': 'ITZY Yeji Elle Korea Magazine 2023'}, {'catalogID': 3, 'title': 'DICON DFESTA SPECIAL 2022'}, {'catalogID': 11, 'title': 'Merriam-Webster'}, {'catalogID': 12, 'title': 'Oxford America'}, {'catalogID': 13, 'title': 'Princeton Language'}, {'catalogID': 123456, 'title': 'Love you twice ebook'}, {'catalogID': 2023013, 'title': 'Time to twice'}, {'catalogID': 20210404, 'title': 'Trust Me'}, {'catalogID': 20220311, 'title': "7llin' in our Youth"}, {'catalogID': 20220714, 'title': 'Celebrate'}, {'catalogID': 20221017, 'title': 'ANTIFRAGILE'}, {'catalogID': 20230501, 'title': 'Unforgiven'}, {'catalogID': 21432699, 'title': 'Coffee and its consumption: benefits and risks'}, {'catalogID': 31072562, 'title': 'The impact of sleep deprivation on declarative memory'}, {'catalogID': 33827030, 'title': 'Sleep and human cognitive development'}, {'catalogID': 62961381, 'title': 'Almond'}, {'catalogID': 307889157, 'title': 'You are the universe'}, {'catalogID': 310116376, 'title': 'Get Out of Your Head Study Guide'}, {'catalogID': 735211299, 'title': 'Atomic Habits'}, {'catalogID': 886825016, 'title': 'Those Who Walk Away From Omelas'}, {'catalogID': 999750410, 'title': "The Artist's Journey"}, {'catalogID': 1250326753, 'title': 'Beyond the story: 10-Year Record of BTS'}, {'catalogID': 1426372302, 'title': 'National Geographic Kids Animal Encyclopedia'}, {'catalogID': 1465462902, 'title': 'The Arts: A Visual Encyclopedia'}, {'catalogID': 1649374046, 'title': 'Fourth Wing'}, {'catalogID': 1649374178, 'title': 'Iron Flame'}, {'catalogID': 1735375123, 'title': 'love you twice'}, {'catalogID': 1735375888, 'title': 'I != Doll ebook'}, {'catalogID': 1780679804, 'title': 'I != Doll'}, {'catalogID': 1780679805, 'title': "Oh, the Places You'll Go!"}, {'catalogID': 1925811778, 'title': 'Plantopedia: The Definitive Guide to Houseplants'}]
def unit_test_sort_catalog(command_19, output_19):
  split_command = command_19.split()
  arguments = split_command[1:]
  if len(arguments) == 0:
    result = dbmodels.SortCatalog().entity
    if result == output_19:
      return True
    else:
      return False
  else:
    return False
#-------------------------------------------------
#20
command_20 = '/total-times-borrowed-book-from 1 20011008'
output_20 = [{'title': 'You are the universe'}]

def unit_test_total_borrows(command_20, output_20):
  split_command = command_20.split()
  arguments = split_command[1:]
  if len(arguments) == 2:
    branch = arguments[0]
    user_id = arguments[1]
    result = dbmodels.TotalTimesBorrowedByFrom(branch, user_id).entity
    if result == output_20:
      return True
    else:
      return False
  else:
    return False

#-------------------------------------------------
#Unit testings
#-------------------------------------------------

test_1 = unit_test_num_books_genre(command_1, output_1)
if test_1:
  print("Unit test for requirement #1: Pass")
else:
  print("Unit test for requirement #1: Failed")
#-------------------------------------------------

test_2 = unit_test_num_books_borrowed_by_at(command_2, output_2)
if test_2:
  print("Unit test for requirement #2: Pass")
else:
  print("Unit test for requirement #2: Failed")

#-------------------------------------------------
test_3 = unit_test_payment_by_user(command_3, output_3)
if test_3:
  print("Unit test for requirement #3: Pass")
else:
  print("Unit test for requirement #3: Failed")

#-------------------------------------------------
test_4 = unit_test_book_ebook_genre_author(command_4, output_4)
if test_4:
  print("Unit test for requirement #4: Pass")
else:
  print("Unit test for requirement #4: Failed")
#-------------------------------------------------
test_5 = unit_test_borrow_book(command_5, output_5)
if test_5:
  print("Unit test for requirement #5: Pass")
else:
  print("Unit test for requirement #5: Failed")
#-------------------------------------------------
test_6 = unit_test_borrow_expires(command_6, output_6)
if test_6:
  print("Unit test for requirement #6: Pass")
else:
  print("Unit test for requirement #6: Failed")

test_7 = unit_test_average_payment(command_7, output_7)
if test_7:
  print("Unit test for requirement #7: Pass")
else:
  print("Unit test for requirement #7: Failed")

test_8 = unit_test_find_book_borrowed(command_8, output_8)
if test_8:
  print("Unit test for requirement #8: Pass")
else:
  print("Unit test for requirement #8: Failed")

test_9 = unit_test_watched_credits(command_9, output_9)
if test_9:
  print("Unit test for requirement #9: Pass")
else:
  print("Unit test for requirement #9: Failed")

test_10 = unit_test_find_book_ebook(command_10, output_10)
if test_10:
  print("Unit test for requirement #10: Pass")
else:
  print("Unit test for requirement #10: Failed")

test_11 = unit_test_hold(command_11, output_11)
if test_11:
  print("Unit test for requirement #11: Pass")
else:
  print("Unit test for requirement #11: Failed")

test_12 = unit_book_research_paper(command_12, output_12)
if test_12:
  print("Unit test for requirement #12: Pass")
else:
  print("Unit test for requirement #12: Failed")
test_13 = unit_test_manager(command_13, output_13)
if test_13:
  print("Unit test for requirement #13: Pass")
else:
  print("Unit test for requirement #13: Failed")

test_14 = unit_test_borrowed_students(command_14, output_14)
if test_14:
  print("Unit test for requirement #14: Pass")
else:
  print("Unit test for requirement #14: Failed")

test_15 = unit_faculty_research_paper(command_15, output_15)
if test_15:
  print("Unit test for requirement #15: Pass")
else:
  print("Unit test for requirement #15: Failed")
test_16 = unit_faculty_publisher_catalog(command_16, output_16)
if test_16:
  print("Unit test for requirement #16: Pass")
else:
  print("Unit test for requirement #16: Failed")

test_17 = unit_faculty_research_student(command_17, output_17)
if test_17:
  print("Unit test for requirement #17: Pass")
else:
  print("Unit test for requirement #17: Failed")

test_18 = unit_test_filter_author(command_18, output_18)
if test_18:
  print("Unit test for requirement #18: Pass")
else:
  print("Unit test for requirement #18: Failed")

test_19 = unit_test_sort_catalog(command_19, output_19)
if test_19:
  print("Unit test for requirement #19: Pass")
else:
  print("Unit test for requirement #19: Failed")
test_20 = unit_test_total_borrows(command_20, output_20)
if test_20:
  print("Unit test for requirement #20: Pass")
else:
  print("Unit test for requirement #20: Failed")

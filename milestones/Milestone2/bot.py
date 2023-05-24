import bot_commands
import dbmodels

def BotResponse(msg):
  response_data = None  #Null
  msg_data = msg.split()
  bot_command = msg_data[0]
  arguments = msg_data[1:]

  if bot_command in bot_commands.SORT_CATALOG: #19
    if len(arguments) == 0:
      response_data = sorting_all_catalog()
    else:
      return "This command requires no arguments"
  elif bot_command in bot_commands.BORROWED_EXPIRES: #6
    if len(arguments) == 2:
      book = arguments[0]
      year = arguments[1]
      response_data = borrows_expires(book, year)
    else:
      return "This command requires 2 arguments, a bookID and a year."
  elif bot_command in bot_commands.PAYMENT_YEAR: #7
    if len(arguments) == 1:
      year = arguments[0]
      response_data = average_year_payment(year)
    else:
      return "This command requires 1 argumnet, a year"
  elif bot_command in bot_commands.NUM_BOOKS_BORROWED_BY_AT: #2
    if len(arguments) == 2:
      author = arguments[0]
      branch = arguments[1]
      response_data = num_books_borrowed_by_at(author, branch)
    else:
      return "This command requires 2 arguments, an author and a branch ID. \n Ex. /number-of-books-by Chopra 1"
  elif bot_command in bot_commands.TOTAL_MANAGERS_AT: #13
    if len(arguments) == 1:
      branch = arguments[0]
      response_data = total_managers_at_branch(branch)
    else:
      return "This command requires 1 argument, the branch ID"
  elif bot_command in bot_commands.COUNT_BORROWED_BY_USER_AT: #20
    if len(arguments) == 2:
      branch = arguments[0]
      user_id = arguments[1]
      response_data = count_borrowed_by_user_at_branch(branch, user_id)
    else:
      return "This command requires 2 arguments, the branch ID and the userID"
  elif bot_command in bot_commands.MOST_CATALOG_PUBLISHER:
    if len(arguments) == 0:
      response_data = most_publishers()
    else:
      return "This command requires no arguments"
  elif bot_command in bot_commands.PAYMENT_BY_USER_YEAR:
    if len(arguments) == 2:
      year = arguments[0]
      user_id = arguments[1]
      response_data = paymnet_by_user_year(year, user_id)
    else:
      return "This command requires 2 arguments, the year and the user id. \n Ex. /payments-by 2023 20000801"
  elif bot_command in bot_commands.NUM_BOOKS_GENRES: #1
    if len(arguments) == 2:
      genre_1 = arguments[0]
      genre_2 = arguments[1]
      response_data = num_books_genre(genre_1, genre_2)
    else:
      return "This command requires 2 arguments, the first genre and the second genre. \n Ex. /number-of-users-borrowed NewAge SelfHelp"
  elif bot_command in bot_commands.BORROWED_GENRE: #8
    if len(arguments) == 2:
      genre_1 = arguments[0]
      user = arguments[1]
      response_data = users_borrowed_genre(genre_1, user)
    else:
      return "This command requires 2 arguments, the genre and user name"
  elif bot_command in bot_commands.HOLD: #11
    if len(arguments) == 2:
      user = arguments[0]
      book_id = arguments[1]
      response_data = hold(user, book_id)
    else:
      return "This command requires 2 arguments, the user id and the book id"
  elif bot_command in bot_commands.FILTER_AUTHOR: #18
    if len(arguments) == 1:
      author = arguments[0]
      response_data = filter_catalog_author(author)
    else:
      return "This command requires 1 argument, the author's last name"
  elif bot_command in bot_commands.BORROW_BOOK: #5
    if len(arguments) == 3:
      user_id = arguments[0]
      book_id = arguments[1]
      branch_id = arguments[2]
      response_data = borrow_book(user_id, book_id, branch_id)
    else:
      return "This command needs 3 arguments, the user id, the book id and the branch id"
  elif bot_command in bot_commands.CATALOG_GENRE_AUTHOR:
    if len(arguments) == 2:
      genre = arguments[0]
      author = arguments[1]
      response_data = book_ebook_author_genre(genre, author)
    else:
      return "This command needs 2 arguments, the genre and the author. \n Ex. /books-ebooks SelfHelp Yunjin"
  elif bot_command in bot_commands.FIND_WATCHED_VIDEOS: #9
    if len(arguments) == 1:
      publisher = arguments[0]
      response_data = videos_watched(publisher)
    else:
      return "This command needs 1 argument, the publisher"
  elif bot_command in bot_commands.BOOK_EBOOK_AUTHOR_YEAR: #10
    if len(arguments) == 2:
      author = arguments[0]
      year = arguments[1]
      response_data = book_ebook_author_year(author, year)
    else:
      return "This command needs 2 arguments, the author and year"
  elif bot_command in bot_commands.BORROW_STUDENTS:
    if len(arguments) == 1:
      genre = arguments[0]
      response_data = borrowed_by_students(genre)
    else:
      return "This command needs 1 argument, the genre"
  elif bot_command in bot_commands.FACULTY_RESEARCH_PAPER:
    if len(arguments) == 0:
      response_data = faculty_reserach_paper()
    else:
      return "This command requires no arguments"
  elif bot_command in bot_commands.STUDENT_RESEARCH_PAPER:
    if len(arguments) == 0:
      response_data = student_reserach_paper()
    return "This command requires no arguments"
  elif bot_command in bot_commands.AUTHOR_RESERACH_PAPER:
    if len(arguments) == 0:
      response_data = author_paper()
    return "This command requires no arguments"
  if response_data:  #if response_data is not NULL
    return response_data
  return "No results found"


#--------------------------------------
#1
def num_books_genre(genre_1, genre_2):
  list_books = dbmodels.BorrowedGenres(genre_1, genre_2).entity
  if len(list_books) >= 1:
    response = "Borrowed Book Count: " + str(len(list_books)) + "\n Titles: \n"
    for i in range(len(list_books)):
      for value in list_books[i].values():
        response = response + value
      response += "\n"
  else:
    response = "No Books found"
  return response
#--------------------------------------
#2
def num_books_borrowed_by_at(author, branch):
  list_books = dbmodels.BorrowedBookBranch(author, branch).entity
  response = "Count: " + str(len(list_books)) + "\n Titles: \n"
  if len(list_books) > 0:
    for i in range(len(list_books)):
      for value in list_books[i].values():
        response = response + value
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#3
def paymnet_by_user_year(year, user_id):
  payments = dbmodels.PaymentByUser(year, user_id).entity
  response = ""
  if len(payments) > 0 :
    for i in range(len(payments)):
      for key, value in payments[i].items():
          response = response + str(key) +": "+ str(value) + " "
    response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#4
def book_ebook_author_genre(genre, author):
  catalog = dbmodels.BookEbookGenreAuthor(genre, author).entity
  response = ""
  if len(catalog) >= 1:
    response = "Titles: \n"
    for i in range(len(catalog)):
      for value in catalog[i].values():
        response = response + value
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#5
def borrow_book(user_id, book_id, branch_id):
  borrow_book = dbmodels.Borrow(user_id, book_id, branch_id).entity
  return borrow_book
#--------------------------------------
#6
def borrows_expires(book, year):
  borrow_table = dbmodels.BorrowExpires(book, year).entity
  response = ""
  if len(borrow_table) > 0:
    for value in borrow_table:
        response = response + str(value) + "\n"
    formatted = response.replace('{', '').replace('}','')
  else:
    formatted = "No results found"
  return formatted
#--------------------------------------
#7
def average_year_payment(year):
  payment_year = dbmodels.AveragePayment(year).entity
  response = "Average: "
  if len(payment_year) > 0:
    for i in range(len(payment_year)):
      for value in payment_year[i].values():
        response = response + str(value)
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#8
def users_borrowed_genre(genre_1, user_name):
  list_books = dbmodels.BorrowedUserGenre(genre_1, user_name).entity
  if len(list_books) >= 1:
    response = "Borrowed Book Count: " + str(len(list_books)) + "\n Titles: \n"
    for i in range(len(list_books)):
      for value in list_books[i].values():
        response = response + value
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#9
def videos_watched(publisher):
  videos = dbmodels.VideosWatched(publisher).entity
  response = ""
  count = len(videos)
  if(count >= 1):
    for i in range(len(videos)):
      for key, value in videos[i].items():
          response = response + str(key) +": "+ str(value) + " "
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#10
def book_ebook_author_year(author, year):
  catalog = dbmodels.BookEbookYearAuthor(author, year).entity
  response = ""
  count = len(catalog)
  if(count >= 1):
    response = "Count: " + str(len(catalog)) + "\n Titles: \n"
    for i in range(len(catalog)):
      for value in catalog[i].values():
        response = response + value
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#11
def hold(user, book_id):
  hold_book = dbmodels.ReserveBook(user, book_id).entity
  return hold_book
#--------------------------------------
#12
def author_paper():
  results = dbmodels.AuthorResearchPaper().entity
  total = len(results)
  if total > 0:
    response = "Count: " + str(total) + "\nTitles: \n"
    for i in range(len(results)):
      for value in results[i].values():
        response = response + str(value) 
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#13
def total_managers_at_branch(branch):
  managers = dbmodels.TotalManagersAtBranch(branch).entity
  num_managers = len(managers)
  response = ""
  if num_managers >= 1:
    response = "Total Managers: " + str(num_managers) + "\n Employee Names: \n"
    for i in range(len(managers)):
      for value in managers[i].values():
        response = response + value
      response += "\n"
  else:
    response = "Branch not found or there are no managers in this branch"
  return response
#--------------------------------------
#14
def borrowed_by_students(genre):
  catalog = dbmodels.BorrowedByStudents(genre).entity
  results = len(catalog)
  response = ""
 
  if(results == 1):
    dictionary_values = list((catalog[0].values()))

    response = "Catalog Title: " + str(dictionary_values[0]) + "\n"
    response = response + "Number of borrows: " + str(dictionary_values[1])
  else:
    response = "No results found"
  return response

#--------------------------------------
#15
def faculty_reserach_paper():
  catalog = dbmodels.FacultyResearchPaper().entity
  response = """Title Name\n"""
  if len(catalog) > 0:
    for i in range(len(catalog)):
      for value in catalog[i].values():
        response = response + str(value) + "|"
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#16
def most_publishers():
  catalog = dbmodels.PublisherCatalog().entity
  results = len(catalog)
  response = ""
 
  if(results == 1):
    dictionary_values = list((catalog[0].values()))

    response = "Publisher Name: " + str(dictionary_values[0]) + "\n"
    response = response + "Number of catalog: " + str(dictionary_values[1])
  else:
    response = "No results found"
  return response
#--------------------------------------
#17
def student_reserach_paper():
  catalog = dbmodels.StudentResearchPaper().entity
  response = """Title Name\n"""
  if len(catalog) > 1:
    for i in range(len(catalog)):
      for value in catalog[i].values():
        response = response + str(value) + "|"
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#18
def filter_catalog_author(author):
  catalog = dbmodels.FilterAuthor(author).entity
  results = len(catalog)
  response = ""
  if results >=1:
    response = "Titles: \n"
    for i in range(len(catalog)):
      for value in catalog[i].values():
        response = response + value
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#19
def sorting_all_catalog():
  catalog = dbmodels.SortCatalog().entity
  response = """Catalog ID Title\n"""
  if len(catalog) > 0:
    for i in range(len(catalog)):
      for value in catalog[i].values():
        response = response + str(value).zfill(10)
      response += "\n"
  else:
    response = "No results found"
  return response
#--------------------------------------
#20
def count_borrowed_by_user_at_branch(branch, user_id):
  titles = dbmodels.TotalTimesBorrowedByFrom(branch, user_id).entity
  count = len(titles)
  if count > 0:
    response = "Count: " + str(count) + "\n Titles: \n"
    for i in range(len(titles)):
      for value in titles[i].values():
        response = response + value
      response += "\n"
  else:
    response = "No results found"
  return response

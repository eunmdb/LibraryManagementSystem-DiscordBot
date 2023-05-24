# Your code to model your objects to handle the data from your database goes here.
from database import Database


#----------------------------------------
#1
class BorrowedGenres:

  def __init__(self, genre_1, genre_2):
    self.database = Database()
    self.genre_1 = genre_1
    self.genre_2 = genre_2
    self.entity = self.load()

  def load(self):
    query = """SELECT Entries.title AS "Book Title"
FROM Borrows 
JOIN Entries ON Borrows.BookBorrowed = Entries.entryID
JOIN RegisteredUser ON RegisteredUser.registeredUserID = Borrows.userIDBorrowed
JOIN Books ON Entries.entryID = Books.ISBN
JOIN Genre g1 ON Books.genre = g1.genreID
JOIN Genre g2 ON Books.genre2 = g2.genreID
WHERE (g1.genreType = %s OR g2.genreType = %s) AND (g1.genreType = %s OR g2.genreType = %s)"""
    arguments = (self.genre_1, self.genre_1, self.genre_2, self.genre_2)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#----------------------------------------
#2
class BorrowedBookBranch:

  def __init__(self, author, branch):
    self.database = Database()
    self.branch = branch
    self.author = author
    self.entity = self.load()

  def load(self):
    query = """SELECT Entries.title AS "Title"
FROM Borrows
JOIN Entries ON Entries.entryID = Borrows.bookBorrowed
JOIN Books ON Books.ISBN = Entries.entryID
WHERE Books.author = %s AND Borrows.borrowedBranch = %s """
    arguments = (self.author, self.branch)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#----------------------------------------
#3
class PaymentByUser:

  def __init__(self, year, user_id):
    self.database = Database()
    self.year = year
    self.user_id = user_id
    self.entity = self.load()

  def load(self):
    query = """SELECT BillingInfo.amount, RegisteredUser.name
FROM BillingInfo
JOIN RegisteredUser ON RegisteredUser.registeredUserID = BillingInfo.userBill
WHERE BillingInfo.year = %s AND BillingInfo.userBill = %s"""
    arguments = (self.year, self.user_id)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#----------------------------------------
#4
class BookEbookGenreAuthor:
  def __init__(self, genre, author):
    self.database = Database()
    self.genre = genre
    self.author = author
    self.entity = self.load()

  def load(self):
    query = """SELECT title FROM (
(SELECT Books.author authorName, Entries.title title, g1.genreType genre1, g2.genreType genre2
FROM Catalog
JOIN Books ON Catalog.catalogID = Books.ISBN
JOIN Entries ON Catalog.catalogID = Entries.entryID
JOIN Genre g1 ON Books.genre = g1.genreID
JOIN Genre g2 ON Books.genre2 = g2.genreID
)
UNION
(SELECT EBooks.author authorName, MultimediaContent.title title,  g1.genreType genre1, g2.genreType genre2
FROM Catalog
JOIN EBooks ON EBooks.ISBNEbook = Catalog.catalogID
JOIN MultimediaContent ON Catalog.catalogID = MultimediaContent.multimediaContentID
JOIN Genre g1 ON EBooks.genre = g1.genreID
JOIN Genre g2 ON EBooks.secondGenre = g2.genreID)
) catalogs
WHERE (catalogs.genre1 = %s OR catalogs.genre2 = %s) AND catalogs.authorName = %s"""
    arguments = (self.genre, self.genre, self.author)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#----------------------------------------
#5
class Borrow:
  def __init__(self, user, book_id, branch):
    self.database = Database()
    self.user = user
    self.book_id = book_id
    self.branch_id = branch
    self.entity = self.load()

  def load(self):
    query = """
    INSERT INTO Borrows (userIDBorrowed, bookBorrowed, borrowedBranch) VALUES (%s, %s, %s);
    """
    arguments = (self.user, self.book_id, self.branch_id)
    data = self.database.insert(query, arguments)
    return data
#----------------------------------------
#6
class BorrowExpires:

  def __init__(self, book, year):
    self.database = Database()
    self.book_id = book
    self.year = year
    self.entity = self.load()

  def load(self):
    query = """SELECT Entries.title AS "Title", RegisteredUser.name AS "Borrowed By"
FROM Borrows
JOIN Entries ON Entries.entryID = Borrows.bookBorrowed
JOIN RegisteredUser ON RegisteredUser.registeredUserID = Borrows.userIDBorrowed
JOIN libraryCard ON libraryCard.cardID = Borrows.userIDBorrowed
WHERE Entries.entryID = %s AND libraryCard.expiry = %s"""
    arguments = (self.book_id, self.year)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#----------------------------------------
#7
class AveragePayment:

  def __init__(self, year):
    self.database = Database()
    self.year = year
    self.entity = self.load()

  def load(self):
    query = """SELECT ROUND(AVG(amount),2) AS "Average" FROM BillingInfo WHERE year = %s;"""
    arguments = (self.year)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#--------------------------------------
#8
class BorrowedUserGenre:

  def __init__(self, genre_1, user_name):
    self.database = Database()
    self.genre_1 = genre_1
    self.user = user_name
    self.entity = self.load()

  def load(self):
    query = """SELECT Entries.title AS "Book Title"
FROM Borrows 
JOIN Entries ON Borrows.BookBorrowed = Entries.entryID
JOIN RegisteredUser ON RegisteredUser.registeredUserID = Borrows.userIDBorrowed
JOIN Books ON Entries.entryID = Books.ISBN
JOIN Genre g1 ON Books.genre = g1.genreID
JOIN Genre g2 ON Books.genre2 = g2.genreID
WHERE (g1.genreType = %s OR g2.genreType = %s) AND RegisteredUser.name = %s"""
    arguments = (self.genre_1, self.genre_1, self.user)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#--------------------------------------
#9
class VideosWatched:
  def __init__(self, publisher):
    self.database = Database()
    self.publisher = publisher
    self.entity = self.load()

  def load(self):
    query = """SELECT RegisteredUser.name, MultimediaContent.title
FROM Watched
JOIN RegisteredUser ON RegisteredUser.registeredUserID = Watched.userIDWatched
JOIN MultimediaContent ON MultimediaContent.multimediaContentID = Watched.videoWatched
JOIN Publisher ON Publisher.publisherID = Watched.videoCredits
WHERE Publisher.publisherName = %s"""
    arguments = (self.publisher)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#----------------------------------------
#10
class BookEbookYearAuthor:
  def __init__(self, author, year):
    self.database = Database()
    self.author = author
    self.year = year
    self.entity = self.load()

  def load(self):
    query = """SELECT title FROM (
(SELECT Books.author authorName, Entries.title title, Books.releasedYear ryear
FROM Catalog
JOIN Books ON Catalog.catalogID = Books.ISBN
JOIN Entries ON Catalog.catalogID = Entries.entryID)
UNION
(SELECT EBooks.author authorName, MultimediaContent.title title, EBooks.releasedYear ryear
FROM Catalog
JOIN EBooks ON EBooks.ISBNEbook = Catalog.catalogID
JOIN MultimediaContent ON Catalog.catalogID = MultimediaContent.multimediaContentID)
) catalogs
WHERE catalogs.authorName = %s AND catalogs.ryear = %s"""
    arguments = (self.author, self.year)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#----------------------------------------
#11
class ReserveBook:
  def __init__(self, user, book_id):
    self.database = Database()
    self.user = user
    self.book_id = book_id
    self.entity = self.load()

  def load(self):
    query = """
    INSERT INTO Holds (userHold, bookReservation) VALUES (%s, %s);
    """
    arguments = (self.user, self.book_id)
    data = self.database.insert(query, arguments)
    return data
#--------------------------------------
#12
class AuthorResearchPaper:
  def __init__(self):
    self.database = Database()
    self.entity = self.load()

  def load(self):
    query = """SELECT Entries.title
FROM Books
JOIN Entries ON Entries.entryID = Books.ISBN
WHERE Books.author IN (
	SELECT RegisteredUser.name authorName
	FROM ResearchPaper
	JOIN MultimediaContent ON ResearchPaper.PMID = MultimediaContent.multimediaContentID
	JOIN RegisteredUser ON RegisteredUser.registeredUserID = ResearchPaper.author
)"""
    data = self.database.selectNoArgs(query)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#--------------------------------------
#13
class TotalManagersAtBranch:

  def __init__(self, branch):
    self.database = Database()
    self.branch = branch
    self.entity = self.load()

  def load(self):
    query = """SELECT Employee.name AS "Employee Name:"
FROM Manager
JOIN Employee on Employee.employeeID = Manager.employeeID
WHERE Employee.branch = %s;"""
    arguments = (self.branch)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#--------------------------------------
#14
class BorrowedByStudents:
  def __init__(self, genre):
    self.database = Database()
    self.genre = genre
    self.entity = self.load()

  def load(self):
    query = """SELECT Entries.title, COUNT(*)
FROM Borrows
JOIN Entries ON Entries.entryID = Borrows.bookBorrowed
JOIN userAccount ON userAccount.accountID = Borrows.userIDBorrowed
JOIN Books ON Entries.entryID = Books.ISBN
JOIN Genre g1 ON Books.genre = g1.genreID
JOIN Genre g2 ON Books.genre2 = g2.genreID
JOIN Role ON userAccount.role = Role.role
WHERE Role.type = "Student" AND (g1.genreType = %s OR g2.genreType = %s)
GROUP BY title
LIMIT 1"""
    arguments = (self.genre, self.genre)
    data = self.database.select(query, arguments)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#--------------------------------------
#15
class FacultyResearchPaper:
  def __init__(self):
    self.database = Database()
    self.entity = self.load()

  def load(self):
    query = """SELECT RegisteredUser.name, MultimediaContent.title
FROM ResearchPaper
JOIN MultimediaContent ON MultimediaContent.multimediaContentID = ResearchPaper.PMID
JOIN RegisteredUser ON RegisteredUser.registeredUserID = ResearchPaper.author
JOIN userAccount ON userAccount.accountID = ResearchPaper.author
JOIN Role ON userAccount.role = Role.role
WHERE Role.type = "Faculty";"""
    data = self.database.selectNoArgs(query)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#--------------------------------------
#16
class PublisherCatalog:

  def __init__(self):
    self.database = Database()
    self.entity = self.load()

  def load(self):
    query = """SELECT publishers.publisherName, COUNT(*) FROM (
            (SELECT Publisher.publisherName , Entries.title
            FROM Catalog
            JOIN Entries ON Entries.entryID = Catalog.catalogID
            JOIN Publisher ON Publisher.publisherID = Entries.publisher) 
            UNION
            (SELECT Publisher.publisherName, MultimediaContent.title
            FROM Catalog
            JOIN MultimediaContent ON Catalog.catalogID = MultimediaContent.multimediaContentID
            JOIN Publisher ON Publisher.publisherID = MultimediaContent.multimediaPublisher) 
            ) AS publishers
            GROUP BY publisherName
            ORDER BY COUNT(*) DESC
            LIMIT 1"""
    data = self.database.selectNoArgs(query)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#--------------------------------------
#17
class StudentResearchPaper:
  def __init__(self):
    self.database = Database()
    self.entity = self.load()

  def load(self):
    query = """SELECT RegisteredUser.name, MultimediaContent.title
FROM ResearchPaper
JOIN MultimediaContent ON MultimediaContent.multimediaContentID = ResearchPaper.PMID
JOIN RegisteredUser ON RegisteredUser.registeredUserID = ResearchPaper.author
JOIN userAccount ON userAccount.accountID = ResearchPaper.author
JOIN Role ON userAccount.role = Role.role
WHERE Role.type = "Student";"""
    data = self.database.selectNoArgs(query)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#--------------------------------------
#18
class FilterAuthor:
  def __init__(self, author):
    self.database = Database()
    self.author = author
    self.entity = self.load()

  def load(self):
    query = """SELECT title FROM (
    (SELECT Books.author authorName, Entries.title title
    FROM Catalog
    JOIN Books ON Catalog.catalogID = Books.ISBN
    JOIN Entries ON Catalog.catalogID = Entries.entryID)
    UNION
    (SELECT EBooks.author authorName, MultimediaContent.title title
    FROM Catalog
    JOIN EBooks ON EBooks.ISBNEbook = Catalog.catalogID
    JOIN MultimediaContent ON Catalog.catalogID = MultimediaContent.multimediaContentID)
    ) catalogs
    WHERE catalogs.authorName = %s"""
    arguments = (self.author)
    data = self.database.select(query, arguments)

    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#--------------------------------------
#19
class SortCatalog:

  def __init__(self):
    self.database = Database()
    self.entity = self.load()

  def load(self):
    query = """(SELECT Catalog.catalogID , Entries.title FROM Catalog JOIN Entries ON Entries.entryID = Catalog.catalogID)
            UNION
            (SELECT Catalog.catalogID , MultimediaContent.title FROM Catalog JOIN MultimediaContent ON Catalog.catalogID = MultimediaContent.multimediaContentID)
            ORDER BY catalogID ASC"""
    data = self.database.selectNoArgs(query)
    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity
#--------------------------------------
#20
class TotalTimesBorrowedByFrom:

  def __init__(self, branch, user_id):
    self.database = Database()
    self.branch = branch
    self.user_id = user_id
    self.entity = self.load()

  def load(self):
    query = """SELECT Entries.title
FROM Borrows
JOIN Entries ON Entries.entryID = Borrows.bookBorrowed
WHERE Borrows.borrowedBranch = %s AND Borrows.userIDBorrowed = %s"""
    arguments = (self.branch, self.user_id)
    data = self.database.select(query, arguments)

    entity = []
    for i in range(len(data)):
      entity.append(data[i])
    return entity

-- Script name: inserts.sql
-- Author:      Eunice Borres
-- Purpose:     insert sample data to test the integrity of this database system
   
-- the database used to insert the data into.
USE librarymanagementdb;

-- Inserting into the general user table
INSERT INTO GeneralUser (Type) VALUES ("Patron"), ("Employee"), ("Manager");

-- Inserting into the library card table
INSERT INTO LibraryCard (LibraryCard, Expiry, Account_ID) VALUES 
(20011008, '2025-10-08', 1),  -- Yunjin
(20010309,'2025-03-09', 2), -- Somi
(20030809, '2025-08-09', 3), -- Kazuha
(20000801, '2025-08-01', 4), -- Chaewon
(19980319, '2025-03-19', 5),-- Sakura
(20061110, '2025-11-10', 6),-- Eunchae
(20000526, '2025-05-26', 7),-- Yeji
(20000721, '2025-07-21', 8),-- Lia
(20010417, '2025-04-17', 9),-- Ryujin
(20010605, '2025-06-05', 10),-- Chaeryeong
(20031209, '2025-12-09', 11);-- Yuna

-- Inserting into the account table
INSERT INTO Account (ID, Role, Email, Password, LibraryCard_LibraryCard) VALUES 
(1, 1, "huhyunjin@gmail.com", "jenaissante",20011008), -- Yunjin
(2, 1,"jeonsomi@gmail.com","somsomi0309", 20010309), -- Somi
(3, 1, "nakamurakazuha@gmail.com","k_a_z_u_h_a__",20030809),-- Kazuha
(4, 1, "kimchaewon@gmail.com", "_chaechae_1",20000801),-- Chaewon
(5, 1, "miyawakisakura@gmail.com", "39saku",19980319),-- Sakura
(6, 1, "hongeunchae@gmail.com", "hhh.e_c.v", 20061110),-- Eunchae
(7, 1,"hwangyeji@gmail.com","lightfury",20000526),-- Yeji
(8, 1, "choijisu@gmail.com", "julia07", 20000721),-- Lia
(9, 1, "shinryujin@gmail.com", "tuk04", 20010417),-- Ryujin
(10, 1, "leechaeryeong@gmail.com", "chaesis", 20010605),-- Chaeryeong
(11, 1, "shinyuna@gmail.com", "cabbit", 20031209);-- Yuna

-- Inserting into the registered users table
INSERT INTO RegisteredUsers (userID, Name, DOB, Address, Account_ID1, GeneralUser_Type) VALUES 
(1, "Yunjin Huh", '2001-10-08',"42 Hangang-daero, Yongsan-gu, Seoul, South Korea",1,"Patron"), -- Yunjin 
(5, "Sakura Miyawaki", '1998-03-19', "42 Hangang-daero, Yongsan-gu, Seoul, South Korea",1,"Patron"),-- Sakura
(4, "Chaewon Kim", '2000-08-01',  "42 Hangang-daero, Yongsan-gu, Seoul, South Korea",1,"Patron");-- Chaewon

-- Inserting into the student table
INSERT INTO Student (studentID, Name, Account_ID) VALUES 
(20010309, "Jeon Somi", 2), -- Somi
(20030809, "Kazuha Nakamura", 3),-- Kazuha
(20061110, "Eunchae Hong", 6);-- Eunchae

-- Inserting into the faculty table
INSERT INTO Faculty (facultyID, Name, Account_ID) VALUES
(20000526, "Yeji Hwang", 7),-- Yeji
(20000721, "Julia Choi", 8),-- Lia
(20010417, "Ryujin Shin", 9),-- Ryujin
(20010605, "Chaeryeong Lee", 10),-- Chaeryeong
(20031209, "Yuna Shin",11);-- Yuna

-- Inserting into the payment table
INSERT INTO Payment (transactionID, PaymentDate, Total, PaymentType, RegisteredUsers_userID) VALUES
(1, '2023-03-30', 15, "Debit Card", 1),
(2, '2023-03-31', 5, "Credit Card", 4),
(3, '2023-04-02', 10, "Debit Card", 5);

-- Inserting into Staff
INSERT INTO Staff(EmployeeID, Name, Type) VALUE
(19950922, "Nayeon Im", "Employee"),
(19951101, "Jeongyeon Yoo", "Employee"),
(19961109, "Momo Hirai", "Employee"),
(19961229, "Sana Minatozaki", "Employee"),
(19970201, "Jihyo Park", "Manager"),
(19970324, "Mina Myoui", "Manager"),
(19980528, "Dahyun Kim", "Manager"),
(19990423, "Chaeyoung Son", "Employee"),
(19990614, "Tzuyu Chou", "Employee" );

-- Inserting into Branch
INSERT INTO Branch (branchID, branchName) VALUES 
(1,"JYP"), -- JYP
(2, "Hybe"), -- HYBE
(3, "SM"); -- SM

-- Inserting into Employee
INSERT INTO Employees (EmployeeID, Name, BranchID) VALUES 
(19950922, "Nayeon Im", 1),
(19951101, "Jeongyeon Yoo", 1),
(19961109, "Momo Hirai", 2),
(19961229, "Sana Minatozaki", 2),
(19990423, "Chaeyoung Son", 3),
(19990614, "Tzuyu Chou", 3);

-- Inserting into Library Manager
INSERT INTO Manager (EmployeeID, Name, Branch) VALUES 
(19970201, "Jihyo Park", 1),
(19970324, "Mina Myoui", 2),
(19980528, "Dahyun Kim", 3);

-- Inserting into Catalog table
INSERT INTO Catalog (catalogID) VALUES 
(1), (2), (3),
(4), (5), (6),
(7), (8), (9),
(10), (11), (12),
(13), (14), (15),
(16), (17), (18),
(19), (20), (21),
(22), (23), (24);

-- Inserting into the GeneralUser_canBrowse_Catalog
INSERT INTO GeneralUser_canBrowse_Catalog (GeneralUser_Type, Catalog_catalogID) VALUES 
("Patron", 1), ("Employee", 1), ("Manager", 1),
("Patron", 2), ("Employee", 2), ("Manager", 2),
("Patron", 3), ("Employee", 3), ("Manager", 3);

-- Inserting into entries table
INSERT INTO Entries (entryID) VALUES 
(1), (2), (3),
(4), (5), (6),
(7), (8), (9),
(10), (11), (12);

-- Inserting books
INSERT INTO Book (ISBN, Title, Author, Genre, Availability, Description, PublishedDate) VALUES
(1, "You Are the Universe", "Deepak Chopra", "New Age",5, "You Are the Universe: is a philosophy book.", '2017-02-07'),
(2, "Atomic Habits", "James Clear", "Self-Help", 2, "Habit formation", '2018-10-16'),
(3, "The Artist's Journey", "Kent Nerburn", "Self-Help", 3, "Love letter to all artist", '2020-11-24');

-- Inerting encyclopedias
INSERT INTO Encyclopedia (encyclopediaID, Publisher, PublishingDate, Description, Title, CallNumber) VALUES 
(4, "DK Children", '2017-08-01', "Art Encyclopedia", "The Arts: A Visual Encyclopedia", 1104),
(5, "National Geographic", '2021-09-28', "Animal Encyclopedia", "Animal Planet" , 2312),
(6, "Smith Street Books", '2020-10-27', "Plantopedia", "Encyclopedia about house plants", 0423);

-- Inserting into Magazine
INSERT INTO Magazine (magazineID, Publisher, Title, CallNumber) VALUES 
(7, "Vogue", "Issue 1", 0323),
(8, "Elle", "Volume 3", 1220),
(9, "Dicon", "D'Festa", 127);

-- Inserting into thesaurus
INSERT INTO Thesaurus (thesaurusID, CallNumber, Publisher, Title) VALUES
(10, 123, "Merriam-Webster", "Merriam-Webster"),
(11, 456, "Oxford America", "Writer's Thesaurus"),
(12, 789, "Princeton Language", "Roget's 21st Century Thesaurus");

-- Inserting into multimedia content table
INSERT INTO MultimediaContent (multimediaContentID) VALUES
(13), (14), (15),
(16), (17), (18),
(19), (20), (21),
(22), (23), (24);

-- Inserting into music
INSERT INTO Music (musicID, Artist, Genre, PublishedDate, Producer, Language, Title) VALUES
(1, "LE SSERAFIM", "K-Pop", '2022-10-16', "HYBE", "Korean", "Antifragile"),
(2, "ITZY", "Pop", '2021-04-04', "JYP", "English", "Trust Me"),
(3, "TWICE", "Pop", '2022-07-14', "JYP", "Japanese", "Celebrate");

-- Inserting into video
INSERT INTO Videos (videoID, Credits, Genre, PublishedDate, Title) VALUES 
(4, "HYBE", "MV", '2022-10-16', "Antifragile MV"),
(5, "JYP", "Variety", '2023-01-13', "Time to twice"),
(6, "SM", "Show", '2022-03-11', "7llin' in our Youth");

-- Inserting into eBooks
INSERT INTO eBooks (eBookID, Publishers, Author) VALUES 
(7, "Harper Collins", "Le Guin"),
(8, "Harper Collins", "Manson"),
(9, "Harriman House", "Housel");

-- -- Insert into research paper
INSERT INTO ResearchPaper (PMID, Author, PublishedDate, Abstract, Publisher) VALUES 
(10, "Sultan", '2011-04-01', "Coffee is the leading worldwide beverage after water and its trade exceeds US $10 billion worldwide. Controversies regarding its benefits and risks still exist as reliable evidence is becoming available supporting its health promoting potential...", "UAF"),
(11, "Mason", '2021-03-13', "Emerging studies across learning domains have shed light on mechanisms underlying sleep's benefits during numerous developmental periods.", "UMASS"),
(12, "Cousins", '2019-03-21', "Sleep plays a crucial role in memory stabilization and integration, yet many people obtain insufficient sleep. ", "Duke");
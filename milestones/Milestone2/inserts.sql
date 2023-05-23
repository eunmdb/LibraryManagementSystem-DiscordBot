-- Script name: inserts.sql
-- Author:      Eunice Borres
-- Purpose:     insert sample data to test the integrity of this database system

USE librarymanagementdb;

INSERT INTO GeneralUser (userID) VALUES 
(19980319), -- Sakura
(20000801), -- Chaewon
(20011008), -- Yunjin
(20030809), -- Kazuha
(20061110), -- Eunchae
(19950922), -- Nayeon
(19951101), -- Jeongyeon
(19961109), -- Momo
(19961229), -- Sana
(19970201), -- Jihyo 
(19970324), -- Mina
(19980528), -- Dahyun
(19990423), -- Chaeyoung
(19990614), -- Tzuyu
(20000526), -- Yeji
(20000721), -- Lia
(20010417), -- Ryujin
(20010605), -- Chaeryeong
(20031209), -- Yuna
(20010309); -- Somi

INSERT INTO Role (role, type) VALUES (1,"Patron"),(2, "Employee"),(3, "Manager"),(4, "Student"), (5, "Faculty");

INSERT INTO RegisteredUser (registeredUserID, name) VALUES 
(19980319, "Sakura"), 
(20000801, "Chaewon"),
(20011008, "Yunjin"),
(20030809, "Kazuha"),
(20061110, "Eunchae "), 
(19950922, "Nayeon "),
(19951101, "Jeongyeon"),
(19961109, "Momo"),
(19961229, "Sana"),
(19970201, "Jihyo"),
(19970324, "Mina"),
(19980528, "Dahyun"),
(19990423, "Chaeyoung"),
(19990614, "Tzuyu"),
(20000526, "Yeji"),
(20000721, "Lia"),
(20010417, "Ryujin"),
(20010605, "Chaeryeong"),
(20031209, "Yuna"),
(20010309, "Somi");

INSERT INTO LibraryStaff (libraryStaffID) VALUES
(19950922), -- Nayeon
(19951101), -- Jeongyeon
(19961109), -- Momo
(19961229), -- Sana
(19970201), -- Jihyo
(19970324), -- Mina
(19980528), -- Dahyun
(19990423), -- Chaeyoung
(19990614); -- Tzuyu

INSERT INTO Organization (organizationID, organization) VALUES 
(1, "HYBE"),
(2, "SM"),
(3, "JYP"),
(4, "YG");

INSERT INTO LibraryBranch (branchID,branchName,organization) VALUES 
(1, "Bighit", 1),
(2, "Division3", 3),
(3, "NCT", 2);

INSERT INTO Employee (employeeID, name,branch, role, isManager) VALUES
(19950922, "Nayeon", 2, 2, 0), 
(19951101, "Jeongyeon", 2, 2, 0),
(19970201, "Jihyo", 2, 2, 2),
(19961109, "Momo", 1, 2, 0),
(19961229, "Sana", 1, 2, 0),
(19970324, "Mina", 1, 2, 1),
(19980528, "Dahyun", 3, 2, 3), 
(19990423, "Chaeyoung", 3, 2, 0),
(19990614, "Tzuyu", 3, 2, 0);

INSERT INTO Manager (employeeID,managerID) VALUES 
(19970201,2),
(19970324,1),
(19980528,3);

INSERT INTO libraryCard (cardID,expiry) VALUES
(19980319, 2028),
(20000801, 2030),
(20011008, 2031),
(20030809, 2033), 
(20061110, 2036),
(20000526, 2030),
(20000721, 2030),
(20010417, 2031),
(20010605, 2031),
(20031209, 2033),
(20010309, 2031);

INSERT INTO userAccount (accountID, email, password, libraryCard, role) VALUES 
(19980319, "miyawakisakura@gmail.com", "39saku",19980319, 1), -- Sakura
(20000801, "kimchaewon@gmail.com", "_chaechae_1",20000801,1), -- Chaewon
(20011008, "huhyunjin@gmail.com", "jenaissante",20011008, 1), -- Yunjin
(20030809, "nakamurakazuha@gmail.com","k_a_z_u_h_a__",20030809 ,1), -- Kazuha
(20061110, "hongeunchae@gmail.com", "hhh.e_c.v", 20061110, 1), -- Eunchae
(20000526, "hwangyeji@gmail.com","lightfury",20000526, 5),-- Yeji
(20000721, "choijisu@gmail.com", "julia07", 20000721, 5),-- Lia
(20010417, "shinryujin@gmail.com", "tuk04", 20010417, 5),-- Ryujin
(20010605, "leechaeryeong@gmail.com", "chaesis", 20010605, 4),-- Chaeryeong
(20031209, "shinyuna@gmail.com", "cabbit", 20031209, 4),-- Yuna
(20010309, "jeonsomi@gmail.com","somsomi0309",20010309, 4); -- Somi

INSERT INTO contentType (contentTypeID, contentType) VALUES
(1, "Book"), (2, "Encyclopedia"), (3, "Magazine"), (4, "Thesaurus"),
(5, "Music"), (6, "Videos"), (7, "Ebook"), (8, "Research Paper");

INSERT INTO Catalog (catalogID, catalogType) VALUES 
(0307889157, 1), (0735211299, 1), (0999750410, 1), 
(1649374046, 1), (1649374178, 1), (1250326753, 1),
(1780679805, 1), (1780679804,1),(1735375123, 1),
(1465462902, 2), (1426372302, 2), (1925811778, 2), 
(01, 3), (02, 3), (03, 3), (11, 4), (12, 4), (13, 4), 
(20221017, 5), (20210404, 5), (20220714, 5), 
(20230501, 6), (2023013, 6), (20220311, 6), 
(0886825016, 7), (0062961381, 7), (0310116376, 7), 
(1735375888, 7), (123456, 7), 
(21432699, 8), (33827030, 8), (31072562, 8);

INSERT INTO Actions (action, role, catalog) VALUES 
-- Patron
("Download", 1, 5),
("Download", 1, 6),
("Download", 1, 7),
("Borrow", 1, 1),
-- Employee and Managers
("Delete", 2, 1),
("Delete", 2, 1),
-- Students
("Borrow", 4, 1),
("Download", 4, 5),
("Download", 4, 6),
("Download", 4, 7),
("Download", 4, 8),
-- Faculty
("Borrow", 5, 1),
("Download", 5, 5),
("Download", 5, 6),
("Download", 5, 7),
("Download", 5, 8);

-- Student
INSERT INTO Student (studentID,name) VALUES 
(20010309, "Somi"),
(20010605, "Chaeryeong"),
(20031209, "Yuna");

-- Faculty
INSERT INTO Faculty (facultyID, name) VALUES
(20000526, "Yeji"), -- Yeji
(20000721, "Lia"), -- Lia
(20010417, "Ryujin"); -- Ryujin

INSERT INTO PaymentType (typeID, address, city, country, zipcode) VALUES
(1, "42 Hangang-daero", "Seoul", "Sourth Korea", 04389),
(2, "3731 Wilshire", "Los Angeles", "North America", 90010),
(3, "205, Gangdong-daero", "Seoul", "South Korea", 05407);

INSERT INTO BillingInfo (billingID, userBill, paymentType, amount, year) VALUES 
(1, 20011008, 1, 13.50, 2023),
(2, 20010605, 3, 5.23, 2023),
(3, 20010309, 2, 10.56, 2021),
(4, 20000801, 1, 2.31, 2023),
(5, 20031209, 3, 1.59, 2022),
(6, 20010417, 2, 7.40, 2022);

INSERT INTO CreditCard (cardNumber,paymentType,expiry,cvv) VALUES
(08102001, 1, '2025-08-01', 810),
(09032001, 2, '2026-09-03', 903),
(05062001, 3, '2024-05-06', 506);

INSERT INTO DebitCard (cardNumber,paymentType,expiry,cvv) VALUES 
(01082000, 1, '2025-08-10', 201),
(04172001, 2, '2024-04-17', 174),
(09122003, 3, '2027-09-12',129);

INSERT INTO MailingList (mailingListID, user) VALUES
(1, 20011008),
(2, 20010605),
(3, 20010417);

INSERT INTO Genre (genreID, genreType) VALUES 
(1, "NewAge"),
(2, "SelfHelp"),
(3, "HabitFormation"),
(4, "ScienceFiction"),
(5, "Fiction"),
(6, "Action"),
(7, "Adventure"),
(8, "Nonfiction"),
(9, "Biographical"),
(10, "Childrens"),
(11, "Fantasy"),
(12, "Historical"),
(13, "Philosophy"),
(14, "Science"),
(15, "Romance");


INSERT INTO Publisher (publisherID, publisherName) VALUES 
(1, "DK Children"),
(2, "National Geographic"),
(3, "Smith Street Books"),
(4, "Vogue"),
(5, "Elle"),
(6, "Dicon"),
(7, "Merriam-Webster"),
(8, "Oxford America"),
(9, "Princeton Language"),
(10, "UAF"),
(11, "UMASS"),
(12, "Duke"),
(13, "Harmony"),
(14, "Avery"),
(15, "Artist's Journey Press"),
(16, "SOMU"),
(17, "JYPD2"),
(18, "JYPD3"),
(19, "Entangled"),
(20, "Random House"),
(21, "Flatiron Books");

INSERT INTO Entries (entryID, title, publisher) VALUES
(0307889157, "You are the universe",13),
(0735211299, "Atomic Habits",14),
(0999750410, "The Artist's Journey",15),
(1649374046, "Fourth Wing", 19),
(1649374178, "Iron Flame", 19),
(1250326753, "Beyond the story: 10-Year Record of BTS", 21),
(1780679805, "Oh, the Places You'll Go!", 20),
(1780679804, "I != Doll", 16),
(1735375123, "love you twice", 16),
(1465462902, "The Arts: A Visual Encyclopedia",1),
(1426372302, "National Geographic Kids Animal Encyclopedia",2),
(1925811778, "Plantopedia: The Definitive Guide to Houseplants",3),
(01, "BTS V Vogue Korea Magazine 2022",4),
(02, "ITZY Yeji Elle Korea Magazine 2023",5),
(03, "DICON DFESTA SPECIAL 2022",6),
(11, "Merriam-Webster",7),
(12, "Oxford America",8),
(13, "Princeton Language",9);

INSERT INTO Books (ISBN, author, availability, genre, releasedYear, genre2) VALUES 
(0307889157, "Chopra", 5, 1,  2017 ,2),
(0735211299, "Clear", 3, 2,  2018, 1),
(0999750410, "Nerburn", 2, 3, 2019, 5),
(1649374046, "Yarros", 0, 11, 2023, 5),
(1649374178, "Yarros", 2, 11, 2023, 5),
(1780679805, "Seuss", 3, 5, 1990, 10),
(1250326753, "BTS", 1, 8, 2023, 9),
(1780679804, "Yunjin", 1, 2,2023, 5),
(1735375123, "Yunjin", 2, 2, 2023, 5);


INSERT INTO MultimediaContent(multimediaContentID, title, multimediaPublisher) VALUES
(20221017, "ANTIFRAGILE",16),
(20210404, "Trust Me",17),
(20220714, "Celebrate",18),
(20230501, "Unforgiven",16),
(2023013, "Time to twice",18),
(20220311, "7llin' in our Youth",18),
(0886825016, "Those Who Walk Away From Omelas",13),
(0062961381, "Almond",13),
(0310116376, "Get Out of Your Head Study Guide",14),
(1735375888, "I != Doll ebook", 16),
(123456, "Love you twice ebook", 16),
(21432699, "Coffee and its consumption: benefits and risks",10),
(33827030, "Sleep and human cognitive development",11),
(31072562, "The impact of sleep deprivation on declarative memory",12);

INSERT INTO Music (musicID, artist, releasedYear) VALUES 
(20221017, "LE SSERAFIM", 2022),
(20210404, "Itzy", 2021),
(20220714, "Twice", 2022);

INSERT INTO EBooks(ISBNEbook, author, genre, description, releasedYear, secondGenre) VALUES
(0886825016, "LeGuin", 4, "A 1973 work of short philosophical fiction by American writer Ursula K. Le Guin. With deliberately both vague and vivid descriptions, the narrator depicts a summer festival in the utopian city of Omelas, whose prosperity depends on the perpetual misery of a single child.",1973, 5),
(0062961381, "Won-pyung", 5, "This story is, in short, about a monster meeting another monster. One of the monsters is me.", 2021, 1),
(0310116376, "Allen", 2, "Freedom comes when we refuse to be victims to our thoughts", 2020,  5),
(1735375888, "Yunjin", 2, "Written by Huh Yunjin", 2023, 5),
(123456, "Yunjin", 2, "A letter for fearnot and lesserafim ", 2023, 5);

INSERT INTO Thesaurus (thesaurusISBN, releasedYear) VALUES
(11, 2020),
(12, 2019),
(13, 2021);

INSERT INTO Encyclopedia (encyclopediaISBN, releasedYear) VALUES
(1465462902, 2017),
(1426372302, 2021),
(1925811778, 2020);

INSERT INTO Magazine (magazineID, releasedYear) VALUES 
(01, 2022),
(02, 2023), 
(03, 2022);

INSERT INTO Holds (holdID, userHold, bookReservation) VALUES 
(1, 20061110, 0307889157),
(2, 20010309, 0307889157),
(3, 20030809, 0735211299);

INSERT INTO Videos (videoID, releasedYear) VALUES
(20230501,2023),
(2023013, 2023),
(20220311,2022);

INSERT INTO ResearchPaper (PMID,  abstract, releasedYear, author) VALUES
(21432699, "Coffee is the leading worldwide beverage after water and its trade exceeds US $10 billion worldwide. Controversies regarding its benefits and risks still exist as reliable evidence is becoming available supporting its health promoting potential", 2011, 20000721),
(33827030, "Emerging studies across learning domains have shed light on mechanisms underlying sleep's benefits during numerous developmental periods.", 2021, 20010309),
(31072562, "Sleep plays a crucial role in memory stabilization and integration, yet many people obtain insufficient sleep.", 2019, 20011008);

INSERT INTO Borrows (borrowID, userIDBorrowed, bookBorrowed, returned, borrowedBranch) VALUES
(1,20011008,0307889157,b'1', 1),
(2,20011008,0735211299,b'0', 2),
(3,20000801,0735211299,b'1',1),
(4,20010309,1780679804, b'0',1),
(5,20031209,1780679804 , b'1',3),
(6,20010309,1735375123, b'0',2);

INSERT INTO Patron (patronID, name) VALUES 
(19980319, "Sakura Miywaki"), -- Sakura
(20000801, "Kim Chaewon"), -- Chaewon
(20011008, "Yunjin Huh"), -- Yunjin
(20030809, "Kazuha Nakamura"), -- Kazuha
(20061110, "Eunchae Hong"); -- Eunchae

INSERT INTO Watched(watchID, userIDWatched, videoWatched, videoCredits) VALUES
(1,20011008, 20230501, 16),
(2,20000526, 20230501, 16),
(3,20011008, 20230501, 16),
(4,20010605, 20220311, 17),
(5,20030809, 20220311, 17);

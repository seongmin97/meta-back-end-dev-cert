-- Can you describe how you would set up three related tables: 
-- Books, Authors, and BorrowingRecords? 
-- Specifically, how would you define their primary and foreign keys 
-- to establish relationships between them?

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE BorrowingRecords (
    record_id INT PRIMARY KEY,
    book_id INT,
    borrower_id INT,
    borrowing_data DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (borrower_id) REFERENCES Borrowers(borrower_id)
);

SELECT Book.title, Author.name FROM Books JOIN Authors
ON Books.author_id = Authors.author_id;

SELECT * FROM Books WHERE publication_date > '2020-01-01';

SELECT * FROM BorrowingRecords JOIN Books ON BorrowingRecords.book_id = Books.book_id WHERE BorrowingRecords.borrower_id = 101;


INSERT INTO Books (book_id, title, author_id, publication_date) VALUES (4, 'The SQL Handbook', 3, '2023-03-15');
import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [books, setBooks] = useState([]);
  const [title,setTitle] = useState("");
  const [release_year, setRelease_year]= useState(0);


  useEffect(() => {
    fetchBooks();
  }, []);

  const fetchBooks = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/books/");
      const data = await response.json();
     // console.log(data);
      setBooks(data);  // Update state with fetched data
    } catch (error) {
      console.log(error);
    }
  };

  const addBook = async () => {
    const bookData={
      title,
      release_year
    };
    try {
      const response = await fetch("http://127.0.0.1:8000/api/books/create/", {
      method: "POST",
      headers:{
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(bookData),
    });
    const data = await response.json();
      setBooks((prev) => [...prev, data]);

    // console.log(data)
    } catch (error) {
      console.log(error)
    }


  };

  return (
    <>
      <h1>Books Website</h1>
      <div>
        <input 
        type="text" name="" id="" 
        placeholder="Book Title...." 
        onChange={(e) =>setTitle(e.target.value)}
        />

        <input 
        type="text" name="" id="" 
        placeholder="Release Year" 
        onChange={(e) => setRelease_year(e.target.value)}
        />
        <button onClick={addBook}> Add Book </button>
      </div>
      {books.map((book) => 
      <div>
        <p>Title: {book.title}</p>
        <p>Release year: {book.release_year} </p>
      </div>
      )}
      {/* <div>
        <h2>Books List</h2>
        {books.length > 0 ? (
          <ul>
            {books.map((book, index) => (
              <li key={index}>{book.title} ({book.release_date})</li>
            ))}
          </ul>
        ) : (
          <p>No books available</p>
        )}
      </div> */}
    </>
  );
}

export default App;

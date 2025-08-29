import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Books Website</h1>
      <div>
        <input type="text" name="" id="" placeholder='Book Title....'/>
        <input type="text" name="" id="" placeholder='Release Date'/>
        <button>Add Book</button>
      </div>
    </>
  )
}

export default App

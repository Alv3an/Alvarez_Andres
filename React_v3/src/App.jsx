
import './App.css'
import Header from './Components/Header/Header'
import CardPersonal from './Components/CardPersonal/CardPersonal'
import { useEffect, useState } from 'react'
import Pagination from '@mui/material/Pagination';

function App() {

  const [count, setCount] = useState(0);

  const [characters, setCharacters] = useState([]);


  useEffect(() => {
    fetch(`https://rickandmortyapi.com/api/character`)
      .then(response => response.json())
      .then(data => {
        setCharacters(data.results)
        setTotalPages(data.info.page)
      }
      )
  }, []);

  const handlePagination = (event, page) => {
    useEffect(() => {
      fetch(`https://rickandmortyapi.com/api/character/?page=${page}`)
        .then(response => response.json())
        .then(data => setCharacters(data.results))
    })
  }

  useEffect(() => {
    fetch('https://rickandmortyapi.com/api/character')
      .then(response => response.json())
      .then(data => setCharacters(data.results))
  })

  return (
    <>
      <Header />
      <main>
        {characters.map((item) => {
          return (<CardPersonal key={item.id} name={item.name} image={item.image} />
          )
        })}
      </main>
      <div id='pagination'>
        <Pagination onChange={handlePagination} count={10} variant="outlined" shape="rounded" />
      </div>
    </>
  )
}

export default App

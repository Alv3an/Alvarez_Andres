import { useEffect } from 'react'
import { useState } from 'react'
import './Header.css'
// import AppleIcon from '@mui/icons-material/Apple';

const Header = () => {

    const [contador, setContadot] = useState(0);

    useEffect(() => { setContadot(0) }, [])

    const handleContador = () => {
        setContadot(contador + 1);
    }

    useEffect(() => {
        console.log('El contador ha cambiado a: ' + contador)
    }, [contador])

    return (
        <header>
            {/* <AppleIcon sx={{ fontSize: "5rem", color: "blue" }} /> */}
            <h1>Ejercicio de React</h1>
            <p>Este es un ejemplo de una App</p>
            <div>
                {contador} Tarjetas
            </div>
            <div>
                <button id='boton' onClick={() => handleContador(contador + 1)}>Agregar Tarjeta</button>
            </div>
        </header>
    )
}

export default Header
import reactLogo from './assets/reactLogo.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function Soma(){
    return (10 + 20);
}

function App(){
    const soma = Soma();
    return (
        <h1>A soma é {soma} </h1>
    )
}

export default App

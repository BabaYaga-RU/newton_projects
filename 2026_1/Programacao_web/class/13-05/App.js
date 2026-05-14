import reactLogo from './assets/reactLogo.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function Soma(){
    return (10 + 20);
}
function Car(props){
    return (<h1>Meu carro é {props.modelo}</h1>);
}

function App(){
    const soma = Soma();
    return (
        <div>
            <h1>A soma é {soma} </h1>
            <Car modelo="Fusca"/>
            <Car modelo="Civic"/>
            <Car modelo="Mustang"/>
        </div>
    )
}
export default App

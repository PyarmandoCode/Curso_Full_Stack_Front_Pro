import React from "react";
import ReactDOM from "react-dom/client";//Manipular el Doom
//import Saludar from "./components/Saludar";
import Menu from "./components/Menu";
import Body from "./components/Body";
import Footer from "./components/Footer";
import 'bootstrap/dist/css/bootstrap.min.css';

const root = ReactDOM.createRoot(document.getElementById('root'))

root.render(
    //Fragment
    <>
        <Menu />
        <Body />
        <br></br>
        <Footer />

    </>)

import React, { useState, useEffect } from 'react';
import { CardTitle } from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';


const ApiComponent = () => {
    //Hooks
    const [movies, setMovies] = useState([]);
    const [error, setError] = useState(null);
    const [isLoaded, setIsLoaded] = useState(false);

    //Hooks es el primer componente a ejecutar
    useEffect(() => {
        async function cargarMoviesApi() {
            try {
                const headers = {'Authorization':'token fbeaa00e9f88976089912115efcadae4402c5be8'}
                const resp = await fetch('http://127.0.0.1:8000/api/List_All_Movies',{headers});
                const data = await resp.json();
                //Test para confirmar si se realizo la peticion al servicio
                //console.log(data);
                setIsLoaded(true);
                setMovies(data);
            } catch (error) {
                setIsLoaded(true);
                setError(error);
            }
        }
        cargarMoviesApi();
    },[])

    if (error) {
        return <>{error.messaje}</>
    }else if (!isLoaded) {
        return <>Estoy Preparando Todo!!!</>
    }else {
        return (
                <div className="container">
                    <div className="row">
                        {movies.map((item) =>(
                            <div className="col-md-4" key={item.movie_id}>
                                <Card style = {{width:'18rem'}}>
                                    <Card.Img variant='top' src={item.top} alt={CardTitle.title} />
                                    <Card.Body>
                                        <Card.Title> {item.title}</Card.Title>
                                        <Card.Text> {item.sipnosis}</Card.Text>
                                        <Button variant="primary">Ver Detalle</Button>
                                    </Card.Body>
                                
                                </Card>
                               </div> 
                        ))}
                    </div>
                </div>
        )
    }

    

}

export default ApiComponent;
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Row from 'react-bootstrap/Row';

import 'bootstrap/dist/css/bootstrap.min.css';

import React, { useState, useEffect } from 'react';
function Body() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        //Realizar una Solicitud a la Api
        fetch('https://api-cars-jb0r.onrender.com/autos')
            .then((response) => response.json())
            .then((data) => {
                setData(data.results);
                setLoading(false);
                console.log(data);
            })

            .catch((error) => console.error(error));
    }, []);

    return (
        <main>
            {loading ? (
                <h1>Cargando Data...</h1>
            ) : (

                <Row xs={1} md={2} className="g-4">
                    {data.map((item, index) => (
                        <Col key={index}>
                            <Card>
                                <Card.Img variant="top" src={item.imagen} />
                                <Card.Body>
                                    <Card.Title>{item.nombre}</Card.Title>
                                    <Card.Text>
                                       {item.detalle}
                                    </Card.Text>
                                </Card.Body>
                            </Card>
                        </Col>
                    ))}
                </Row>
            )}
        </main>
    );
}


export default Body;














// const images = [
//     'https://res.cloudinary.com/dream-music/image/upload/v1630280157/full_stack/python_jgr7oy.png',
//     'https://res.cloudinary.com/dream-music/image/upload/v1630280157/full_stack/python_jgr7oy.png',
//     'https://res.cloudinary.com/dream-music/image/upload/v1630280157/full_stack/python_jgr7oy.png',
// ]

// function Body() {
//     return (
//         <div>
//             <h2>Galeria de Imagenes</h2>
//             <div className='image-container'>
//                 {images.map((image, index) => (
//                     <img key={index} src={image} alt={index} width={400}>
//                     </img>
//                 ))}

//             </div>
//         </div>
//     )

// }

// export default Body;
import { Parallax } from 'react-parallax';
import './image.css'
import { Link } from 'react-router-dom';
import Ast2 from '../images/asteroid2.jpg'
const Image3 = () => (
    <Parallax className='image' bgImage= {Ast2} strength={800}>
        <div className= "content">
            <Link to='/predict'>
            <button className='img-btn'>Predict the diameter</button>
            </Link>
            
        </div>
    </Parallax>
);

export default Image3;
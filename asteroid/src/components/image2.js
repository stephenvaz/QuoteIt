import { Parallax } from 'react-parallax';
import './image.css'
import Ast1 from '../images/asteroid1.jpg'
import { Link } from 'react-router-dom';
const Image2 = () => (
    <Parallax className='image' bgImage= {Ast1} strength={800}>
        <div className= "content">
            <Link to='/chat'>
            <button className='img-btn'>Chat with fellow space heads</button>
            </Link>
        </div>
    </Parallax>
);

export default Image2;
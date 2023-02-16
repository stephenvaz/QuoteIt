import { Parallax } from 'react-parallax';
import './image.css'
import Nasa from '../images/nasa.jpg'
const Image1 = () => (
    <Parallax className='image' bgImage= {Nasa} strength={800}>
        <div className= "content">
            <span className='img-text'>A trip to space</span>
        </div>
    </Parallax>
);

export default Image1;
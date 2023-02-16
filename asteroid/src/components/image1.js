import { Parallax } from 'react-parallax';
import './image.css'
import artificial from '../images/artificial_intelligence.jpg'
const Image1 = () => (
    <Parallax className='image' bgImage= {artificial} strength={800}>
        <div className= "content">
            <span className='img-text'>Quotes that help you</span>
        </div>
    </Parallax>
);

export default Image1;
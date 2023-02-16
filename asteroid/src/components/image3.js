import { Parallax } from 'react-parallax';
import './image.css'
import { Link } from 'react-router-dom';
import analytics from '../images/analytics.jpg'
const Image3 = () => (
    <Parallax className='image' bgImage= {analytics} strength={800}>
        <div className= "content">
            <Link to='/predict'>
            <button className='img-btn'>Suggest me some good quotes</button>
            </Link>
            
        </div>
    </Parallax>
);

export default Image3;
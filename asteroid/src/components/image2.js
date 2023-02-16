import { Parallax } from 'react-parallax';
import './image.css'
// import datascience from '../images/data_science.jpg'
import datascience from '../images/data_science.jpg'
import { Link } from 'react-router-dom';
const Image2 = () => (
    <Parallax className='image' bgImage= {datascience} strength={800}>
        <div className= "content">
            <Link to='/predict'>
            <button className='img-btn'>Quotes recommendation</button>
            </Link>
        </div>
    </Parallax>
);

export default Image2;
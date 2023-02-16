import React, { useRef, useState } from 'react'
import {Card, Form, Button, Container} from 'react-bootstrap'
import { Link, useNavigate } from 'react-router-dom'
import{createUserWithEmailAndPassword, updateProfile} from 'firebase/auth'
import {auth} from '../firebase'

export default function Signup() {
    const navigate = useNavigate()
    const [values, setValues] = useState({
        name: "",
        email: "",
        pass: ""
    })
    const emailRef = useRef()
    const passwordRef = useRef()
    const nameRef = useRef()
    const [errorMsg, setErrorMsg]= useState('')
    const handleSubmission= () =>{
        console.log(values)

        createUserWithEmailAndPassword(auth, values.email, values.pass).then(async(res)=>{
            const user = res.user
            await updateProfile(user, {
                displayName: values.name,
            });
            console.log(user)
            navigate('/login')
        }).catch((err)=> {
            setErrorMsg(err.message)
            console.log("Error - ", err.message)
    
    })
    }
    
  return (
    <>
    <Container className="d-flex align-items-center justify-content-center" style={{minHeight: '100vh'}}>
        <div className='w-100' style={{maxWidth: '400px'}}>
        <Card>
            <Card.Body>
                <h2 className='text-center mb-4'>Sign Up</h2>
                <h6>{errorMsg}</h6>
                
                <Form>
                <Form.Group id ='text'>
                        <Form.Label>Name</Form.Label>
                        <Form.Control onChange={e => setValues((prev) => ({ ...prev, name: e.target.value}))}  type='text' ref = {nameRef} required />
                    </Form.Group>
                    <Form.Group id ='email'>
                        <Form.Label>Email</Form.Label>
                        <Form.Control onChange={e => setValues((prev) => ({ ...prev, email: e.target.value}))} type='email' ref = {emailRef} required />
                    </Form.Group>
                    <Form.Group id ='password'>
                        <Form.Label>Password</Form.Label>
                        <Form.Control onChange={e => setValues((prev) => ({ ...prev, pass: e.target.value}))} type='password' ref = {passwordRef} required />
                    </Form.Group>
                    {/* <Form.Group id ='password-confirm'>
                        <Form.Label>Password Conformation</Form.Label>
                        <Form.Control type='password' ref = {passwordConfirmRef} required />
                    </Form.Group> */}
                    <Button type="button" className='w-100 mt-2' onClick={handleSubmission}>Sign Up
                    </Button>
    
                </Form>
            </Card.Body>
        </Card>
        <div className='w-100 text-center mt-2'>
            Already have an account? <Link to="/login">Log In</Link> 
        </div>
        </div>
        </Container>
    </>
  )
}







// const passwordConfirmRef = useRef()
    // const {signup} = useAuth()
    // const [error, setError] = useState("")
    // const [loading, setLoading] = useState(false)

    // async function handleSubmit(e){
    //     e.preventDefault()

    //     if(passwordRef.current.value !==
    //         passwordConfirmRef.current.value){
    //             return setError('Passwords do not match')
    //         }
    //         try{
    //             setError('')
    //             setLoading(true)
    //            await signup(emailRef.current.value, passwordRef.current.value)
    //         }
    //         catch{
    //             setError('Failed to create an account')
    //         }
    //         setLoading(false)

    //     signup(emailRef.current.value, passwordRef.current.value)
    // }
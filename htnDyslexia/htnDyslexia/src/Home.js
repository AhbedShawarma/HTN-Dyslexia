import React, { Component } from 'react'
import Typing from 'react-typing-animation';
import "./App.css";

import { Link, animateScroll as scroll } from "react-scroll";

export class Home extends Component {
  render() {
    
    return (
        <div style={container1Style}>
            <div style={titleStyle}>
                <AnimatedTypingComponent/>
            </div>
        </div>
    );
  }
}

const AnimatedTypingComponent = () => (
  <Typing speed={75}>
    <span>Dslyxeia</span>
    <Typing.Delay ms={2000} />
    <Typing.Backspace count={10} speed={50}/>
    <Typing.Delay ms={500} />
    <Typing.Speed ms={50} />
    <span>Dyxsleai</span>
    <Typing.Delay ms={1500} />
    <Typing.Backspace count={10} speed={50}/>
    <Typing.Delay ms={500} />
    <span>Dyslexia</span>
    <Typing.Delay ms={2000} />
  </Typing>
)

const container1Style = {
    position: 'absolute',
    top: '0', 
    left: '0', 
    right: '0',
    bottom: '0',
    background: '#000',
    zIndex: '0',
    padding: '100px',
    backgroundColor: '#fff',
    height: '700px',
    textAlign: 'center',
    marginTop: '0'
  //marginTop: '0',
}

const titleStyle = {
  fontFamily: "IkarosR",
  fontSize: '100px',
  color: '#4A1942',
  textAlign: 'center',
  marginTop: '150px'

}

export default Home

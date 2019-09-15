import React, { Component } from 'react'
import "./App.css";

export class DyslexiaTest extends Component {
    render() {
        return (
            <div style={testStyle}>
                <h1>Here are some tests</h1>
                <p>The first test is:</p>
            </div>
        )
    }
}

const testStyle = {
    position: 'absolute',
    left: '0', 
    right: '0', 
    bottom: '0',
    background: '#DEC6D5',
    marginTop: '1000px',
    padding: '20px',
    color: '#fff',
    fontFamily: "IkarosL",
    fontSize: '50px',
    color: '#fff',
    textAlign: 'center',
    //height: '1000px',
    zIndex: 1
}

const titleStyle = {
    //position: 'absolute',

  }

  const pStyle = {
    fontFamily: "IkarosL",
    fontSize: '25px',
    color: '#fff',
    padding: '10px'
  }
export default DyslexiaTest

import React, { Component } from 'react'
import "./App.css";

export class testResults extends Component {
    render() {
        return (
            <div style={resultsStyle}>
                <h1>Here are your results</h1>
            </div>
        )
    }
}

const resultsStyle = {
    position: 'absolute',
    left: '0', 
    right: '0', 
    bottom: '0',
    background: '#fff',
    padding: '20px',
    color: '#fff',
    zIndex: 2
}

export default testResults

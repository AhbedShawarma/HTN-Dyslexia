import React, { Component } from "react";
import { Route, Switch, Redirect } from "react-router-dom";
import "./App.css";

import Home from './Home';
import DyslexiaTest from './DyslexiaTest';
import TestResults from './TestResults';
import Nav from './Nav';


//TODO Web Template Studio: Add routes for your new pages here.
class App extends Component {



  render() {
    
    return (
      <div className="App" style={{overflowX : 'auto'}}>
        
        <Home />
        <div style={{height: '2000px', background: '#DEC6D5', fontFamily: "IkarosL", fontSize: '50px', color: '#fff',  zIndex: 1}}>
          <p>v Take the Test v</p>
        </div>
      </div>
    );
  }
}


export default App;

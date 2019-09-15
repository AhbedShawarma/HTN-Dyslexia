import React, { Component } from "react";
import { Route, Switch, Redirect } from "react-router-dom";
import "./App.css";
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";

import Blank from "./components/Blank";
//TODO Web Template Studio: Add routes for your new pages here.
class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="AppHeader">
          <a>workn</a>
        </header>
      </div>
    );
  }
}

export default App;

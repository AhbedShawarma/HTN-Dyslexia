import React, { Component } from 'react'
import "./App.css";
import { Link, animateScroll as scroll } from "react-scroll";


export class Nav extends Component {
    render() {
        return (
            <nav className="nav" id="navbar">
        <div className="nav-content">
          <ul className="nav-items">
            <li className="nav-item">
              <Link
                activeClass="active"
                to="Home"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Home
              </Link>
            </li>
            <li className="nav-item">
              <Link
                activeClass="active"
                to="DyslexiaTest"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Take the Test
              </Link>
            </li>
            <li className="nav-item">
              <Link
                activeClass="active"
                to="TestResults"
                spy={true}
                smooth={true}
                offset={-70}
                duration={500}
              >
                Analytics
              </Link>
            </li>
            
          </ul>
        </div>
      </nav>
        )
    }
}

export default Nav

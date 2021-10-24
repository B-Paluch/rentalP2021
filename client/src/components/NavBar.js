import React, { Component } from "react";
import { Navbar, Nav } from "react-bootstrap";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import Home from "../Home";
import About from "../About";
import Contact from "../Contact";
import Register from "../Register";
import Login from "../Login";

export default class NavBar extends Component {
  linkStyle = {
    margin: "1rem",
    textDecoration: "none",
    color: "blue",
  };

  render() {
    return (
      <Router>
        <div>
          <Navbar class="navbar navbar-expand-lg navbar-light">
            <Navbar.Brand href="#">Serwis wypożyczeń</Navbar.Brand>
            <Navbar.Toggle aria-controls="navbarScroll" />
            <Navbar.Collapse id="navbarScroll">
              <Nav
                className="mr-auto my-2 my-lg-0"
                style={{ maxHeight: "100px" }}
                navbarScroll
              >
                <Nav.Link as={Link} to="/home">
                  Home
                </Nav.Link>
                <Nav.Link as={Link} to="/about">
                  About
                </Nav.Link>
                <Nav.Link as={Link} to="/contact">
                  Contact
                </Nav.Link>
              </Nav>
            </Navbar.Collapse>
            <form class="d-flex">
              <input
                class="form-control me-2"
                type="search"
                placeholder="Szukaj"
                aria-label="Search"
              />
              <button class="btn btn-outline-success" type="submit">
                Szukaj
              </button>
            </form>
            <div>
              <Link as={Link} to="/login">
                Zaloguj się
              </Link>
              <Link as={Link} to="/register">
                Zarejestruj się
              </Link>
            </div>
          </Navbar>
        </div>
        <div>
          <Switch>
            <Route path="/about">
              <About />
            </Route>
            <Route path="/contact">
              <Contact />
            </Route>
            <Route path="/register">
              <Register />
            </Route>
            <Route path="/login">
              <Login />
            </Route>
            <Route path="/">
              <Home />
            </Route>
          </Switch>
        </div>
      </Router>
    );
  }
}

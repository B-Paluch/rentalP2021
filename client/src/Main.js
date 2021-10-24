import React, { Component } from "react";
import { Route, NavLink, HashRouter } from "react-router-dom";
import Home from "./Home";
import About from "./About";
import Contact from "./Contact";
import NavBar from "./components/NavBar";

class Main extends Component {
  render() {
    return (
      <HashRouter>
        <div>
          <NavBar />
        </div>
      </HashRouter>
    );
  }
}
export default Main;

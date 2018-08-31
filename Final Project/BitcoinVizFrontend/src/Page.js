import React, { Component } from 'react';
import {Grid, Row, Col, MenuItem, Modal, Button, Navbar, Nav, NavItem, NavDropdown, Form, FormGroup, FormControl, InputGroup} from 'react-bootstrap';
import { BrowserRouter as Router, Route, Link} from "react-router-dom";

import Graph from "./Graph"

class Page extends Component {
  constructor(props) {
    super(props);
    this.state = {show: false, 
      loaded: true,
      nodes:[{id:"n1", label:"Alice", color:"#f63"}, {id:"n2", label:"Rabbit", color:"#06f"}],
      edges:[{id:"e1",source:"n1",target:"n2",label:"SEES"}],
      graph:"Spam Address" };
    this.search = this.search.bind(this);
    this.hideSearch = this.hideSearch.bind(this);
    this.renderNavbar = this.renderNavbar.bind(this);
  }

  search() {
    this.setState({show:true});
  }

  hideSearch() {
    this.setState({show:false, graph:"Spam Block"});
  }

  renderNavbar() {
    return ( 
          <Row>
            <Navbar inverse collapseOnSelect>
              <Navbar.Header>
                <Navbar.Brand>
                  <a href="#">BitcoinViz</a>
                </Navbar.Brand>
                <Navbar.Toggle />
              </Navbar.Header>
              <Navbar.Collapse>
                <Nav>
                  <NavItem><Link to="./">Home</Link></NavItem>
                  <NavDropdown title="Visualisations" id="basic-nav-dropdown">
                    <MenuItem><Link to="/SilkRoadBlock">Silk Road Block</Link></MenuItem> 
                    <MenuItem><Link to="/FBIAddress">FBI Address (Beta)</Link></MenuItem>
                    <MenuItem><Link to="/SpamAddress">Spam Address</Link></MenuItem>
                    <MenuItem><Link to="/SpamBlock">Spam Block</Link></MenuItem>
                    <MenuItem><Link to="/SpamBlock2">Spam Block 2</Link></MenuItem>
                    <MenuItem divider />
                    <MenuItem><Link to="/MyAddress">My Address</Link></MenuItem>
                  </NavDropdown>
                </Nav>
                <Nav pullRight>
                  <NavItem href="http://github.com/suryanash">by Surya Rastogi</NavItem>
                </Nav>
              </Navbar.Collapse>
            </Navbar>
          </Row> 
          )
  }

  render() {
    var msg;
    if(this.state.show){
      msg = (
        <div className="static-modal">
          <Row>
            <Modal.Dialog>
              <Modal.Footer>
                <Form componentClass="fieldset" horizontal>
                  <FormGroup>
                    <Col xs={9}>
                      <InputGroup>
                        <InputGroup.Addon>#</InputGroup.Addon>
                        <FormControl type="text" />
                      </InputGroup>
                      <FormControl.Feedback />
                    </Col>
                    <Col xs={3}>
                      <Button onClick={this.hideSearch} bsStyle="primary">Visualise</Button>
                    </Col>
                  </FormGroup>
                </Form>
              </Modal.Footer>
            </Modal.Dialog>
          </Row>
        </div>)
    } else {
      msg = (<div></div>)
    }
    return (
      <Router>
        <div>
          <Grid>
            {this.renderNavbar()}
            {msg}
            <Route exact path="/" render={() => (
              <Graph />
            )}/>
            <Route path="/SpamBlock" render={() => (
              <Graph graph="Spam Block" />
            )}/>
            <Route path="/SpamBlock2" render={() => (
              <Graph graph="Spam Block 2" />
            )}/>
            <Route path="/SpamAddress" render={() => (
              <Graph graph="Spam Address" />
            )}/>
            <Route path="/SilkRoadBlock" render={() => (
              <Graph graph="Silk Road Block" />
            )}/>
            <Route path="/FBIAddress" render={() => (
              <Graph graph="FBI Address" />
            )}/>
            <Route path="/MyAddress" render={() => (
              <Graph graph="My Address" />
            )}/>
          </Grid>
        </div>
      </Router>
    );
  }
}


export default Page;

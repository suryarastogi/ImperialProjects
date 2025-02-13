import React, { Component } from 'react';
import { Grid, Row, Col, MenuItem, Modal, Button, Navbar, Nav, NavItem, NavDropdown } from 'react-bootstrap';
import {Sigma, RandomizeNodePositions, RelativeSize} from 'react-sigma';

class Layout extends Component {
  render() {
    return (
      <div>
        <Grid>
          <Row>
            <Navbar inverse collapseOnSelect>
              <Navbar.Header>
                <Navbar.Brand>
                  <a href="#">{this.props.title}</a>
                </Navbar.Brand>
                <Navbar.Toggle />
              </Navbar.Header>
              <Navbar.Collapse>
                <Nav>
                  <NavItem eventKey={1} href="#">Link</NavItem>
                  <NavItem eventKey={2} href="#">Link</NavItem>
                  <NavDropdown eventKey={3} title="Dropdown" id="basic-nav-dropdown">
                    <MenuItem eventKey={3.1}>Action</MenuItem>
                    <MenuItem eventKey={3.2}>Another action</MenuItem>
                    <MenuItem eventKey={3.3}>Something else here</MenuItem>
                    <MenuItem divider />
                    <MenuItem eventKey={3.3}>Separated link</MenuItem>
                  </NavDropdown>
                </Nav>
                <Nav pullRight>
                  <NavItem eventKey={1} href="#">Link Right</NavItem>
                  <NavItem eventKey={2} href="#">Link Right</NavItem>
                </Nav>
              </Navbar.Collapse>
            </Navbar>
          </Row>
          {this.props.children}
        </Grid>
      </div>
    );
  }
}

export default Layout;

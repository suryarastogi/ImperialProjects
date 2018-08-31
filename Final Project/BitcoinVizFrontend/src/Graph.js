import React, { Component } from 'react';
import { Row, Jumbotron} from 'react-bootstrap';

import {Sigma, RelativeSize, LoadJSON} from 'react-sigma';

class Graph extends Component {
  render() {
  	var graph;
  	var text;
    var page = this.props.graph
    if(page == "Spam Address") {
      graph = (
        <Sigma style={{ "height": "75vw"}} setting={{drawLabels:false, maxNodeSize: 1, enableEdgeHovering:true}}>
          <LoadJSON path={String(process.env.PUBLIC_URL) + "./SpamAddress.json"}/>
          <RelativeSize initialSize={1000}/>
        </Sigma>)
      text = ( <h3>Spam Address: 1BV5dPBFNf7YjZoYwxQBSXkHRzJsGwTXrN</h3> )
    }
    else if (page == "Spam Block"){
      graph = (
        <Sigma style={{ "height": "75vw"}} setting={{drawLabels:false, maxNodeSize: 1, enableEdgeHovering:true}}>
          <LoadJSON path={String(process.env.PUBLIC_URL) + "/SpamBlock.json"}/>
          <RelativeSize initialSize={1000}/>
        </Sigma>)
      text = ( <h3>Block 364133: Spam Against the Network</h3> )
    }
    else if (page == "Silk Road Block"){
      graph = (
        <Sigma style={{ "height": "75vw"}} setting={{drawLabels:false, maxNodeSize: 1, enableEdgeHovering:true}}>
          <LoadJSON path={String(process.env.PUBLIC_URL) + "/SilkRoadBlock.json"}/>
          <RelativeSize initialSize={1000}/>
        </Sigma>);
      text = ( <h3>Block 261272: Silk Road Seizure</h3> )
    }
    else if (page == "Spam Block 2"){
      graph = (
        <Sigma style={{ "height": "75vw"}} setting={{drawLabels:false, maxNodeSize: 1, enableEdgeHovering:true}}>
          <LoadJSON path={String(process.env.PUBLIC_URL) + "/SpamBlock2.json"}/>
          <RelativeSize initialSize={1000}/>
        </Sigma>);
      text = ( <h3>Block 365150: Spam Block 2 </h3> )
    }
    else if (page == "FBI Address"){
      graph = (
        <Sigma style={{ "height": "75vw"}} setting={{drawLabels:false, maxNodeSize: 1, enableEdgeHovering:true}}>
          <LoadJSON path={String(process.env.PUBLIC_URL) + "/FBIAddress.json"}/>
          <RelativeSize initialSize={1000}/>
        </Sigma>);
      text = ( <h3>FBI Address: 1F1tAaz5x1HUXrCNLbtMDqcw6o5GNn4xqX</h3> )
    }
    else if (page == "My Address"){
      graph = (
        <Sigma style={{ "height": "75vw"}} >
          <LoadJSON path={String(process.env.PUBLIC_URL) + "/MyAddress.json"}/>
          <RelativeSize initialSize={15} />
        </Sigma>);
      text = ( <h3>My Address: 1GrMBnYfivEpVs1BHD3FDAzHUnM6WkriPF</h3> )
    }
    else {
      graph = (
        <Sigma style={{ "height": "75vw"}} setting={{drawLabels:false, maxNodeSize: 1, enableEdgeHovering:true}}>
          <LoadJSON path={String(process.env.PUBLIC_URL) + "/BlockViz154.json"}/>
          <RelativeSize initialSize={1000}/>
        </Sigma>)
      text = ( <h3>Block 458838: Recent Bitcoin Block</h3> )
    }

    
    return (
    	<div>
	    	<Row>
	          {text}
	        </Row>
	        <Row>
	        <Jumbotron>
	          {graph}
	        </Jumbotron>            
	        </Row>
        </div>    
      )
  }
}

export default Graph;

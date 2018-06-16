import React from 'react';
import {Table} from 'antd';
import {Link} from 'react-router-dom';
import axios from 'axios';
import G6 from '@antv/g6';
import * as d3 from 'd3';
import Header from '../../common/header/header';
import './style.css';

// var myRef = null;
class CompanyGraph extends React.Component {
  constructor(props) {
    super(props);
    this.myRef = React.createRef();
  }
  state = {
    loading: true,
    dataSource: {}
  };


  componentDidMount() {
    console.log(this.myRef);
    const this_ = this;
    window.addEventListener('resize', function() {

      this_.drawGraph(this_.state.dataSource)
    });

    axios('http://graphcompany.feiger.com.cn/api/showInvest?key=sdfsdfyhut478h654j').then(res => {

      if (res.status === 200) {
        // res.json().then((data) => {
          const data = res.data;
          console.log(data);
          const graphData = {
            nodes: [],
            links: []
          };
          data.success.results[0].data[0].graph.nodes.map((item, i) => {
            graphData.nodes.push(item)
          })
          data.success.results[0].data[0].graph.relationships.map((item, i) => {
            item.source = item.startNode;
            item.target = item.endNode;
            graphData.links.push(item)
          })



          // console.log(this.myRef)
          // this.drawGraph(graphData);

          this.setState({
            dataSource: graphData,
            loading: false,
          })

        // })
      }
    })
  }
  componentDidUpdate() {
    setTimeout(()=>{
      // myRef = this.myRef.current;
      console.log(this.myRef)
      if(this.myRef.current === null) return;
      this.drawGraph(this.state.dataSource)
    }, 0)


  }


  drawGraph = (graph) => {
    // this.myRef.current.removeChild(this.myRef.current.childNodes[0]);

    const canvas = this.myRef.current;
    const context = canvas.getContext("2d");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const width = canvas.width;
    const height = canvas.height;

    var simulation = d3.forceSimulation(graph.nodes)
      .force("link", d3.forceLink(graph.links).distance(50).id(function(d) {
        return d.id;
      }))
      .force("charge", d3.forceManyBody().distanceMax(200).distanceMin(20).strength(-80))
      .force("center", d3.forceCenter(width / 4, height / 2))
      .on("tick", ticked);

    // simulation
    //   .nodes(graph.nodes)
    //   .on("tick", ticked);
    //
    // simulation.force("link")
    //   .links(graph.links);

      d3.select(canvas)
        .call(d3.drag()
          .container(canvas)
          .subject(dragsubject)
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));


    d3.timeout(function(){
      for (var i = 0, n = Math.ceil(Math.log(simulation.alphaMin()) / Math.log(1 - simulation.alphaDecay())); i < n; ++i) {
        simulation.tick();
      }
      ticked()
    })




    function ticked() {
      context.clearRect(0, 0, width, height);

      context.beginPath();
      graph.links.forEach(drawLink);
      context.strokeStyle = "#aaa";
      context.stroke();

      context.beginPath();
      graph.nodes.forEach(drawNode);
      // context.fill();
      context.strokeStyle = "#fff";
      context.closePath();

    }

    function dragsubject() {
      return simulation.find(d3.event.x, d3.event.y);
    }

    function dragstarted() {
      if (!d3.event.active) simulation.alphaTarget(0.3).restart();
      d3.event.subject.fx = d3.event.subject.x;
      d3.event.subject.fy = d3.event.subject.y;
    }

    function dragged() {
      d3.event.subject.fx = d3.event.x;
      d3.event.subject.fy = d3.event.y;
    }

    function dragended() {
      if (!d3.event.active) simulation.alphaTarget(0);
      d3.event.subject.fx = d3.event.x;
      d3.event.subject.fy = d3.event.y;
    }

    function drawLink(d) {
      context.moveTo(d.source.x, d.source.y);
      context.lineTo(d.target.x, d.target.y);
    }

    function drawNode(d) {
      context.moveTo(d.x + 3, d.y);
      context.arc(d.x, d.y, 10, 0, 2 * Math.PI);
      if(d.labels[0] === 'Company'){
        context.fillStyle = "lightblue";
        context.strokeStyle = "lightblue";
      }else{
        context.strokeStyle = "brown";
        context.fillStyle = "brown";
      }
      context.fill();

    }

    // var color = d3.scaleOrdinal(d3.schemeCategory20);
    //
    // var svg = d3.select(this.myRef.current)
    //   .append('svg')
    //   .attr('width', window.innerWidth)
    //   .attr('height', window.innerHeight);
    //
    //
    // var simulation = d3.forceSimulation()
    //   .force("charge", d3.forceManyBody())
    //   .force("link", d3.forceLink().id(function(d) {
    //     return d.id
    //   }))
    //
    //   .force("center", d3.forceCenter(300, 300))
    //   // .force('collide', d3.forceCollide().radius(30))
    //
    //
    // var link = svg.append("g")
    //   .attr("class", "links")
    //   .selectAll("line")
    //   .data(graphData.links)
    //   .enter().append("line")
    //   .attr('stroke', '#ccc')
    //   .attr('text', 'ssss')
    //   .attr("stroke-width", function(d) {
    //     return Math.sqrt(d.value);
    //   });
    //
    // var text = svg.append('g')
    //   .attr('class', 'text')
    //   .selectAll('text')
    //   .data(graphData.links)
    //   .enter().append('text')
    //   .attr('dx', 0)
    //   .attr('dy', 0)
    //   .text('ssss')
    //
    //
    //
    // var node = svg.append("g")
    //   .attr("class", "nodes")
    //   .selectAll("circle")
    //   .data(graphData.nodes)
    //   .enter().append("circle")
    //   .attr("r", 5)
    //   .attr("fill", function(d) {
    //     return color(d.group);
    //   })
    //   .call(d3.drag()
    //     .on("start", dragstarted)
    //     .on("drag", dragged)
    //     .on("end", dragended));
    //
    //
    //
    //
    // simulation.nodes(graphData.nodes)
    //   .on("tick", function() {
    //     ticked(1)
    //   }, false);
    //
    // simulation.force("link")
    //   .links(graphData.links)
    //   .distance(20)
    //   .strength(1);
    //
    //
    // function ticked(scale) {
    //
    //
    //
    //   link
    //     .attr("x1", function(d) {
    //       return scale * d.source.x;
    //     })
    //     .attr("y1", function(d) {
    //       return scale * d.source.y;
    //     })
    //     .attr("x2", function(d) {
    //       return scale * d.target.x;
    //     })
    //     .attr("y2", function(d) {
    //       return scale * d.target.y;
    //     });
    //
    //   node
    //     .attr("cx", function(d) {
    //       return scale * d.x;
    //     })
    //     .attr("cy", function(d) {
    //       return scale * d.y;
    //     });
    //   text
    //     .style('fill', 'black')
    //     .attr('dx', function(d) {
    //       return (parseInt(scale * d.source.x) + parseInt(scale * d.target.x)) / 2
    //     })
    //     .attr('dy', function(d) {
    //       return (parseInt(scale * d.source.y) + parseInt(scale * d.target.y)) / 2
    //     })
    //
    // }
    //
    // function dragstarted(d) {
    //   if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    //   d.fx = d.x;
    //   d.fy = d.y;
    // }
    //
    // function dragged(d) {
    //   d.fx = d3.event.x;
    //   d.fy = d3.event.y;
    // }
    //
    // function dragended(d) {
    //   if (!d3.event.active) simulation.alphaTarget(0);
    //   d.fx = null;
    //   d.fy = null;
    // }
  }



  render() {
    console.log(this.state)
    if (Object.keys(this.state.dataSource).length === 0) {
      return null;
    }
    const {
      dataSource
    } = this.state;




    return (
      <div>
        <div  className = "eleCenter">
          <canvas ref = {this.myRef} > < /canvas>
        </div>
      </div >
    )
  }
}

export default CompanyGraph;

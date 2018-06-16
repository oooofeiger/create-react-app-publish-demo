import React from 'react';
import { Table } from 'antd';
import { Link } from 'react-router-dom';
import axios from 'axios';
import Header from '../../common/header/header';
import './style.css';


class CompanyList extends React.Component {
  state = {
    loading: true,
    dataSource: []
  };

  componentDidMount(){
    axios('http://graphcompany.feiger.com.cn/api/list?page_number=1').then(res=>{
      if(res.status === 200){
        // res.json().then((data)=>{
          const data = res.data;
          console.log(data);
          let formateData = [];
          for(let i = 0,len = data.length; i < len ; i++){
            formateData.push({
              key: i,
              name: data[i].name,
              type: data[i].type,
              scope: data[i].scope,
              establishTime: data[i].establishTime,
              conCapital: data[i].conCapital,
              regCapital: data[i].regCapital,
              status: data[i].status
            })
          }
          this.setState({
            dataSource: formateData,
            loading: false
          })
        // })
      }
    })
  }

  onChange = (pageNumber) => {
    console.log('Page: ', pageNumber);
  }


  render() {
    const pagination = {
      showQuickJumper : true,
      defaultCurrent : 1,
      total : this.state.dataSource.length,
      onChange : this.onChange
    }
    const columns = [{
      title: '公司名称',
      dataIndex: 'name'
    }, {
      title: '公司类型',
      dataIndex: 'type',
    }, {
      title: '实缴资本',
      dataIndex: 'conCapital',
    },{
      title: '注册资本',
      dataIndex: 'regCapital'
    }, {
      title: '经营范围',
      dataIndex: 'scope',
    }, {
      title: '成立日期',
      dataIndex: 'establishTime',
    }, {
      title: '经营状态',
      dataIndex: 'status',
    },{
      title: '操作',
      dataIndex: 'operation',
      key: 'operation',
      render: (text, record) => (
        <Link to={`/info?key=${record.key}`}>查看详情</Link>
      )
    }];
    console.log(this.state)
    return (
      <div>
        <Header />
        <div className="eleCenter">
          <div style={{ marginBottom: 16 }}></div>
          <Table size="default" loading={this.state.loading} bordered pagination={pagination}  columns={columns} dataSource={this.state.dataSource} />
        </div>
      </div>

    );
  }
}

export default CompanyList;

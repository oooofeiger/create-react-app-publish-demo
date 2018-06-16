import React from 'react';
import { Table } from 'antd';
import { Link } from 'react-router-dom';
import axios from 'axios';
import Header from '../../common/header/header';
import './style.css';


class CompanyInfo extends React.Component {
  state = {
    loading: true,
    dataSource: null
  };

  componentDidMount(){
    axios('http://localhost:3000/api/baseInfo?key=sdfsdfyhut478h654j').then(res=>{
      if(res.status === 200){
        // res.json().then((data)=>{
          const data = res.data;
          console.log(res);
          this.setState({
            dataSource: data,
            loading: false
          })
        // })
      }
    })
  }

  render() {
    console.log(this.state)
    if(this.state.dataSource === null){
      return null;
    }
    const { dataSource } = this.state;
    const { base, gudong, employ, branches } = dataSource;
    gudong.map((item, i) => {
      gudong[i]['key'] = i;
    })
    const gudongColumns = [{
      title: '序号',
      dataIndex: 'number'
    },{
      title: '姓名',
      dataIndex: 'name'
    },{
      title: '持股比例',
      dataIndex: 'rate'
    },{
      title: '认缴出资额(万元)',
      dataIndex: 'money'
    },{
      title: '认缴出资日期',
      dataIndex: 'date'
    }];

    employ.map((item, i) => {
      employ[i]['key'] = i;
    })
    const employColumns = [{
      title: '序号',
      dataIndex: 'number'
    },{
      title: '姓名',
      dataIndex: 'name'
    },{
      title: '职务',
      dataIndex: 'duty'
    }]

    branches.map((item, i) => {
      branches[i]['key'] = i;
    });
    const branchesColumns = [{
      title: '序号',
      dataIndex: 'number'
    },{
      title: '姓名',
      dataIndex: 'name'
    }]


    return (
      <div>
        <Header />
        <div className="eleCenter">
          <div style={{ marginBottom: 16 }}></div>
          <h3>工商信息</h3>
          <table className="table detailCon">
            <tbody>
            <tr>
              <td width="20%" className="th">公司名称：</td>
              <td width="30%">{base["公司名称"]}</td>
              <td width="20%" className="th">成立日期：</td>
              <td width="30%">{base["成立日期"]}</td>
            </tr>
            <tr>
              <td width="20%" className="th">公司类型：</td>
              <td width="30%">{base["公司类型"]}</td>
              <td width="20%" className="th">登记机关：</td>
              <td width="30%">{base["登记机关"]}</td>
            </tr>
            <tr>
              <td width="20%" className="th">曾用名：</td>
              <td width="30%">{base["曾用名"]}</td>
              <td width="20%" className="th">核准日期：</td>
              <td width="30%">{base["核准日期"]}</td>
            </tr>
            <tr>
              <td width="20%" className="th">实缴资本：</td>
              <td width="30%">{base["实缴资本"]}</td>
              <td width="20%" className="th">注册资本：</td>
              <td width="30%">{base["注册资本"]}</td>
            </tr>
            <tr>
              <td width="20%" className="th">法人：</td>
              <td width="30%">{base["法人"]}</td>
              <td width="20%" className="th">所属地区：</td>
              <td width="30%">{base["所属地区"]}</td>
            </tr>
            <tr>
              <td width="20%" className="th">注册号：</td>
              <td width="30%">{base["注册号"]}</td>
              <td width="20%" className="th">纳税人识别号：</td>
              <td width="30%">{base["纳税人识别号"]}</td>
            </tr>
            <tr>
              <td width="20%" className="th">统一社会信用代码：</td>
              <td width="30%">{base["统一社会信用代码"]}</td>
              <td width="20%" className="th">法人链接：</td>
              <td width="30%">{base["法人链接"]}</td>
            </tr>
            <tr>
              <td width="20%" className="th">英文名：</td>
              <td width="30%">{base["英文名"]}</td>
              <td width="20%" className="th">营业期限：</td>
              <td width="30%">{base["营业期限"]}</td>
            </tr>
            <tr>
              <td width="20%" className="th">人员规模：</td>
              <td width="30%">{base["人员规模"]}</td>
              <td width="20%" className="th">所属行业：</td>
              <td width="30%">{base["所属行业"]}</td>
            </tr>
            <tr>
              <td width="20%" className="th">经营方式：</td>
              <td width="30%">{base["经营方式"]}</td>
              <td width="20%" className="th">组织机构代码：</td>
              <td width="30%">{base["组织机构代码"]}</td>
            </tr>
            <tr>
              <td width="20%" className="th">经营状态：</td>
              <td width="30%">{base["经营状态"]}</td>
              <td width="20%" className="th">投资关系图谱：</td>
              <td width="30%"><Link to={`/graph?key=${base["公司名称"]}`}>点击查看</Link></td>
            </tr>
            <tr>
              <td width="30%" className="th">企业地址：</td>
              <td width="70%" colSpan={3}>{base["企业地址"]}</td>
            </tr>
            <tr>
              <td width="30%" className="th">经营范围：</td>
              <td width="70%" colSpan={3}>{base["经营范围"]}</td>
            </tr>
            </tbody>
          </table>
          <h3>股东信息</h3>
          <Table bordered pagination={false} className="gudongInfo" dataSource={gudong} columns={gudongColumns} />
          <h3>主要成员</h3>
          <Table bordered pagination={false} dataSource={employ} columns={employColumns} />
          <h3>分支机构</h3>
          <table width="100%" style={{marginBottom: '20px'}}>
            <tbody>
              <Branches data={branches}/>
            </tbody>
          </table>
        </div>
      </div>

    );
  }
}

const Branches = (props) => {
  const arr = [];
  for(let i = 0, len = Math.ceil(props.data.length/2); i < len ; i++){
    if(props.data[2*i+1] === undefined){
      arr.push(
        <tr key={i}>
          <td className='th' style={{textAlign:'center'}}>{2*i+1}</td>
          <td>{props.data[2*i].name}</td>
        </tr>
      )
    }else{
      arr.push(
        <tr key={i}>
          <td className='th' style={{textAlign:'center'}}>{2*i+1}</td>
          <td>{props.data[2*i].name}</td>
          <td className='th' style={{textAlign:'center'}}>{2*i+2}</td>
          <td>{props.data[2*i+1].name}</td>
        </tr>
      )
    }

}
  return arr
}


export default CompanyInfo;

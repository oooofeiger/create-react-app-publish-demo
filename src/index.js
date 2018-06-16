import React from 'react';
import ReactDOM from 'react-dom';
import { Switch, HashRouter as Router, Route} from 'react-router-dom';
import CompanyList from './components/companyList/companyList';
import CompanyInfo from './components/companyInfo/companyInfo';
import CompanyGraph from './components/companyGraph/companyGraph';
import registerServiceWorker from './registerServiceWorker';
import './common/common.css';

class App extends React.Component{
  render(){
    return (
      <Router>
        <div>
          <Route exact path="/" component={CompanyList}></Route>
          <Route path="/info" component={CompanyInfo}></Route>
          <Route path="/graph" component={CompanyGraph}></Route>
        </div>
      </Router>
    )
  }
}

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();

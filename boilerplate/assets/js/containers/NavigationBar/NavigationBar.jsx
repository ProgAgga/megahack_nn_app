import React from 'react';
import { Link } from 'react-router-dom';
import { Route, Redirect, Switch } from 'react-router';

import OrderManagment from '../mainComponent/OrderManagment/OrderManagment';
import CheckComponent from '../mainComponent/CheckComponent/CheckComponent';
import './NavigationBar.scss';

  const page3 = () => (
    <div>drop down</div>
  )

class NavigationBar extends React.Component {
    render() {
        return(
                <div className="baseContainer">
                    <div className="navBlock">
                        <div className="container">
                            <ul>
                                <Link to="/page1/">order managment</Link>
                            </ul>
                        </div>
                        <div className="container">
                            <ul>
                                <Link to="/page2/">check</Link>
                            </ul>
                        </div>
                        <div className="container">
                            <ul>
                                <div className="dropdown">
                                <span>settings</span>
                            <div className="dropdown-content">
                                <div><Link to="/page3/">Add source</Link></div>
                                <div><Link to="/page3/">Add offer</Link></div>
                                <div><Link to="/page3/">Add option</Link></div>
                            </div>
                            </div>
                            </ul>
                        </div>
                    </div>
                    <Switch>
                        <Route path="/page1/" component={OrderManagment} />
                        <Route path="/page2/" component={CheckComponent} />
                        <Route path="/page3/" component={page3} />
                        <Route path="/">
                            <Redirect to="/page1/" />
                        </Route>
                    </Switch>  
                </div>
        );
    }
}

export default NavigationBar;
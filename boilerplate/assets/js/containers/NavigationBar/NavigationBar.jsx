import React from 'react';
import { Link } from 'react-router-dom';

import './NavigationBar.scss';

class NavigationBar extends React.Component {
    render() {
        return(

            <div className="navBlock">
                <div className="container">
                    <ul>
                        <Link to="/orders">order managment</Link>
                    </ul>
                </div>
                <div className="container">
                    <ul>
                        <Link to="/check_offers">check</Link>
                    </ul>
                </div>
                <div className="container">
                    <ul>
                        <div className="dropdown">
                        <span>settings</span>
                    <div className="dropdown-content">
                      <div><Link to="/settings/sources">Add source</Link></div>
                      <div><Link to="/settings/offers">Add offer</Link></div>
                      <div><Link to="/settings/options">Add option</Link></div>
                    </div>
                    </div>
                    </ul>
                </div>
            </div>
        );
    }
}

export default NavigationBar;
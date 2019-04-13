import React from 'react';
import { Link } from 'react-router-dom';

import './NavigationBar.scss';

class NavigationBar extends React.Component {
    render() {
        return(
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
        );
    }
}

export default NavigationBar;
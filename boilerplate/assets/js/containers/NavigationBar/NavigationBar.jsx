import React from 'react';
import { Link } from 'react-router-dom';

import './NavigationBar.scss';

class NavigationBar extends React.Component {
    render() {
        return(
          
          //   <nav className="navbar navbar-default" role="navigation">
          //   <div className="container">
          //     <div className="collapse navbar-collapse" id="navbar-brand-centered">
          //       <ul className="nav navbar-nav">
          //         <li><Link to="/page1/">order managment</Link></li>
          //         <li><Link to="/page2/">check</Link></li>
          //         <li>
          //             <div className="dropdown">
          //                <span>settings</span>
          //               <div className="dropdown-content">
          //                   <div><Link to="/settings/sources">Add source</Link></div>
          //                   <div><Link to="/settings/offers">Add offer</Link></div>
          //                   <div><Link to="/settings/options">Add option</Link></div>
          //               </div>
          //            </div>
          //          </li>
          //       </ul>
          //     </div>
          //   </div>
          // </nav>

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
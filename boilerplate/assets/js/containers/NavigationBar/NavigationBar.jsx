import React from 'react';
import { Link } from 'react-router-dom';

import './NavigationBar.scss';

class NavigationBar extends React.Component {
    render() {
        return(
            // <nav class="navbar navbar-expand-lg navbar-light bg-light">
            // <a class="navbar-brand" href="#">Navbar</a>
            // <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            //     <span class="navbar-toggler-icon"></span>
            // </button>
            // <div class="collapse navbar-collapse" id="navbarNav">
            //     <ul class="navbar-nav">
            //         <li class="nav-item active">
            //             <Link to="/page1/">order managment</Link>
            //         </li>
            //         <li class="nav-item">
            //             <Link to="/page2/">check</Link>
            //         </li>
            //         <li class="nav-item dropdown">
            //             <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            //             Dropdown
            //             </a>
            //             <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            //             <a class="dropdown-item" href="#">Action</a>
            //             <a class="dropdown-item" href="#">Another action</a>
            //             <div class="dropdown-divider"></div>
            //             <a class="dropdown-item" href="#">Something else here</a>
            //             </div>
            //         </li>
            //     </ul>
            // </div>
            // </nav>
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
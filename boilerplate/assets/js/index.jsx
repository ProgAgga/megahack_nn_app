
import * as React from 'react'
import * as ReactDOM from 'react-dom';
import {BrowserRouter} from 'react-router-dom'

import App from './containers/App';
import {BrowserRouter} from "react-router-dom";

ReactDOM.render(
    <BrowserRouter>
        <App />
    </BrowserRouter>,
    document.getElementById('root')
);

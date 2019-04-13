import React from 'react';
import { Route, Redirect, Switch } from 'react-router';

import OrderManagment from './OrderManagment/OrderManagment';
import CheckComponent from './CheckComponent/CheckComponent';
import SettingsComponent from './SettingsComponent/SettingsComponent';


class MainComponent extends React.Component {
    render() {
        return(
            <>
                <Switch>
                        <Route path="/page1/" component={OrderManagment} />
                        <Route path="/page2/" component={CheckComponent} />
                        <Route path="/page3/" component={SettingsComponent} />
                        <Route path="/">
                            <Redirect to="/page1/" />
                        </Route>
                 </Switch> 
            </>
        );
    }
}

export default MainComponent;
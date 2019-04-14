import React from 'react';
import { Route, Redirect, Switch } from 'react-router';

import OrderManagment from './OrderManagment/OrderManagment';
import CheckComponent from './CheckComponent/CheckComponent';
import SettingsComponent from './SettingsComponent/SettingsComponent';
import SourcesContainer from "../SettingsSections/Sources/SourcesContainer";
import OffersContainer from "../SettingsSections/OffersSections/OffersContainer";


class MainComponent extends React.Component {
    render() {
        return(
            <>
                <Switch>
                        <Route exact path="/order/" component={OrderManagment} />
                        <Route exact path="/check_offers/" component={CheckComponent} />
                        <Route exact path="/settings/" component={SettingsComponent} />

                        <Route exact path="/settings/sources" component={SourcesContainer} />
                        <Route exact path="/settings/offers" component={OffersContainer} />
                        <Route exact path="/settings/options" component={SettingsComponent} />
                        <Route path="/">
                            <Redirect to="/order/" />
                        </Route>
                 </Switch> 
            </>
        );
    }
}

export default MainComponent;
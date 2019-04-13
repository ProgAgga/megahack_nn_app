import React from "react"
import {Switch, Route, Redirect} from 'react-router-dom'
import OrdersComp from "./OrdersComp";
import VerificationComp from "./VerificationComp";
import OffersComp from "./OffersComp";
import SourcesComp from "./SourcesComp";
import OptionsComp from "./OptionsComp";
export default class  Main extends React.Component{
    render() {
        return <main>
            <Switch>
                <Route exact path='/orders' component={OrdersComp}/>
                <Route exact path='/check_offer' component={VerificationComp}/>
                <Route exact path='/settings/offers' component={OffersComp}/>
                <Route exact path='/settings/sources' component={SourcesComp}/>
                <Route exact path='/settings/options' component={OptionsComp}/>
                <Route path='/' component={() => <Redirect to="/orders"/>}/>
                <Route/>
            </Switch>
        </main>
    }
}
import React from "react"

import MainComponent from '../containers/mainComponent/mainComponent';
import NavigationBar from './NavigationBar/NavigationBar'

export default class App extends React.Component{
    render(){
        return (
            <>
            <NavigationBar/>
            <MainComponent/>
            </>
        );
    }
}

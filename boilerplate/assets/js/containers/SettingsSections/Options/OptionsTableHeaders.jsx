import React from "react"


export default class OptionsTableHeaders extends React.Component{
    render(){
        return <div className="OffersHeaders">
            <div className="item">ID</div>
            <div className="item">Description</div>
            <div className="item">sources</div>
            <div className="item">column</div>
            <div className="item">value</div>
            <div className="item">operator</div>
        </div>
    }
}
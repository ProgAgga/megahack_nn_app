import React from "react"


export default class OfferListRow extends React.Component{
    constructor(props){
        super(props);
    }
    render() {
        return <div className="container">
            <div className="id">{this.props.id}</div>
            <div className="name">{this.props.name}</div>
            <div className="due_date">{this.props.due_date}</div>
            <div className="options">{this.props.options}</div>
        </div>
    }
}
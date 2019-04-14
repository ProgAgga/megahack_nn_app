import * as React from "react";

import "./style.scss";

export default class OffersTableRows extends React.Component{
    constructor(props){
        super(props);
        this.data = props.data;
    }
    render(){
        return <div className="OffersTablecontainer">
            {
                this.props.data.map(
                    (source,i) => (
                        <div className="OffersRow" key={i}>
                            <div className="item">{source.id}</div>
                            <div className="item">{source.name}</div>
                            <div className="item">{source.due_date}</div>
                            <div className="item">{source.options}</div>
                        </div>
                    )
                )
            }
        </div>
    }
}
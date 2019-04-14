import * as React from "react";

import "./style.scss";

export default class SourcesTableRows extends React.Component{
    constructor(props){
        super(props);
        this.data = props.data;
    }
    render(){
        return <div className="SourceTablecontainer">
            {
                this.props.data.map(
                    (source,i) => (
                        <div className="row" key={i}>
                            <div className="item">{source.id}</div>
                            <div className="item">{source.name}</div>
                            <div className="item">{source.host}</div>
                            <div className="item">{source.port}</div>
                            <div className="item">{source.username}</div>
                            <div className="item">{source.password}</div>
                            <div className="item">{source.type}</div>
                            <div className="item">{source.database}</div>
                        </div>
                    )
                )
            }
            </div>
    }
}
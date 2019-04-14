import * as React from "react";
import {URL_DEALERS} from "../../Constants/Urls";


export default class DealerCheckBox extends React.Component{
    constructor(props){
        super(props);

        this.state = {
            dealers : []
        }
    }
    componentDidMount() {
        fetch(URL_DEALERS).then(
            response => response.json()
        ).then(
            dealers => this.setState({
                dealers : dealers
            })
        )
    }

    render(){
        return   <>
        {this.state.dealers?
            this.state.dealers.map(
                (elem,i) => <div key={i}><label>{elem.name}</label><input type="checkbox" name={elem.id} label={elem.name} onChange={this.props.handleChange}/></div>
                    ):""}
        </>
    }

}
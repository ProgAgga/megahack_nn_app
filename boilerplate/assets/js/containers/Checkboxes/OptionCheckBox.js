import * as React from "react";
import {URL_DEALERS, URL_OPTIONS} from "../../Constants/Urls";


export default class OptionCheckBox extends React.Component{
    constructor(props){
        super(props);

        this.state = {
            options : []
        }
    }
    componentDidMount() {
        fetch(URL_OPTIONS).then(
            response => response.json()
        ).then(
            options => this.setState({
                options : options
            })
        )
    }

    render(){
        return   <>
            {this.state.options?
                this.state.options.map(
                    elem => <div key={elem.description}><label>{elem.description}</label><input type="checkbox" name={elem.id} label={elem.description} onChange={this.props.handleChange}/></div>
                ):""}
        </>
    }

}
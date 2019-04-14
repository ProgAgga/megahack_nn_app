import React from "react";
import {URL_SOURCES} from "../../../Constants/Urls";
import {ADD_NEW_SOURCE_BODY} from "../../../helpers/RequestBodies";

export default class NewSourcesForm extends React.Component {
    constructor () {
        super();
        this.state = {
            name: '',
            host: '',
            port: '',
            username: '',
            password: '',
            type: '',
            database: '',
        };
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange (evt) {
        this.setState({ [evt.target.name]: evt.target.value });
    }
    sendRequest(){
        fetch(
            URL_SOURCES,
            ADD_NEW_SOURCE_BODY(this.state)
        ).then(
            response => {
                window.location.reload()
                // console.log(response); //FOR DEBUG ;)))
            }
        )
    }
    render () {
        return (
            <>
            <form className="formBlock">
                <label>name</label>
                <input type="text" name="name" onChange={this.handleChange} />
                <label>host</label>
                <input type="text" name="host" onChange={this.handleChange} />
                <label>port</label>
                <input type="text" name="port" onChange={this.handleChange} />
                <label>username</label>
                <input type="text" name="username" onChange={this.handleChange} />
                <label>password</label>
                <input type="text" name="password" onChange={this.handleChange} />
                <label>type</label>
                <input type="text" name="type" onChange={this.handleChange} />
                <label>database</label>
                <input type="text" name="database" onChange={this.handleChange} />
            </form>
                <button onClick={() => this.sendRequest()}>submit</button>
            </>
                );
    }
}

//window.location.reload()
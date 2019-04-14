import React from "react";
import {URL_OFFERS} from "../../../Constants/Urls";
import {ADD_NEW_OFFER_BODY} from "../../../helpers/RequestBodies";
import DealerCheckBox from "../../Checkboxes/DealerCheckBox";
import OptionCheckBox from "../../Checkboxes/OptionCheckBox";



export default class NewOffersForm extends React.Component{
    constructor () {
        super();
        this.state = {
            name: '',
            due_date: '',
            dealers:{},
            options:{}
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleChangeDealer = this.handleChangeDealer.bind(this);
        this.handleChangeOption = this.handleChangeOption.bind(this);
    }

    handleChange (evt) {
        this.setState({ [evt.target.name]: evt.target.value });
    }
    handleChangeDealer(e) {
        const item = e.target.name;
        const isChecked = e.target.checked;
        console.log(item);
        console.log(isChecked);
        this.setState(prevState => {
            console.log(prevState);
            prevState.dealers[item] = isChecked;
            return prevState;
        });
    }
    handleChangeOption(e) {
        const item = e.target.name;
        const isChecked = e.target.checked;

        this.setState(prevState => {
            console.log(prevState);
            prevState.options[item] = isChecked;
            return prevState;
        });
    }
    sendRequest(){
        console.log(ADD_NEW_OFFER_BODY(this.state));
        fetch(
            URL_OFFERS,
            ADD_NEW_OFFER_BODY(this.state)
        ).then(
            response => {
                // console.log(response);
                window.location.reload()
            }
        )
    }
    render () {
        return (
            <>
                <form>
                    <label>name</label>
                    <input type="text" name="name" onChange={this.handleChange} />
                    <label>due date</label>
                    <input type="date" name="due_date" onChange={this.handleChange} />
                    <label>Dealers</label>
                    <DealerCheckBox handleChange={(e) => this.handleChangeDealer(e)}/>
                    <label>options</label>
                    <OptionCheckBox handleChange={(e) => this.handleChangeOption(e)}/>
                </form>
                <button onClick={() => this.sendRequest()}>submit</button>
            </>
        );
    }
}
import * as React from "react";
import {URL_OPTIONS} from "../../../Constants/Urls";
import ModalCaller from "../OffersSections/OffersContainer";
import LoadingComp from "../common/LoadingComp";


export default class OptionsContainer extends React.Component{
    constructor(props){
        super(props);

        this.state = {
            options : []
        }
    }

    componentDidMount() {
        fetch(URL_OPTIONS)
            .then(
                response => response.json()

            ).then(
                options => this.setState(
                    {
                        options: options
                    }
                )
        )
    }

    render(){


        return <div className="OptionsContainer">
            <div className="row">
                <div className="callCreator">
                    <ModalCaller>
                        <NewOptionsForm/>
                    </ModalCaller>
                </div>
            </div>
            <OptionsTableHeaders/>
            {
                this.state.options ?
                    <OptionsTableRows data={this.state.option}/>
                    : <LoadingComp/>
            }
        </div>


    }

}
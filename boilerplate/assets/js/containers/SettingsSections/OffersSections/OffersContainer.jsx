import * as React from "react";
import {URL_OFFERS} from "../../../Constants/Urls";
import LoadingComp from "../common/LoadingComp";

import "../Sources/style.scss";
import ModalCaller from "../common/ModalCaller";
import OffersTableHeaders from "./OffersTableHeaders";
import OffersTableRows from "./OffersTableRows";
import NewOffersForm from "./NewOffersForm";

export default class SourcesContainer extends React.Component{
    constructor(props){

        super(props);
        this.state = {
            offers: []
        }

    }

    componentDidMount() {
        fetch(URL_OFFERS).then(
            raw_response => raw_response.json()
        ).then(
            response => this.setState({
                offers: response
            })
        )
    }

    render() {
        return <div className="offersContainer">
            <div className="row">
                <div className="callCreator">
                    <ModalCaller>
                        <NewOffersForm/>
                    </ModalCaller>
                </div>
            </div>
            <OffersTableHeaders/>
            {
                this.state.offers ?
                    <OffersTableRows data={this.state.offers}/>
                    : <LoadingComp/>
            }
        </div>
    }
}
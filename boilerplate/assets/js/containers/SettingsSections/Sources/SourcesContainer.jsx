import * as React from "react";
import {URL_SOURCES} from "../../../Constants/Urls";
import SourcesTableHeaders from "./SourcesTableHeaders";
import LoadingComp from "../common/LoadingComp";
import SourcesTableRows from "./SourcesTableRows";

import "./style.scss";
import ModalCaller from "../common/ModalCaller";
import NewSourcesForm from "./NewSourcesForm";

export default class SourcesContainer extends React.Component{
    constructor(props){

        super(props);
        this.state = {
            sources: []
        }

    }

    componentDidMount() {
        fetch(URL_SOURCES).then(
            raw_response => raw_response.json()
        ).then(
            response => this.setState({
                sources: response
            })
        )
    }

    render() {
        return <div className="sourceContainer">
                <div className="row">
                    <div className="callCreator">
                        <ModalCaller>
                            <NewSourcesForm/>
                        </ModalCaller>
                    </div>
                </div>
            <div className="Table">   
                <SourcesTableHeaders/>
            {
                this.state.sources ?
                    <SourcesTableRows data={this.state.sources}/>
                    : <LoadingComp/>
            }
            </div>
            </div>
    }
}
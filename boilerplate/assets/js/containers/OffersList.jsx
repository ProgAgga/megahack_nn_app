import React from "react"
import OffersListHeader from "./OffersListHeader";
import OfferListRow from "./OfferListRow";


export default class OffersList extends React.Component{
    constructor(props) {
        super(props);
        this.offers = this.props.offers;
        console.log(this.props)
    }



    render(){
        console.log(this.offers);
        return <>
            <OffersListHeader />
            {/*{JSON.parse(data["offers"])}*/}
            {/*{this.offers}*/}
        </>
    }
}
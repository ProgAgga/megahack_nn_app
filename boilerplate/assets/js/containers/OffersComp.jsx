import * as React from "react";
import OffersList from "./OffersList";

export default class OffersComp extends React.Component{
    constructor() {
        super();
        this.state = {
            offers: null
        };
    }

    componentDidMount() {
        console.log("offers mounted");
        this.fetchOffers();
    }


    fetchOffers() {
        const URL = "/api/offers";

        fetch(URL).then(res => res.json()).then(json => {
            this.setState({ offers: json });
        });
    }

    render() {

        const  data  = this.state;

        if (!data)
            return <div>Loading</div>;

        // return <div>{JSON.stringify(data)}</div>;
        return <OffersList data={data}/>



    }
}
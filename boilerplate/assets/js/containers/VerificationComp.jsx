import * as React from "react";

export default class VerificationComp extends React.Component{
    constructor() {
        super();
        this.state = {
            offers: null
        };
    }
    componentDidUpdate(prevProps) {
        if (prevProps.data !== this.props.data) {
            this.fetchVerify();
        }
    }
    fetchVerify(){
        const URL = "/api/verify";
        fetch(URL).then(res => res.json()).then(json => {
            this.setState({ orders: json });
        });
    }
    componentDidMount() {
        // this.fetchOffers();
    }

    render() {
        const data = this.state;

        if (!data) return <div>Loading</div>;

        return <div>{JSON.stringify(data)}</div>;
    }
}
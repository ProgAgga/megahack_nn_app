import * as React from "react";

export default class OrdersComp extends React.Component{
    constructor() {
        super();
        this.state = {
            orders: null
        };
    }

    componentDidMount() {
        this.fetchOrders();
    }


    fetchOrders() {
        const URL = "/api/orders";

        fetch(URL).then(res => res.json()).then(json => {
            this.setState({ orders: json });
        });
    }

    render() {
        const data = this.state;

        if (!data) return <div>Loading</div>;

        return <div>{JSON.stringify(data)}</div>;
    }
}
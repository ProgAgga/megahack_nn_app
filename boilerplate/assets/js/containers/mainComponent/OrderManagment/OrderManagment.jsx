import React from 'react';
import Order from './Order/Order';

import './OrderManagment.scss';

class OrderManagment extends React.Component {

    constructor(props){
        super(props)
        this.state = {orders:[],clients:[]}
    }
    componentDidMount(){
        fetch("/api/orders").then(
            response => response.json()
        ).then(
            orders => fetch("/api/clients").then(
                response => response.json()
            ).then(
                clients => this.setState({
                    orders: orders,
                    clients: clients
                })
            )
        )
    }
    render() {
        return(
            <>
                <div className="tableHeader">
                    <div className="title">client</div>
                    <div className="title">order</div> 
                    <div className="title">status</div> 
                    <div className="title">start date</div> 
                    <div className="title">finish date</div> 
                </div>
                {this.state.orders.length !== 0 && this.state.clients.length !== 0?
                    this.state.orders.map(
                        (order_data,i) => {
                            for (var j = 0 ; j < this.state.clients.length; j++)
                                    if (this.state.clients[j].id === order_data.client)
                                        return <Order data={order_data} key={i} client={this.state.clients[j]}/>
                    }
                    ):""
                }
           </>
        );
    }
}

export default OrderManagment;
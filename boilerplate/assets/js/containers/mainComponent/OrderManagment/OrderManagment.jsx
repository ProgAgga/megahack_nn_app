import React from 'react';
import Order from './Order/Order';

import './OrderManagment.scss';

class OrderManagment extends React.Component {

    constructor(props){
        super(props)
        this.state = {orders:[],clients:[], offers:[]}
    }
    componentDidMount(){
        fetch("/api/orders").then(
            response => response.json()
        ).then(
            orders => fetch("/api/clients").then(
                response => response.json()
            ).then(
                clients => fetch("/api/offers").then(
                    response => response.json()
                ).then(
                    offers =>
                        this.setState({
                        orders: orders,
                        clients: clients,
                        offers: offers
                    })
                )
            )
        )
    }
    render() {
        return(
            <>
            <div className="orderTable">
                <div className="tableHeader">
                    <div className="client" className="title">client</div>
                    <div className="clientOrder" className="title">order</div> 
                    <div className="status" className="title">status</div> 
                    <div className="startDate" className="title">start date</div> 
                    <div className="finishDate" className="title">finish date</div> 
                </div>
                <div className="separator"/>
                {this.state.orders.length !== 0 && this.state.clients.length !== 0 && this.state.offers.length !== 0?
                    this.state.orders.map(
                        (order_data,i) => {
                            for (var j = 0 ; j < this.state.clients.length; j++){
                                for(var k = 0; k < this.state.offers.length; k++){
                                    if (this.state.clients[j].id === order_data.client && this.state.offers[k].id === order_data.offer) {
                                        return <Order   
                                                    data={order_data} 
                                                    key={i} 
                                                    client={this.state.clients[j]} 
                                                    offer={this.state.offers[k]} 
                                                />
                                    }
                                }
                            }
                        }
                    ):""
                }
                </div>
           </>
        );
    }
}

export default OrderManagment;
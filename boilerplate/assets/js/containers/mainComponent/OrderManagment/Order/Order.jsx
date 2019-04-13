import React from 'react';

class Order extends React.Component {

    constructor(props) {
        super(props);

        this.state = {};
      }

    render() {
        return(
            <> 
                <div>{orderItem.id}</div>
                <div>{orderItem.offer}</div> 
                <div>{orderItem.status}</div> 
                <div>{orderItem.dateStart}</div> 
                <div>{orderItem.dateFinish}</div> 
            </> 
        );
    }
}

export default Order;
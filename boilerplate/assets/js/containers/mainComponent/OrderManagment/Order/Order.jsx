import React from 'react';

import './Order.scss';
//import { transformData } from '../../../../helpers/transformDataHelper';
import * as helper from '../../../../helpers/transformDataHelper';
class Order extends React.Component {

    constructor(props) {
        super(props);

        this.state = {};
        this.phone = this.phone
        this.orderObject = helper.transformData(this.pro)
      }

    render() {
        return(
            <div className="singleOrder">
                <p>{this.props.client.phone}</p>
                <p>{this.props.data.offer}</p>
                <p>{this.props.data.status}</p>
                <p>{this.props.data.date_created}</p>
                <p>{this.props.data.date_processed}</p>
            </div>
        );
    }
}

export default Order;
import React from 'react';
import Moment from 'react-moment';

import './Order.scss';
//import { transformData } from '../../../../helpers/transformDataHelper';

class Order extends React.Component {

    constructor(props) {
        super(props);

        this.state = {};
        this.phone = this.phone
      }

    render() {
        return(
            <div className="singleOrder">
                <p>{this.props.client.phone}</p>
                <p>{this.props.offer.name}</p>
                <p>{this.convertStatus(this.props.data.status)}</p>
                <p>  
                    <Moment format="MMMM Do YYYY, h:mm:ss a" withTitle>
                        {this.props.date_created}
                    </Moment>
                </p>
                <p>
                    <Moment format="MMMM Do YYYY, h:mm:ss a" withTitle>
                        {this.props.data.data_processed}
                    </Moment>
                </p>
            </div>
        );
    }

    convertStatus(status) {
        var tmp = '';
        switch (status){
            case "F": tmp="Отклонено";
            break;
            case "S": tmp = "Принято";
            break;
            case "P": tmp="В обработке";
            break;
        }
        return tmp;
    }

    convertOffer(offer) {
        var tmp = '';
        return tmp;
    }
}

export default Order;
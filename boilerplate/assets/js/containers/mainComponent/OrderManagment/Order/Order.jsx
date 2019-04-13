import React from 'react';
import Moment from 'react-moment';
import moment from 'moment';

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
                <div className="client">{this.props.client.phone}</div>
                <div className="clientOrder">{this.props.offer.name}</div>
                <div className="status">{this.convertStatus(this.props.data.status)}</div>
                <div className="startDate">  
                    {moment(this.props.data.date_created).format('MMMM Do YYYY, h:mm:ss a')}
                </div>
                <div className="finishDate">
                    {moment(this.props.data.data_processed).format('MMMM Do YYYY, h:mm:ss a')}
                </div>
            </div>
        );
    }

    convertStatus(status) {
        var tmp = '';
        switch (status){
            case "F": tmp="Отклонено";
            break;
            case "S": tmp = "Одобрено";
            break;
            case "P": tmp="В обработке";
            break;
        }
        return tmp;
    }
}

export default Order;
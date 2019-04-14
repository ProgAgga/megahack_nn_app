import React from 'react';
import Moment from 'react-moment';
import moment from 'moment';

import './Order.scss';
//import { transformData } from '../../../../helpers/transformDataHelper';

class Order extends React.Component {

    constructor(props) {
        super(props);
        this.state = {checkOfferObject: {}}
        this.phone = this.phone
        this.state = {
            data:{},
            invalid_options:[],
            valid_options:[]
        }
      }
 
      componentDidMount() {
        
        var payload = {
            client: this.props.client.id,
            dealer: this.props.client.dealer,
            offer: this.props.data.offer
        };
        
        fetch("/api/check-offer",
        {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
             },
            method: "POST",
            body: JSON.stringify( payload )
        }).then(
            resp => resp.json()
        )
        .then((res) =>{
            this.invalid_ids = res.invalid;
            this.invalid_options = []
            Promise.all(
                this.invalid_ids.map(
                    id => fetch(`/api/options/${id}`)
                    .then(
                        response => response.json()
                    ).then(
                        option =>{ this.invalid_options.push(option.description)}
                    )
                )
            ).then(() =>this.setState(prevState => {
                prevState.invalid_options = this.invalid_options;
                prevState.data = res;
                return prevState;
            }))
             this.setState({data: res}) 
            }
             )
       
      }

    render() {
        return(<>
            {/* <div>{this.state.data?this.state.data.invalid:"loading..."}</div> */}
            <div className="singleOrder">
                <div className="client">{this.props.client.phone}</div>
                <div className="clientOrder">{this.props.offer.name}</div>
                <div className="status">
                    {this.convertStatus(this.props.data.status)}
                    <div className="tooltip">{this.setToolTipMessage()}</div>
                </div>
                <div className="startDate">  
                    {moment(this.props.data.date_created).format('MMMM Do YYYY, h:mm:ss a')}
                </div>
                <div className="finishDate">
                    {moment(this.props.data.data_processed).format('MMMM Do YYYY, h:mm:ss a')}
                </div>
            </div>
            </>
        );
    }

    convertStatus(status) {
        let tmp = '';

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

    setToolTipMessage() {
        status = this.props.data.status;
        let message="";

        switch (status){
            case "F": 
                message =
<>
                         {
                             this.state.invalid_options.length !== 0? this.state.invalid_options.map((elem,i) => (
                                <li key={i} className="invalidOption"> {elem}</li> 
                             )): "randomnoechoto"
                         }
</>
                
                break;
            
            case "S": message = <div className="validOptions">Все условия выполнены</div>;
            break;
            case "P": message= <div className="pendingOptions">Заказ в обработке</div>;
            break;
        }
        return message;
    }

    setInvalidOptions(){
        return (
        <ul>
            <li>{}</li>
        </ul>);
    }

    // getCheckOffer() {

    // }
}

export default Order;
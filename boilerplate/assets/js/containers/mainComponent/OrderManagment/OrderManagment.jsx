import React from 'react';
import Order from './Order/Order';


import './style.scss';

class OrderManagment extends React.Component {

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
           </>
        );
    }

    // generateLine = () => {
    //     return(
    //         <select>
    //           {
    //              Users.map(el =>
    //                 <> 
    //                     <Order orderData={el} />
    //                 </> 
    //             )
    //           }
    //         </select>
    //      )
    // }
}



export default OrderManagment;
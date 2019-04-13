import React from 'react';
import Order from './Order/Order';


import './style.scss';

class OrderManagment extends React.Component {

    render() {
        return(
            <>
                <div className="container">
                    <div className="title">абонент</div>
                    <div className="title">акция</div> 
                    <div className="title">статус</div> 
                    <div className="title">дата создания</div> 
                    <div className="title">дата завершения</div> 
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
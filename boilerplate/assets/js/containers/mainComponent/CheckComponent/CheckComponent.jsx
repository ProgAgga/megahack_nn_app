import React from 'react';

import './CheckComponent.scss'

class CheckComponent extends React.Component {

        // compareImage() {
    // //    var tmp = false;
    // //    if(tmp) {
    //        return (
    //             <img className="imageResult" src={require('./times-solid.svg')}  width="50" height="50"/>
    //        );
    // //    }
    // //    if(!tmp) {
    // //     return <img src={require('./times-solid.svg')}  width="50" height="50"/>; 
    // //    }

    // }

    render() {
        return(
            <div className="checkContainer">
                <div className="fieldsForCheck">
                    <input className="idInput" />
                    <select className="dealerList">

                    </select>
                    <select className="offerList">

                    </select>
                    <button className="checkButton">
                        click
                    </button>
                </div>

{/* блок ниже отображается после получения ответа о валидности опции для клиента */}

                <div className="result">                   
                    {/* {this.compareImage()} */}
                    <progress className="loadingBlock" max="100" value="75" />
                    <div className="optionsBlock">
                        <div className="approvedUserSettings">

                        </div>
                        <div className="declinedUserSettings">

                        </div>
                    </div>
                </div>

            </div>
        );
    } 
}

export default CheckComponent;
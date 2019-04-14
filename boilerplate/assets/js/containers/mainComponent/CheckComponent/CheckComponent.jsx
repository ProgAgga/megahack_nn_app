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

    
    constructor(props){
        super(props)
        this.inputInfo="";
        this.selectedOffer="";

        this.state = {dealers:[], offers:[]}
    }
    componentDidMount(){
        fetch("/api/offers").then(
            response => response.json()
        ).then(
            offers => fetch("/api/dealers").then(
                response => response.json()
            ).then(
                    dealers =>
                        this.setState({
                        dealers: dealers,
                        offers: offers
                    })
            )
        )
    }

    render() {
        return(
            <div className="checkContainer">
                <div className="fieldsForCheck">
                    <input className="idInput" />
                    {/* <select className="dealerList">
                        {
                             this.state.dealers? this.state.dealers.map((elem,i) => (
                                <option key={i} > {elem.name}</option> 
                             )): "randomnoechoto"
                        }
                    </select> */}
                    <select  className="offerList">
                        {
                             this.state.offers? this.state.offers.map((elem,i) => (
                                <option key={i} > {elem.name}</option> 
                             )): "randomnoechoto"
                        }
                    </select>
                    <button className="checkButton" >
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

    onClickHandler(e) {
        console.log(this.state.inputInfo);
        
        console.log(this.state.selectedOffer);
    }
}

export default CheckComponent;
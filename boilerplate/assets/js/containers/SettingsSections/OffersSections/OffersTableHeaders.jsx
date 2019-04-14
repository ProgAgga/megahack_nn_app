import React from "react";
import "../Sources/style.scss"
export default class OffersTableHeaders extends React.Component{
    render(){
        return <div className="OffersHeaders">
            <div className="item">ID</div>
            <div className="item">Название</div>
            <div className="item">Дата окончания</div>
            <div className="item">Условия</div>
        </div>
    }
}
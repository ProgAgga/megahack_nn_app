import React from "react";
import "./style.scss"
export default class SourcesTableHeaders extends React.Component{
    render(){
        return <div className="headers">
                    <div className="item" className="title">ID</div>
                    <div className="item" className="title">Название</div>
                    <div className="item" className="title">Адрес(URL)</div>
                    <div className="item" className="title">Порт</div>
                    <div className="item" className="title">Логин</div>
                    <div className="item" className="title">Пароль</div>
                    <div className="item" className="title">Тип</div>
                    <div className="item" className="title">База данных</div>
                </div>
    }
}
import React from "react";
import "./style.scss"
export default class SourcesTableHeaders extends React.Component{
    render(){
        return <div className="headers">
                    <div className="item">ID</div>
                    <div className="item">Название</div>
                    <div className="item">Адрес(URL)</div>
                    <div className="item">Порт</div>
                    <div className="item">Логин</div>
                    <div className="item">Пароль</div>
                    <div className="item">Тип</div>
                    <div className="item">База данных</div>
                </div>
    }
}
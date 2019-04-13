import React from "react"
import { Link } from 'react-router-dom'
export default class Header extends React.Component{
    render(){
        return <header>
            <nav>
                <ul>
                    <li><Link to='/orders'>orders</Link></li>
                    <li><Link to='/check_offer'>veriry</Link></li>
                    <li><Link to='/settings/offers'>offers</Link></li>
                    <li><Link to='/settings/sources'>sources</Link></li>
                    <li><Link to='/settings/options'>options</Link></li>
                </ul>
            </nav>
        </header>
    }
}
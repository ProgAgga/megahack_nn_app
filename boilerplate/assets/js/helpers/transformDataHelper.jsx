import React from "react";
import Moment from 'react-moment';

export const transformData = (obj) => 
   <> 
        <Moment format="MMMM Do YYYY, h:mm:ss a" withTitle>
            {this.obj.data.date_created}
        </Moment>
    </>



export const newFun = () => {}
import React from "react";


function Data(props) {
    return (
        <React.Fragment>
        <tr>
           <td>{ props.dat.order }</td>
           <td>{ props.dat.price }</td>
           <td>{ props.dat.date }</td>
           <td>{ props.dat.price_rub }</td>
        </tr>
        </React.Fragment>
    )
}

export default Data;
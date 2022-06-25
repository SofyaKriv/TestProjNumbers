import React from "react";
import axios from "axios";
import Table from "react-bootstrap/Table";
import Data from "./Data";

import "./Datas.css"

function Datas() {
    const [dats, setDats] = React.useState([]);
    if (!dats.length) {
        axios.get("http://localhost:8000/api/dats/").then(res => {
            setDats(res.data);
        });
    }
    return(
        <React.Fragment>
        <body>
        <h3> Тестовое задание </h3>
            <Table className="tableData">
                <thead align="center">
                    <td> № заказа </td>
                    <td> Стоимость, $ </td>
                    <td> Срок доставки </td>
                    <td> Стоимость, руб. </td>
                </thead>
                <tbody align="center" margin-top="50%">
                    {dats.map(dat => <Data dat={dat}/>)}
                </tbody>
            </Table>
        </body>
        </React.Fragment>
    );
}

export default Datas;

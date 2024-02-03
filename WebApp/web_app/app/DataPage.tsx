'use client'

import React, { useState, useEffect } from 'react'

function ShowData() {
  const [data, setData] = useState("")

  useEffect(() => {
    fetch("http://localhost:5000/crops").then(
      res => res.text()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  console.log(data) 
  return <div>{data}</div>;
}

export default ShowData;

/*
export class DataPage extends React.Component {
  data = ""

  render() {
    {ShowData()}
    return <div>{this.data}</div>
  }
}
*/
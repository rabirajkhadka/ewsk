const comboBoxCreate = async()=>{
    
    const response = await fetch('http://127.0.0.1:8000/api/station/?format=json');
    const stationData = await response.json();
    let select = document.getElementById("station");

    stationData.forEach((item)=>{
        let option = document.createElement("option");
        option.value = item['stationID'];
        option.text = item['stationID'];
        select.add(option);
    });
    averageTable();
    setInterval(()=>averageTable(), 180000);

    graphCreator();

}
comboBoxCreate();



const averageTable = async () =>{
    graphCreator();
    const station=document.getElementById('station').value;
    const response = await fetch(`http://127.0.0.1:8000/api/average/${station}/?format=json`);
    const averageData = await response.json();
    let table = document.getElementById("averageTable");
    while(table.rows.length > 1) {
        table.deleteRow(-1);
    }

    averageData.forEach((item)=>{
        
            let row = table.insertRow(-1);
            
            let cell1 = row.insertCell(0);
            cell1.innerHTML=`${item["id"]}`;

            let cell2 = row.insertCell(1);
            cell2.innerHTML=`${item["station"]}`;

            let cell3 = row.insertCell(2);
            cell3.innerHTML=`${item["oneHour"]}`;

            let cell4 = row.insertCell(3);
            cell4.innerHTML=`${item["threeHour"]}`;

            let cell5 = row.insertCell(4);
            cell5.innerHTML=`${item["sixHour"]}`;

            let cell6 = row.insertCell(5);
            cell6.innerHTML=`${item["nineHour"]}`;

            let cell7 = row.insertCell(6);
            cell7.innerHTML=`${item["twelveHour"]}`;

            let cell8 = row.insertCell(7);
            cell8.innerHTML=`${item["oneDay"]}`;

            let cell9 = row.insertCell(8);
            cell9.innerHTML=`${item["oneWeek"]}`;

            let cell10 = row.insertCell(9);
            cell10.innerHTML=`${item["twoWeek"]}`;

            let cell11 = row.insertCell(10);
            cell11.innerHTML=`${item["threeWeek"]}`;
            
            let cell12 = row.insertCell(11);
            cell12.innerHTML=`${item["fourWeek"]}`;
            
            let cell13 = row.insertCell(12);
            cell13.innerHTML=`${item["dateTime"]}`;

        

    });
}

const graphCreator = async () => {
  
    const station=document.getElementById('station').value;
    const graphResponse = await fetch(`http://127.0.0.1:8000/api/datasetstation/${station}/?format=json`);
    const graphData = await graphResponse.json();

    let yAxis = [];
    let xAxis=[];
    let count = 0;

    graphData.forEach((item)=>{
        //convert data
        xAxis[count]=item["dateTime"];
        yAxis[count]=item["drainageLevel"];
        count+=1;
    });
    var data = [
    {
        x: xAxis,
        y: yAxis,
        mode: 'lines+markers'
    }
    ];
    var layout = {
        title: {
            text:`Past 1 Hour Data of ${station}`,
            font: {
                family: 'Courier New, monospace',
                size: 20,
            },
            
        },
        xaxis: {
            title: {
            text: 'Time',
            font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
            }
            },
        },
        yaxis: {
            title: {
            text: 'Water Level',
            font: {
                family: 'Courier New, monospace',
                size: 18,
                color: '#7f7f7f'
            }
            }
        }
    };

    Plotly.newPlot('myDiv', data,layout);

}

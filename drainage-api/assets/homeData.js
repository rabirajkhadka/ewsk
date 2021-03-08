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
    allData();
    setInterval(()=>allData(), 180000);
}

const probabilityImage = () => {
    document.getElementsByClassName("chanceImg")[0].style.backgroundImage = "url('static/img/DangerImage.gif')";
}

const allData = async () => {
  
    probabilityImage();

    const station=document.getElementById('station').value;
    const levelResponse = await fetch(`http://127.0.0.1:8000/api/datasetstation/${station}/?format=json`);
    const levelData = await levelResponse.json();

    const averageResponse = await fetch(`http://127.0.0.1:8000/api/average/${station}/?format=json`);
    const averageData = await averageResponse.json();

    const trendResponse = await fetch(`http://127.0.0.1:8000/api/trend/${station}/?format=json`);
    const trendData = await trendResponse.json();

    //water Data
    console.log(trendData[0]["trendValue"]);
    

    document.getElementById("waterData").innerHTML=levelData[0]['drainageLevel'];
    if (parseFloat(levelData[0]['drainageLevel'])>5){
        
        document.getElementById("waterLabel").style.backgroundColor = "#ff726f";
        document.getElementById("waterData").style.borderColor = "#ff726f";
        document.getElementById("waterLabel").style.borderLeftColor = "#8b0000";

    } else if(parseFloat(levelData[0]['drainageLevel'])<-5){
    
        document.getElementById("waterLabel").style.backgroundColor = "#49b675";
        document.getElementById("waterData").style.borderColor = "#49b675";
        document.getElementById("waterLabel").style.borderLeftColor = "#006038";

    } else{
      
        document.getElementById("waterLabel").style.backgroundColor = "#c3e4e8";
        document.getElementById("waterData").style.borderColor = "#c3e4e8";
        document.getElementById("waterLabel").style.borderLeftColor = "#31639c";
    }

    //Average Data

    document.getElementById("avgData").innerHTML=averageData[0]['oneDay'];
    if (parseFloat(averageData[0]['oneDay'])>5){
        
        document.getElementById("avgLabel").style.backgroundColor = "#ff726f";
        document.getElementById("avgData").style.borderColor = "#ff726f";
        document.getElementById("avgLabel").style.borderLeftColor = "#8b0000";

    } else if(parseFloat(averageData[0]['oneDay'])<-5){
    
        document.getElementById("avgLabel").style.backgroundColor = "#49b675";
        document.getElementById("avgData").style.borderColor = "#49b675";
        document.getElementById("avgLabel").style.borderLeftColor = "#006038";

    } else{
      
        document.getElementById("avgLabel").style.backgroundColor = "#c3e4e8";
        document.getElementById("avgData").style.borderColor = "#c3e4e8";
        document.getElementById("avgLabel").style.borderLeftColor = "#31639c";
    }

    //trend Data
    if (parseFloat(trendData[0]['trendValue'])>0.2){
        document.getElementById("trendData").innerHTML="Increasing";
        document.getElementById("trendLabel").style.backgroundColor = "#ff726f";
        document.getElementById("trendData").style.borderColor = "#ff726f";
        document.getElementById("trendLabel").style.borderLeftColor = "#8b0000";

    } else if(parseFloat(trendData[0]['trendValue'])<-0.2){
        document.getElementById("trendData").innerHTML="Decreasing";
        document.getElementById("trendLabel").style.backgroundColor = "#49b675";
        document.getElementById("trendData").style.borderColor = "#49b675";
        document.getElementById("trendLabel").style.borderLeftColor = "#006038";

    } else{
        document.getElementById("trendData").innerHTML="Steady";
        document.getElementById("trendLabel").style.backgroundColor = "#c3e4e8";
        document.getElementById("trendData").style.borderColor = "#c3e4e8";
        document.getElementById("trendLabel").style.borderLeftColor = "#31639c";
    }
    console.log('updated');
    var data = [
        {
            type: "indicator",
            mode: "number+gauge",
            value: parseFloat(levelData[0]['drainageLevel']),
            domain: { x: [0, 1], y: [0, 1] },
            delta: { reference: 20, position: "top" },
            title: {
            text:
                "<b>Water</b><br><b>Level</b>",
            font: { size: 12 }
            },
            gauge: {
            shape: "bullet",
            axis: { range: [-20, 20] },
            threshold: {
            },
            bgcolor: "white",
            steps: [{ range: [-5, 5], color: "lightblue" },
                    { range: [-20, -5], color: "lightgreen" },
                    { range: [5, 20], color: "red" }
                    ],
            bar: { color: "blue" }
            }
        }
        ];

    var layout = { height:200 };

    Plotly.newPlot('bulletGraph', data, layout);

}
comboBoxCreate();


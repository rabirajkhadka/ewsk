
//language converter

function convertToNepaliDigit(number) {
    var number = number.toString();
    var sliced = [];
    var numberLength = number.length;
    var nepali_digits = ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'];
    for (i = 0; i < numberLength; i++) {
        sliced.push(nepali_digits[number.substr(number.length - 1)]);
        number = number.slice(0, -1);
    }
    return sliced.reverse().join('').toString();
}
function convertToNepaliNumber(number) {
    var number = number.toString();
    var number_before_decimal = number.split(".")[0];
    var number_after_decimal = number.split(".")[1];
    var text1 = convertToNepaliDigit(number_before_decimal);
    var text2 = "";
    if (typeof number_after_decimal !== "undefined") {
        text2 = convertToNepaliDigit(number_after_decimal);
        return text1 + "." + text2;
    }
    else {
        return text1;
    }

}

//station selection
const comboBoxCreate = async()=>{
    
    const response = await fetch('http://127.0.0.1:8000/api/station/?format=json');
    const stationData = await response.json();
    let select = document.getElementById("station");

    stationData.forEach((item)=>{
        let option = document.createElement("option");
        option.value = item['stationID'];
        option.text = item['name'];
        select.add(option);
    });
    allData();
    setInterval(()=>allData(), 180000);
}

// const probabilityImage = () => {
//     document.getElementsByClassName("chanceImg")[0].style.backgroundImage = "url('static/img/DangerImage.gif')";
// }

const allData = async () => {
  
    // probabilityImage();
    try{
    stationTable();
    const station=document.getElementById('station').value;
    globalNumbersTable(station);
    const levelResponse = await fetch(`http://127.0.0.1:8000/api/datasetstation/${station}/?format=json`);
    const levelData = await levelResponse.json();

    // const averageResponse = await fetch(`http://127.0.0.1:8000/api/average/${station}/?format=json`);
    // const averageData = await averageResponse.json();

    const trendResponse = await fetch(`http://127.0.0.1:8000/api/trend/${station}/?format=json`);
    const trendData = await trendResponse.json();

    const numberResponse = await fetch(`http://127.0.0.1:8000/api/stationNumber/${station}/?format=json`);
    const numberData = await numberResponse.json();

    //water Data
    // console.log(numberData[0].mapImage.replace('assets','static'));

    document.getElementById("stationMap").src = numberData[0].mapImage.replace('assets','static');
    document.getElementById("someText").innerHTML = numberData[0]['name']+' जल मापन केन्द्र';

    // document.getElementById("imageCommunityHero1").src = numberData[0].communityHero1Image.replace('assets','static');
    // document.getElementById("imageCommunityHero2").src = numberData[0].communityHero2Image.replace('assets','static');

    
    function floodTimer() {
        
        let trendIndex;

        for (i = 0; i < trendData.length; i++) {
            if(parseFloat(trendData[i].trendValue)<0.2 ){
                if(i==0){
                    console.log(i);
                }
                else{
                    trendIndex=i-1;
                }
                break;
            }
        }

        var countDownDate = new Date(trendData[trendIndex].dateTime).getTime();
        var newdate=countDownDate + 60*60000;
        // Update the count down every 1 second
        var x = setInterval(function() {
                
            // Get today's date and time
            var now = new Date().getTime();
                
            // Find the distance between now and the count down date
            var distance = newdate-now;
                
            // Time calculations for days, hours, minutes and seconds

            var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            var seconds = Math.floor((distance % (1000 * 60)) / 1000);
                
            // Output the result in an element with id="demo"
            document.getElementById("trendTimer").innerHTML=minutes + "m " + seconds + "s ";
                
            // If the count down is over, write some text 
            if (distance < 0) {
                console.log(distance);
                clearInterval(x);
                document.getElementById("trendTimer").innerHTML = "00:00!";
            }
        }, 1000);
    }
        

    
        // document.getElementById("communityHero1").innerHTML=numberData[0]['communityHero1'];
        // document.getElementById("communityHero2").innerHTML=numberData[0]['communityHero2'];


        document.getElementById("timeLabel").style.backgroundColor = "#49b675";
        document.getElementById("timeLabel").style.borderColor = "#49b675";
        document.getElementById("timeLabel").style.borderLeftColor = "#49b675";
        document.getElementById("timeLabel").innerHTML='डाटा प्राप्त भईरहेको छ । पछिल्लो पटक प्राप्त डाटा: '+ new Date(levelData[0]['dateTime']);
        document.getElementById("waterData").innerHTML=convertToNepaliNumber(levelData[0]['drainageLevel']);
    if (parseFloat(levelData[0]['drainageLevel'])>parseFloat(numberData[0]['dangerLevel'])){
        
        document.getElementById("waterLabel").style.backgroundColor = "#ff726f";
        document.getElementById("waterData").style.borderColor = "#ff726f";
        document.getElementById("waterLabel").style.borderLeftColor = "#8b0000";

    } else if(parseFloat(levelData[0]['drainageLevel'])>parseFloat(numberData[0]['warningLevel'])){
    
        document.getElementById("waterLabel").style.backgroundColor = "#f8fc14";
        document.getElementById("waterData").style.borderColor = "#f8fc14";
        document.getElementById("waterLabel").style.borderLeftColor = "#f8fc14";

    } else{
      
        document.getElementById("waterLabel").style.backgroundColor = "#c3e4e8";
        document.getElementById("waterData").style.borderColor = "#c3e4e8";
        document.getElementById("waterLabel").style.borderLeftColor = "#31639c";
    }

    //Average Data

    // document.getElementById("avgData").innerHTML=averageData[0]['oneDay'];
    // if (parseFloat(averageData[0]['oneDay'])>5){
        
    //     document.getElementById("avgLabel").style.backgroundColor = "#ff726f";
    //     document.getElementById("avgData").style.borderColor = "#ff726f";
    //     document.getElementById("avgLabel").style.borderLeftColor = "#8b0000";

    // } else if(parseFloat(averageData[0]['oneDay'])<-5){
    
    //     document.getElementById("avgLabel").style.backgroundColor = "#49b675";
    //     document.getElementById("avgData").style.borderColor = "#49b675";
    //     document.getElementById("avgLabel").style.borderLeftColor = "#006038";

    // } else{
      
    //     document.getElementById("avgLabel").style.backgroundColor = "#c3e4e8";
    //     document.getElementById("avgData").style.borderColor = "#c3e4e8";
    //     document.getElementById("avgLabel").style.borderLeftColor = "#31639c";
    // }

    //trend Data
    if (parseFloat(trendData[0]['trendValue'])>0.2){
        document.getElementById("trendData").innerHTML="बढ्दै";
        document.getElementById("trendLabel").style.backgroundColor = "#ff726f";
        document.getElementById("trendData").style.borderColor = "#ff726f";
        document.getElementById("trendLabel").style.borderLeftColor = "#8b0000";
        floodTimer();
        document.getElementById("trendTimer").style.backgroundColor = "#ff726f";
        document.getElementById("trendTimer").style.borderColor = "#ff726f";
        document.getElementById("timerLabel").style.backgroundColor = "#ff726f";
        document.getElementById("timerLabel").style.borderColor = "#ff726f";
        document.getElementById("timerLabel").style.borderLeftColor = "#8b0000";

    } else if(parseFloat(trendData[0]['trendValue'])<-0.2){
        document.getElementById("trendData").innerHTML="घट्दै";
        document.getElementById("trendLabel").style.backgroundColor = "#49b675";
        document.getElementById("trendData").style.borderColor = "#49b675";
        document.getElementById("trendLabel").style.borderLeftColor = "#006038";

    } else{
        document.getElementById("trendData").innerHTML="स्थिर";
        document.getElementById("trendLabel").style.backgroundColor = "#c3e4e8";
        document.getElementById("trendData").style.borderColor = "#c3e4e8";
        document.getElementById("trendLabel").style.borderLeftColor = "#31639c";
    }
    console.log('updated');
    Highcharts.setOptions({
        chart: {
            inverted: false,
            type: 'bullet'
        },
        title: {
            text: null
        },
        legend: {
            enabled: false
        },
        yAxis: {
            gridLineWidth: 0
        },
        plotOptions: {
            series: {
            borderWidth: 0,
            color: '#000',
            targetOptions: {
                width: '200%'
                
            }
            }
        },
        credits: {
            enabled: false
        },
        exporting: {
            enabled: false
        }
        });

    Highcharts.chart('container1', {
        chart: {
            marginTop: 40,
            height:900,
        },
        xAxis: {
            categories: ['<span>पानीको तह</span>']
        },
        yAxis: {
            plotBands: [{
            from: parseFloat(numberData[0]['warningLevel']),
            to: parseFloat(numberData[0]['dangerLevel']),
            color: 'yellow'
            }, {
            from: -1000,
            to: parseFloat(numberData[0]['warningLevel']),
            color: 'lightblue'
            }, {
            from: parseFloat(numberData[0]['dangerLevel']),
            to: 1000,
            color: 'red'
            }],
            title: null
        },
        series: [{
            
            data: [{
            y: parseFloat(levelData[0]['drainageLevel']),
            target: 0,
            
            }]
        }]
        
        });

     }
    
    catch(err){
        console.log(err);
        document.getElementById("timeLabel").style.backgroundColor = "#ff726f";
        document.getElementById("timeLabel").style.borderColor = "#ff726f";
        document.getElementById("timeLabel").style.borderLeftColor = "#8b0000";
        document.getElementById("timeLabel").innerHTML='डाटा प्राप्त भईरहेको छैन । समस्या यस कम्प्युटरमा रहेको छ । समयको  डाटा छैन ।';
        // document.getElementById("avgData").innerHTML='डाटा छैन';
        document.getElementById("trendData").innerHTML="डाटा छैन";
        document.getElementById("waterData").innerHTML='डाटा छैन';
        Highcharts.setOptions({
        chart: {
            inverted: false,
            type: 'bullet'
        },
        title: {
            text: null
        },
        legend: {
            enabled: false
        },
        yAxis: {
            gridLineWidth: 0
        },
        plotOptions: {
            series: {
            borderWidth: 0,
            color: '#000',
            targetOptions: {
                width: '200%'
                
            }
            }
        },
        credits: {
            enabled: false
        },
        exporting: {
            enabled: false
        }
        });

    Highcharts.chart('container1', {
        chart: {
            marginTop: 40,
            height:900,
        },
        xAxis: {
            categories: ['<span>डाटा छैन</span>']
        },
        yAxis: {
            plotBands: [{
            from: -5,
            to: 5,
            color: 'red'
            }, {
            from: -20,
            to: -5,
            color: 'red'
            }, {
            from: 5,
            to: 20,
            color: 'red'
            }],
            title: null
        },
        series: [{
            
            data: [{
            y: null,
            target: 0,
            
            }]
        }]
        
        });


    }

    

    

    // var data = [
    //     {
    //         type: "indicator",
    //         mode: "gauge",
    //         value: parseFloat(levelData[0]['drainageLevel']),
    //         domain: { x: [0, 1], y: [0, 1] },
    //         delta: { reference: 20, position: "top" },
    //         title: {
    //         text:
    //             "<b>Water</b><br><b>Level</b>",
    //         font: { size: 12 }
    //         },
    //         gauge: {
    //         shape: "bullet",
    //         axis: { range: [-20, 20] },
    //         threshold: {
    //         },
    //         bgcolor: "white",
    //         steps: [{ range: [-5, 5], color: "lightblue" },
    //                 { range: [-20, -5], color: "lightgreen" },
    //                 { range: [5, 20], color: "red" }
    //                 ],
    //         bar: { color: "blue" }
    //         }
    //     }
    //     ];

    // var layout = { width: 450, height: 200 };

    // Plotly.newPlot('bulletGraph', data, layout);

}
const stationTable = async () =>{
        
    const response = await fetch(`http://127.0.0.1:8000/api/station/`);
    const stationData = await response.json();
    let table = document.getElementById("stationTable");
    console.log(table);
    while(table.rows.length > 1) {
        table.deleteRow(-1);
    }

    stationData.forEach((item)=>{
        
            let row = table.insertRow(-1);
            
            let cell1 = row.insertCell(0);
            cell1.innerHTML=`${item["name"]}`;

            let cell2 = row.insertCell(1);
            cell2.innerHTML=`${item["EmergencyNumbersTitle"]}`;

            let cell3 = row.insertCell(2);
            cell3.innerHTML=`${item["EmergencyNumbers"]}`;

            let cell4 = row.insertCell(3);
            cell4.innerHTML=`${convertToNepaliNumber(item["warningLevel"])}`;

            let cell5 = row.insertCell(4);
            cell5.innerHTML=`${convertToNepaliNumber(item["dangerLevel"])}`;
     

    });
}
const globalNumbersTable = async (id) =>{
    console.log(id);
    const response = await fetch(`http://127.0.0.1:8000/api/stationNumber/${id}/`);
    const stationData = await response.json();
    let table = document.getElementById("globalTable");
    console.log(table);
    while(table.rows.length > 1) {
        table.deleteRow(-1);
    }
    let allNames= stationData[0]['GlobalNames'].split(',');
    let allNumbers= stationData[0]['GlobalNumbers'].split(',');
    for (let i = 0; i < allNames.length; i++) {
        let row = table.insertRow(-1);

        let cell1 = row.insertCell(0);
        cell1.innerHTML=`${allNames[i]}`;

        let cell2 = row.insertCell(1);
        cell2.innerHTML=`${allNumbers[i]}`;
    }

    // stationData.forEach((item)=>{
        
    //         let row = table.insertRow(-1);
            
    //         let cell1 = row.insertCell(0);
    //         cell1.innerHTML=`${item["name"]}`;

    //         let cell2 = row.insertCell(1);
    //         cell2.innerHTML=`${item["EmergencyNumbersTitle"]}`;

    //         let cell3 = row.insertCell(2);
    //         cell3.innerHTML=`${item["EmergencyNumbers"]}`;

    //         let cell4 = row.insertCell(3);
    //         cell4.innerHTML=`${item["warningLevel"]}`;

    //         let cell5 = row.insertCell(4);
    //         cell5.innerHTML=`${item["dangerLevel"]}`;
     

    // });
}
comboBoxCreate();



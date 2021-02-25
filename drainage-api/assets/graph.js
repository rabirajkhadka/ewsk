
const graphCreator = async () => {
  
    probabilityImage();

    const station=document.getElementById('station').value;
    const graphResponse = await fetch(`http://127.0.0.1:8000/api/datasetstation/${station}/?format=json`);
    const graphData = await graphResponse.json();

    let yAxis = [];
    let xAxis=[];
    let count = 0;

    graphData.forEach((item)=>{
        //convert data
        yAxis[count]=item["dateTime"];
        xAxis[count]=item["drainageLevel"];
        count+=1;
    });
    console.log(yAxis);
    console.log(xAxis);
}
graphCreator();
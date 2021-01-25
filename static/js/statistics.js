let table = $('#statisticsTable').DataTable({
  processing: true,
  serverSide: true,
  ajax: {
    url: '/dashboard/api/sensorDatalist?format=json',
    type: 'GET',
    dataType: 'json',
    /*
        "dataFilter": function(data){
            var json = jQuery.parseJSON( data );
            json.recordsTotal = json.total;
            json.recordsFiltered = json.total;
            json.data = json.list; 
            return JSON.stringify( json ); // return JSON string
       }
*/
    /*
        "dataSrc": function ( json ) {
            return convertArray(json);
        }
*/
  },
  'content-type': 'application/json',
  processData: true,
  paging: true,
  columns: [{data: 'id'}, {data: 'water_level'}, {data: 'date_time'}],
});

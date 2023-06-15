var map,myVar;
    var i=0;

    function initMap() { 
        var locList = [{lat:13.0196,lng:77.5968},{lat:13.0358,lng:77.5970},{lat:12.8399,lng:77.6831},{lat:12.9081,lng:77.6476},
                       {lat:12.9279,lng:77.6271},{lat:12.9166,lng:77.6101},{lat:12.972442,lng:77.580643},{lat:12.9279,lng:77.6271},
                       {lat:12.9719,lng:77.6412}];
        if(i<locList.length){

        map = new google.maps.Map(document.getElementById('map'), {
          center: locList[i],
          zoom: 14                    
        });

        var marker=new google.maps.Marker({
          position: locList[i],map: map,
        }); 
        }
        i++;
        window.setTimeout("initMap();", 1000*1); 
    }
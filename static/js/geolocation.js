var markers = [];

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  // TODO: Display a popup instead of an infoWindow
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
}

function clearMarkers() {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
}

function placeMarkerAndPanTo(latLng, map) {
  clearMarkers();
  var marker = new google.maps.Marker({
    position: latLng,
    map: map
  });


  markers.push(marker);
  map.panTo(latLng);
}

function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 49.174924, lng: -0.339841},
    zoom: 15
  });
  var infoWindow = new google.maps.InfoWindow({map: map});

  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      infoWindow.setPosition(pos);
      // TODO: Display a popup instead of an infoWindow
      infoWindow.setContent('Location found.');
      map.setCenter(pos);
    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }

  map.addListener('click', function(e) {
    placeMarkerAndPanTo(e.latLng, map);
  });
}

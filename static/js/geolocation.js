var markers = [];
var map = null;

function handleLocationError(browserHasGeolocation, pos) {
  // TODO: Display a popup instead of an infoWindow
  console.log(browserHasGeolocation ?
    'Error: The Geolocation service failed.' :
    'Error: Your browser doesn\'t support geolocation.');
}

function parseAddress(addressObject, index) {
  var addressComponent = '';
  try {
    addressComponent = addressObject.address_components[index].long_name;
  } catch (e){
    // TODO: Display a popup instead of an infoWindow
    console.log('Can\'t get all the components of the formatted address');
    console.console.error(e);
  }

  return addressComponent
}

function reverseGeocode(location) {
  var geocoder = new google.maps.Geocoder();

  geocoder.geocode({'location': location}, function(results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
      if(results[1]) {
        var addressObject = results[1];

        // Fill the form
        $('input[name=coordinate_x]').val(location.lat);
        $('input[name=coordinate_y]').val(location.lng);
        $('input[name=town]').val(parseAddress(addressObject, 0));
        $('input[name=department]').val(parseAddress(addressObject, 1));
        $('input[name=country]').val(parseAddress(addressObject, 3));
      }
    } else {
      // TODO: Display a popup instead of an infoWindow
      console.log('Geocoder failed due to: ' + status);
    }
  });
}

function clearMarkers() {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(null);
  }
}

function setPosition(latLng, map) {
  clearMarkers();
  var marker = new google.maps.Marker({
    position: latLng,
    map: map
  });

  // Center the map on the marker
  markers.push(marker);
  map.panTo(latLng);
  reverseGeocode(latLng);
}

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 49.174924, lng: -0.339841},
    zoom: 15
  });

  map.addListener('click', function(e) {
    setPosition(e.latLng, map);
  });
}

function geolocate() {
  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      setPosition(pos, map);
    }, function() {
      handleLocationError(true, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
}

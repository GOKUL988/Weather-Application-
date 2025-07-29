function getLocation() {
    navigator.geolocation.getCurrentPosition(function(position) {
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;
      document.getElementById("Input").value = `${lat},${lon}`;
      window.location.href = `main/${lat},${lon}`;
    });
  }
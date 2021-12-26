var lat = 0;
var lng = 0;

var map = L.map("map").setView([41.719562, 44.788718], 8);
L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
  maxZoom: 20,
  subdomains:['mt0','mt1','mt2','mt3']
}).addTo(map);

L.control.scale({
  metric: true,
  imperial: false,
  position: 'topright'
}).addTo(map);

window.onload = (e) => {
  fetch("/get_points").then(e => e.json()).then(data=>{
    for(var elem of data){
      var circle = L.circle([elem.point.latitude, elem.point.longtitude], {
          color: `${elem.category.category_color}`,
          fillColor: `${elem.category.category_color}`,
          fillOpacity: 0.5,
          radius: 300
      }).addTo(map);
      circle.bindPopup(`<p style="display:inline-block">სახელი: </p>${elem.point.fullname}<br><p style="display:inline-block">ტელეფონი: </p> ${elem.point.phone}<br><p style="display:inline-block">კომენტარი: </p> ${elem.point.comment}`);

    }
  })
}
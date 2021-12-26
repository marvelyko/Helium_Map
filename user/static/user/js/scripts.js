var lat = 0;
var lng = 0;

var map = L.map("dashboardmap").setView([41.719562, 44.788718], 8);
L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
  maxZoom: 20,
  subdomains:['mt0','mt1','mt2','mt3']
}).addTo(map);

L.control.scale({
  metric: true,
  imperial: false,
  position: 'topright'
}).addTo(map);

map.on("click", function (event) {
  handleClick(event.latlng);
});

function handleClick(cord) {
  var popup = document.getElementById("popup");
  document.querySelector("[name='phone']").value = USER_PHONE;
  document.querySelector("[name='fullname']").value = USER_NAME;
  console.log(USER_NAME);
  popup.style.display = "block";

  lat = cord.lat;
  lng = cord.lng;
}

function popupClose() {
  var popup = document.getElementById("popup");

  popup.style.display = "none";
}

function submitData(e){
  e.preventDefault();
  var phone = e.target.elements.phone.value;
  var name = e.target.elements.fullname.value;
  var comment = e.target.elements.comment.value;
  var csrfmiddlewaretoken = e.target.elements.csrfmiddlewaretoken.value;
  var category = e.target.elements.category.value;
  fetch("/add_point", {
    method: 'post',
    headers:{ 
      'Content-Type': 'application/json',
      "X-CSRFToken": csrfmiddlewaretoken },
    body: JSON.stringify({
      "phone":phone,
      "fullname":name,
      "comment":comment,
      "latitude":lat,
      "longtitude" : lng,
      "category" : category
    })
  }).then(window.location.reload());
}

window.onload = (e) => {
  fetch("/get_points").then(e => e.json()).then(data=>{
    for(var elem of data){
      var circle = L.circle([elem.point.latitude, elem.point.longtitude], {
          color: `${elem.category.category_color}`,
          fillColor: `${elem.category.category_color}`,
          fillOpacity: 0.5,
          radius: 300
      }).addTo(map);
      circle.bindPopup(`${elem.point.name}<br>${elem.point.phone}<br>${elem.point.comment}`);
    }
  })

  var myLocations = document.getElementsByTagName("table")[0];
  newHtml = myLocations.innerHTML;
  fetch("/get_my_points").then(e => e.json()).then(data=>{
    for(var elem of data){
      newHtml = newHtml.concat(`
      <tr>
        <td>${elem.fullname}</td>
        <td>${elem.phone}</td>
        <td>${elem.comment}</td>
        <td><a class="remove" href=/delete_point/${elem.id}>წაშლა</a></td>
      </tr>`);
    }
    
  myLocations.innerHTML = newHtml;
  });

  const urlParams = new URL(document.URL);
  var dest = urlParams.searchParams.get("dest");
  if(dest == 'addLocations'){
    openCity(e, 'addLocations')
  }else if(dest == 'myLocations'){
    openCity(e, 'myLocations')
  }else if(dest == 'myProfile'){
    openCity(e, 'myPorfile')
  }
}
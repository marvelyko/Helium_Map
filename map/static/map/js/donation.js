function myDonation () {
    var donation = document.getElementById("donation");

    if(donation.style.display == "block"){
        donation.style.display = "none";
    }else{
        donation.style.display = "block";
    }
}
// get and display temerature value
let current_temp = sensor_data.herby_details[newest_entry].temp;
document.getElementById('temperature-value').innerText = current_temp + "\u00B0C"

// color the value box green or red depenening acceptable range
function color() {
  if (current_temp >= 18 && current_temp <= 25) {
    document.getElementById('temperature-box').style.backgroundColor = "#6BB834"
    document.getElementById('temperature-box').style.color = "#1C370A"
    document.getElementById('temperature-box').style.boxShadow = "5px 10px 30px #6BB834"
  }
  else {
    document.getElementById('temperature-box').style.backgroundColor = "#C12415"
    document.getElementById('temperature-box').style.color = "#370D0A"
    document.getElementById('temperature-box').style.boxShadow = "5px 10px 30px #C12415"
  }
}
color();
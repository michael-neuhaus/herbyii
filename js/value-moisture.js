// get and display moisture value
let current_moist = sensor_data.herby_details[newest_entry].moisture;
document.getElementById('TDS-value').innerText = current_moist

// color the value box green or red depenening acceptable range
function color() {
  if (current_moist >= 1000 && current_moist <= 2000) {
    document.getElementById('TDS-box').style.backgroundColor = "#6BB834"
    document.getElementById('TDS-box').style.color = "#1C370A"
    document.getElementById('TDS-box').style.boxShadow = "5px 10px 30px #6BB834"
  }
  else {
    document.getElementById('TDS-box').style.backgroundColor = "#C12415"
    document.getElementById('TDS-box').style.color = "#370D0A"
    document.getElementById('TDS-box').style.boxShadow = "5px 10px 30px #C12415"
  }
}
color();

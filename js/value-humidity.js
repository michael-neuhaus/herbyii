// get and display humidity moisture value
let current_humidity = sensor_data.herby_details[newest_entry].humidity;
document.getElementById('humidity-value').innerText = current_humidity + "%"

// color the value box green or red depenening acceptable range
function color() {
    if (current_humidity >= 40 && current_humidity <= 80) {
      document.getElementById('humidity-box').style.backgroundColor = "#6BB834"
      document.getElementById('humidity-box').style.color = "#1C370A"
      document.getElementById('humidity-box').style.boxShadow = "5px 10px 30px #6BB834"
    }
    else {
      document.getElementById('humidity-box').style.backgroundColor = "#C12415"
      document.getElementById('humidity-box').style.color = "#370D0A"
      document.getElementById('humidity-box').style.boxShadow = "5px 10px 30px #C12415"
    }
  }
  color();

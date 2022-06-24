// get and display light moisture value
let current_light = sensor_data.herby_details[newest_entry].light;
document.getElementById('light-value').innerText = current_light

// color the value box green or red depenening acceptable range
function color() {
    if (current_light >= 500) {
      document.getElementById('light-box').style.backgroundColor = "#6BB834"
      document.getElementById('light-box').style.color = "#1C370A"
      document.getElementById('light-box').style.boxShadow = "5px 10px 30px #6BB834"
    }
    else {
      document.getElementById('light-box').style.backgroundColor = "#C12415"
      document.getElementById('light-box').style.color = "#370D0A"
      document.getElementById('light-box').style.boxShadow = "5px 10px 30px #C12415"
    }
  }
  color();
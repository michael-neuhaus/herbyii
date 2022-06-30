// create array for x axis labels
x_axis_labels = []
for (let i = 0; i < sensor_data.herby_details.length; i++) { 
  x_axis_labels.push(new_entry = sensor_data.herby_details[i].date + " " + sensor_data.herby_details[i].time)
}

// create array for humidity data
let humidity_data = []
for (let i = 0; i < sensor_data.herby_details.length; i++) { 
  humidity_data.push(sensor_data.herby_details[i].humi)
}

if (current_humidity >= 18 && current_humidity <= 25) {
  chartcolor = "#6BB834"
}
else {
  chartcolor = "#C12415"
}

// genereate chart
new Chart(document.getElementById("humidity-chart"), {
  type: 'line',
  data: {
    labels: x_axis_labels,
    datasets: [{ 
        data: humidity_data,
        label: "humidity",
        borderColor: chartcolor,
        fill: false
      }
    ]
  },
});

// create array for x axis labels
x_axis_labels = []
for (let i = 0; i < sensor_data.herby_details.length; i++) { 
  x_axis_labels.push(new_entry = sensor_data.herby_details[i].date + " " + sensor_data.herby_details[i].time)
}

// create array for temperature data
let moist_data = []
for (let i = 0; i < sensor_data.herby_details.length; i++) { 
  moist_data.push(sensor_data.herby_details[i].moisture)
}

// genereate chart
new Chart(document.getElementById("moisture-chart"), {
  type: 'line',
  data: {
    labels: x_axis_labels,
    datasets: [{ 
        data: moist_data,
        label: "moisture",
        borderColor: "blue",
        fill: false
      }
    ]
  },
});
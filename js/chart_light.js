// create array for x axis labels
x_axis_labels = []
for (let i = 0; i < sensor_data.herby_details.length; i++) { 
  x_axis_labels.push(new_entry = sensor_data.herby_details[i].date + " " + sensor_data.herby_details[i].time)
}

// create array for light data
let light_data = []
for (let i = 0; i < sensor_data.herby_details.length; i++) { 
  light_data.push(sensor_data.herby_details[i].light)
}

// genereate chart
new Chart(document.getElementById("light-chart"), {
  type: 'line',
  data: {
    labels: x_axis_labels,
    datasets: [{ 
        data: light_data,
        label: "light",
        borderColor: "orange",
        fill: false
      }
    ]
  },
});
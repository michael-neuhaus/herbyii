// create array for x axis labels
x_axis_labels = []
for (let i = 0; i < sensor_data.herby_details.length; i++) { 
  x_axis_labels.push(new_entry = sensor_data.herby_details[i].date + " " + sensor_data.herby_details[i].time)
}

// create array for temperature data
let temp_data = []
for (let i = 0; i < sensor_data.herby_details.length; i++) { 
  temp_data.push(sensor_data.herby_details[i].temp)
}

// genereate chart
new Chart(document.getElementById("temperature-chart"), {
  type: 'line',
  data: {
    labels: x_axis_labels,
    datasets: [{ 
        data: temp_data,
        label: "temperature in C",
        borderColor: "black",
        fill: false
      }
    ]
  },
  // options: {
  //   title: {
  //     display: true,
  //     text: 'temperature in °C'
  //   }
  // }
});
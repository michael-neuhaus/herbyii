
new Chart(document.getElementById("temperature-chart"), {
  type: 'line',
  data: {
    labels: [1,2,3,4,5,6,7,8,9,10],
    datasets: [{ 
        data: [18,14,16,15,19,21,23,24,28,16],
        label: "temperature in C",
        borderColor: "#3e95cd",
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

new Chart(document.getElementById("moisture-chart"), {
  type: 'line',
  data: {
    labels: [1,2,3,4,5,6,7,8,9,10],
    datasets: [{ 
        data: [20,18,16,14,17,20,21,22,20,19],
        label: "moisture",
        borderColor: "orange",
        fill: false
      }
    ]
  },
});

new Chart(document.getElementById("light-chart"), {
  type: 'line',
  data: {
    labels: [1,2,3,4,5,6,7,8,9,10],
    datasets: [{ 
        data: [86,11,12,13,14,14,100,5,4,0],
        label: "light",
        borderColor: "green",
        fill: false
      }
    ]
  },
});

new Chart(document.getElementById("TDS-chart"), {
  type: 'line',
  data: {
    labels: [1,2,3,4,5,6,7,8,9,10],
    datasets: [{ 
        data: [86,114,106,106,107,111,133,221,783,2478],
        label: "TDS",
        borderColor: "red",
        fill: false
      }
    ]
  },
});